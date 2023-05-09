# [step 1]>> 例如： API_KEY = "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" （此key无效）
API_KEY = "sk-此处填API密钥"    # 可同时填写多个API-KEY，用英文逗号分割，例如API_KEY = "sk-openaikey1,sk-openaikey2,fkxxxx-api2dkey1,fkxxxx-api2dkey2"

# [step 2]>> 改为True应用代理，如果直接在海外服务器部署，此处不修改
USE_PROXY = True
if USE_PROXY:
    # 填写格式是 [协议]://  [地址] :[端口]，填写之前不要忘记把USE_PROXY改成True，如果直接在海外服务器部署，此处不修改
    # 例如    "socks5h://localhost:11284"
    # [协议] 常见协议无非socks5h/http; 例如 v2**y 和 ss* 的默认本地协议是socks5h; 而cl**h 的默认本地协议是http
    # [地址] 懂的都懂，不懂就填localhost或者127.0.0.1肯定错不了（localhost意思是代理软件安装在本机上）
    # [端口] 在代理软件的设置里找。虽然不同的代理软件界面不一样，但端口号都应该在最显眼的位置上

    # 代理网络的地址，打开你的*学*网软件查看代理的协议(socks5/http)、地址(localhost)和端口(11284)
    proxies = {
        #          [协议]://  [地址]  :[端口]
        "http": "http://10.144.1.10:8080",
        "https": "https://10.144.1.10:8080",
    }
else:
    proxies = None

# [step 3]>> 多线程函数插件中，默认允许多少路线程同时访问OpenAI。Free trial users的限制是每分钟3次，Pay-as-you-go users的限制是每分钟3500次
# 一言以蔽之：免费用户填3，OpenAI绑了信用卡的用户可以填 16 或者更高。提高限制请查询：https://platform.openai.com/docs/guides/rate-limits/overview
DEFAULT_WORKER_NUM = 3


# [step 4]>> 以下配置可以优化体验，但大部分场合下并不需要修改
# 对话窗的高度
CHATBOT_HEIGHT = 1115

# 代码高亮
CODE_HIGHLIGHT = True

# 窗口布局
LAYOUT = "LEFT-RIGHT"  # "LEFT-RIGHT"（左右布局） # "TOP-DOWN"（上下布局）
DARK_MODE = True  # "LEFT-RIGHT"（左右布局） # "TOP-DOWN"（上下布局）

# 发送请求到OpenAI后，等待多久判定为超时
TIMEOUT_SECONDS = 30

# 网页的端口, -1代表随机端口
WEB_PORT = 18888

# 如果OpenAI不响应（网络卡顿、代理失败、KEY失效），重试的次数限制
MAX_RETRY = 2

# OpenAI模型选择是（gpt4现在只对申请成功的人开放，体验gpt-4可以试试api2d）
#LLM_MODEL = "gpt-3.5-turbo" # 可选 ↓↓↓
LLM_MODEL = "newbing" # 可选 ↓↓↓
AVAIL_LLM_MODELS = ["gpt-3.5-turbo", "api2d-gpt-3.5-turbo", "gpt-4", "api2d-gpt-4", "chatglm", "newbing"]

# 本地LLM模型如ChatGLM的执行方式 CPU/GPU
LOCAL_MODEL_DEVICE = "cpu" # 可选 "cuda"

# 设置gradio的并行线程数（不需要修改）
CONCURRENT_COUNT = 100

# 加一个看板娘装饰
ADD_WAIFU = False

# 设置用户名和密码（不需要修改）（相关功能不稳定，与gradio版本和网络都相关，如果本地使用不建议加这个）
# [("username", "password"), ("username2", "password2"), ...]
AUTHENTICATION = []

# 重新URL重新定向，实现更换API_URL的作用（常规情况下，不要修改!!）
# （高危设置！通过修改此设置，您将把您的API-KEY和对话隐私完全暴露给您设定的中间人！）
# 格式 {"https://api.openai.com/v1/chat/completions": "在这里填写重定向的api.openai.com的URL"} 
# 例如 API_URL_REDIRECT = {"https://api.openai.com/v1/chat/completions": "https://ai.open.com/api/conversation"}
API_URL_REDIRECT = {}

