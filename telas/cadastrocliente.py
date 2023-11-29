from flask import Flask, render_template, request, redirect, url_for,flash
from telas.database import*
from flask import Blueprint
from flask import request
cliente  = Blueprint('cliente',__name__)

@cliente.route('/cliente')
def clientes():
    return render_template('cliente.html')

@cliente.route('/CadastraCliente', methods=['POST'])
def cadastraCliente():
    nome = request.form['nome']
    print(nome)
    return render_template('cliente.html')