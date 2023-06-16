from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_google():
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run()