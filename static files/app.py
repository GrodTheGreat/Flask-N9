from flask import Flask, render_template

app = Flask(
    import_name=__name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/'
)

@app.route(rule='/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)
