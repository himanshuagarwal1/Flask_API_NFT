from data import db
 

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


