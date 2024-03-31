from flask import Flask, render_template, request, redirect, url_for
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

template_dir = os.path.join(current_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

passwords = []

@app.route('/')
def index():
    return render_template('index.html', passwords=passwords)

@app.route('/add_password', methods=['POST'])
def add_password():
    website = request.form['website']
    email = request.form.get('email', '')
    password = request.form['password']
    passwords.append({'website': website, 'email': email, 'password': password})
    return redirect(url_for('index'))

@app.route('/update_password/<int:index>', methods=['POST'])
def update_password(index):
    website = request.form['website']
    email = request.form.get('email', '')
    password = request.form['password']
    passwords[index] = {'website': website, 'email': email, 'password': password}
    return redirect(url_for('index'))

@app.route('/delete_password/<int:index>')
def delete_password(index):
    del passwords[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
