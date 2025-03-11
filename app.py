from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Obtém todas as imagens da pasta static/images
    imagens_pasta = os.path.join(app.static_folder, 'images')
    extensoes_permitidas = {'.jpg', '.jpeg', '.png', '.gif'}
    
    imagens = []
    for arquivo in os.listdir(imagens_pasta):
        ext = os.path.splitext(arquivo)[1].lower()
        if ext in extensoes_permitidas:
            imagem = {
                'nome': arquivo,
                'url': url_for('static', filename=f'images/{arquivo}')
            }
            imagens.append(imagem)
    
    return render_template('index.html', imagens=imagens)

@app.route('/foto/<nome_arquivo>')
def foto(nome_arquivo):
    return render_template('foto.html', nome_arquivo=nome_arquivo)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
