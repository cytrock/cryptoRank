from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)


@app.route('/')
def crypto():
    return render_template('crypto.html')


@app.route('/api/cryptocurrencies', methods=['GET'])
def get_cryptocurrencies():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=volume_desc"
    response = requests.get(url)
    data = response.json()

    # 简化数据以只返回我们需要的信息
    simplified_data = [
        {
            "image": coin["image"],
            "name": coin["name"],
            "symbol": coin["symbol"],
            "current_price": coin["current_price"],
            "price_change_percentage_24h": coin["price_change_percentage_24h"],
            "total_volume": coin["total_volume"],
        } for coin in data
    ]

    return jsonify(simplified_data)


if __name__ == '__main__':
    app.run(debug=True)
