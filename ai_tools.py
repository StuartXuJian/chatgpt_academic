#策略：仅推荐工作相关的AI工具
#策略：少而精，同类工具里只推荐最好用的

#建议每行内容不要超过20个字
#注意：换行不要用/n，用<br>
AI_Tool_list = {
        "common": [
            {
                "Name": "ChatGPT", 
                "Link": "https://chat.openai.com/", 
                "Brief_Usage": "目前最好的AI聊天机器人,你懂的", 
                "Charge": "需要注册。GPT3.5模型的chatGPT免费，调用API收费。<br>可付费升级为更强大的GPT4模型。", 
                "Stars": 5, 
                "Others": "国内需要科学上网方可访问。"
            },
            {
                "Name": "NewBing", 
                "Link": "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx", 
                "Brief_Usage": "微软AI搜索机器人", 
                "Charge": "需要注册。免费使用。", 
                "Stars": 5,  
                "Others": "国内需要科学上网方可访问。"
            },
            {
                "Name": "ChatPDF", 
                "Link": "https://www.chatpdf.com/?ref=futuretools.io", 
                "Brief_Usage": "PDF快速阅读器", 
                "Charge": "无需注册。免费使用。", 
                "Stars": 5,  
                "Others": "国内需要科学上网方可访问。<br>仅适用文字类PDF阅读。"
            },
            {
                "Name": "Deepl Translator", 
                "Link": "https://www.deepl.com/translator/files", 
                "Brief_Usage": "能直接翻译PPT,PDF,Word文档", 
                "Charge": "无需注册，免费使用。", 
                "Stars": 4,  
                "Others": ""
            },
            {
                "Name": "Notion AI", 
                "Link": "https://www.midjourney.com/auth/signin/", 
                "Brief_Usage": "目前最好的智能笔记本", 
                "Charge": "需注册，免费使用。", 
                "Stars": 5,  
                "Others": "名校大学学霸们的首选私人notebook"
            },
            {
                "Name": "Huemint", 
                "Link": "https://huemint.com/brand-intersection/", 
                "Brief_Usage": "智能配色工具 e.g. PBI, ppt", 
                "Charge": "无需注册，免费使用。", 
                "Stars": 5,  
                "Others": ""
            },
            {
                "Name": "GitMind", 
                "Link": "https://gitmind.cn/", 
                "Brief_Usage": "国产思维导图生成器", 
                "Charge": "需注册，收费使用。", 
                "Stars": 3,  
                "Others": ""
            },
        ],
        "image": [
                {
                    "Name": "MidJourney", 
                    "Link": "https://www.midjourney.com/auth/signin/", 
                    "Brief_Usage": "目前最好的图片生成器,设计师专属生产力工具", 
                    "Charge": "需注册，收费使用。", 
                    "Stars": 4,  
                    "Others": "本身国内可访问,但是依赖的Discord社区需要科学上网"
                },
                {
                    "Name": "Hama", 
                    "Link": "https://www.hama.app/", 
                    "Brief_Usage": "抹掉一些图上的杂物，比如水印", 
                    "Charge": "免费使用。", 
                    "Stars": 4,  
                    "Others": ""
                },
                {
                    "Name": "文心一格", 
                    "Link": "https://yige.baidu.com/", 
                    "Brief_Usage": "文字生成图片, e.g. PPT插图", 
                    "Charge": "可以直接用百度账号。有限免费使用额度。", 
                    "Stars": 3,  
                    "Others": ""
                },
            ],
    }


def generate_md_table(label):

    Tools_text = "| 工具（链接） | 特色功能 | 收费情况 | 上手星级 | 补充说明 |\n|------|-----|------|-------|-------|\n"
    for row in AI_Tool_list[label]:
        Tools_text += "| [{}]({}) | {} | {} | ".format(row["Name"], row["Link"], row["Brief_Usage"], row["Charge"])
        for i in range(row["Stars"]):
            Tools_text += "&#9733;"
        Tools_text += " | {} |\n".format(row["Others"])

    return Tools_text