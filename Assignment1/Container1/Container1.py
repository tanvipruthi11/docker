from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__)


@app.route('/definition', methods=['GET', 'POST'])
def container1():

    json_output = json.loads(request.get_data())
    json_output = (json_output['word'])

    if json_output is None:
        result = (json.dumps({"word": None, "error": "Invalid JSON input."}))

    elif json_output == "":
        result = (json.dumps({"word": "", "error": "Invalid JSON input."}))

    else:
        output = (json.dumps({"word": json_output.lower().strip()}))

        result = requests.post("http://app1:5001/definition", data=output)
        result = result.json()
        result['word'] = json_output

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
