from flask import Flask, render_template, request, url_for

gif_list = ['https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3dxbWVjcWN2aWFsdWhvaXNteTN5Y2JoMHB5cG1sNWlyZDJyNzllbiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/pWVyMr2TXAgx1EitnT/giphy.webp', 'https://media1.giphy.com/media/QB6RCVtmaOSNQ51OcJ/giphy.webp?cid=790b7611swqmecqcvialuhoismy3ycbh0pypml5ird2r79en&ep=v1_gifs_search&rid=giphy.webp&ct=g', 'https://media3.giphy.com/media/eVC1QmtNKmud0vUWDk/giphy.webp?cid=790b7611swqmecqcvialuhoismy3ycbh0pypml5ird2r79en&ep=v1_gifs_search&rid=giphy.webp&ct=g', 'https://media3.giphy.com/media/RYy9eo2j78ZFx7Adom/200w.gif?cid=6c09b95296hl7bgm1iro7pb2hlna3ovk4461koclq9ah3tsg&ep=v1_internal_gif_by_id&rid=200w.gif&ct=g', ]

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])

def sackboy():
    dic = {
        'sackboy' : gif_list
    }
    if request.method == 'POST':
        query = request.form['query']
        if query not in dic:
            return "No data found for" + query
        return render_template('password.html', sackboy=dic['sackboy'])
    return render_template('password.html', url=url_for('sackboy'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)