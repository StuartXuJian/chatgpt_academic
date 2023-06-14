import gradio as gr
from ui_v1.ui_common import check_gradio_version

class home_page:
    def __init__(self):
        check_gradio_version()
        self.title = "Home Page"
        self.description = "This is a home page"
        self.examples = [
            ["I love this app!"],
            ["I don't like this app."]
        ]
        self.interface = gr.Interface(
            fn=self.predict,
            inputs=gr.inputs.Textbox(lines=2, placeholder="Enter some text here ..."),
            outputs=gr.outputs.Textbox(),
            title=self.title,
            description=self.description,
            examples=self.examples,
            allow_flagging=False,
            allow_screenshot=False,
            allow_download=False,
            allow_share=False,
            theme="huggingface",
            layout="vertical",
            server_name=""
        )

    def launch(self):
        self.interface.launch()