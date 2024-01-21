from flask import Flask
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    num = random.randint(1,100)
    print(num)
    return f'Your lucky number for the day is {num}'


if __name__ == '__main__':
    app.run(debug=True, port=3000)
    
    
    