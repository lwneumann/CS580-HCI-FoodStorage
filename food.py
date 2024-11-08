from datetime import datetime, timedelta


class Food:
    def __init__(self, name, food_group, storage_time, added):
        self.name = name
        self.food_group = food_group
        self.storage_time = storage_time
        self.added = added
        self.expiration = datetime.strptime(added, "%d-%m-%y") + timedelta(days=int(storage_time))
        return
    
    def __repr__(self):
        return f"Food({self.name}, {self.food_group}, {self.storage_time}, {repr(self.added)}, {repr(self.expiration)})"

    def get_info(self):
        return self.name, self.food_group, self.storage_time, self.added


class Fridge:
    def __init__(self):
        # Initializes
        self.contents = []
        self.get_csv()
        return
    
    def get_csv(self):
        with open("./FoodLife/shelf_life.csv") as file:
            text = file.read()

        text = text.split("\n")
        self.food_life = [ line.split(',') for line in text[1:] ]
        return

    def sort(self):
        # Sorts by death
        # sorted(list)
        new_index = []

        # Get all times
        for i, f in enumerate(self.contents):
            new_index.append([f.expiration, i])

        # Sort
        new_index = sorted(new_index)

        # Reorder
        new_content = []
        for i in new_index:
            new_content.append(self.contents[i[1]])

        self.contents = new_content
        return

    def stock(self):
        # Checks Local File to populate

        self.sort()
        return

    def save(self):
        # Saves to file
        with open("fridge.txt", "w+") as file:
            for f in self.contents:
                file.write(repr(f))
                file.write("\n")
        return

    def add(self, f):
        # Smart insert so don't need to sort every time 
        for i, fod in enumerate(self.food_life):
            if fod[0] == f:
                f = Food(
                        self.food_life[i][0],
                        self.food_life[i][1],
                        self.food_life[i][2],
                        datetime.today().strftime('%d-%m-%y')
                    )
                self.contents.append(f)
                self.sort()
                self.save()
                return

    def get_all(self):
        # Returns all food
        return [f for f in self.contents]
