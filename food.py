from datetime import datetime, timedelta


class Food:
    def __init__(self, name, food_group, storage_time, added):
        self.name = name
        self.food_group = food_group
        self.storage_time = storage_time
        self.added = added
        self.expiration = datetime.strptime(added, "%d-%m-%y") + timedelta(days=int(storage_time))        
        exp_text = str(self.expiration).split(" ")[0].split("-")
        self.expiration_text = f'{exp_text[1]}/{exp_text[2]}/{exp_text[0][-2:]}'
        self.days_left = (self.expiration - datetime.now()).days
        self.color = self.get_color()
        return
    
    def get_color(self):
        if self.days_left < 0:
            return "black"
        elif self.days_left == 0:
            return "red"
        elif 1 <= self.days_left <= 3:
            return "orange"
        elif 4 <= self.days_left <= 7:
            return "yellow"
        else:
            return "green"

    def __repr__(self):
        return f"Food('{self.name}', '{self.food_group}', {self.storage_time}, {repr(self.added)})"

    def get_info(self):
        return self.name, self.food_group, self.storage_time, self.added


class Fridge:
    def __init__(self):
        # Initializes
        self.contents = []
        self.get_csv()
        self.stock()
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
            if f is not None:
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
        with open("fridge.txt", "r+") as file:
            text = file.read()
            for f in text.split('\n'):
                if f != "":
                    f = eval(f)
                    self.add(f)

        self.sort()
        return

    def save(self):
        # Saves to file
        with open("fridge.txt", "w+") as file:
            for f in self.contents:
                if f is not None:
                    file.write(repr(f))
                    file.write("\n")
        return

    def add(self, f):
        # TODO Smart insert so don't need to sort every time 
        if isinstance(f, str):
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

        elif isinstance(f, Food):
            self.contents.append(f)
            self.sort()

        return

    def get_all(self):
        # Returns all food
        all_food = [(i, f) for i, f in enumerate(self.contents) if f is not None]
        return all_food

    def count_food(self):
        counts = [0 for i in range(5)]
        for f in self.contents:
            if f is not None:
                counts[["green", "yellow", "orange", "red", "black"].index(f.color)] += 1
        return counts

    def purge(self):
        self.contents = []
        self.save()
        return
