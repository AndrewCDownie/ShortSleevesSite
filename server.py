from flask import Flask

app = Flask(__name__,static_url_path='')



@app.route('/')
def index():
    data =""
    with open("index.html","r") as file:
        data = file.read()
    return data


if __name__ == "__main__":
    app.run(debug=True)
