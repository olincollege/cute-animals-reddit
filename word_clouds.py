import ast
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def create_word_cloud(animal):
    '''
    '''
    text = ''
    with open('data/animals_posts.txt', 'r') as animals_id:
        animals_dict = ast.literal_eval(str(animals_id.read()))
    for post_id in animals_dict[animal]:
        comment = open(f"data/comments/{post_id}.txt", 'r')
        text += str(comment.read())
        comment.close()
    word_cloud = WordCloud().generate(text)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(f'visualizations/{animal}wordcloud.png')
create_word_cloud('dog')
create_word_cloud('cat')
create_word_cloud('human')
