from flask import Flask, render_template, redirect, Response, abort, url_for, request
import os

app = Flask(__name__)

words = []
n = int(os.environ.get('n'))

for i in range(n):
    word = os.environ.get(f'w{i}')
    words.append(word)


@app.route('/<word>')
def index(word):
    if word in words:
        return 'Hello %s!' % word
    else:
        abort(404)


if __name__ == '__main__':
    app.run()

#
