from flask import Flask, jsonify
from flasgger import swag_from

app = Flask(__name__)

@app.route('/colors/<palette>')
@swag_from('../templates/colors.yml')
def collors(palette):
    all_colors = {
        'cmyk': ['cyan', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)