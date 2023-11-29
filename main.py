
from flask import Flask
from flask import Flask, render_template, request, redirect, url_for,flash
from telas.vendas import*
from telas.cadastrocliente import*
from telas.inicial import*
import os
app = Flask(__name__)
app.register_blueprint(inicial, url_prefix='/')
app.register_blueprint(app2, url_prefix='/')
app.register_blueprint(cliente, url_prefix='/')
app.secret_key = os.urandom(24)
if __name__ == '__main__':
    app.run(debug=True)
