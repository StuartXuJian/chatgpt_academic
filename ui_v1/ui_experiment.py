import gradio as gr

class UIExperiment:
    def __init__(self):
        pass
    
    def launch(self):
        with gr.Tab("开发者试验田"):   
            with gr.Row():
                with gr.Column():
                    gr.Markdown(f"生成图提示词（需要先录入openAI Key）：")
                    txt2img_txt = gr.Textbox(show_label=False, placeholder="Input for image generation.", label="img_prompt").style(container=False)
                
            with gr.Row():
                image_input_a = gr.Image()
                image_output_a = gr.Image()

            with gr.Row():
                flip_button = gr.Button("翻转图片")
                text2img_button = gr.Button("文字生图")
                #img2img_button = gr.Button("图片变幻")
        
        import numpy as np
        flip_button.click(lambda x: np.fliplr(x), inputs=image_input_a, outputs=image_output_a)
        from request_llm.bridge_chatgpt import txt2img
        from request_llm.bridge_chatgpt import img2img
        text2img_button.click(txt2img, inputs=[txt2img_txt, cookies], outputs=image_output_a)
        #img2img_button.click(img2img, inputs=[image_input_a, cookies], outputs=image_output_a)