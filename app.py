# Import Dependencies 
from flask import Flask, render_template , redirect

import pymongo
import scrape_mars


# creating the instance of flask
app = Flask(__name__)

# Create connection 
conn = 'mongodb://localhost:27017/mission_mars'
#Using Pymongo
client = pymongo.MongoClient(conn)


# create a route
@app.route("/")
def index(): 

    # Find data
    mars_info = client.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

#  scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_info = client.db.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)