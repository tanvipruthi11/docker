from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/definition', methods=['GET', 'POST'])
def definition():
    word_exist = False
    word_define = ""
    json_input = json.loads(request.get_data())
    json_input = (json_input['word'])

    with open('/usr/src/app/dictionary.txt') as f:
        lines = f.readlines()

    for line in lines:
        if json_input.lower().strip() == line.split("=")[0]:
            word_exist = True
            word_define = line.split("=")[1]
            word_define = word_define.replace("\n", "")

    if word_exist:
        json_output = (json.dumps({"word": json_input, "definition": word_define}))
    else:
        json_output = (json.dumps({"word": json_input, "error": "Word not found in dictionary."}))

    return json_output


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

