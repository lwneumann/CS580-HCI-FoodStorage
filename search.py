from datetime import datetime
from food import Food


def search(phrase):
    if phrase is not None:
        with open("./FoodLife/shelf_life.csv") as file:
            text = file.read()

        text = text.split("\n")
        flife = [ line.split(',') for line in text[1:] ]
        names = [ f[0] for f in flife ]
        search_result = []

        for i, n in enumerate(names):
            if len(flife[i]) > 3 and flife[i][2] != "None" and phrase.lower() in n.lower():
                search_result.append(n)
        return search_result
    else:
        return []


if __name__ == "__main__":
    search("coffee")
