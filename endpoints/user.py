from flask_restful import Api, Resource, reqparse,request, fields, marshal_with, marshal
from data_models.All_models import User
from  data import db
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
        print(args)
        print(args["user_wallet"])
        print(type(args))
        user = User(**args)
        db.session.add(user)
        db.session.commit()

        return user, 201