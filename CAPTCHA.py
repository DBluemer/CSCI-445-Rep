import random
from captcha.image import ImageCaptcha
class CAPTCHA:
    def generateCaptcha(self):

        result_str = ''.join(
            (random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(5)))

        # Create an image instance of the given size
        image = ImageCaptcha(width=280, height=90)

        # Image captcha text will equal random result
        captcha_text = result_str

        # generate the image of the given text
        data = image.generate(captcha_text)

        # write the image on the given file and save it
        image.write(captcha_text, 'CAPTCHAman.png')
