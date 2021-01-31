# Fotocasa scraper
- Built a scraper of the Spanish real state portal [Fotocasa](https://www.fotocasa.es/es/). 
- Extracts information for every listed property for a certain search in the **rent section** (*Alquilar* in Spanish). 
- Used [Scrapy](https://scrapy.org/) to build it
- The scraper extracts the following elements:
	- Title 
	- Type of property	
	- url
	- Price
	- Number of rooms
	- Number of bathrooms
	- Size
	- Floor
	- Antiquity
	- Community expenses (y/n)
	- Condition of the property
	- Deposit (y/n)
	- Elevator (y/n)
	- Furnished (y/n)
	- Neighborhood
	- Orientation
	- Parking (y/n)
	- Pets (y/n)
	- Photos  
	- Heating
	- Water_Heater
	- Emissions
	- Energy consumption
	- Other possible extra features listed in the page
	
# Packages
**Python Version**: 3.8.3

**Packages used**: Scrapy, numpy

**Requirements**: <code>pip install -r requirements.txt</code>

# How to run the scraper
1. Open the terminal and go to the same folder where the folder **FotocasaScraper** and **scrapy.cfg** are stored. **It needs to be that folder!**
2. Run the following command in the terminal: <code>scrapy crawl FotoCasa -o file_name.csv</code>
	- Other supported formats are *.json* and *.xml*.
3- After running the command, the file should be created in the same folder you run it. 

## Changing the location
To change the location where you want to scrape the data you need to follow the next steps:
1. Go to the main page of [Fotocasa](https://www.fotocasa.es/es/) 
2. In the *rent tab* (**Alquilar** in Spanish) type the name of the place you want to scrape the data. 
3. Press enter or click the search button.
4. Copy the link of the page after performing the search 
5. Go to FotocasaScraper/spiders and open fotocasa.py
6. Paste the url in the variable called <code>start_urls</code>. 

Your final code should look like this:

<code>start_urls = ['https://www.your_new_fotocasa_url.com']</code>

**WARNING!!** Do not delete the tab before the variable otherwise the scraper won't work.

# Note
This scraper works for any kind of search in Fotocasa (buy, rent, share,...) in any of its locations. As of today, the items it extracts are adapted to the rent tab (**Alquiler** in Spanish). An adaptation to the other tabs should be fairly easy.  