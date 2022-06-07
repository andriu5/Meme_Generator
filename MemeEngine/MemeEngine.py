import random
import textwrap
from PIL import Image, ImageDraw, ImageFont
import libs.config as cf


class MemeGenerator():
    """MemeGenerator class creates a meme using a given image adding a quote
    and a quote author to the image. 
    Finally, MemeGenerator class saves the meme to the given path.

    Argument:
        meme_directory (str) : Full path to save the meme.
    """


    def __init__(self, meme_directory: str) -> None:
        """MemeGenerator Object constructor.
        Argument:
            meme_directory (str) : Path to save the meme.
        """
        self.out_path = meme_directory
        self.quote_coordinates = (10, 30)
        self.fill=(255, 255, 255)
        self.stroke_width=2
        self.stroke_fill=(0,0,0)

    @staticmethod
    def crop_image(in_path: str, width: int = None) -> Image:
        """Creates a cropped image.
        Crop the image from image path 'path' according to the
        with given as 'width'.
        Argument:
            in_path (str) : Path to the input figure
            width (int) : Expected width of the output image
        """
        try:
            crop_img = Image.open(in_path)
            crop_img = crop_img.convert('RGB')
        except Exception:
            raise OSError('Invalid image path')

        try:
            ratio = width/float(crop_img.size[0])
            height = int(ratio * float(crop_img.size[1]))
        except Exception:
            raise OSError('Invalid image path')
        else:
            crop_img = crop_img.resize((width, height), Image.NEAREST)

        return crop_img

    def make_meme(self, in_path: str, text: str, author: str,
                  width: int = 500) -> str:
        """Creates a new Meme.
        Creates a meme with using a given image adding a quote
        and the quote author to the image. 
        Arguments:
            in_path (str) : Path of image to create meme.
            text (str) : Text to add on the caption.
            author (str) : Name of author.
            width (int) : Width of the new cropped image without changing
                          aspect ratio of the imput image.
        """
        new_meme = self.crop_image(in_path, width)

        draw = ImageDraw.Draw(new_meme)

        # Wrap the text
        try:
            font = ImageFont.truetype(
                            cf.SERVER_PATH+'/_data/fonts/impact/impact.ttf',
                            size=int(new_meme.size[1]/15))
        except Exception:
            raise OSError('Invalid font path')
        char_width, char_height = font.getsize('A')

        char_per_line = int(width/char_width)
        text_wrapped = textwrap.wrap(text, char_per_line)
        author_wrapped = textwrap.wrap('by ' + author, char_per_line)

        # Draw the text
        x, y = self.quote_coordinates
        for line in text_wrapped:
            line_width, line_height = font.getsize(line)
            x = (width - line_width) / 2
        
            draw.text((x,y),
                    line,
                    font=font,
                    fill=self.fill,
                    stroke_width=self.stroke_width,
                    stroke_fill=self.stroke_fill)
            y += line_height

        y = new_meme.size[1] - char_height * len(author_wrapped) - 40
        for line in author_wrapped:
            line_width, line_height = font.getsize(line)
            x = (width - line_width) / 2
            draw.text((x,y),
                line,
                font=font,
                fill=self.fill,
                stroke_width=self.stroke_width,
                stroke_fill=self.stroke_fill)
            y += line_height

        try:
            num=random.randrange(1,1000000)
            extension = 'png'
            meme_path = cf.SERVER_PATH+cf.STATIC_PATH+ \
                        'meme-{}.{}'.format(str(num),extension)
        except Exception:
            raise OSError('Unable to create meme')
        else:
            new_meme.save(meme_path)

        return meme_path