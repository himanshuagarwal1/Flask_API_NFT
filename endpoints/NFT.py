from flask_restful import Api, Resource, reqparse,request, fields, marshal_with, marshal
from data_models.All_models import Nft
from data import db



# Serializing NFT Objects
nft_fields ={
    'id':fields.Integer,
    "asset_id": fields.Integer,
    "name": fields.String,
    "picture" : fields.String,
    "external_link": fields.String,
    "description": fields.String,
    "collection": fields.List(fields.Nested({ 
                                        'id':fields.Integer,                                  
                                        'uuid': fields.Integer
                                        })),
    "supply": fields.Integer,
    "royalties" : fields.Integer,
    "date_of_creation" : fields.String,
    "buyer": fields.String,
}


nft_list_fields = {
    'count': fields.Integer,
    'NFT': fields.List(fields.Nested(nft_fields)),
}

# NFT Argumnets parsing 
nft_post_parser = reqparse.RequestParser()
nft_post_parser.add_argument('asset_id', type=int, required=True, help='uuid parameter is required')
nft_post_parser.add_argument('name', type=str, required=True, help='name parameter is required')                             
nft_post_parser.add_argument('picture', type=str, required=True, help='picture parameter is required')                           
nft_post_parser.add_argument('external_link', type=str, required=True, help='external link parameter is required')                           
nft_post_parser.add_argument('description', type=str, required=True, help='description parameter is required')  
nft_post_parser.add_argument('supply', type=int, required=True, help='supply parameter is required')
nft_post_parser.add_argument('royalties', type=int, required=True, help='royalties parameter is required')                           
nft_post_parser.add_argument('date_of_creation', help='date parameter is required')                           
nft_post_parser.add_argument('buyer', type=str, required=True, help='buyer parameter is required')




# NFT class driver code
class NftResource(Resource):
    def get(self, Nft_id=None):
        if Nft_id:
            nft1 = Nft.query.filter_by(id=Nft_id).first()
            return marshal(nft1, nft_fields)
        else:
            args = request.args.to_dict()
               
            nft1 = Nft.query.filter_by(**args).order_by(Nft.date_of_creation)           
            nft1 = nft1.all()
            return marshal({
                'count': len(nft1),
                'NFT': [marshal(x, nft_fields) for x in nft1]
            }, nft_list_fields)

    @marshal_with(nft_fields)
    def post(self):
        args = nft_post_parser.parse_args()
        print(args["name"])
        nft = Nft(**args)
        print(nft.name)
        db.session.add(nft)
        db.session.commit()

        return nft, 201

