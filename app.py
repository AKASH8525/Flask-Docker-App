from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return "Hello, Docker!"

# Add the app.run() statement here at the bottom of the file
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
