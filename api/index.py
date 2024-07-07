from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

def text_to_sticker(text):
    width, height = 512, 512
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 100)
    text_width, text_height = draw.textsize(text, font=font)
    position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(position, text, fill="black", font=font)
    img.save('/tmp/sticker.png')

@app.route('/ttp', methods=['GET'])
def ttp():
    text = request.args.get('text', default='Hello World', type=str)
    text_to_sticker(text)
    return send_file('/tmp/sticker.png', mimetype='image/png')

if __name__ == '__main__':
    app.run()
