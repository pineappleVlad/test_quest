# from flask import Flask, render_template, request
# import math
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/calculate', methods=['POST'])
# def calculate():
#     try:
#         latitude = float(request.form['latitude'])
#         longitude = float(request.form['longitude'])
#         zoom = int(request.form['zoom'])
#
#         x = math.floor((longitude + 180) / 360 * 2 ** zoom)
#         y = math.floor((1 - math.log(math.tan(math.radians(latitude)) + 1 / math.cos(math.radians(latitude))) / math.pi) / 2 * 2 ** zoom)
#
#         map_url = f'https://core-carparks-renderer-lots.maps.yandex.net/maps-rdr-carparks/tiles?l=carparks&x={x}&y={y}&z={zoom}&scale=1&lang=ru_RU'
#
#         return render_template('result.html', x=x, y=y, map_url=map_url)
#     except ValueError:
#         error = 'Пожалуйста, введите корректные координаты и зум.'
#         return render_template('index.html', error=error)
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        zoom = int(request.form['zoom'])

        x = math.floor((longitude + 180) / 360 * 2 ** zoom)
        y = math.floor((1 - math.log(math.tan(math.radians(latitude)) + 1 / math.cos(math.radians(latitude))) / math.pi) / 2 * 2 ** zoom)

        map_url = f'https://core-carparks-renderer-lots.maps.yandex.net/maps-rdr-carparks/tiles?l=carparks&x={x}&y={y}&z={zoom}&scale=1&lang=ru_RU'

        return render_template('result.html', x=x, y=y, map_url=map_url)
    except ValueError:
        error = 'Пожалуйста, введите корректные координаты и зум.'
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)

