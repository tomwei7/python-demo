#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/datetime')
def server_time():
    return jsonify(datetime=time.strftime('%Y-%m-%d'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
