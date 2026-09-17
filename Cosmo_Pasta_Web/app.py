from flask import Flask, render_template, jsonify

app = Flask(__name__)

RESTAURANT = {
    "name": "COSMO PASTA",
    "tagline": "Fresca. Espressa. Spaziale.",
    "address": "Piazza Mancini Battaglia 22, 95126 Catania CT",
    "phone": "+39 351 987 8796",
    "email": "cosmopastaita@gmail.com",
    "hours": "12:00–15:30 | 19:00–00:00",
    "website": "https://www.cosmopasta.eu/"
}

IMG = {
    "Pistacosmo":"pistacosmo.jfif", "Carbonaut":"Carbonaut.jfif", "Amatrix":"Amatrix.jfif",
    "Normoon":"normoon.jfif", "Ragùplanet":"Ragùplanet.jfif", "Redmoon":"redmoon.jfif", "PestoGalaxy":"PestoGalaxy.jfif",
    "Sardonauta":"Sardonauta.jfif", "Trapanix":"Trapanix.jfif", "CacioHole":"CacioHole.jfif",
    "ceres":"ceres.jfif", "coca":"coca cola.jfif", "cocazero":"coca cola 0.jfif",
    "moretti":"Birra moretti.jfif", "heineken":"heineken.jfif", "sprite":"sprite.jfif",
    "fanta":"fanta.jfif", "frizzante":"acqua frizzante.jfif", "lete":"acqua lete.jfif",
    "rigatini":"rigatini.jfif", "spaghetti":"spaghetti.jfif", "paccheri":"paccheri.jfif"
}

MENU = [
 {"category":"Pasta Fresca Espressa","items":[
  {"name":"Amatrix","description":"Guanciale di Norcia croccante, pelati di pomodoro, Pecorino Romano DOP, peperoncino e pepe nero.","price":8.00,"image":IMG["Amatrix"]},
  {"name":"Pistacosmo","description":"Pesto di pistacchio siciliano, guanciale di Norcia croccante, stracciatella fresca e polvere di pistacchio.","price":8.00,"image":IMG["Pistacosmo"]},
  {"name":"Normoon","description":"Salsa di pomodoro, melanzane fritte siciliane, ricotta salata, basilico fresco e olio EVO.","price":8.00,"image":IMG["Normoon"]},
  {"name":"Ragùplanet","description":"Ragù di carne bovino e suino, passata di pomodoro, Parmigiano Reggiano 24 mesi e olio EVO.","price":8.00,"image":IMG["Ragùplanet"]},
  {"name":"CacioHole","description":"Pecorino Romano DOP, Parmigiano Reggiano 24 mesi e pepe nero.","price":8.00,"image":IMG["CacioHole"]},
  {"name":"Redmoon","description":"Pomodori siciliani, olio EVO, basilico, Parmigiano Reggiano 24 mesi e burro.","price":8.00,"image":IMG["Redmoon"]},
  {"name":"Carbonaut","description":"Tuorlo d'uovo, guanciale di Norcia, Pecorino Romano DOP, Parmigiano Reggiano 24 mesi e pepe nero.","price":8.00,"image":IMG["Carbonaut"]},
  {"name":"Trapanix","description":"Pesto siciliano con mandorle, basilico, pomodori siciliani, olio EVO e pecorino romano DOP.","price":8.00,"image":IMG["Trapanix"]},
  {"name":"Sardonauta","description":"Sarde fresche siciliane, finocchietto, pinoli, uva passa, pomodoro, mollica tostata e olio EVO.","price":8.00,"image":IMG["Sardonauta"]},
  {"name":"PestoGalaxy","description":"Pesto di basilico fresco siciliano, pinoli, olio EVO siciliano e Grana Padano 24 mesi.","price":8.00,"image":IMG["PestoGalaxy"]}
 ]},
 {"category":"Pasta Sfusa","items":[
  {"name":"Rigatini Cosmici 1 kg","description":"Pasta fresca all'uovo con farine biologiche siciliane e uova bio.","price":9.80,"image":IMG["rigatini"]},
  {"name":"Spaghettoni Intergalattici 1 kg","description":"Pasta fresca all'uovo realizzata ogni giorno.","price":9.80,"image":IMG["spaghetti"]},
  {"name":"Paccheri Stellari 1 kg","description":"Pasta fresca all'uovo del laboratorio Cosmo Pasta.","price":9.80,"image":IMG["paccheri"]},
  {"name":"Tortellini Spaziali 1 kg","description":"Pasta fresca all'uovo da portare a casa.","price":9.80,"image":None}
 ]},
 {"category":"CosmoDrink","items":[
  {"name":"Coca-Cola 330 ml","description":"Lattina","price":2.50,"image":IMG["coca"]},
  {"name":"Coca-Cola Zero 330 ml","description":"Lattina","price":2.50,"image":IMG["cocazero"]},
  {"name":"Fanta 330 ml","description":"Lattina","price":2.50,"image":IMG["fanta"]},
  {"name":"Sprite 330 ml","description":"Lattina","price":2.50,"image":IMG["sprite"]},
  {"name":"Acqua naturale 50 cl","description":"","price":1.50,"image":IMG["lete"]},
  {"name":"Acqua frizzante 50 cl","description":"","price":1.50,"image":IMG["frizzante"]},
  {"name":"Acqua Lete 50 cl","description":"","price":1.50,"image":IMG["lete"]}
 ]},
 {"category":"CosmoBeer","items":[
  {"name":"Ceres Strong Ale","description":"Birra ad alta gradazione.","price":4.00,"image":IMG["ceres"]},
  {"name":"Heineken","description":"Birra internazionale.","price":3.50,"image":IMG["heineken"]},
  {"name":"Moretti","description":"Birra italiana classica.","price":3.00,"image":IMG["moretti"]},
  {"name":"Messina Cristalli di Sale","description":"Birra siciliana con cristalli di sale.","price":3.50,"image":None}
 ]}
]

@app.get("/")
def home():
    return render_template("index.html", restaurant=RESTAURANT, menu=MENU)

@app.get("/api/menu")
def menu_api():
    return jsonify(MENU)

if __name__ == "__main__":
    app.run(debug=True)
