from flask import Flask, render_template, request, redirect, url_for,flash
from telas.database import*
from flask import Blueprint
from flask import request
inicial  = Blueprint('inicial',__name__)

@inicial.route('/inicial')
def clientes():
    return render_template('inicial.html')
