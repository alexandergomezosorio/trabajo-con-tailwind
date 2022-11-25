from flask import Flask

from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") 


@app.route('/grupoA')
def grupoA():
    return render_template("auth/grupoA.html")


@app.route('/grupoB')
def grupoB():
    return render_template("auth/grupoB.html")


@app.route('/grupoC')
def grupoC():
    return render_template("auth/grupoC.html")


@app.route('/grupoD')
def grupoD():
    return render_template("auth/grupoD.html")


@app.route('/grupoE')
def grupoE():
    return render_template("auth/grupoE.html")


@app.route('/grupoF')
def grupoF():
    return render_template("auth/grupoF.html")


@app.route('/grupoG')
def grupoG():
    return render_template("auth/grupoG.html")


@app.route('/grupoH')
def grupoH():
    return render_template("auth/grupoH.html")
if __name__ == "__main__":
    app.run(debug=True,port=3000)