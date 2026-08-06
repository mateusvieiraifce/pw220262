from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style='color: blue;'>Hello, World!</h1>"

@app.route('/casa')
def casa():
    return "<h1 style='color: green;'>Welcome to Casa!</h1>"

@app.route('/about')
def about( name=None):
    return render_template('hellow.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you can add logic to validate the username and password
        if (password == '12345'):
            return about(name=username);

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)