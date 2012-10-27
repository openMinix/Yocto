from google.appengine.ext import db
import datetime


class Post(db.Model):
    content = db.TextProperty()
    name    = db.StringProperty()
    date    = db.DateTimeProperty()
    votes   = db.IntegerProperty()

    @classmethod
    def get_by_name(cls, name):
        return cls.all().filter("name =", name).get()


