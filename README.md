# Avito_scraping
I collected data from "https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre" and deploy it Scrapinghub cloud.

I'm trying to collect data of cars from an e-commerce site in order to build a machine learning model which predict prices of used cars.\
In this project, i will just do the scraping using scrapy from python.\
The building of the machine learning model will be implemented in another project.\

# dataset:
The dataset collected in the CSV file named `test.csv`, which contains the following columns:\
'car_city' : The name of city where is the car sold.\
'car_cv_man_auto': how many Horsepower the car have. \
'car_equipements': Car equipements.\
'car_information	': Some information about the car.\
'car_name': The car name.\
'car_price': The car price.\
Purpose of this Project :\
Collect data in order to have data to predict price of used cars. 

Files:\
Avito_scraping/avito_cars/avito_cars/spiders/av_cars.py : the main code of scraping data.\
test.csv : Contains some of the collected data.
