#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/datetime')
def server_time():
    return jsonify(datetime=time.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    app.run()
