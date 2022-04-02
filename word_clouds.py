'''
Creates words clouds for the top cutest categories based on the comments
    on posts with that animal.
'''
import ast
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def add_comments(animal, posts_for_animal):
    '''
    Adds all the comments for an animal into one big string.

    Args:
        animal: A string that represents an animal name.
        post_for_animal: A string that is the path to a
                txt file that has a dictionary that has
                all the posts sorted into which animal it is.
    Returns:
        text: A string that is all the comments for posts with that
            animal in it.
    '''
    text = ''
    with open(posts_for_animal, 'r', encoding='utf8') as animals_id:
        animals_dict = ast.literal_eval(str(animals_id.read()))
    # Adds every comment from the animal to the string.
    for post_id in animals_dict[animal]:
        with open(f'data/comments/{post_id}.txt', 'r', encoding='utf8')\
             as comment:
            text += str(comment.read())
    return text

def create_word_cloud(animal):
    '''
    Takes in an animal name and creates and shows a word cloud image
        of the most common words in the comments for posts
        with that animal.
    Args:
        animal: A string that is an animal name.
    '''
    text = add_comments(animal, 'data/animals_posts.txt')
    #Plots the word cloud and saves it to visualizations folder.
    plt.figure( figsize=(20,10) )
    word_cloud = WordCloud(width=1600, height=800).generate(text)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(f'visualizations/{animal}wordcloud.png')
    plt.show()
#Creates a word cloud for the top 4 cutest animals based on the bar graphs.
create_word_cloud('dog')
create_word_cloud('cat')
create_word_cloud('human')
create_word_cloud('bird')
