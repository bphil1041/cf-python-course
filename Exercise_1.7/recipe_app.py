from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Database credentials
USERNAME = 'cf-python'
PASSWORD = 'password'
HOST = 'localhost'
DATABASE = 'task_database'

# Create engine object
engine = create_engine(
    f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}', echo=True)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'final_recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})>"

    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {self.ingredients}\nCooking Time: {self.cooking_time} minutes\nDifficulty: {self.difficulty}\n{'-'*20}"

    def calculate_difficulty(self):
        ingredients_count = len(self.return_ingredients_as_list())
        if self.cooking_time < 30 and ingredients_count < 5:
            self.difficulty = 'Easy'
        elif self.cooking_time < 60:
            self.difficulty = 'Medium'
        elif self.cooking_time >= 60:
            self.difficulty = 'Hard'
        else:
            self.difficulty = 'Intermediate'

    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return []
        return self.ingredients.split(", ")


Base.metadata.create_all(engine)


def create_recipe():
    name = input("Enter recipe name (max 50 chars): ")
    # Allow alphabetic characters and spaces
    while len(name) > 50 or not name.replace(" ", "").isalpha():
        name = input("Invalid input. Enter recipe name (max 50 chars): ")

    ingredients = []
    ingredients_count = int(
        input("How many ingredients would you like to enter? "))
    for i in range(ingredients_count):
        ingredient = input(f"Enter ingredient {i + 1}: ")
        ingredients.append(ingredient)

    cooking_time = input("Enter cooking time in minutes: ")
    while not cooking_time.isnumeric():
        cooking_time = input("Invalid input. Enter cooking time in minutes: ")

    ingredients_str = ", ".join(ingredients)

    recipe_entry = Recipe(
        name=name, ingredients=ingredients_str, cooking_time=int(cooking_time))
    recipe_entry.calculate_difficulty()

    session.add(recipe_entry)
    session.commit()

    print("Recipe created successfully!")


def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return

    for recipe in recipes:
        print(recipe)


def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes available.")
        return

    results = session.query(Recipe.ingredients).all()
    all_ingredients = []

    for result in results:
        temp_list = result[0].split(", ")
        for ingredient in temp_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    for idx, ingredient in enumerate(all_ingredients, 1):
        print(f"{idx}. {ingredient}")

    ingredient_nums = input(
        "Choose ingredients by entering their numbers separated by spaces: ").split()

    try:
        search_ingredients = [
            all_ingredients[int(num)-1] for num in ingredient_nums]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    conditions = [Recipe.ingredients.like(
        f"%{ingredient}%") for ingredient in search_ingredients]
    recipes = session.query(Recipe).filter(*conditions).all()

    if recipes:
        for recipe in recipes:
            print(recipe)
    else:
        print("No recipes found with those ingredients.")


def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes available.")
        return

    results = session.query(Recipe.id, Recipe.name).all()
    for recipe in results:
        print(f"{recipe.id}. {recipe.name}")

    recipe_id = input("Enter the ID of the recipe you'd like to edit: ")
    recipe_to_edit = session.query(Recipe).get(recipe_id)

    if recipe_to_edit:
        print("1. Name\n2. Ingredients\n3. Cooking Time")
        choice = input("Which attribute would you like to edit (1/2/3)? ")

        if choice == "1":
            new_name = input("Enter new name: ")
            recipe_to_edit.name = new_name
        elif choice == "2":
            new_ingredients = input("Enter new ingredients: ")
            recipe_to_edit.ingredients = new_ingredients
        elif choice == "3":
            new_time = input("Enter new cooking time: ")
            recipe_to_edit.cooking_time = int(new_time)

        recipe_to_edit.calculate_difficulty()
        session.commit()
        print("Recipe updated successfully.")
    else:
        print("Recipe not found.")


def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes available.")
        return

    results = session.query(Recipe.id, Recipe.name).all()
    for recipe in results:
        print(f"{recipe.id}. {recipe.name}")

    recipe_id = input("Enter the ID of the recipe you'd like to delete: ")
    recipe_to_delete = session.query(Recipe).get(recipe_id)

    if recipe_to_delete:
        confirm = input(
            f"Are you sure you want to delete {recipe_to_delete.name}? (y/n): ").lower()
        if confirm == "y":
            session.delete(recipe_to_delete)
            session.commit()
            print("Recipe deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Recipe not found.")


def main_menu():
    while True:
        print("\n--- Recipe App Main Menu ---")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit.")

        choice = input("Enter your choice: ").lower()

        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == 'quit':
            session.close()
            engine.dispose()
            print("Exiting the Recipe app. Goodbye!")
            break
        else:
            print("Invalid input, please try again.")


if __name__ == "__main__":
    main_menu()
