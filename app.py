from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        enter flavor
        <input type="text" name="flavor"><br/>
        enter toppings
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo with toppings {users_froyo_toppings}!'
    

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        Favorite color?
        <input type="text" name="color"><br/>
        Favorite animal?
        <input type="text" name="animal"><br/>
        Favorite city?
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    favorite_color = request.args.get('color')
    favorite_animal = request.args.get('animal')
    favorite_city = request.args.get('city')
    return f'Wow, I didn\'t know {favorite_color} {favorite_animal} lived in {favorite_city}!' 


@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Enter your secret message:
        <input type="text" name="message"><br/>
        <input type="submit" value="submit">
    </form> 
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    user_message = request.form.get('message')
    sorted_message = sort_letters(user_message)
    return f' Here\'s your secret message! <br/> {sorted_message}'

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    
    num_one = int(request.args.get('operand1'))
    num_two = int(request.args.get('operand2'))
    operation = request.args.get('operation')

    result = 0

    if operation == "add":
        result = (num_one + num_two)
    elif operation == "subtract":
        result = (num_one - num_two)
    elif operation == "multiply":
        result = (num_one * num_two)
    elif operation == "divide":
        result = (num_one / num_two)

    context = { 
        'operation' : operation,
        'num_one' : num_one,
        'num_two' : num_two,
        'result' : result
    }
    
    return render_template('calculator_results.html', **context)

 

# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    users_name = request.args.get('users_name')
    wants_compliments = request.args.get('wants_compliments')
    num_compliments = int(request.args.get('num_compliments'))
    result = ""



    if wants_compliments == "yes":
        result = random.sample(list_of_compliments, num_compliments)

    context = {
        'users_name' : users_name,
        'wants_compliments' : wants_compliments,
        'num_compliments' : num_compliments,
        'result' : result
    }

    print(users_name)
    print(wants_compliments)
    print(num_compliments)
    print(result)

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
