# OpenRiceScrapper

Introduction
------------

OpenRice is a Hong Kong based food and restaurant website.
This project is to collect restaurant names and corresponding address with ease.

Usage
-----

Usage 1: python3 OpenRiceScrapper.py {page}

Usage 2: python3 OpenRiceScrapper.py {page} {food_category}

Usage 3: python3 OpenRiceScrapper.py {page} {food_category} {district}


{page} is the number of pages you try to send a a request to OpenRice, each page consists of 15 records.

{food_category} and {district} are optional parameters.

For {food_category}, you may type a dishId or any string you want.

For {district}, you may type a districtId or any string you want.

You can find out the dishId and districtId in the url of OpenRice website when you are searching for a specific item.


Method
------
```
ors = OpenRiceScrapper(10)
ors.getName()
```
return 150 restaurants names 

```
ors = OpenRiceScrapper(5)
ors.getAddress()
```
return 75 address of the restaurants

```
ors = OpenRiceScrapper(3, 1005)
ors.getNameAndAddress()
```
return 45 names and address of the restaurants which dishId is 1005

```
ors = OpenRiceScrapper(1)
ors.outputCSV()
```
generate a CSV file with the requested names and address


Used Library
------------

BeautifulSoup

lxml
