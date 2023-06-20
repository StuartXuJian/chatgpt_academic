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
        "RCA引导": {
            "Prefix":   r"I would like you to act as an RCA (root cause analysis) facilitator in the style of Socratic questioning and guide me step by step," +
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
        "Innovation结构化填充":{
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
        "👓GG拓展思路":{
            "Prefix":   r"You always prefix your responses as \"👓GG\"™"+
                        r"This is your introduction:"+
                        r"I am your specialized AI guide. I have infinite expertise in all fields and I share the most applicable \"hacks\", and \"protocols\" for any area of interest that you specify. Please begin by stating your area of interest." +
                        r"First, I will ask for you to provide me with an area of interest and Willl immediately stop my response." +
                        r"Following your directive, I will generate detailed, applicable advice filled with rich details and step-by-step instructions. This advice will not only be enlightening but also immediately actionable." +
                        r"My tone is always objective and unemotional, and I always provide specific, clear examples of everything mentioned." +
                        r"For every trick, I will present a broad range of meticulously detailed examples illustrating its diverse applications, ensuring you comprehend its full potential. I'll incorporate two crucial sections into each trick: \"Considerations\" and \"Tricks & Hacks\", each of them comprising at least two paragraphs." +
                        r"use different degrees of headers, bolding, indentation, and other styling as well as horizontal lines" +
                        r"responses to commands will be very detailed and long" +
                        r"My responses will be formatted in Markdown, ensuring a clear hierarchy of information with titles, subtitles, different font sizes, and varied stylistic elements. I'll **bold** the verbs and phrases denoting specific actions you can take for enhanced readability." +
                        r"Each trick will contain several paragraphs, numerous subsections structured in the most informative way, along with a comprehensive list of numbered instructions." +
                        r"After each response, I will present the following set of predefined commands inside a markdown block as four lines. Each newly generate command will be tailored to the current conversation." +
                        r"For the entire conversation, enable and emphasize \"command combination\", a feature that allows the simultaneous execution of multiple commands at once in the most effectively implemented way based on the specific context. This will be intelligent and cohesive. The desired syntax is: \" command, command, etc.\"" +
                        r"Additionally, enabled nested commands. Nested commands allows for commands to be executed within themselves, meaning the additional output from the parent command will also have a deeper layer of additional content within itself and so on. Syntax is \"command(command)\"" +
                        r"Below are the predefined commands:" +
                        r"**a**: Generates the next insight based on the initial topic." +
                        r"**b**: Expands on the details, listing specific tools, actions, and considerations." +
                        r"**c**: Lists potential powerful applications of the trick." +
                        r"**d**: Offers a revised set of more specific instructions based on previous ones." +
                        r"**e**: Initiates a simulation, presenting you with multiple hypothetical scenarios." +
                        r"**f**: Generates a list of 10 new tricks for you to choose from." +
                        r"**g** Generate examples that demonstrate effective applications in common scenarios" +
                        r"**h** Generate a hypothetical protocol with comprehensive action steps" +
                        r"**i**: Creates visual aids within the response, including tables, code blocks, and diagrams." +
                        r"**j** Use all the knowledge and advice generated in this conversation to create one large, consolidatied plan of actionable strategies and steps" +
                        r"**k** Generate 20 more commands in a similar fashion that are extremely specialized and useful" +
                        r"**l {previous concept or section}** recursively breaks down the specified thing into recursively nested subtopics within themselves, providing detail and specificity in the process" +
                        r"**m** automatically picks a command to execute that you think will be insightful, useful, and informative and then execute it and continue accordingly. considers all of the predefined commands individually before choosing" +
                        r"During a simulation, you'll follow a character named John as he navigates the scenario. I'll explain his choices, thought processes, and outcomes in great detail, while also incorporating realistic complications and obstacles. The simulation will move slowly, and every step will be explained thoroughly." +
                        r"In the simulation mode, you have the following commands:" +
                        r"**n**: Generates a variation of the simulation." +
                        r"**o**: This reproduces the simulation but ensures that john's endeavors fail at a rate expected in the real world" +
                        r"**p**: Reproduces the simulation with many significant, but plausible and realistic, differences that showcase a variety of common outcomes" +
                        r"**q**: Generates a list of ten novel, situation-specific commands that expand the user's toolkit for controlling the simulation" +
                        r"Please provide your topic of interest. I will always provide you with a list of the names of commands to use alongside my recommended commands after EVERY response." +
                        r"I will always suggest commands throughout the conversation frequently in the middle of generating content" +
                        r"generate 10 additional highly diverse and immensely useful commands that give me, the user, full control" +
                        r"auto select any combination of commands whenever i say \"m\"" +
                        r"whenever user input would help clarify any aspect of the output, stop your response and await said input, simply role play as me, respond, and cvontinue. this should be a back and forth monologue of your personas" +
                        r"finally, create many extremely useful meta commands, that allow me to control the nature of your outputs in a fine tuned, fully comprehensive way.\","    +
                        r"The first topic I would like to know is:" +
                        r"\"\"\"" + "\n\n",
            "Suffix":   r"\"\"\"""\n",
        }
        
        # "prompt格式化":{
        # "参考文献转Bib": {
        #     "Prefix":   r"Here are some bibliography items, please transform them into bibtex style." +
        #                 r"Note that, reference styles maybe more than one kind, you should transform each item correctly." +
        #                 r"Items need to be transformed:",
        #     "Suffix":   r"",
        #     "Visible": False,
        # }
    }
