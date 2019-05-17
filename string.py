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

def ngram(seq, n):
    return [(seq[i:i+n])for i, j in enumerate(seq)if len(seq[i:i+n]) == n]

if __name__ == "__main__":
    words = "I am an NLPer"
    list_ = words.split(" ")
    ans_word = ngram(words, 2)
    ans_list = ngram(list_, 2)
    print(ans_word, ans_list)
