#舍弃原有的和LLM的POST方式，改为调用langchain来实现连接
from toolbox import CatchException, update_ui

import langchain
from langchain import OpenAI, LLMMathChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
)

from typing import Any, Dict, List, Union

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction, AgentFinish, LLMResult
import sys

# 读取时首先看是否存在私密的config_private配置文件（不受git管控），如果有，则覆盖原config文件
from toolbox import get_conf, update_ui, is_any_api_key, select_api_key, what_keys, clip_history, trimmed_format_exc
proxies, API_KEY, TIMEOUT_SECONDS, MAX_RETRY = \
    get_conf('proxies', 'API_KEY', 'TIMEOUT_SECONDS', 'MAX_RETRY')
 

#重写callback输出到页面打印
class StreamingUIOutCallbackHandler(BaseCallbackHandler):
    """Callback handler for streaming. Only works with LLMs that support streaming."""
    def __init__(self, input, chatbot, history):
        self.chatbot = chatbot
        self.history = history
        self.chatbot.append([input, ""])

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Run when LLM starts running."""

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run on new LLM token. Only available when streaming is enabled."""
        # sys.stdout.write(token)
        # sys.stdout.flush()
        print("token:"+token)
        #self.history += token  ##history 得补上
        
        self.chatbot[-1][-1] += token
        print(self.chatbot)
        #yield from update_ui(chatbot=self.chatbot, history=self.history) 
        # yield from update_ui(chatbot=self.chatbot, history=self.history)

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Run when LLM ends running."""

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Run when LLM errors."""

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Run when chain starts running."""

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        """Run when chain ends running."""

    def on_chain_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Run when chain errors."""

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> None:
        """Run when tool starts running."""

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        """Run on agent action."""
        pass

    def on_tool_end(self, output: str, **kwargs: Any) -> None:
        """Run when tool ends running."""

    def on_tool_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        """Run when tool errors."""

    def on_text(self, text: str, **kwargs: Any) -> None:
        """Run on arbitrary text."""

    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> None:
        """Run on agent end."""



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
    

    print(chatbot)
    #代理没添加，回头加
    #各种错误情况的打印没加
    #模型抽象和替换需要考虑
    #api_base的问题再想办法解决
    #llm = OpenAI(temperature=1, openai_api_base=openai_endpoint, openai_api_key=select_api_key(llm_kwargs['api_key'], llm_kwargs['llm_model']), proxies=proxies, streaming=True, TIMEOUT_SECONDS=TIMEOUT_SECONDS)
    #llm_math = LLMMathChain.from_llm(llm, verbose=True)
    langchain.debug = True
    chat = ChatOpenAI(temperature=1, openai_api_base="https://api.chatanywhere.com.cn/v1", openai_api_key=select_api_key(llm_kwargs['api_key'], llm_kwargs['llm_model']), streaming=True, callbacks=[StreamingUIOutCallbackHandler(txt, chatbot, history)])
    gpt_say = chat([HumanMessage(content=txt)])
    # stream_response =  gpt_say.iter_lines()

    #chatbot.append((resp.content))
    # chatbot.append([txt, gpt_say])
    # history.extend([txt, gpt_say])
    
    #llm_math.run("What is 13 raised to the .3432 power?")
    
    # chatbot.append(("这是什么功能？", "[Local Message] 请注意，您正在调用一个[函数插件]的模板，该函数面向希望实现更多有趣功能的开发者，它可以作为创建新功能函数的模板（该函数只有20多行代码）。此外我们也提供可同步处理大量文件的多线程Demo供您参考。您若希望分享新的功能模组，请不吝PR！"))
    yield from update_ui(chatbot=chatbot, history=history) # 刷新界面