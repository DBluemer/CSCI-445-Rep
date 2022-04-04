import random
from flask import Flask, render_template
from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha

app = Flask(__name__)


@app.route('/')
def generateCaptcha():
    return render_template('main.html')

@app.route('/getTextCaptcha', methods=['POST'])

def getTextCaptcha():
    result_str_image = ''.join(
        (random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(5)))
    image = ImageCaptcha(width=335, height=90)
    imageData = image.generate(result_str_image)
    image.write(result_str_image, result_str_image + '.png')
    return result_str_image

@app.route('/getAudioCaptcha', methods=['POST'])
def getAudioCaptcha():
    result_str_audio = ''.join(
        (random.choice('0123456789') for i in range(7)))
    audio = AudioCaptcha()
    audioData = audio.generate(result_str_audio)
    audio.write(result_str_audio, result_str_audio + '.wav')
    return result_str_audio

if __name__ == "__main__":
    app.run(debug=True)