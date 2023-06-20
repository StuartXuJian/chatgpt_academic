
##用于很长的prompt直接能写入core_functional.py中。
import re

def split_prompt_in_format(text):
    lines = text.split("\n")
    result = ""
    
    # 拆分每行文本并添加到结果中
    for line in lines:
        line = line.strip()  # 移除行首和行尾的空白字符
        if line:  # 检查行是否为空
            result += "r\"" + line + "\" +\n"
    
    # 移除最后一个加号和换行符
    result = result.rstrip(" +\n")
    
    return result

test_input = """
这是第一句话。
questioning and guide me step by step,
until I have found the root cause and preventive action.
hkkkk
how are you? 
"""

output = split_prompt_in_format(test_input)
print(output)