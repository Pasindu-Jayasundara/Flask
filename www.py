from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcomePage():
    return "Welcome to python flask, is it working?"

if __name__ == "__main__":
    app.run(debug=True)