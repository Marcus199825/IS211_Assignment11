from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Global list to store todo items
todo_list = []

# Main route to display todo list and add new items
@app.route('/', methods=['GET', 'POST'])
def todo_list_view():
    if request.method == 'POST':
        task = request.form['task']
        email = request.form['email']
        priority = request.form['priority']
        
        # Data validation
        if not email or '@' not in email:
            return redirect('/')
        if priority not in ['Low', 'Medium', 'High']:
            return redirect('/')
        
        todo_list.append({'task': task, 'email': email, 'priority': priority})
        return redirect('/')
    else:
        return render_template('todo.html', todo_list=todo_list)

# Controller to clear the todo list
@app.route('/clear', methods=['POST'])
def clear_todo_list():
    global todo_list
    todo_list = []
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)