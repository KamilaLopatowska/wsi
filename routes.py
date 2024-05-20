from app import app
from flask import render_template, request, redirect, url_for
from bs4 import BeautifulSoup
import requests
from app import utils
import json
import os

@app.route('/')
def index():
    return render_template('index.html.jinja')


@app.route('/extract', methods=['POST', 'GET'])
def extract():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        url = f"https://www.ceneo.pl/{product_id}"
        response = requests.get(url=url)
        if response.status_code == requests.codes['ok']:
            page_dom = BeautifulSoup(response.text, "html.parser")
            try:
                opinions_count = utils.extract(page_dom, "a.product-review__link > span")
            except AttributeError:
                opinions_count = 0
            if opinions_count:
                all_opinions = []
                while (url):
                    response = requests.get(url)
                    page_dom = BeautifulSoup(response.text, "html.parser")
                    opinions = page_dom.select("div.js_product-review")
                    for opinion in opinions:
                        single_opinion = {
                            key:utils.extract(opinion, *value)
                                for key, value in utils.selectors.items()
                        }
                        all_opinions.append(single_opinion)
                    try:
                        url = "https://www.ceneo.pl"+utils.extract(page_dom ,"a.pagination__next", "href")
                    except TypeError:
                        url = None
                if not os.path.exists("opinions"):
                    os.mkdir("opinions")
                with open(f"opinions/{product_id}.json", "w", encoding="UTF-8") as jf:
                    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
                return redirect(url_for('product', product_id=product_id))
            error = "Brak opinii"
            return render_template('extract.html.jinja', error=error)
        error = "Błędny kod - strona nie istnieje"
        return render_template('extract.html.jinja', error=error)
    return render_template('extract.html.jinja')

@app.route('/products')
def products():
    return render_template('products.html.jinja')

@app.route('/author')
def author():
    return render_template('author.html.jinja')

@app.route('/product/<product_id>')
def product(product_id):
    return render_template('product.html.jinja', product_id=product_id)