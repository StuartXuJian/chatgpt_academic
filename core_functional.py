# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
# 默认按钮颜色是 secondary
from toolbox import clear_line_break


def get_core_functions():
    return {
        # "英语学术润色": {
        #     # 前言
        #     "Prefix":   r"Below is a paragraph from an academic paper. Polish the writing to meet the academic style, " +
        #                 r"improve the spelling, grammar, clarity, concision and overall readability. When necessary, rewrite the whole sentence. " +
        #                 r"Furthermore, list all modification and explain the reasons to do so in markdown table." + "\n\n",
        #     # 后语
        #     "Suffix":   r"",
        #     "Color":    r"secondary",    # 按钮颜色
        # },
        # "中文学术润色": {
        #     "Prefix":   r"作为一名中文学术论文写作改进助理，你的任务是改进所提供文本的拼写、语法、清晰、简洁和整体可读性，" +
        #                 r"同时分解长句，减少重复，并提供改进建议。请只提供文本的更正版本，避免包括解释。请编辑以下文本" + "\n\n",
        #     "Suffix":   r"",
        # },
        "查找语法错误": {
            "Prefix":   r"Can you help me ensure that the grammar and the spelling is correct? " +
                        r"Do not try to polish the text, if no mistake is found, tell me that this paragraph is good." +
                        r"If you find grammar or spelling mistakes, please list mistakes you find in a two-column markdown table, " +
                        r"put the original text the first column, " +
                        r"put the corrected text in the second column and highlight the key words you fixed.""\n"
                        r"Example:""\n"
                        r"Paragraph: How is you? Do you knows what is it?""\n"
                        r"| Original sentence | Corrected sentence |""\n"
                        r"| :--- | :--- |""\n"
                        r"| How **is** you? | How **are** you? |""\n"
                        r"| Do you **knows** what **is** **it**? | Do you **know** what **it** **is** ? |""\n"
                        r"Below is a paragraph from an academic paper. "
                        r"You need to report all grammar and spelling mistakes as the example before."
                        + "\n\n",
            "Suffix":   r"",
            "PreProcess": clear_line_break,    # 预处理：清除换行符
        },
        # "中译英": {
        #     "Prefix":   r"Please translate following sentence to English:" + "\n\n",
        #     "Suffix":   r"",
        # },
        # "学术中英互译": {
        #     "Prefix":   r"I want you to act as a scientific English-Chinese translator, " +
        #                 r"I will provide you with some paragraphs in one language " +
        #                 r"and your task is to accurately and academically translate the paragraphs only into the other language. " +
        #                 r"Do not repeat the original provided paragraphs after translation. " +
        #                 r"You should use artificial intelligence tools, " +
        #                 r"such as natural language processing, and rhetorical knowledge " +
        #                 r"and experience about effective writing techniques to reply. " +
        #                 r"I'll give you my paragraphs as follows, tell me what language it is written in, and then translate:" + "\n\n",
        #     "Suffix": "",
        #     "Color": "secondary",
        # },
        # "英译中": {
        #     "Prefix":   r"翻译成地道的中文：" + "\n\n",
        #     "Suffix":   r"",
        # },
        # "找图片": {
        #     "Prefix":   r"我需要你找一张网络图片。使用Unsplash API(https://source.unsplash.com/960x640/?<英语关键词>)获取图片URL，" +
        #                 r"然后请使用Markdown格式封装，并且不要有反斜线，不要用代码块。现在，请按以下描述给我发送图片：" + "\n\n",
        #     "Suffix":   r"",
        # },
        "解释代码": {
            "Prefix":   r"请解释以下代码：" + "\n```\n",
            "Suffix":   "\n```\n",
        },
        "RCA": {
            "Prefix":   r"I would like you to act as an RCA (root cause analysis) facilitator and guide me step by step," +
                        r"until I have found the root cause and preventive action. " +  
                        r"I would like you to speak in Chinese, and wait for my answer after one step asking." +
                        r"I expect your question if you don't think my answer is reasonable. " +  
                        r"I need you act in below steps, step by step, start since step 2:""\n" +
		                r"{Step 1}: I will state the {problem} in this message.""\n" +
		                r"{Step 2}: You ask me: \"Why did the problem occur of {problem}?\" and wait for my answer.""\n" +
		                r"{Step 3}: Once I've come up with a potential reason, you ask \"why you have made that happen?\" and wait for my answer.""\n" +
		                r"{Step 4}: Repeat {Step 3} again and again until the problem has been located in development process, tool or people issue which we can improve.""\n" + 
                        r"{Step 5}: I will answer if I have the idea to improve and avoid similar case," + 
                        r"and you will go to {step 3} if I don't have good idea, or provide some long-term preventive suggestion by changing the process," + 
                        r"or provide some long-term preventive suggestion by changing the process," + 
                        r"instead of resolving the problem this time only, if I have already some ideas.""\n" +
                        r"{Step 6}: You summary the preventive action list we have agreed.""\n" +
		                r"The {problem} in {Step 1} I would like to state is:" +
                        r"\"\"\"" + "\n\n",
            "Suffix":   r"\"\"\"",
        },
        # "EDA": {
        #     "Prefix":   r"I would like you to act as an innovation specialist. " + 
        #                 r"I will share with you my draft idea and you will provide a structured analytic report for all subjects below" + 
        #                 r", one bullet for one point, with a minimum of 400 words. Please provide the report in English.""\n" +
		#                 r"0. Title: Please provide a summary of the idea in 15 words or less.""\n" +
		#                 r"1. Innovation Point: Compare the idea to existing methods and describe the normal process. Include at least two points of comparison.""\n" +
		#                 r"2. Background: Describe at least two problems that this idea can resolve.""\n" +
		#                 r"3. Benefits and Impact Scope: Quantify the value of the idea based on hypothesis, and provide at least three points of impact." + 
        #                 r"Identify user scenarios to illustrate the scope of impact.""\n" +
		#                 r"4. Solution Introduction: Provide a detailed explanation of how the idea can be implemented, including a feasibility assessment.""\n" +
		#                 r"The first idea I would like to propose is:" +
        #                 r"" + "\n\n",
        #     "Suffix":   r"",
        # },
        "Innovation idea":{
            "Prefix":   r"I would like you to act as an innovation specialist. " + 
                        r"I will share with you my draft idea and you will provide a structured analytic report for all subjects below" + 
                        r", one bullet for one point, with a minimum of 400 words. Please provide the report in English.""\n" +
		                r"0. Title: Please provide a summary of the idea in 15 words or less.""\n" +
		                r"1. Innovation Point: Compare the idea to existing methods and describe the normal process. Include at least two points of comparison.""\n" +
		                r"2. Background: Describe at least two problems that this idea can resolve.""\n" +
		                r"3. Benefits and Impact Scope: Quantify the value of the idea based on hypothesis, and provide at least three points of impact." + 
                        r"Identify user scenarios to illustrate the scope of impact.""\n" +
		                r"4. Solution Introduction: Provide a detailed explanation of how the idea can be implemented, including a feasibility assessment.""\n" +
		                r"The first idea I would like to propose is:" +
                        r"\"\"\"" + "\n\n",
            "Suffix":   r"\"\"\"",
        },
    }
