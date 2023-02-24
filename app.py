from flask import Flask 
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

hoteis = [
    {
        'hoteis':'alpha',
        'nome':'Alpha Hotel',
        'Estrelas': 4.3,
        'diaria': 420.434,
        'cidade':'Santa Cataria'
    },
    {
        'hoteis':'bass',
        'nome':'bass Hotel',
        'Estrelas': 4.3,
        'diaria': 380.434,
        'cidade':'Santa '

    },
    {
        'hoteis':'tico',
        'nome':'tico Hotel',
        'Estrelas': 4.3,
        'diaria': 520.434,
        'cidade':'Cataria'

    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis':hoteis}
    
api.add_resource(Hoteis,'/hoteis')

if __name__ == '__main__':
    app.run(debug=True)
        