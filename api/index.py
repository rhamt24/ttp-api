from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

def text_to_sticker(text):
    width, height = 512, 512
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Path ke file font
    font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'Roboto-Regular.ttf')
    
    # Load font
    font = ImageFont.truetype(font_path, 100)
    
    # Ukuran teks
    text_width, text_height = draw.textsize(text, font=font)
    
    # Posisi tengah gambar untuk teks
    position = ((width - text_width) // 2, (height - text_height) // 2)
    
    # Gambar teks di tengah gambar
    draw.text(position, text, fill="black", font=font)
    
    # Simpan gambar sebagai file PNG sementara
    temp_image_path = '/tmp/sticker.png'
    img.save(temp_image_path)
    
    return temp_image_path

@app.route('/ttp', methods=['GET'])
def ttp():
    # Ambil teks dari parameter GET
    text = request.args.get('text', default='Hello World', type=str)
    
    # Buat stiker berdasarkan teks yang diberikan
    sticker_path = text_to_sticker(text)
    
    # Kirim file stiker sebagai respons
    return send_file(sticker_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
