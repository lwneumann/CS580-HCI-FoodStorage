class Fridge:
    def __init__(self):
        # Initializes
        self.contents = []
        return
    
    def stock(self):
        # Checks Local File to populate
        return

    def add(self, f):
        self.contents.append(f)
        return

    def add_card(self, cart):
        for i in cart:
            self.add(i)
        return

    def get_all(self):
        # Returns all food
        return [f.get_info() for f in self.contents]


class Food:
    def __init__(self, name, product, storage_time, storage, life_time, added):
        self.name = name
        self.product = product
        self.storage_time = storage_time
        self.storage = storage
        self.life_time = life_time
        self.added = added
        return
    
    def get_info(self):
        
        return



def load_csv():
    with open("./FoodLife/shelf_life.csv") as file:
        text = file.read()

    text = text.split("\n")
    flife = [ line.split(',') for line in text ]

    """
    names = [ f[0] for f in flife[1:] ]

    while True:
        print()
        print()
        search = input("What is your food?\n")
        print()
        for n in names:
            if search.lower() in n.lower():
                print(n)
    """

    print(text[0])
    for i, l in enumerate(text):
        if "open" in l:
            print(flife[i][0])
    return


if __name__ == "__main__":
    load_csv()
