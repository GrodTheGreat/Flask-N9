from app import create_app

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=9000, debug=True)