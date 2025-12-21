from flask import Flask, render_template, request
from summarizer import summarize_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    original_text = ""

    if request.method == "POST":
        original_text = request.form["text"]
        if original_text.strip():
            summary = summarize_text(original_text)

    return render_template(
        "index.html",
        summary=summary,
        original_text=original_text
    )

if __name__ == "__main__":
    app.run(debug=True)
