import os
from flask import Flask

PORT = int(os.getenv("PORT", "3000"))

print(f"Server started in port {PORT}")

app = Flask(__name__)


@app.route("/")
def index():
    return "Todo app running\n"


if __name__ == "__main__":
    # local testing
    app.run(host="0.0.0.0", port=PORT)
