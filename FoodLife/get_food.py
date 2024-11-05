def turn_raw_to_csv():
    # Get Text
    with open("./raw/raw.txt") as file:
        text = file.read()
    lines = text.split("\n")

    # Make CSV
    # strip removes whitespace which is useful.
    food = {}
    categories = None
    header = []
    for i, line in enumerate(lines):
        # Get local header
        # - Either empty line before or the first line        
        if i == 0 or lines[i-1] == "":
            categories = lines[i+1].split(" ")
        # Get global header
        for c in categories:
            if c not in header:
                header.append(c)

        # When there are items to get
        if "$" in line:
            # Clean line
            f = [line.strip() for line in line.split("$")]

            # Add to food
            food[f[0]] = {}
            for ki, k in enumerate(categories):
                food[f[0]][k] = f[ki]

    # Get text for csv
    # - Header
    db = ",".join(header) + "\n"
    # - Text
    for f in food:
        for hi, h in enumerate(header):
            # For all food, for all header items
            if h in food[f].keys():
                db += food[f][h]
            else:
                db+= "None"
            # Comma for all non final values
            if hi != len(header) - 1:
                db += ","
        # Newlines per food
        db += "\n"
    
    # Save File
    # w+ means write, + is create if file isn't there.
    with open("shelf_life.csv", "w+") as file:
        file.write(db)
    return


if __name__ == "__main__":
    turn_raw_to_csv()
