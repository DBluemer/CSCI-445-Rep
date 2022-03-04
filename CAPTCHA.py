pip install captcha
class CAPTCHA:
    # Import the following modules
    from captcha.image import ImageCaptcha
 
    # Create an image instance of the given size
    image = ImageCaptcha(width = 280, height = 90)
 
    # Image captcha text
    captcha_text = 'TeSt' 
 
    # generate the image of the given text
    data = image.generate(captcha_text) 
 
    # write the image on the given file and save it
    image.write(captcha_text, 'CAPTCHA.png')