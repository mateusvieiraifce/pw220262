from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/menu')
def menu():
    return render_template('menuPage.html')

@app.route('/about')
def about_page():
    return render_template('about.html')
   
@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/services')
def services_page():
    return render_template('services.html')

@app.route('/casa')
def casa():
    return "<h1 style='color: green;'>Welcome to Casa!</h1>"

@app.route('/about')
def about( name=None):
    return render_template('hellow.html', name=name)

@app.route('/hello/<name>')
def hello(name):
    return render_template('hellow.html', name=name)

@app.route('/imc/<float:weight>/<float:height>')
def imc(weight, height):
    print(f"Calculating IMC for weight: {weight} kg and height: {height} m")
    imc = weight / (height ** 2) if height > 0 else 0;
    return "<h1 style='color: blue;'>Your IMC is: {:.2f}</h1>".format(imc)

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