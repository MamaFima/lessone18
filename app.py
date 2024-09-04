from flask import Flask, render_template
import requests

app = Flask(__name__)

# Функция для получения случайной цитаты
def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return data['content'], data['author']
    else:
        return "Не удалось получить цитату", "Неизвестный автор"

@app.route('/')
def index():
    quote, author = get_random_quote()
    return render_template('dz.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)
