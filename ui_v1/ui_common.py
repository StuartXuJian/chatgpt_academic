import gradio as gr
import os

def GetCookies():
    cookies = gr.State({'api_key': API_KEY, 'llm_model': LLM_MODEL})
    return cookies

def check_gradio_version():
    if gr.__version__ not in ['3.28.3','3.32.2']:
        assert False, "Invalid gradio version, please make sure us command pip install -r requirements.txt install dependencies"

def InitializeLogging():
    import logging
    os.makedirs("gpt_log", exist_ok=True)
    try:logging.basicConfig(filename="gpt_log/chat_secrets.log", level=logging.INFO, encoding="utf-8")
    except:logging.basicConfig(filename="gpt_log/chat_secrets.log", level=logging.INFO)
    print("所有问询记录将自动保存在本地目录./gpt_log/chat_secrets.log, 请注意自我隐私保护哦！")

def GetCoreFunctional():
    from core_functional import get_core_functions
    return get_core_functions()

def GetCrazyFunctional():
    from crazy_functional import get_crazy_functions
    return get_crazy_functions()

