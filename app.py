from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Salam Mounir ! Ceci est une app Flask dans Docker."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
