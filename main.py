from flask import Flask, jsonify, request

from app.utils import find_forms

app = Flask(__name__)

@app.route('/get_form', methods=['POST'])
def get_form():
    params = request.args.to_dict()
    forms = find_forms(params)
    return jsonify(forms)

if __name__ == '__main__':
    app.run()