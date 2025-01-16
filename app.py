from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

# Game Routes
@app.route('/')
def home():
    return render_template('index.html')
# ----------------------------------------------------------------------------
@app.route('/pictionary')
def play_guessgame():
    return render_template('guess_rules.html')

@app.route('/runpictionary')
def run_guessgame():
    subprocess.run(["python", "folderguess/main.py"])
    return render_template('guess_rules.html')

# ----------------------------------------------------------------------------
@app.route('/snake')
def play_snakegame():
    return render_template('snake_rules.html')

@app.route('/runsnake')
def run_snakegame():
    subprocess.run(["python", "foldersnake/main.py"])
    return render_template('snake_rules.html')

# ----------------------------------------------------------------------------
@app.route('/pingpong')
def play_pinggame():
    return render_template('ping_rules.html')

@app.route('/runpingpong')
def run_pinggame():
    subprocess.run(["python", "folderping/main.py"])
    return render_template('ping_rules.html')

# ----------------------------------------------------------------------------
@app.route('/crossgame')
def play_crossgame():
    return render_template('cross_rules.html')

@app.route('/runcrossgame')
def run_crossgame():
    subprocess.run(["python", "foldercross/main.py"])
    return render_template('cross_rules.html')
# @app.route('/pingpong')
# def play_pingpong():
#     # Run ppong.py game (you can modify to use subprocess or directly integrate the game logic)
#     subprocess.run(["python", "ppong.py"])
#     return render_template('index.html')

# @app.route('/snake')
# def play_snake():
#     subprocess.run(["python", "snake.py"])
#     return render_template('index.html')

# @app.route('/guess')
# def play_guess():
#     subprocess.run(["python", "guessgem/guess.py"])
#     return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
