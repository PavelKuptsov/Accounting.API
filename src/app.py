from flask import Flask, jsonify, make_response

from config import RESPONSE_NOT_FOUND, DB, DevConfig
from repository import Repository
from urls import rules
from flask_restful import Api


app = Flask(__name__)
app.config.from_object(DevConfig)
DB.init_app(app)
with app.app_context():
    DB.drop_all()
    DB.create_all()
    Repository().create_initial_testing_data()
api = Api(app)
for rule in rules:
    api.add_resource(rule.view, rule.url)


@app.errorhandler(RESPONSE_NOT_FOUND)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), RESPONSE_NOT_FOUND)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
