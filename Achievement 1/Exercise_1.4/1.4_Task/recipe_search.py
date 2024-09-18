import pickle


def display_recipe(recipe):
    print(f"Recipe Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print(f"Difficulty: {recipe['difficulty']}")
    print()


def search_ingredient(data):
    all_ingredients = data["all_ingredients"]

    print("Available ingredients:")
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}. {ingredient}")

    try:
        index = int(input(
            "Enter the number corresponding to the ingredient you want to search for: "))
        ingredient_searched = all_ingredients[index]
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
        return

    print(f"\nRecipes containing {ingredient_searched}:")
    for recipe in data["recipes_list"]:
        if ingredient_searched in recipe["ingredients"]:
            display_recipe(recipe)


filename = input("Enter the filename containing your recipes: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print(f"File {filename} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    search_ingredient(data)
