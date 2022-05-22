from flask_restful import Api, Resource, reqparse,request, fields, marshal_with, marshal
from data_models.All_models import Collection
from data import db




# Serializing Collection Objects
collection_fields = {
    'id': fields.Integer,
    'uuid': fields.Integer,
    'name':fields.String,
    'description':fields.String,
    'creator': fields.List(fields.Nested({ 'id':fields.Integer ,                                
                                        'user_wallet': fields.Integer
                                        })),   
    'creator_network':fields.Integer,
}

collection_list_fields = {
    'count': fields.Integer,
    'collections': fields.List(fields.Nested(collection_fields)),
}


# Collection Argumnets parsing 
collection_post_parser = reqparse.RequestParser()

collection_post_parser.add_argument('uuid', type=int, required=True, help='uuid parameter is required')
collection_post_parser.add_argument('name', type=str, required=True, help='name parameter is required')
collection_post_parser.add_argument('description', type=str, required=True, help='description parameter is required')
collection_post_parser.add_argument('creator_network', type=int, required=True, help='creator_network parameter is required')


# Collection class driver code
class collectionsResource(Resource):
    def get(self, collection_id=None):
        if collection_id:
            collection = Collection.query.filter_by(id=collection_id).first()
            print(collection)
            
            print(collection.name)
            return marshal(collection, collection_fields)
        else:
            args = request.args.to_dict()
            collection = Collection.query.filter_by(**args).order_by(Collection.id)          
            collection = collection.all()

            return marshal({
                'count': len(collection),
                'collections': [marshal(u, collection_fields) for u in collection]
            }, collection_list_fields)

    @marshal_with(collection_fields)
    def post(self):
       
        args = collection_post_parser.parse_args()
        collection = Collection(**args)

        db.session.add(collection)
        db.session.commit()

        return collection, 201