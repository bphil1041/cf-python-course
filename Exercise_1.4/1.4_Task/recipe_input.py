import pickle


def take_recipe():
    recipe_name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input(
        "Enter the ingredients (separated by commas): ").split(',')
    ingredients = [ingredient.strip() for ingredient in ingredients]

    difficulty = calc_difficulty(cooking_time, ingredients)

    recipe = {
        "name": recipe_name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }

    return recipe


def calc_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients)

    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    return difficulty


filename = input("Enter the filename to store recipes: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }
except Exception as e:
    print(f"An error occurred: {e}")
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }
finally:
    recipes_list = data.get("recipes_list", [])
    all_ingredients = data.get("all_ingredients", [])

num_recipes = int(input("How many recipes would you like to enter? "))

for _ in range(num_recipes):
    recipe = take_recipe()
    recipes_list.append(recipe)

    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

data = {
    "recipes_list": recipes_list,
    "all_ingredients": all_ingredients
}

with open(filename, 'wb') as file:
    pickle.dump(data, file)

print(f"Recipes have been saved to {filename}.")
