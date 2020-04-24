from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template("landing_page.html")

@app.route('/book')
def book():
    return render_template("google_map.html")

if __name__ == '__main__':
   app.run(debug = True, port = 4123)