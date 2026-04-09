italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]

def find_meal(name, menu):
    name_lower = name.lower()
    for item in menu:
        if item.lower() == name_lower:
            return item
    return None

def select_meal(name, food_type):
    if food_type == "Italian":
        return find_meal(name, italian_food)
    elif food_type == "Indian":
        return find_meal(name, indian_food)
    else:
        return None

def display_available_meals(food_type):
    if food_type == "Italian":
        print("Available Italian Meals: ")
        for italian_foods in italian_food:
            print(italian_foods)
    elif food_type == "Indian":
        print("Available Indian Meals: ")
        for indian_foods in indian_food:
            print(indian_foods)
    else:
        print("Invalid food type")

def create_summary(name, amount, food_type):
    order = select_meal(name, food_type)
    if order:
        return f"Success! You ordered {amount} {order}"
    else:
        return "Meal not found on the menu."

print("Welcome to the Food Order System!")

while True:
    type_input = input("Italian/Indian?").strip().title()
    if type_input in ["Italian", "Indian"]:
        display_available_meals(type_input)
        break 
    else:
        print(" Invalid food type. Please choose 'Italian' or 'Indian'")

name_input = input("Enter meal name: ").strip()
while True:
    try:
        amount_input = int(input("Enter amount: "))
        if amount_input > 0:
            break
        else:
            print("Amount must be greater than 0.")
    except ValueError:
        print(" Please enter a valid number.")

result = create_summary(name_input, amount_input, type_input)
print(result)
