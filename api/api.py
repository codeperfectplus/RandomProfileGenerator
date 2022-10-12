import os
from flask import Flask, jsonify
from random_profile import RandomProfile

# random_profile==0.2.3 required
rp = RandomProfile()
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'api is working'})   

@app.route('/api/v1/random_profile')
def single_profile():
    profile = rp.full_profile()
    return jsonify({'profile': profile})

@app.route('/api/v1/random_profile/<int:num>')
def multiple_profile(num):
    if num > 100:
        num = 100
    profile = rp.full_profile(num)
    return jsonify({'profile': profile})


if __name__ == '__main__':
    app.run(debug=True)