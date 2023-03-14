from flask import Flask, render_template, request, url_for

from scheme import searching
from web.fun import get_ajax_results


def website():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/index')
    def home():
        return render_template(
            'home.html',
            title='GameScraper'
        )

    @app.route('/get_results', methods=['POST'])
    def get_results():
        if request.method == 'POST':
            return get_ajax_results(request.form['field'], request.form['query'])
        return None

    app.run()
    app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='static/favicon.ico'))
