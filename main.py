from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/creator')
def creator():
    return render_template('creator.html')

@app.route('/belj_games_studio')
def beljGamesStudio():
    return render_template('belj_games_studio.html')

@app.route('/modpacks')
def modpacks():
    return render_template('modpacks.html')

@app.route('/smk')
def smk():
    return render_template('smk.html')


@app.route('/modpacks/7_days_to_die')
def game_7dtd():
    return render_template('games_list/7 days to die.html')

@app.route('/modpacks/lethal_company')
def game_lc():
    return render_template('games_list/lethal company.html')

@app.route('/modpacks/minecraft')
def game_m():
    return render_template('games_list/minecraft.html')

@app.route('/modpacks/project_zomboid')
def game_pz():
    return render_template('games_list/project zomboid.html')

@app.route('/modpacks/rimworld')
def game_r():
    return render_template('games_list/rimworld.html')

@app.route('/modpacks/stardew_valley')
def game_sv():
    return render_template('games_list/stardew valley.html')

@app.route('/modpacks/minecraft/test_modpack')
def mod1():
    return render_template('games_list/minecraft/test modpack.html')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')