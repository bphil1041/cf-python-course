class Recipe:
    all_ingredients = []

    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None

    # Getter and Setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # Getter and Setter for cooking_time
    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, cooking_time):
        self._cooking_time = cooking_time
        self.calculate_difficulty()

    # Method to add ingredients
    def add_ingredients(self, *ingredients):
        self.ingredients.extend(ingredients)
        self.update_all_ingredients()
        self.calculate_difficulty()

    # Getter for ingredients
    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        self._ingredients = ingredients

    # Method to calculate difficulty
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    # Getter for difficulty
    @property
    def difficulty(self):
        if self._difficulty is None:
            self.calculate_difficulty()
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self._difficulty = difficulty

    # Method to search for an ingredient
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    # Method to update all ingredients
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    # String representation of the Recipe object
    def __str__(self):
        return (f"Recipe for {self.name}:\n"
                f"Ingredients: {', '.join(self.ingredients)}\n"
                f"Cooking time: {self.cooking_time} minutes\n"
                f"Difficulty: {self.difficulty}")

# Function to search for recipes with a specific ingredient


def recipe_search(data, search_term):
    print(f"Searching for recipes with {search_term}:\n")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
            print("-" * 40)


# Creating Recipe objects and displaying their string representations
tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
print(tea)

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)

cake = Recipe("Cake", 50)
cake.add_ingredients("Sugar", "Butter", "Eggs",
                     "Vanilla Essence", "Flour", "Baking Powder", "Milk")
print(cake)

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients(
    "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
print(banana_smoothie)

# Wrapping the recipes into a list
recipes_list = [tea, coffee, cake, banana_smoothie]

# Using the recipe_search() method to search for recipes with specific ingredients
for ingredient in ["Water", "Sugar", "Bananas"]:
    recipe_search(recipes_list, ingredient)
    print("=" * 40)
