from PIL import Image
import random

from libs import helper
from libs.config import SERVER_PATH, STATIC_PATH

from app import setup

from MemeEngine import MemeGenerator



def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote """
    
    meme = MemeGenerator(SERVER_PATH+STATIC_PATH)
    
    try:
        if path is None or body is None or author is None:
            quotes, imgs = setup()
            path = random.choice(imgs)
            body = random.choice(quotes).body
            author = random.choice(quotes).author
    except Exception as e:
        print("Error generating random meme: " + str(e))
    else:
        out_path = meme.make_meme(path, body, author)
        img = Image.open(out_path)
        img.show()
        return out_path


if __name__ == "__main__":
    # Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = helper.build_parser()
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
