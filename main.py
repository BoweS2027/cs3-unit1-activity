def get_ready():
    print("Get dough")
    print("Get sauce")
    print("Get cheese")

def welcome_message():
    print("Welcome to Python's Virtual Kitchen!")
    print("Today, we’ll learn how to make pizza")

def list_ingredients(main_ingredient, side_dish):
    print(f"Main Ingredient: {main_ingredient}")
    print(f"Side Dish: {side_dish}")

def make_dish(ingredient1, ingredient2, ingredient3):
    return f"shape {ingredient1}, spread {ingredient2}, and spread {ingredient3}"

def add_spice(dish, spice="oregano"):
    print(f"Add a dash of {spice} to the {dish}. Yum!")

def cook_recipe():
    welcome_message()
    get_ready()
    list_ingredients("dough", "garlic knots")
    make_dish("dough", "sauce", "cheese")
    add_spice("pizza")

cook_recipe()
