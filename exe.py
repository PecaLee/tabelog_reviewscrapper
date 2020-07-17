from scrapper import get_reviews
from save import save_to_file
from mecab import text_parsing


data = get_reviews()


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


wording = wordsNVA(comment_datas(data))


# save_to_file(data)
