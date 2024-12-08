from flask import Flask
from flask_restx import Api, Resource, fields
import json

app = Flask(__name__)
api = Api(
    app,
    version='1.0',
    title='API Example',
    description='Une API simple avec documentation Swagger',
    doc='/docs'  # Point d'accès à la documentation Swagger
)

# Définir un namespace pour organiser les endpoints
ns = api.namespace('items', description='Opérations liées aux objets')

# Modèle de données pour Swagger
item_model = api.model('Item', {
    'id': fields.Integer(required=True, description='Identifiant unique'),
    'name': fields.String(required=True, description='Nom de l\'objet'),
})

# Données simulées
ITEMS = []

def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Charger les données avant de lancer le serveur Flask
ITEMS = load_data_from_json('data.json')

@ns.route('/')
class ItemList(Resource):
    @ns.marshal_list_with(item_model)
    def get(self):
        """Liste tous les objets"""
        print(ITEMS)
        return ITEMS

    @ns.expect(item_model)
    def post(self):
        """Ajoute un nouvel objet"""
        new_item = api.payload
        ITEMS.append(new_item)
        return new_item, 201

@ns.route('/<int:id>')
@ns.param('id', 'L\'identifiant de l\'objet')
@ns.response(404, 'Objet non trouvé')
class Item(Resource):
    @ns.marshal_with(item_model)
    def get(self, id):
        """Récupère un objet par son identifiant"""
        for item in ITEMS:
            if item['id'] == id:
                return item
        api.abort(404, "Objet non trouvé")

    def delete(self, id):
        """Supprime un objet par son identifiant"""
        global ITEMS
        ITEMS = [item for item in ITEMS if item['id'] != id]
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