# 如果需要在二级路径下运行（常规情况下，不要修改!!）（需要配合修改main.py才能生效!）
CUSTOM_PATH = "/"

# 如果需要使用newbing，把newbing的长长的cookie放到这里
NEWBING_STYLE = "creative"  # ["creative", "balanced", "precise"]
NEWBING_COOKIES = """
SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=0ABA73731FB04118B169144F4E812EB5&dmnchg=1; MicrosoftApplicationsTelemetryDeviceId=2ec87f16-b50d-45ce-9795-def5ef7af543; ANON=A=738D0964B0831D21B56A734AFFFFFFFF&E=1c09&W=1; NAP=V=1.9&E=1baf&C=34N63ATaSxF8gQDfbX9Y8D7DFAE3zk8j5VzKCYpe7n4qmT8bAnHP4A&W=1; PPLState=1; _EDGE_V=1; SnrOvr=X=rebateson; ANIMIA=FRE=1; _UR=TQS=0&QS=0; MMCASM=ID=738330B9DD6B4977AB1E13961984BCDA; BCP=AD=1&AL=1&SM=1; GI_FRE_COOKIE=gi_prompt=1; _TTSS_IN=hist=WyJ6aC1IYW5zIiwiZW4iLCJhdXRvLWRldGVjdCJd; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnMiXQ==; _tarLang=default=zh-Hans; _clck=ii1emg|1|fav|0; ABDEF=V=13&ABDV=11&MRNB=1683262740226&MRB=0; USRLOC=HS=1&ELOC=LAT=60.2199592590332|LON=24.772729873657227|N=Espoo%2C%20Uusimaa|ELT=1|; SUID=A; MUID=3C1ECA382AF662873746D9342BB563AB; MUIDB=3C1ECA382AF662873746D9342BB563AB; _HPVN=CS=eyJQbiI6eyJDbiI6MTMsIlN0IjoyLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjEzLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjoxMywiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wNS0wOVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6NzB9; SRCHUSR=DOB=20230330&T=1683615681000&POEX=W; _EDGE_S=SID=2A5AB92E015066562260AA22009067CD&mkt=en-fi; ipv6=hit=1683619287482&t=4; KievRPSSecAuth=FABiBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACE7uggtAjFPwIARxJGISJHE7JkTKTPHhjLkrnV8OpSbv3ur/TXs0dl1D1LK84dgZwJrOZPcO2g9wNGWL2jEP/Qym81nwkmn/wg6pzsRcVGJp5CxIQIcDELw7m2yZ8+vfJvhwVgaVhz7Lqt4OG9O3AYuzU0xt+0TMX0z8bsIBijIOLAk6LO2P/OBtMT8ljbQWaC2HHFVdbJ6wuzKBOJM6w+aBbz1H7kSEZj+eIEM4ktlZBKP4wan/Fu8xBuzHN8cqJkdG4QSpouzeAN5gy9+wiemF1gs7wMRM56cH6pIVY5VkKYlz+lSYGHqd+svS+gSFJnOHfYp9NYAHgfgvj/nOikdgCnnj1BHT5U/pE+Au9A63LtExFbN9g31gO9KcjytLkD72aOgHI0gUw1Eb7lcHnRIkXy/cOVgY6aNx7ZAmWH5bBxIww9Vwh5Ochagm8n2Zl2huy3pGbvOTFx2nL+4xz+4o0QITNQNQ8ewR3uJzaaaWqAPxoFXLJ6WbsfGeNHcjkdYwPtZajl5Llg8MCMzm8XpJdg/YCtOiHvuW8r/2oB9RkC0gnZQx59YesmWouLnCBrolbQ9Fgb1gXJqJnK3ABV4BmeTm7JBh6Nx6YKjIUC334RcNntH7pyNSdkgCJOqQ0/GYFizl0kBGQTsQqBLePdlKnjdVLpHbFJzeL889U3z2RfZWgkNYnkonZELqCsy3nyUD/JGmENsI0daSvYqS59el4jOTOBOzshcbc1krvV7kaKRETdpv/0/qTlW51NeTzoN/GA525Q3oNnUvwjvGD8UBRy5UtPxVA3symAr+KWYKZi77K+yI1vtAsbVOW1C9sPzPUinQAA02Yi5dyMl51BnCpxoANGyAql1DeD49i0rcNBV5lv6reejF2NQazVxEbZckYcKgn64YfIXXp7Rr2ybQzR5iP0roKCVnoIgCCo4X1h1iYbp4FgYWuKHhNoh6PjrFVA24Upx/YUMH3s5ChM6hiPVL7zu5T4x8olcuhISVAQS+HYKbw6ui5CHElDfCn/CRzN8cJvD34FALv98p8xDJgNMozgpa/VUjxOU7kLKX5uABB/4tuZgZSAt3IT0PGt4oq8bnka7iklhHOjyFA9VCuBlkYwYBLSyv4LF15SPV8QtAiipgNWTWgNHqUcqIxUqlsEuCpefawZgQn09BhfkTQ7SPT1Z9lMoRPm8kO0/pDXh4A2iYZ6YVJbxEKiJAnLBxKokrDRjCNlK8kN2UtOGp15HiqZbUIw5M0U1wiy2pxDXjr5jKTr8aDWtwWKzLajchh7RAjlEJpd8XWUlE4a5vQrV5HfCvaix0qVNgz+9jMNo5d5Jfhdw6qdBxWQq/1mLZeh6xpgCop+8M5/FTAXg+y34q493iTJCY2iM9Y0Km//mf2Rhtm5rerm69cwDYvwt8Vzwnpwm5sNsUAPBzmyc5EeIL9bOhnLJ+ZmEpO9h/; _U=1ifa6I2O_TOjscvcEwNQY06OxCquVP9h8Cfc94wrWjWPB_i9Maw4GJ8LpyA-FLlPW-JGsyVbirxhJmz9GQTQ30-MxbDsuEGUEFEdEmc40F82RMx3HqjpqjLMKA_3O9Bdts4B0aAGLmPNyiDFHDzAGCOgB9VuQJ0JRq72hnkBSJaxoGw5SsTyMGSjyHTqaQ54hG4Yj3JumL7UtTiC9ztiODQ; WLS=C=08fc46246a3ace63&N=Jian; ai_session=62VHrdbVfdUnzq6zeKCl76|1683615688654|1683615757910; WLID=LLLaoLC66MdWMoFju0ZBAzmeRKdufNL6rVHus3AIIVu9vlbKLZ0zU4wae9rmCvcVaBfMllcLQmNvPF5H+1ZClOyQMB9GQbxfTUDbsXJbqso=; _SS=SID=2A5AB92E015066562260AA22009067CD&R=729&RB=729&GB=0&RG=0&RP=729; _RwBf=ilt=2&ihpd=1&ispd=1&rc=729&rb=729&gb=0&rg=0&pc=729&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=2&l=2023-05-09T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=bingcopilotwaitlist&c=MY00IA&t=1633&s=2023-02-24T02:26:55.8093895+00:00&ts=2023-05-09T07:02:41.5691845+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&r=1&mta=0&e=VZWrKG1Y1XAydR1VEoNmtpHacsrNthXnfxcniQ6i4vfpgkN4cWIUnW9uoa6PT7wg1e5WM-DfTx2mrNf1f9bMBw&A=738D0964B0831D21B56A734AFFFFFFFF&mte=0; OID=AhAjKTTqmv0mKGld2OUmFFwMF10aE2riVg_Vm-aRhpu1h2837uc6ydAp2ZEkYHtUjKBLL3Lj9d1ToGSScL3kbkHN; dsc=order=ShopOrderNewsOverShop; SRCHHPGUSR=BRW=NOTP&BRH=M&CW=328&CH=838&SCW=1164&SCH=3220&DPR=1.3&UTC=480&DM=0&SRCHLANG=en&PV=10.0.0&PRVCW=895&PRVCH=838&EXLTT=31&HV=1683615763&WTS=63819211871&cdxtone=Balanced&cdxtoneopts=galileo&BZA=0
"""
