from flask import Flask, render_template
from melon import song_rank

app = Flask(__name__)

@app.route('/')
def chart():
    return render_template('chart.html', chart=song_rank)

if __name__ == "__main__":
    app.run()