import requests
from bs4 import BeautifulSoup

def scrape():

    print("calling web page to scrape")
    url = "https://www.americancampus.com/student-apartments/tx/austin/crest-at-pearl/floor-plans"
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, "html.parser")
    apartments = soup.find_all("div", class_="description")

    for apartment in apartments:

        if  apartment.span != None:
            #Scrape the floor plan information
            print("Floor Plan: {}".format(apartment.h4.string))

            #Scrape the pricing information
            print("Price: {0} {1}".format(apartment.span.string, apartment.p.contents[1]))
            print("")

def main():
    scrape()
    return

if __name__ == "__main__":
    main()