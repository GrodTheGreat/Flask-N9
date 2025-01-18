from flask import Flask, make_response, redirect, render_template, request, url_for

app = Flask(__name__, template_folder='templates')

@app.route(rule='/')
def index():
    my_value = 'text goes here'
    my_calc = 1 + 2
    my_list = [1.0, 2.0, 3.0, 30]

    return render_template(
        template_name_or_list='index.html',
        my_value=my_value,
        my_calc=my_calc,
        my_list=my_list
    )

@app.route(rule='/other')
def other():
    some_text = 'Hello, World!'
    return render_template(template_name_or_list='other.html', some_text=some_text)

@app.template_filter('reverse_string')
def reverse_string(string: str):
    return string[::-1]

@app.template_filter('repeat')
def repeat(string, times=2):
    return string * times

@app.template_filter('alternate_case')
def alternate_case(string):
    return ''.join([
        character.upper() if
        index % 2 == 0 else
        character.lower()
        for index, character in enumerate(string)
    ])

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

@app.route(rule='/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        response = make_response('Hello, World!')
        response.status_code = 200
        response.headers['Content-Type'] = 'text/plain'
        return response
    elif request.method == 'POST':
        return 'You made a POST request', 200
    else:
        return 'You shouldn\'t have seen this'


@app.route(rule='/greet/<name>')
def greet(name):
    return f'Hello, {name}'

@app.route(rule='/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' not in request.args.keys() or 'name' not in request.args.keys():
        return 'Parameters missing'

    greeting = request.args.get('greeting')
    name = request.args['name']  # Both these methods work

    return f'{greeting}, {name}'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)
