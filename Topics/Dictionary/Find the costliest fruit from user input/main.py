# Find the fruit with the highest price

fruit = {}


def find_max_fruit():
    max_price = 0
    max_fruit = ""
    for key, value in fruit.items():
        if value > max_price:
            max_price, max_fruit = value, key
    return max_fruit


# Read fruit-price pairs into a dictionary
def get_fruits():
    while True:
        name = input()
        if name == "":
            break
        else:
            price = input()
            fruit.update({name: float(price)})
    print(find_max_fruit())


get_fruits()
