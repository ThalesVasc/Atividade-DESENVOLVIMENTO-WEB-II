from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    # Recebe dados do formulário
    variavel1 = request.form.get('variavel1')
    variavel2 = request.form.get('variavel2')
    
    # Exemplo de cálculo simples
    resultado = int(variavel1) + int(variavel2)
    
    return render_template('resultado.html', resultado=resultado)

@app.route('/autor')
def autor():
    return render_template('autor.html')

if __name__ == '__main__':
    app.run(debug=True)
    