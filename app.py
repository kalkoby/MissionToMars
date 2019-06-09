from flask import Flask, render_template,redirect
from splinter import Browser

# Import scrape_mars
import scrape_mars

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable & pass connection to the pymongo instance.
conn = 'mongodb://localhost:27017/mission_to_mars'
client = pymongo.MongoClient(conn)

# Database Collection establishment
db = client.mars_db
collection = db.listing

# Set route
@app.route("/")
def index():
    listing = client.db.mars.find_one()
    return render_template("index.html", listing=listing)


@app.route("/scrape")
def scrape():
     mars_data = scrape_mars.scrape()
     db.listing.update({}, mars_data,upsert=True)
     return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
