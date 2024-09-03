from flask import Flask, render_template

app = Flask(__name__)

players = [
    {"name": "Lionel Messi", "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Lionel-Messi-Argentina-2022-FIFA-World-Cup_%28cropped%29.jpg"},
    {"name": "Cristiano Ronaldo", "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg"},
    {"name": "Neymar Jr", "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Neymar_Jr._with_Al_Hilal%2C_3_October_2023_-_03_%28cropped%29.jpg"},
    {"name": "Kylian Mbappe", "image_url": "https://i.guim.co.uk/img/media/fbdc12e6cfe494deb66ae18f6f0e59b73bebd5b8/531_36_3108_1865/master/3108.jpg?width=465&dpr=1&s=none"},
    {"name": "Mohamed Salah", "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Mohamed_Salah_2018.jpg"},
    {"name": "Robert Lewandowski", "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/2019147183134_2019-05-27_Fussball_1.FC_Kaiserslautern_vs_FC_Bayern_M%C3%BCnchen_-_Sven_-_1D_X_MK_II_-_0228_-_B70I8527_%28cropped%29.jpg/800px-2019147183134_2019-05-27_Fussball_1.FC_Kaiserslautern_vs_FC_Bayern_M%C3%BCnchen_-_Sven_-_1D_X_MK_II_-_0228_-_B70I8527_%28cropped%29.jpg"},
    {"name": "Sergio Ramos", "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Sergio_Ramos_Interview_2021_%28cropped%29.jpg"},
]

@app.route("/")
def index():
    return render_template('index.html', players=players)

@app.route('/player/<int:index>')
def player(index):
    if 0 <= index < len(players):
        info = players[index]
        return render_template('player.html', player=info)
    
    return "Player not found", 404

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
