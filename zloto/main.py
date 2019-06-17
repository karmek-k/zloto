import sys
import locale

from zloto.data import Fetcher, JSONParser


locale.setlocale(locale.LC_TIME, ('pl_PL', 'UTF-8'))
def main():
    # load args
    if len(sys.argv) > 2:
        print("Nieprawidłowa ilość argumentów!")
        sys.exit(1)
    elif len(sys.argv) == 2:
        try:
            mass = int(sys.argv[1])
        except ValueError:
            print("Nieprawidłowy typ argumentu!")
            sys.exit(1)
    else:
        mass = 1

    # load data from NBP
    fetch = Fetcher(Fetcher.url)
    if fetch.data == b"":
        print("Nie można pobrać danych.")
        sys.exit(1)
    
    # parse JSON
    parser = JSONParser(fetch.data)

    # print message
    message = "W dniu {} {}g złota próby 1000 kosztował(y) {} złotych."
    print(
        message.format(
            parser.date.strftime("%d %B %Y"),
            mass,
            round(parser.price * mass),
        )
    )
    