from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def front_page():
    links_dictionary = get_links()
    return render_template("base.html.jinja", links=links_dictionary)


@app.route("/test")
def test_page():
    return render_template("test.html.jinja")


def get_links() -> list[dict[str, list[dict[str, str]]]]:
    with open("links.json", "r") as links:
        return json.load(links)


if __name__ == "__main__":
    print(get_links())
