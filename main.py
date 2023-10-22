from random import randint, shuffle
from flask import Flask, redirect, url_for, session, request, render_template
import os

quiz = 1


def index():
    global counter
    session['counter'] = 0
    session['quiz'] = 1
    session['last_question'] = 0
    session['total'] = 0
    session['answers'] = 0
    return '<a href="/test">Рандомные числа</a>'
#    redirect(url_for('test'))




def buttons():
    return "<a href='/anectod'>  №№№№№№№№№№№№№№№№№№№№№№№№№№ </a>"

def result():
    redirect(url_for('result'))
    return render_template('result.html', total = session['total'], answers = session['answers'])

app = Flask(__name__, template_folder=os.getcwd())
app.add_url_rule('/test', 'test', test,
                methods=['POST', 'GET'])
app.add_url_rule('/result', 'result', result)
app.add_url_rule('/buttons', 'buttons', buttons)
app.add_url_rule('/', 'index', index,
                methods=['POST', 'GET'])
app.run(debug = True)
