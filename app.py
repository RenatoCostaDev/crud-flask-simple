from flask import Flask, render_template, request, redirect, url_for, flash
from tools import get_employee, remove_employee

data_employees = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template (
        'index.html',
        data_employees=data_employees
    )

@app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        celphone = request.form['celphone']
        address = request.form['address']
        data_employees.append({ 
            'id': (len(data_employees) + 1), 
            'name': name, 
            'email': email, 
            'celphone': celphone, 
            'address': address 
        })
        flash('Input Data Success !!')
        return redirect(url_for('index'))
    return render_template(
        'input.html'
    )

@app.route('/edit/<int:id>')
def edit_data(id):
    data = get_employee(id, data_employees)
    return render_template(
        'edit.html',
        data=data
    )

@app.route('/edit-do/<int:id>', methods=['GET', 'POST'])
def edit_do(id):

    data = get_employee(id, data_employees)
    data['name'] = request.form['name']
    data['email'] = request.form['email']
    data['celphone'] = request.form['celphone']
    data['address'] = request.form['address']

    flash(' Data updated successfully!')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    
    remove_employee(id, data_employees)
    flash(' Data Deleted successfully!')
    return render_template(
        'index.html',
        data_employees=data_employees
    )

if __name__=='__main__':
    app.secret_key = 'unique key'
    app.config['SESSION_TYPE'] = 'filesystem'


app.run(debug=True)