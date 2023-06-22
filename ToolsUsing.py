#舍弃原有的和LLM的POST方式，改为调用langchain来实现连接
from toolbox import CatchException, update_ui

import langchain

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
)

from typing import Any, Dict, List, Union


# 读取时首先看是否存在私密的config_private配置文件（不受git管控），如果有，则覆盖原config文件
from toolbox import get_conf, update_ui, is_any_api_key, select_api_key, what_keys, clip_history, trimmed_format_exc
proxies, API_KEY, TIMEOUT_SECONDS, MAX_RETRY = \
    get_conf('proxies', 'API_KEY', 'TIMEOUT_SECONDS', 'MAX_RETRY')
 
import json
from typing import Optional, Type
from langchain.tools import BaseTool
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
import requests
class daily_news(BaseTool):
    name = "今日头条"
    description = f"""This tool is useful if you need to answer today's news and related information.
                The output of this tool is today's news, and expect your request as action input.\n
                当原始问题中期望了解新闻时, You should select at least 8 news and provide Final Answer directly immediately once you get news, in \"Chinese\".\n
                Following in three double quotes is an examples of the desired output format, which requires each news to be followed by a new line in \"Chinese\":\n\n
                \"\"\"今日头条：\n\n1. 新闻一；\n\n2. 今日发生xxx事件\n\n3. 研究表明\n\n4. 新闻四\n\n5. 新闻五\n\n..."\"\""""
    # return_direct = True
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use the tool."""
        url= f"https://api.vvhan.com/api/60s?type=json"
        headers = {'Content-Type': 'text/json;charset=UTF-8',}
        return json.loads(requests.get(url, headers=headers).text)["data"]

    async def _arun(self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")
    
class chat_bot(BaseTool):
    name = "聊天机器人"
    description = f"这是一个默认工具选项，当客户问的内容不需要用到列表中其他所有工具，请你扮演chatGPT直接和用户对话。"\
                "如果你觉得Question中的不是一个问题，或者无法用列表中的任何工具解决时，"\
                "请你扮演chatGPT基于Question的内容有礼貌的对话，或者完成Question中的指令要求，"\
                "并把你输出的结果用/<中文/>作为the input to the action。不要用英语！"
    return_direct = True
    
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use the tool."""
        return query

    async def _arun(self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")

@CatchException
def new_predict(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
    
    # yield from update_ui(chatbot=chatbot, history=[]) # 刷新界面

    # Endpoint 重定向, 这里还要识别原始的endpoint不合理，回头改
    # 这个api base和openai的不兼容，nnd
    API_URL_REDIRECT, = get_conf("API_URL_REDIRECT")
    openai_endpoint = "https://api.openai.com/v1/chat/completions"
    if openai_endpoint in API_URL_REDIRECT: openai_endpoint = API_URL_REDIRECT[openai_endpoint]
    
    if not is_any_api_key(llm_kwargs['api_key']):
        chatbot.append(("你提供了错误的API_KEY。\n\n1. 临时解决方案：直接在输入区键入api_key，然后回车提交。\n\n2. 长效解决方案：在config.py中配置。"))
        yield from update_ui(chatbot=chatbot, history=[]) 
        return
    
    history.append(txt)
    chatbot.append([txt,"GPT思考中......请给它一点时间思考"])
    yield from update_ui(chatbot=chatbot, history=history) # 刷新界面

    #各种错误情况的打印没加
    #模型抽象和替换需要考虑
    #api_base的问题再想办法解决
    #llm = OpenAI(temperature=1, openai_api_base=openai_endpoint, openai_api_key=select_api_key(llm_kwargs['api_key'], llm_kwargs['llm_model']), proxies=proxies, streaming=True, TIMEOUT_SECONDS=TIMEOUT_SECONDS)
    #llm_math = LLMMathChain.from_llm(llm, verbose=True)
    langchain.debug = False
    llm = ChatOpenAI(temperature=0, openai_api_base="https://api.chatanywhere.com.cn/v1", openai_api_key=select_api_key(llm_kwargs['api_key'], llm_kwargs['llm_model']), proxies=proxies)
    # result = llm([HumanMessage(content=txt)])
    # stream_response =  gpt_say.iter_lines()

    # from langchain import OpenAI, LLMMathChain
    # llm_math = LLMMathChain.from_llm(llm, verbose=True)
    # result = llm_math.run("What is 13 raised to the .3432 power?")


    #from langchain.agents.agent_toolkits import create_python_agent
    # from langchain.tools.python.tool import PythonREPLTool
    # from langchain.python import PythonREPL
    from langchain.agents import initialize_agent
    from langchain.agents import load_tools
    from langchain.agents import Tool
    from langchain.agents import AgentType
    from langchain import OpenAI, LLMMathChain

    tools = load_tools(["llm-math"], llm=llm)
    tools.append(daily_news())
    tools.append(chat_bot())
    
    #agent的问题是，上下文太长，不能保持长久的上下文
    agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    try:
        result = agent.run(txt)
    except Exception as e:
        result = "对不起，我不知道。\n\n我目前能做的只有:\n\n<简单的数学题>\n\n<给你讲今天的新闻>\n\n<陪你聊聊天>"


    # print(result)
    # print(chatbot)

    history.append(result)
    chatbot[-1]=[history[-2], history[-1]]
    
    # chatbot.append(("这是什么功能？", "[Local Message] 请注意，您正在调用一个[函数插件]的模板，该函数面向希望实现更多有趣功能的开发者，它可以作为创建新功能函数的模板（该函数只有20多行代码）。此外我们也提供可同步处理大量文件的多线程Demo供您参考。您若希望分享新的功能模组，请不吝PR！"))
    yield from update_ui(chatbot=chatbot, history=history) # 刷新界面