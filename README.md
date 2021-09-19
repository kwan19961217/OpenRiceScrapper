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


food_category and district are optional parameters.

For food_category, you may type a dishId or any string you want.

For district, you may type a districtId or any string you want.

You can find out the dishId and districtId in the url of OpenRice website when you are searching for a specific item.


Method
------
getName

return the names of the restaurants


getAddress

return the address of the restaurants


getNameAndAddress

return the names and address of the restaurants


outputCSV

generate a CSV file with the requested names and address


Used Library
------------

BeautifulSoup

lxml
