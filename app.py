from flask import Flask
from flask import render_template
import escons
import time

app = Flask(__name__)

@app.route('/') #Use template to display the list
def display_escons():
    diccionari = escons.get_escons()
    diccionari = 'Error'
    if diccionari == 'Error':
        return render_template('error.html', data=time.ctime())

    independencia = 'no'
    suma_indepe = 0

    suma_indepe += diccionari['CUP'] + diccionari['JUNTS+'] + diccionari['ERC']

    if suma_indepe > 68:
        independencia = 'sí'

    escons_list = [(k, int(v)) for k, v in diccionari.items()]
    return render_template('index.html', llista=escons_list, independencia=independencia, data=time.ctime())

if __name__ == '__main__':
    app.run(debug=True)