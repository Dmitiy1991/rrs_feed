from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def index():

    rss_xml = render_template('eldorado.xml')
    response = make_response(rss_xml)
    response.headers['Content-Type'] = 'application/rss+xml; charset=utf8'
    return response


if __name__ == '__main__':
    app.run()


