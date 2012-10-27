from google.appengine.ext import db
import datetime
from utils import commonUtils


class Post(db.Model):
    content = db.TextProperty()
    title   = db.StringProperty()
    author  = db.StringProperty()
    date    = db.DateTimeProperty( auto_now_add = True )
    votes   = db.IntegerProperty( default = 0 )

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
        return commonUtils.render_template('post.html', post = self )

