import json
import traceback
import os

import data_classifier
from api import app
from flask import request, jsonify
from collections import namedtuple


@app.route('/classifyData', methods=["POST"])
def classify_data():
    content = request.get_json(force=True)
    print('content', content)

    try:
        print('Classifying data.')
        x = namedtuple("SampleData", content.keys())(*content.values())
        print(x.attr1, x.attr2, x.attr3)
        response = data_classifier.classify_data(x)
        return json.dumps(response._asdict())
    except Exception as e:
        tb = traceback.format_exc()
        print(e, tb)
        return 'Failed to classify data. Please try after some time.'


if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)