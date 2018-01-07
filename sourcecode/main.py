from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/home/")
def home():
  return render_template('home.html'), 200

@app.route("/genres/")
def genres():
  return render_template('genres.html'), 200

@app.route("/year/")
def year():
  return render_template('year.html'), 200

@app.route("/horror/")
def horror():
  return render_template('horror.html'), 200

@app.route("/scifi/")
def scifi():
  return render_template('scifi.html'), 200

@app.route("/comedy/")
def comedy():
  return render_template('comedy.html'), 200

@app.route("/action/")
def action():
  return render_template('action.html'), 200

@app.route("/shining/")
def shining():
  return render_template('shining.html'), 200

@app.route("/ring/")
def ring():
  return render_template('ring.html'), 200

@app.route("/bladerunner/")
def bladerunner():
  return render_template('bladerunner.html'), 200

@app.route("/matrix/")
def matrix():
  return render_template('matrix.html'), 200

@app.route("/up/")
def up():
  return render_template('up.html'), 200

@app.route("/toystory/")
def toystory():
  return render_template('toystory.html'), 200

@app.route("/bright/")
def bright():
  return render_template('bright.html'), 200

@app.route("/spiderman/")
def spiderman():
  return render_template('spiderman.html'), 200

@app.route("/")
def blank():
  return redirect(url_for('home'))


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
