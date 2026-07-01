from flask import Flask, render_template
from routes import api

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# Register API
app.register_blueprint(api, url_prefix="/api")


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)