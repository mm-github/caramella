# alphanumber/main.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'], defaults={'path': ''})
@app.route('/<path:path>')
def alphanumber(path):
    # excluding special chars from request.url
    alphanumeric = [character for character in path.rsplit('/', 1)[-1] if character.isalnum()]
    NUM = 31
    # declaring the list which will contain the output:
    charlist = []
    for character in alphanumeric:
        # if digit then leave it untouched:
        if character.isdigit():
            charlist.append(str(character))
        # 
        else:
        # if char then transform it to its ASCII position:
            chartonum = str(ord(character) & NUM)
            charlist.append(chartonum)
    ostring = ''.join(charlist)
    # return path
    return jsonify(result=ostring)


@app.route('/ready', methods=['GET'])
def ready():
    output= "ok"
    return jsonify(status=output)


@app.route('/pippo/', methods=['GET'])
def pippo():
    # return request.query_string
    # return request.url
    return request.url.rsplit('/', 1)[-1]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')