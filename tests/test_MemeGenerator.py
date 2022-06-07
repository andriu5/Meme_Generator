import os
import random
import unittest

from app import setup
from MemeEngine import MemeGenerator
import libs.config as cf

meme_test = MemeGenerator(cf.SERVER_PATH+cf.STATIC_PATH)
quotes, imgs = setup()

class TestMemeGenerator(unittest.TestCase):
    """TestMemeGenerator class tests the MemeGenerator class.
    """

    def test_crop_image(self):
        """TestMemeGenerator class test_crop_image method.
        """
        try:
            img = meme_test.crop_image(random.choice(imgs), 500)
        except Exception as e:
            print("Error cropping image: " + str(e))
        self.assertTrue(img is not None)
        self.assertTupleEqual(img.size, (500, 500))

    def test_make_meme(self):
        """TestMemeGenerator class test_make_meme method.
        """
        try:
            img = random.choice(imgs)
            quote = random.choice(quotes)
        except Exception as e:
            print("Error generating random meme: " + str(e))

        path = meme_test.make_meme(img, quote.body, quote.author)
        self.assertTrue(path is not None)
        self.assertTrue(os.path.isfile(path))
        extension = path.split('.')[-1]
        self.assertTrue(extension in ['jpg', 'png', 'jpeg'])
        os.remove(path)


if __name__ == '__main__':
    unittest.main()