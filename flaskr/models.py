from flaskr import db

class Entry(db.Model):
    __tablename__='entries'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)
    image = db.Column(db.Text)
    usernames = db.Column(db.Text)
    username = db.Column(db.String(100), default='', nullable=False)
    password = db.Column('password', db.String(100), nullable=False)

    def __repr__(self):
        return '<Entry id={id},title={title!r},text={text!r}>'.format(id=self.id,title=self.title,text=self.text)

    # def init_db():
    # db.drop_all()
    # db.create_all()
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100), default='', nullable=False)
    password = db.Column('password', db.String(100), nullable=False)

    def __repr__(self):
        return '<Entry id={id},username={username!r},password={password!r}>'.format(id=self.id, username=self.username, password=self.password)

# '<Entry id={id},title={title!r}>'.format(id=self.id,title=self.title)とかなんで全部じゃないのか。

def init():
    db.create_all()
