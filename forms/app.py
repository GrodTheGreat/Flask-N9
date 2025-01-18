import os
import uuid

from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    Response,
    send_from_directory
)
import pandas as pd

app = Flask(import_name=__name__, template_folder='templates')

@app.route(rule='/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template(template_name_or_list='index.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form.get(key='password')  # These are equivalent

        if username == 'neuralninja' and password == 'password':
            return 'Success'
        else:
            return 'Failure'


@app.route(rule='/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.ms-excel' or file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        df = pd.read_excel(io=file)
        return df.to_html()

@app.route(rule='/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']

    df = pd.read_excel(io=file)

    response = Response(
        response=df.to_csv(index=False),
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )

    return response

@app.route(rule='/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file = request.files['file']

    df = pd.read_excel(io=file)

    if not os.path.exists(path='downloads'):
        os.mkdir(path='downloads')

    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads', filename))

    return render_template(
        template_name_or_list='download.html',
        filename=filename
    )

@app.route(rule='/download/<filename>')
def download(filename):
    return send_from_directory(
        directory='downloads',
        path=filename,
        download_name='result.csv'
    )

@app.route(rule='/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']

    with open(file='file.txt', mode='w', encoding='utf-8') as file:
        file.write(f'{greeting}, {name}')

    return jsonify({'message': 'Successfully written!'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)
