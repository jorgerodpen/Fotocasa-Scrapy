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
1. Open the terminal and go to the same folder where the folder **FotocasaScraper** and **scrapy.cfg** are stored