# Exercise_1.3.py

recipes_list = []
ingredients_list = []


def take_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input(
        "Enter the ingredients (separated by commas): ").split(',')
    ingredients = [ingredient.strip() for ingredient in ingredients]

    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    return recipe


n = int(input("How many recipes would you like to enter? "))

for _ in range(n):
    recipe = take_recipe()

    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    recipes_list.append(recipe)

for recipe in recipes_list:
    name = recipe['name']
    cooking_time = recipe['cooking_time']
    ingredients = recipe['ingredients']
    num_ingredients = len(ingredients)

    if cooking_time < 10:
        if num_ingredients < 4:
            difficulty = 'Easy'
        else:
            difficulty = 'Medium'
    else:
        if num_ingredients < 4:
            difficulty = 'Intermediate'
        else:
            difficulty = 'Hard'

    print(f"\nRecipe: {name}")
    print(f"Cooking Time (in minutes): {cooking_time}")
    print(f"Ingredients: {', '.join(ingredients)}")
    print(f"Difficulty: {difficulty}")

print("\nAll ingredients used:")
for ingredient in sorted(ingredients_list):
    print(ingredient)
