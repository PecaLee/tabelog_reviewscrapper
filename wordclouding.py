# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def tabelog_wordcloud(words_counted):
    font_path = "./font/NotoSansJP-Bold.otf"
    wordcloud = WordCloud(
        font_path=font_path,
        width=800,
        height=800,
        background_color="white",
    )
    wordcloud = wordcloud.generate_from_frequencies(words_counted)

    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
