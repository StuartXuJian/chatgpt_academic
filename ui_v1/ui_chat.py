import gradio as gr

class ChatBoxUI:
    def __init__(self):
        self.gr_L1 = lambda: gr.Row().style()
        self.gr_L2 = lambda scale: gr.Column(scale=scale)
        if LAYOUT == "TOP-DOWN":
            self.gr_L1 = lambda: DummyWith()
            self.gr_L2 = lambda scale: gr.Row()
            CHATBOT_HEIGHT /= 2
        pass
    
    def CurrentModelLabel(self):
        with self.gr_L2(scale=2):
            self.chatbot = gr.Chatbot(label=f"当前模型：{LLM_MODEL}")
            self.chatbot.style(height=CHATBOT_HEIGHT)
            self.history = gr.State([])

    def ChatInput(self):
        with gr.Accordion("输入区", open=True) as area_input_primary:
            # with gr.Row():
            #     gr.Markdown(r"[使用手册](https://confluence.ext.net.nokia.com/display/RCP/Working+tool+user+guide)")
            with gr.Row():
                self.txt = gr.Textbox(show_label=False, placeholder="Input question here.").style(container=False)
            with gr.Row():
                self.submitBtn = gr.Button("提交", variant="primary")
                self.submitBtnNew = gr.Button("进化版(测试中)", variant="primary")
            with gr.Row():
                self.resetBtn = gr.Button("重置", variant="secondary"); resetBtn.style(size="sm")
                self.stopBtn = gr.Button("停止", variant="secondary"); stopBtn.style(size="sm")
                self.clearBtn = gr.Button("清除", variant="secondary", visible=False); clearBtn.style(size="sm")
            with gr.Row():
                self.status = gr.Markdown(f"Tip: 按Enter提交, 按Shift+Enter换行。当前模型: {LLM_MODEL} \n {proxy_info}")

    def BasicFunctional(self):
        with gr.Accordion("基础功能区", open=True) as area_basic_fn:
            with gr.Row():
                for k in functional:
                    if ("Visible" in functional[k]) and (not functional[k]["Visible"]): continue
                    variant = functional[k]["Color"] if "Color" in functional[k] else "secondary"
                    functional[k]["Button"] = gr.Button(k, variant=variant)

    def PluginsFunctional(self):
        with gr.Accordion("函数插件区", open=False) as area_crazy_fn:
            with gr.Row():
                gr.Markdown("注意：以下“红颜色”标识的函数插件需从输入区读取路径作为参数.")
            with gr.Row():
                for k in crazy_fns:
                    if not crazy_fns[k].get("AsButton", True): continue
                    variant = crazy_fns[k]["Color"] if "Color" in crazy_fns[k] else "secondary"
                    crazy_fns[k]["Button"] = gr.Button(k, variant=variant)
                    crazy_fns[k]["Button"].style(size="sm")
            with gr.Row():
                with gr.Accordion("更多函数插件", open=True):
                    dropdown_fn_list = [k for k in crazy_fns.keys() if not crazy_fns[k].get("AsButton", True)]
                    with gr.Row():
                        self.dropdown = gr.Dropdown(dropdown_fn_list, value=r"打开插件列表", label="").style(container=False)
                    with gr.Row():
                        self.plugin_advanced_arg = gr.Textbox(show_label=True, label="高级参数输入区", visible=False, 
                                                        placeholder="这里是特殊函数插件的高级参数输入区").style(container=False)
                    with gr.Row():
                        self.switchy_bt = gr.Button(r"请先从插件列表中选择", variant="secondary")
            with gr.Row():
                with gr.Accordion("点击展开“文件上传区”。上传本地文件可供红色函数插件调用。", open=False) as area_file_up:
                    self.file_upload = gr.Files(label="任何文件, 但推荐上传压缩文件(zip, tar)", file_count="multiple")
        self.file_upload.upload(on_file_uploaded, [self.file_upload, self.chatbot, self.txt, self.txt2, self.checkboxes], [self.chatbot, self.txt, self.txt2])      

    def Settings(self):
        with gr.Accordion("更换模型 & SysPrompt & 交互界面布局", open=(LAYOUT == "TOP-DOWN")):
            self.system_prompt = gr.Textbox(show_label=True, placeholder=f"System Prompt", label="System prompt", value=initial_prompt)
            self.top_p = gr.Slider(minimum=-0, maximum=1.0, value=1.0, step=0.01,interactive=True, label="Top-p (nucleus sampling)",)
            self.temperature = gr.Slider(minimum=-0, maximum=2.0, value=1.0, step=0.01, interactive=True, label="Temperature",)
            self.max_length_sl = gr.Slider(minimum=256, maximum=4096, value=512, step=1, interactive=True, label="Local LLM MaxLength",)
            self.checkboxes = gr.CheckboxGroup(["基础功能区", "函数插件区", "底部输入区", "输入清除键", "插件参数区"], value=["基础功能区", "函数插件区"], label="显示/隐藏功能区")
            self.md_dropdown = gr.Dropdown(AVAIL_LLM_MODELS, value=LLM_MODEL, label="更换LLM模型/请求源").style(container=False)
            gr.Markdown(description)
    
    def BackupInput(self):
        with gr.Accordion("备选输入区", open=True, visible=False) as area_input_secondary:
            with gr.Row():
                self.txt2 = gr.Textbox(show_label=False, placeholder="Input question here.", label="输入区2").style(container=False)
            with gr.Row():
                self.submitBtn2 = gr.Button("提交", variant="primary")
            with gr.Row():
                self.resetBtn2 = gr.Button("重置", variant="secondary"); resetBtn2.style(size="sm")
                self.stopBtn2 = gr.Button("停止", variant="secondary"); stopBtn2.style(size="sm")
                self.clearBtn2 = gr.Button("清除", variant="secondary", visible=False); clearBtn2.style(size="sm")       

    def ChatInterface(self):
        with gr.Tab("基本功能区"):
            with self.gr_L1():
                self.CurrentModelLabel()
                with self.gr_L2(scale=1):
                    self.ChatInput()
                    self.BasicFunctional()
                    self.PluginsFunctional()
                    self.Settings()
                    self.BackupInput()
