# Recipe App (Command Line Version)

## Objective
Build the command line version of a Recipe app, which acts as a precursor to its web app counterpart in Achievement 2.

## Context
This project focuses on learning Python fundamentals, data structures, and object-oriented programming. You'll also learn how to interact with databases using Python, which will help you when working with the Django framework. The project also aims to teach you standard programming practices that will make your code simpler, easier to read, and robust during execution.

## The 5 W's

1. **Who**: Your professional network and potential employers. Potential employers can view this project as a demonstration of your skills in Python. Achievement 2 is where you’ll deliver a project worthy of portfolio inclusion, while Achievement 1 can illustrate your Python scripting skills.
2. **What**: A command line application for a Recipe app, which is able to create, read, and modify recipes, as well as search for recipes based on ingredients.
3. **When**: The code will be readily available on your GitHub repository and will require a local installation of Python 3.6+ to run it on any machine.
4. **Where**: Your code can be run on any machine that has an active Python installation. You may either use your GitHub profile or your portfolio site to host the code for potential employers and your professional network to view.
5. **Why**: This Achievement is geared towards exhibiting your understanding of the fundamentals of Python programming and the potential to apply this knowledge when working with web application frameworks like Django.

## User Goals
- Users should be able to create and modify recipes with ingredients, cooking time, and a difficulty parameter that is automatically calculated by the app.
- Users should be able to search for recipes by their ingredients.

## Key Features
- Create and manage the user’s recipes on a locally hosted MySQL database.
- Option to search for recipes that contain a set of ingredients specified by the user.
- Automatically rate each recipe by their difficulty level.
- Display more details on each recipe if the user prompts it, such as the ingredients, cooking time, and difficulty of the recipe.

## Technical Requirements
- The app should handle any common exceptions or errors that may pop up during user input, database access, and display user-friendly error messages.
- The app must connect to a MySQL database hosted locally on your system.
- The app must provide an easy-to-use interface, supported by simple forms of input and concise instructions.
- The app should work on Python 3.6+ installations.
- App code must be well-formatted according to standardized guidelines.
- App code should also be supported by concise, helpful comments that illustrate the flow of the program.

## Nice to Have
- Ideally, the application should be able to handle any kind of input from the user. Test the limits of your application by entering erroneous choices, random characters, or long strings.
- Make an instruction manual! A simple, one-page document would do: it should describe the features of your application, as well as simple instructions that can take the user through your program. You can use the README file of your GitHub repository for hosting this instruction manual.

## Installation and Setup

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/bphil1041/cf-python-course
   cd cf-python-course
