import gradio as gr
from ui_v1.ui_common import check_gradio_version

class home_page:
    def __init__(self):
        check_gradio_version()

    def launch(self):
        self.interface.launch()