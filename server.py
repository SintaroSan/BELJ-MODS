from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from forms.user import RegisterForm, LoginForm
from data.users import User
from data.mods import Mods
from data import db_session

app = Flask(__name__)
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).filter(User.id == int(user_id)).first()


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init("db/testMods.db")
    app.run(port=8080, host='127.0.0.1')


def transform_name(name: str) -> str:
    return '_'.join(name.lower().split())


def uncorrect_url(Catalog, Mod=None):
    all_category = ['minecraft', 'rimworld', 'lethal_company', 'project_zomboid',
                    'stardew_valley', '7_days_to_die', 'content_warning', 'modpacks']
    db_sess = db_session.create_session()
    all_mods = list(map(lambda x: x.mod_name, db_sess.query(Mods).all()))
    if (Catalog in all_category) and (Mod == None or Mod in all_mods):
        return False
    return True


def add_mod(user_info: dict):
    db_session.global_init("db/testMods.db")
    mod = Mods()
    mod.author_name = user_info['author_name']
    mod.game_image = user_info['game_image']
    mod.game_name = transform_name(user_info['game_name'])
    mod.visible_game_name = user_info['game_name']
    mod.mod_name = transform_name(user_info['modpack_name'])
    mod.visible_mod_name = user_info['modpack_name']
    mod.game_version = user_info['game_version']
    mod.description = user_info['modpack_short_description']
    mod.about_mod = user_info['modpack_description']
    mod.download_guide = user_info['download_guide']
    mod.game_link = user_info['game_link']
    db_sess = db_session.create_session()
    db_sess.add(mod)
    db_sess.commit()


@app.route("/belj_games_studio")
def studioProject():
    return render_template("belj_games_studio.html", current_user=current_user)


@app.route("/creator", methods=['GET', 'POST'])
def creator():
    if not current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        db_sess = db_session.create_session()
        dict_ = request.form.to_dict()
        mod = db_sess.query(Mods).filter(Mods.visible_mod_name == dict_["modpack_name"]).first()
        if mod != None:
            return render_template("creator.html", current_user=current_user, error=True)
        user_image = request.files['modpack_icon']
        image_url = f'static/img/{transform_name(dict_["game_name"])}/{transform_name(dict_["modpack_name"])}.{user_image.filename.split(".")[-1]}'
        dict_["game_image"] = image_url
        with open(image_url, 'wb') as new_image:
            new_image.write(user_image.read())
        add_mod(dict_)
        return redirect('/')
    return render_template("creator.html", current_user=current_user, error=False)


@app.route("/smk")
def smk():
    return render_template("smk.html", current_user=current_user)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    return render_template("index.html", current_user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/<string:Catalog>')
def allModsInCatalog(Catalog):
    if uncorrect_url(Catalog):
        return redirect('/')

    db_sess = db_session.create_session()

    if Catalog == 'modpacks':
        data = db_sess.query(Mods).all()
    else:
        data = db_sess.query(Mods).filter(Mods.game_name == Catalog).all()

    return render_template('modpacks.html', current_user=current_user, game_name=Catalog, mods=data)


@app.route('/<string:Catalog>/<string:Mod>')
def singleMod(Catalog, Mod):
    if uncorrect_url(Catalog, Mod):
        return redirect('/')

    db_sess = db_session.create_session()

    data = db_sess.query(Mods).filter(Mods.game_name == Catalog, Mods.mod_name == Mod).first()
    print(data.game_image)
    return render_template('sample.html', current_user=current_user, mod=data)


if __name__ == '__main__':
    main()
