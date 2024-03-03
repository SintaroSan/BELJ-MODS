from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/jarenki')
def hihihaha():
    result = """
                <html>
                  <head>
                    <meta charset="utf-8">
                    <meta name="author" content="JZ">
                    <meta name="description" content="test">
                    <meta name="keywords" content="test,css,html">
                    <title>hihihaha</title>
                  </head>
                  <body title="made by BELJ Games Studio">
                      <img src="https://avatars.mds.yandex.net/i?id=e27e8eb32c9c95648515ab6ce4704a06_l-4859870-images-thumbs&n=13" width="200px" alt="hihihaha"><br>
                      <a href="index">назад</a><br>
                      <a href="mailto:yaroslavspb2006@gmail.com">написать мне)</a>
                  </body>
                </html>
             """
    return result


@app.route('/index')
def index():
    return """<html>
    <head>
        <meta charset="utf-8">
        <meta name="author" content="JZ">
        <meta name="description" content="test">
        <meta name="keywords" content="test,css,html">
        <title>lolkek</title>
    </head>
    <body title="made by BELJ Games Studio">
        <a href="jarenki">иди туда</a>
    </body>
</html>"""



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')