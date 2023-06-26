def get_employee(id, data_employees):
    for employee in data_employees:
        if employee['id'] == int(id):
            return employee
    return 'Employee not found'

def remove_employee(id, data_employees):
    for employee in data_employees:
        if employee['id'] == id:
            data_employees.remove(employee)