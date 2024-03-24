from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/personal_details')
def personal_details():
    return render_template('personal_details.html')

@app.route('/educational_details')
def educational_details():
    return render_template('educational_details.html')
if __name__ == '__main__':
    app.run(debug=True)
