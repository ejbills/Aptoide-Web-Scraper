from flask import Flask, request, Response, url_for
from web_scraper import scrape, url_validation

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index() -> Response:  # Loads index.html
    return app.send_static_file("index.html")


@app.route('/scrape', methods=['POST'])
def scrape_url() -> str:  # Prints input link to console and loads scrape result form
    input_link = request.form['input']
    print("The input link is '" + input_link + "'")

    if url_validation(input_link):
        returned_data = scrape(input_link)

        return f"""\
        <div>
            <strong style='color: red;'>Title:</strong>
            <div>{returned_data[0]}</div>
            <br>
        </div>
        <div>
            <strong style='color: red;'>Version:</strong>
            <div>{returned_data[1]}</div>
            <br>
        </div> 
        <div>
            <strong style='color: red;'>Downloads:</strong>
            <div>{returned_data[2]}</div>
            <br>
        </div>
        <div>
            <strong style='color: red;'>Release Date:</strong>
            <div>{returned_data[3]}</div>
            <br>
        </div>
        <div>
            <strong style='color: red;'>Description:</strong>
            <div>{returned_data[4]}</div>
        </div>
        <a href="{url_for('static', filename='index.html')}">Return to homepage</a>
        """
    else:
        return f"""
        <header>Invalid input or error occurred, please try again.</header><br>
        <a href="{url_for('static', filename='index.html')}">Return to homepage</a>
        """


if __name__ == '__main__':
    app.run()
