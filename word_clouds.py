from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import ast

def create_word_cloud(animal):
    text = ''
    with open('data/animals_posts.txt', 'r') as animals_id:
        animals_dict = ast.literal_eval(str(animals_id.read()))
    for id in animals_dict[animal]:
        f = open(f"data/comments/{id}.txt", 'r')
        text += str(f.read())
        f.close()
    word_cloud = WordCloud().generate(text)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(f'visualizations/{animal}wordcloud.png')
create_word_cloud('dog')
create_word_cloud('cat')
create_word_cloud('human')