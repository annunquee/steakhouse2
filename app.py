# Database configuration
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
#from flask_script import Manager

# Create the Flask application instance
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask_user:yourpassword@localhost/restaurant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
#migrate = Migrate(app, db)

# Import models after initializing db 
from models import *

# Set the static folder
app.config['STATIC_FOLDER'] = 'static'

# Define routes
@app.route('/')
def home():
    categories = Category.query.all()
    return render_template('index.html', categories=categories)

@app.route('/recipes')
def recipes():
    all_recipes = Recipe.query.all()  # Fetch all recipes
    return render_template('recipes.html', recipes=all_recipes)

@app.route('/recipe/<int:id>')
def recipe_detail(id):
    recipe = Recipe.query.get_or_404(id)
    return render_template('recipe.html', recipe=recipe)

@app.route('/recipes/<int:category_id>')
def category_recipes(category_id):
    category = Category.query.get_or_404(category_id)
    recipes = Recipe.query.filter_by(category_id=category_id).all()
    return render_template('recipes.html', category=category, recipes=recipes)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# Run the application if executed directly
if __name__ == '_main_':
    app.run(debug=True)