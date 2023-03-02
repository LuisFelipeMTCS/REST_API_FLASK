from flask_restful import Resource

hoteis = [
    {
        'hotel_id':'alpha',
        'nome':'Alpha Hotel',
        'Estrelas': 4.3,
        'diaria': 420.434,
        'cidade':'Santa Cataria'
    },
    {
        'hotel_id':'bass',
        'nome':'bass Hotel',
        'Estrelas': 4.3,
        'diaria': 380.434,
        'cidade':'Santa '

    },
    {
        'hotel_id':'tico',
        'nome':'tico Hotel',
        'Estrelas': 4.3,
        'diaria': 520.434,
        'cidade':'Cataria'

    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
    
class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message':'hotel not found.'},404
    
    
    def post(self, hoteis_id):
        pass
    
    def put(self, hoteis_id):
        pass
    
    def delete(self, hoteis_id):
        pass