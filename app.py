from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    color = request.form['color']
    return render_template('result.html', name=name, color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
