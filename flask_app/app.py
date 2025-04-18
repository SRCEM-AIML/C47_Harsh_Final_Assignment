from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    form_html = '''
    <form method="post">
        Name: <input type="text" name="name"><br>
        Age: <input type="number" name="age"><br>
        <input type="submit" value="Submit">
    </form>
    '''
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        try:
            age = int(age)
            return f"Hello, {name}! You are {age} years old."
        except ValueError:
            return "Invalid age entered. Please enter a number.", 400
    return render_template_string(form_html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
