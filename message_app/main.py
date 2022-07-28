from flask import Flask, jsonify, request

main = Flask(__name__)

tutorials = [
    {
        'title': 'V1',
        'description': 'slghw;ijeg'
    },
    {
        'title': 'V2',
        'description': 'aler;wg'
    }
]


@main.route('/', methods=['GET'])
def get_list():
    return jsonify(tutorials), 'GET - ok'


@main.route('/tut', methods=['POST'])
def update_list():
    new_one = request.json
    tutorials.append(new_one)
    return jsonify(tutorials), 'POST - ok'


if __name__ == '__main__':
    main.run(debug=True, host='0.0.0.0', port=5000)
