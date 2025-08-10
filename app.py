from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask in Docker! The app is running."

if __name__ == "__main__":
    # Host 0.0.0.0 ensures it listens on all container network interfaces
    app.run(host="0.0.0.0", port=5000, debug=True)

