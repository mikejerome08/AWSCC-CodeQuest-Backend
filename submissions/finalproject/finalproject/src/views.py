from flask import Blueprint, render_template, request, redirect, flash
from .model import Password
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    passwords = Password.query.all()
    return render_template('index.html', passwords=passwords)

@main.route('/add', methods=['POST'])
def add_password():
    website = request.form['website']
    email = request.form['email']
    password = request.form['password']
    new_password = Password(website=website, email=email, password=password)
    db.session.add(new_password)
    db.session.commit()
    flash('Password added successfully!', 'success')
    return redirect('/')

@main.route('/update/<int:id>', methods=['POST'])
def update_password(id):
    password = Password.query.get_or_404(id)
    password.website = request.form['website']
    password.email = request.form['email']
    password.password = request.form['password']
    db.session.commit()
    flash('Password updated successfully!', 'success')
    return redirect('/')

@main.route('/delete/<int:id>', methods=['POST'])
def delete_password(id):
    password = Password.query.get_or_404(id)
    db.session.delete(password)
    db.session.commit()
    flash('Password deleted successfully!', 'success')
    return redirect('/')
