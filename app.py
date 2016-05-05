#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
import json

app = Flask(__name__)

def load_recipes_from_file(file_path):
    with open(file_path) as f:
        recipes = json.load(f)
        return recipes
# load global from file
recipe_path = './recipes.json'
recipes = load_recipes_from_file(recipe_path)

@app.route('/recipe/api/v1.0/recipe', methods=['GET'])
def get_recipes():
    return jsonify({'recipes': recipes})

@app.route('/recipe/api/v1.0/recipe/<int:recipe_id>', methods=['GET'])
def get_task(recipe_id):
    task = [recipe for recipe in recipes if recipe['id'] == recipe_id]
    if len(recipe) == 0:
        abort(404)
    return jsonify({'recipes': task[0]})

@app.route('/')
def index():
    return "recipe-api-v1"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

