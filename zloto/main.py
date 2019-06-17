import sys
import locale

from zloto.data import Fetcher, JSONParser


locale.setlocale(locale.LC_TIME, ('pl_PL', 'UTF-8'))
def main():
    # load data from NBP
    fetch = Fetcher(Fetcher.url)
    if fetch.data == b"":
        print("Nie można pobrać danych.")
        sys.exit(1)
    
    # parse JSON
    parser = JSONParser(fetch.data)

    # print message
    message = "W dniu {0} 1g złota próby 1000 kosztował {1} złotych."
    print(message.format(
        parser.date.strftime("%d %B %Y"),
        parser.price
    ))
    