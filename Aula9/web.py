from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def incia():
    return render_template('inicio.html')
app.run()