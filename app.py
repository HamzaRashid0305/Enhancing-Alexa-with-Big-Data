from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(r'C:\Users\ihiba\Videos\template\recommendation.html')

if __name__ == "__main__":
    app.run()