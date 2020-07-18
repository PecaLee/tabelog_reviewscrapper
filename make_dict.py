from typing import Counter
from mecab import text_parsing


def comment_datas(data):
    comment_datas = []
    for dic in data:
        comment_datas.append(list(dic.values())[-1])
    return comment_datas


def wordsNVA(data):
    NVA = []
    for nva in data:
        parsed = text_parsing(nva)
        for word in parsed:
            NVA.append(word)
    return NVA


def make_dict(data):
    wording = wordsNVA(comment_datas(data))
    count = Counter(wording)
    words_counted = count.most_common()
    words_counted = dict(tuple(words_counted))
    return words_counted
