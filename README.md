postgresql
://
steakhouse_kyzx_user
:
xhX2olDlBglWIfzueyTSZ6u49YEqMf0j
@
dpg-ct71rj0gph6c73c5n5pg-a.oregon-postgres.render.com
/
steakhouse_kyzx
 
link to github https://github.com/annunquee/steakhouse2.git

link to github pages https://annunquee.github.io/steakhouse2/

# This website is based on a restaurant

Recipe Management System
This project implements a Recipe Management System using Flask, SQLAlchemy, and PostgreSQL. The focus is on creating and managing recipes and associating them with predefined categories.


Features Implemented

Database Models
Category Table:
Fields: 
id (Primary Key)
name (String, max 100 characters, required)
image (String with the image name, the image file is stored on the file system)
Purpose: 
Stores recipe categories.
Categories are displayed in a dropdown when creating or editing a recipe.

Recipe Table:
Fields: 
id (Primary Key)
name (String, max 100 characters, required)
ingredients (Text, required)
instructions (Text, required)
image (String, optional, for future use)
category_id (Foreign Key, links to the Category table)
Purpose: 
Stores recipe details, including the category it belongs to.

CRUD Functionality
Recipes
Create:
Users can add new recipes.
A dropdown menu dynamically fetches and displays all available categories.
Read:
A list of all recipes is displayed.
Recipes include their associated category names.
Update:
Recipes can be edited.
The category dropdown is prefilled with the correct category.
Delete:
Users can delete recipes.
Categories
Categories are read dynamically to display in the recipe dropdown but are not editable via the current application interface.

3. Javascript
Form Validation for Create Recipes
Delete is implemented using JavaScript, for example when a user clicks delete a dialog box appears asking are they sure they want to delete. 
4. CSS 
Fully Mobile responsive application
Clean, modern design 
Elements on the screen are spaced out to reflect a modern design 

5. Templates and HTML
All web-pages follow the same base template which is defined in base.html. 
Each HTML file extend base.html 

How It Works
Category Integration:
Categories are pre-created using SQL and stored in the database.
When creating or editing a recipe, categories are dynamically fetched and displayed in a dropdown to ensure accurate selection.
Recipe Management:
Recipes are the main focus of this application, allowing users to add, view, edit, and delete them seamlessly.
Data Relationships:
Recipes are linked to categories via a ForeignKey (category_id), enabling relational functionality in the database.

Technologies Used
Flask: Web framework.
SQLAlchemy: ORM for database interaction.
PostgreSQL: Relational database.
SQL: To create tables and insert categories. sql is available in db.sql


Deployment
Code Hosting: GitHub.
Database Hosting: Render.com.
