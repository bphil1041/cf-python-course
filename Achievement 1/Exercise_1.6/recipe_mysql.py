import mysql.connector

# Function to calculate difficulty based on cooking time and number of ingredients


def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
        return 'Medium'
    elif cooking_time >= 10 and len(ingredients) < 4:
        return 'Intermediate'
    else:
        return 'Hard'

# Function to create a new recipe


def create_recipe(conn, cursor):
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))

    # Calculate difficulty
    difficulty = calculate_difficulty(cooking_time, ingredients.split(','))

    # Insert the new recipe into the database
    cursor.execute('''
        INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
        VALUES (%s, %s, %s, %s)
    ''', (name, ingredients, cooking_time, difficulty))

    print("Recipe created successfully!\n")

# Function to search for recipes by ingredient


def search_recipe(conn, cursor):
    ingredient = input("Enter an ingredient to search for: ")
    query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(query, ("%" + ingredient + "%",))

    results = cursor.fetchall()

    if results:
        for row in results:
            print(
                f"ID: {row[0]}, Name: {row[1]}, Ingredients: {row[2]}, Cooking Time: {row[3]}, Difficulty: {row[4]}")
    else:
        print("No recipes found with that ingredient.\n")

# Function to update an existing recipe


def update_recipe(conn, cursor):
    recipe_id = int(input("Enter the ID of the recipe you want to update: "))

    new_name = input("Enter the new recipe name: ")
    new_ingredients = input("Enter the new ingredients (comma-separated): ")
    new_cooking_time = int(input("Enter the new cooking time (in minutes): "))

    # Calculate new difficulty
    new_difficulty = calculate_difficulty(
        new_cooking_time, new_ingredients.split(','))

    # Update the recipe in the database
    cursor.execute('''
        UPDATE Recipes
        SET name = %s, ingredients = %s, cooking_time = %s, difficulty = %s
        WHERE id = %s
    ''', (new_name, new_ingredients, new_cooking_time, new_difficulty, recipe_id))

    print("Recipe updated successfully!\n")

# Function to delete a recipe


def delete_recipe(conn, cursor):
    recipe_id = int(input("Enter the ID of the recipe you want to delete: "))

    # Delete the recipe from the database
    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))

    print("Recipe deleted successfully!\n")

# Main menu function


def main_menu(conn, cursor):
    while True:
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            conn.commit()  # Commit changes before exiting
            cursor.close()
            conn.close()  # Close the connection
            break
        else:
            print("Invalid choice, please try again.")


# Establish connection to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    password='password'
)

# Create a cursor object
cursor = conn.cursor()

# Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

# Create Recipes table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
''')

# Run the main menu
if __name__ == "__main__":
    main_menu(conn, cursor)
