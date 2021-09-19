from bs4 import BeautifulSoup
import requests
import csv
import sys

class OpenRiceScrapper:
	__url = "https://www.openrice.com/zh/hongkong/restaurants"
	__headers = {"User-Agent": "Mozilla/5.0"}

	def __init__(self, pages, params):
		print(f"Requesting {pages * 15} records\nRequest Parameters: {params}")
		self.__pages = pages
		self.__params = dict(params)
		self.__content = []
		self.__getHTML(self.__pages)

	def getName(self):
		names = []
		for k in range(len(self.__content)):
			tags = self.__content[k].find_all("h2") 
			for tag in tags:
				names.append(tag.a.text.strip())
		return names

	def getDistrict(self):
		districts = []
		for k in range(len(self.__content)):
			tags = self.__content[k].find_all("div", class_="icon-info address") 
			for tag in tags:
				districts.append(tag.a.text.strip() )
		return districts		

	def getAddress(self):
		address = []
		for k in range(len(self.__content)):
			tags = self.__content[k].find_all("div", class_="icon-info address")
			for tag in tags:
				address.append(tag.a.text.strip() + tag.span.text.strip())
		return address

	def getNameAndAddress(self):
		dict = []
		names = self.getName()
		address = self.getAddress()
		for i in range(len(names)):
			dict.append({"name": names[i],"address": address[i]})
		return dict

	#Generating a CSV file to the same directory with names and address
	def outputCSV(self):
		print("Generating output.csv.....")
		with open("output.csv", "w") as f:
			fieldnames = ["name", "address"]
			writer = csv.DictWriter(f, fieldnames = fieldnames)
			writer.writeheader()
			writer.writerows(self.getNameAndAddress())
		print("output.csv generated")

	#saving get results in content to ensure the data is consistent in the coming action
	def __getHTML(self, pages):
		for page in range(pages):
			self.__params["page"] = page + 1
			html = requests.get(self.__url, params = self.__params, headers = self.__headers)
			soup = BeautifulSoup(html.text,"lxml")
			self.__content.append(soup)
		

#params use key "dishId" if you know exact ID
#otherwise use key "what" and type whatever value you want to search in string
def isId(string):
	try: 
		int(string)
		return True

	except:
		return False


if __name__ == "__main__":
	pages = int(sys.argv[1])
	params = {}
	#If provided restaurants catergories
	if len(sys.argv) >= 3:
		dish = sys.argv[2]
		if isId(dish):
			params["dishId"] = dish
		else:
			params["what"] = dish

	if len(sys.argv) == 4:
		location = sys.argv[3]
		if isId(location):
			params["districtId"] = location
		else:
			params["where"] = location

	a = OpenRiceScrapper(pages, params)
	#Search random restaurants

	print(a.getNameAndAddress())
	a.outputCSV()
