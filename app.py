from flask import Flask, redirect, url_for, render_template, request, session, Response


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World gozo!'

@app.route("/aboutUs")
def aboutUs():
    return render_template("tutorial-components.html")

if __name__ == '__main__':
    app.run()
