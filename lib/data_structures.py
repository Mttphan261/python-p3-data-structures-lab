spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    return [el['name'] for el in spicy_foods]
    pass


def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    return spiciest_foods
    pass


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_emoji = '🌶' * food['heat_level']
        print(
            f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emoji}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    pass


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print_spicy_foods([food])
    pass


def get_average_heat_level(spicy_foods):
    total_heat = 0
    num_foods = len(spicy_foods)
    for food in spicy_foods:
        total_heat += food['heat_level']
    average_heat_level = total_heat / num_foods
    return average_heat_level 
    pass


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
