from flask_app import app
from flask_app.controllers import template_controller



if __name__ == "__main__":
    app.run(debug=True, port=4200)