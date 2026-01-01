from flask import Flask, render_template
import requests

app = Flask(__name__)

def random_books():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    res = requests.get(url)
    data = res.json()

    if data and data.get("data"):
        volume = data["data"]["volumeInfo"]

        title = volume.get("title", "No Title")
        authors = volume.get("authors", ["Unknown"])
        description = volume.get("description", "No Description Available")
        preview_link = volume.get("previewLink", "")

        return {
            "title": title,
            "author": authors[0],
            "description": description,
            "preview_link": preview_link
        }
    else:
        return None

@app.route("/")
def home():
    book = random_books()
    return render_template("index.html", book=book)

if __name__ == "__main__":
    app.run(debug=True)
