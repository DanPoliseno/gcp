from flask import Flask, render_template, request

app = Flask(__app__)

@app.route("/")
def main():
    model = {"title": "Hello DevOps 3 Fans 2."}
    return render_template('index.html', model=model)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)