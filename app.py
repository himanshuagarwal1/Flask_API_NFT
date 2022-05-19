

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse,request, fields, marshal_with, marshal
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions




app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)


##### Database Models

# User Model
class User(db.Model):  
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_wallet = db.Column(db.Integer, db.ForeignKey('collection.id'), nullable = False)

    def __repr__(self):
        return 'Id: {}, user_wallet: {}'.format(self.id, self.user_wallet)


# Collection model
class Collection(db.Model):
    __tablename__ = 'collection'    
    id= db.Column(db.Integer, primary_key=True, unique = True)
    uuid= db.Column(db.Integer,db.ForeignKey("nft.id"), nullable = False)
    name=  db.Column(db.String(50))
    description= db.Column(db.Text())
    creator= db.relationship('User', backref='collection', lazy='select')
    creator_network= db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return 'Id: {}, name: {},description: {},creator: {},creator_network: {}'.format(self.id, self.name, self.description, self.creator, self.creator_network)


# NFT Model
class Nft(db.Model):
    __tablename__ = 'nft'
    id = db.Column(db.Integer, primary_key=True)
    asset_id= db.Column(db.Integer, nullable = False)
    name= db.Column(db.String(50))
    picture = db.Column(db.Text())
    external_link= db.Column(db.Text())
    description= db.Column(db.Text())
    collection= db.relationship('Collection', backref ="nft" , lazy='select')
    supply= db.Column(db.Integer, nullable = False)
    royalties = db.Column(db.Integer, nullable = False)
    date_of_creation = db.Column(db.String(50))
    buyer= db.Column(db.Text())

    def __repr__(self):
        return 'Id: {}, asse_id: {}, name: {}, picture: {}, external_link: {}, description: {}, royalties: {}, date: {}, buyer:{}'.format(self.id, self.asset_id, self.name, self.picture, self.external_link, self.description, self.royalties, self.date_of_creation, self.buyer)



# creating model
db.create_all()


# Serializing User Objects
user_fields = {
    'id': fields.Integer, 
    'user_wallet': fields.Integer
}

users_list_fields = {
    'count': fields.Integer,
    'user': fields.List(fields.Nested(user_fields)),
}

# User Argumnets parsing 
user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument('user_wallet', type=int, required=True,  help='user-wallet parameter is required')


# User class driver code
class userResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.filter_by(id=user_id).first()
            return marshal(user, user_fields)
        else:
            args = request.args.to_dict()
            user = User.query.filter_by(**args).order_by(User.id)           
            user = user.all()

            return marshal({
                'count': len(user),
                'user': [marshal(t, user_fields) for t in user]
            }, users_list_fields)

    @marshal_with(user_fields)
    def post(self):
        args = user_post_parser.parse_args()
        user = User(**args)
        db.session.add(user)
        db.session.commit()

        return user, 201

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
        nft = Nft(**args)
        db.session.add(nft)
        db.session.commit()

        return nft, 201








# Routing URLS
api.add_resource(userResource, '/users', '/users/<int:user_id>')
api.add_resource(NftResource, '/NFT', '/NFT/<int:Nft_id>')
api.add_resource(collectionsResource, '/collections', '/collections/<int:collection_id>')



if __name__ == '__main__':
    app.run(debug=True)
