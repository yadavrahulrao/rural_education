from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classes')
def classes():
    return render_template('classes.html')

@app.route('/quizzes')
def quizzes():
    return render_template('quizzes.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
