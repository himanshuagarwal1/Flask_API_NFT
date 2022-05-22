

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse,request, fields, marshal_with, marshal
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
from data import db



app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False





@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)


from endpoints.collection import collectionsResource
from endpoints.NFT import NftResource   
from endpoints.user  import userResource


# Routing URLS
api.add_resource(userResource, '/users', '/users/<int:user_id>')
api.add_resource(NftResource, '/NFT', '/NFT/<int:Nft_id>')
api.add_resource(collectionsResource, '/collections', '/collections/<int:collection_id>')
db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
