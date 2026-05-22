from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renderiza la página principal de LUCET
    return render_template('index.html')

if __name__ == '__main__':
    # El debug=True sirve para que la web se actualice sola cuando hagas cambios
    app.run(debug=True)