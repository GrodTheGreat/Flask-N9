from flask import Flask, render_template, session, make_response, request, flash

app = Flask(import_name=__name__, template_folder='templates')
app.secret_key = 'KEY GOES HERE'  # In production this should be something serious

@app.route(rule='/')
def index():
    return render_template(template_name_or_list='index.html', message='Index')


@app.route(rule='/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello, World!'

    return render_template(template_name_or_list='index.html', message='Session data set.')


@app.route(rule='/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']

        return render_template(template_name_or_list='index.html', message=f'Name: {name}, Other: {other}')
    else:
        return render_template(template_name_or_list='index.html', message='No session found')


@app.route('/clear_session')
def clear_session():
    session.clear()
    # session.pop('name')  # If you only want to clear a single item

    return render_template(template_name_or_list='index.html', message='Session cleared')


@app.route('/set_cooke')
def set_cookie():
    response = make_response(render_template(template_name_or_list='index.html', message='Cookie set.'))
    response.set_cookie(key='cookie_name', value='cookie_value')

    return response


@app.route('/get_cooke')
def get_cookie():
    cookie_value = request.cookies['cookie_name']

    return render_template(template_name_or_list='index.html', message=f'Cookie Value: {cookie_value}')


@app.route('/remove_cooke')
def remove_cookie():
    response = make_response(render_template(template_name_or_list='index.html', message='Cookie removed.'))
    response.set_cookie(key='cookie_name', expires=0)

    return response


@app.route(rule='/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template(template_name_or_list='login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'neuralninja' and password == 'password':
            flash('Successful login!')
            return render_template(template_name_or_list='index.html', message='')
        else:
            flash('Login failed!')
            return render_template(template_name_or_list='index.html', message='')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)
    