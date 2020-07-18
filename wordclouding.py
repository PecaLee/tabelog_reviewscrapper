# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def remove_word_from_dict(words_counted):
    counted_words_dict = words_counted
    stopwords = ["ある", "いる", "あ", "い", "の", "する", "ます", "ｗ", "www", "ｗｗｗ"]
    for stopword in stopwords:
        try:
            counted_words_dict.pop(stopword)
        except:
            pass

    return counted_words_dict


def tabelog_wordcloud(words_counted):
    keywords = remove_word_from_dict(words_counted)
    font_path = "./font/NotoSansJP-Bold.otf"
    wordcloud = WordCloud(
        font_path=font_path,
        width=800,
        height=800,
        background_color="white",
    )
    wordcloud = wordcloud.generate_from_frequencies(keywords)

    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
