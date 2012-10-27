from google.appengine.ext import db
import datetime


class Post(db.Model):
    content = db.TextProperty()
    title   = db.StringProperty()
    author  = db.StringProperty()
    date    = db.DateTimeProperty()
    votes   = db.IntegerProperty()

    @classmethod
    def get_by_name(cls, name):
        return cls.all().filter("author =", name).get()

    @classmethod
    def get_all_posts(cls):
        """Returns all posts"""
        return cls.all()

    @classmethod
    def get_popular_posts( votes ):
        """Returns posts with more votes than ' votes '"""
        self.votes = int(votes)
        return cls.all().filter("votes >", votes )

    @classmethod
    def get_unpopular_posts( votes ):
        """Returns posts with less votes than ' votes '"""
        self.votes = int(votes)
        return cls.all().filter( "votes <", vote )

    def render(self):
        return comm
