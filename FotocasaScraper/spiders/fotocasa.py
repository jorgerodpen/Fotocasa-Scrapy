import scrapy
from ..items import FotocasascraperItem
import numpy as np

class FotoCasaSpider(scrapy.Spider):
    name = 'FotoCasa'
    allowed_domains = ['fotocasa.es']
    start_urls = ['https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/todas-las-zonas/l?latitude=40.4096&longitude=-3.6862&combinedLocationIds=724,14,28,173,0,28079,0,0,0']
    page = 0
    def parse(self, response):
        # Getting the items
        items = FotocasascraperItem()

        # Looping over each property
        property_cards = response.xpath('//article//a[contains(@class,"re-Card-link")]')
    
        for card in property_cards:            
            # Url
            url = card.css('::attr(href)').get()
            neighborhood = card.css('.re-Card-title::text').extract_first().split(', ')[-1]
            # Entering the url
            yield response.follow(url, callback = self.parse_rent, cb_kwargs=dict(items = items, neighborhood = neighborhood))  
            
        # Moving to the next page
        next_page = response.xpath('//li[contains(@class,"sui-MoleculePagination-item")][last()]/a/@href').get()
        print("The next page is :", next_page)
        if next_page is not None:
            FotoCasaSpider.page = FotoCasaSpider.page + 1
            print("Scraped page ", FotoCasaSpider.page)
            yield response.follow(next_page, callback = self.parse)


    def parse_rent(self, response, items, neighborhood):
        # Filling all columns
        cols_en = ["Antiquity","Bathrooms","Community_Expenses","Condition","Deposit","Elevator",
                "Emissions","Energy_Consumption","Extra","Floor","Furnished","Heating",
                "Neighborhood","Orientation","Parking","Pets","Photos","Price","Rooms",
                "Size","Title","Type","url","Water_Heater"]
        cols_sp = ["Antigüedad","baño","GastosDeComunidad","Estado","Depósito","Ascensor",
                "Emisiones","ConsumoEnergía","Extra","Planta","Amueblado","Calefacción",
                "Barrio","Orientación","Parking","Mascotas","Fotos","Precio","hab.",
                "m²","Título","TipoDeInmueble","url","AguaCaliente"]
        for key in cols_en:
            items[key] = np.nan
            
        # Neighborhood
        items['Neighborhood'] = neighborhood
        items['url'] = response.request.url
        
        # Price
        items['Price'] = response.css('.re-DetailHeader-price::text').extract_first()
        
        # Title of residence
        title = response.css('.re-DetailHeader-propertyTitle::text').extract_first()
        items['Title'] = title
        
        # Extra features
        items["Extra"] = "-".join(response.css('li.re-DetailExtras-listItem::text').extract())
        
        # Number of photos
        photos = response.css('.re-DetailMosaic-actionsButton ::text').extract_first()
        items["Photos"] = photos.replace("s", "").replace(" Foto","")
        
        # Initial features
        features = response.css('.re-DetailHeader-featuresItemIcon+ span')
        for feature in features:
            feature_text = feature.xpath('./text()').extract_first().replace(" ","").replace("s","")
            # Replacing the feature to a column
            for i in range(len(cols_en)):
                feature_text = feature_text.replace(cols_sp[i],cols_en[i])
            if (feature_text == "Entreuelo") or (feature_text == "Bajo") or (feature_text == "Sótano"):
                pass
            else:
                items[feature_text] = feature.xpath('./span/text()').extract_first()
        
        # Other features
        features2 = response.css('.re-DetailFeaturesList-featureContent')
        for feature in features2:
            feature_text = feature.xpath('./p[1]/text()').extract_first().title().replace(" ","")
            for i in range(len(cols_en)):
                feature_text = feature_text.replace(cols_sp[i],cols_en[i])
            if (feature_text == "Energy_Consumption") or (feature_text == "Emissions"):
                items[feature_text] = feature.xpath('.//div[contains(@class,"re-DetailEnergyCertificate-value")]/text()').extract_first()
            else:
                items[feature_text] = feature.xpath('./p[2]/text()').extract_first()
        
        yield items