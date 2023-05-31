from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route("/getFile")
def get_file():
    file_fp = "file.txt"
    with open(file_fp, "r") as f:
        temp = f.read()
        return temp

if __name__ == "__main__":
    app.run(debug=True)
