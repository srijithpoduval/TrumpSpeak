from flask import Flask, request, render_template
from getTrumpTweet import find_closest_tweet
from gensim.models import KeyedVectors
import pickle

app = Flask(__name__)
google_model = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def my_form():
    return render_template('form.html',tweet="")

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    text = request.form['text']
    trump_tweet = find_closest_tweet(text, vectorizer, google_model)
    return render_template('form.html',tweet=trump_tweet)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
