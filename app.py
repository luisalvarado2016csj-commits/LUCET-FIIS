from flask import Flask, render_template

app = Flask(__name__)

app.wsgi_app = app.wsgi_app 

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Esto solo se ejecutará cuando tú lo corras en tu computadora (local)
    app.run(debug=True)