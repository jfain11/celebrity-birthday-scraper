from bs4 import BeautifulSoup
import requests
import random

# Birthday Finder

def main():
    # User inputs search
    inputPerson = str(input("Enter a person: "))

    # Accesses wiki page of search term
    result = requests.get("https://en.wikipedia.org/wiki/" + inputPerson)

    # Gets html of wiki page
    src = result.content

    # Checks if person was found
    status = result.status_code
    if status == 404:
        print("Person not found. Try again")
        main()
    # Enters the html into BS4
    soup = BeautifulSoup(src, "html.parser")

    # Prints the name of the wiki page to verify it found the correct person

    name = soup.find("h1").text

    birthday = soup.find("span", {"class": "bday"})
    if birthday is None:
        print("No birthday was found")
        main()

    print(name + "'s birthday is " + birthday.text)
    print("\n")
    main()


main()
