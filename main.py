from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
    return render_template('index.html', weather=weather, news=news)
def get_weather(city):
    api_key = '(вставить ключ)'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = '(вставить ключ)'
    url = f'https://newsapi.org/v2/everything?q=technology&sortBy=popularity&apiKey={api_key}'

    response = requests.get(url)
    data = response.json()
    print("News API response:", data)  # Отладочный вывод
    return data.get('articles', [])



if __name__ == '__main__':
    app.run(debug=True)
