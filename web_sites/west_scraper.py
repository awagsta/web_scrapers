import requests
from bs4 import BeautifulSoup

def scrape():

    print("calling web page to scrape")
    url = "https://www.americancampus.com/student-apartments/tx/austin/26-west/floor-plans"
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, "html.parser")
    apartments = soup.find_all("div", class_="description")

    for apartment in apartments:

        if  apartment.span != None:
            print("Floor Plan: {}".format(apartment.h4.string))
            print("Price: {}".format(apartment.span.string))
            print("")

def main():
    scrape()
    return

if __name__ == "__main__":
    main()