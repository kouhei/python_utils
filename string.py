"""
文字列操作系
"""
from copy import deepcopy

def zen_num_to_han_num(text):
    """文字列中の全角数字を半角数字に"""
    text = deepcopy(text)
    zen_nums = ["０","１","２","３","４","５","６","７","８","９"]
    for i, zen_num in enumerate(zen_nums):
        text = text.replace(zen_num,str(i))
    return text