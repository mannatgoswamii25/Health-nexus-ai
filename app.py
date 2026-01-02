from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Health Nexus AI</h1>
    <p>Your smart healthcare assistant is coming soon.</p>
    <p>Built by Mannat 🚀</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
