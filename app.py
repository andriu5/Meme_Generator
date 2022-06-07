import random
import os
import requests
from flask import Flask, render_template, abort, request

# Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor
from MemeEngine import MemeGenerator

import libs.config as cf

app = Flask(__name__)

meme = MemeGenerator(cf.SERVER_PATH+cf.STATIC_PATH)


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable

    quotes = []
    for quote_file in quote_files:
        try:
            quotes.extend(Ingestor.parse(quote_file))
        except Exception as e:
            print("Error parsing file: " + quote_file + " due to: " + str(e))

    images_path = "./_data/photos/dog/"

    # Use the python's standard library os class to find all
    # images within the images images_path directory
    try:
        imgs = os.listdir(images_path)
        imgs = [images_path + img for img in imgs if img.endswith('.jpg')]
    except FileNotFoundError:
        imgs = []
        raise Exception("Could not find images directory: " + images_path)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    try:
        img = random.choice(imgs)
        quote = random.choice(quotes)
    except Exception as e:
        print("Error generating random meme: " + str(e))

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    num=random.randrange(1,1000000)
    extension = image_url.split('.')[-1]
    temp = cf.SERVER_PATH+cf.TMP_PATH+'tmp-{}.{}'.format(str(num),extension)
    with open(temp, 'wb') as handle:
        response = requests.get(image_url, stream=True)
        if not response.ok:
            print(response)
            abort(response.status_code)
        handle.write(response.content)

    path = meme.make_meme(request.form['image_url'], request.form['body'], request.form['author'])

    os.remove(temp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
