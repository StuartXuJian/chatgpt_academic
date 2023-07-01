import gradio as gr

class AITools:
    def __init__(self):
        pass
    
    def AIToolsPage():
        with gr.Tab("AI工具"): 
            from ai_tools import AI_Tool_list
            from ai_tools import generate_md_table
            with gr.Tab("通用"):
                common_tools = generate_md_table("common")
                gr.Markdown(common_tools)
            with gr.Tab("文档处理"):
                doc_tools = generate_md_table("doc")
                gr.Markdown(doc_tools)
            with gr.Tab("图像视频"):
                image_tools = generate_md_table("image")
                gr.Markdown(image_tools)
