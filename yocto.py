import webapp2
import jinja2
from models import dbModels
from utils import commonUtils

jinja_env = jinja2.Environment( loader =
    jinja2.FileSystemLoader('./templates/'), autoescape = True )



class BaseHandler( webapp2.RequestHandler ):
    """Base class for handlers"""

    def render_response( self, template, **kwargs):
        """ Renders the template 'template' with the values from kwargs"""

        rendered_page = commonUtils.render_template( template, **kwargs )
        self.response.out.write( rendered_page )


class MainPageHandler( BaseHandler ):
    """Handler for the main page"""

    def get(self):
        posts = dbModels.Post.get_all_posts() 
        self.render_response('mainpage.html', posts = self.posts)
  
    def post(self):
        
        title = self.request.get('title')
        content = self.request.get('content')
        author = self.request.get('author')

        if title and content and author:
            post_entry = dbModels.Post( title = title, content = content,
                            author = author )
            post.put()

        self.redirect('/')





app = webapp2.WSGIApplication( [ ('/', MainPageHandler )
                                ], debug=True )
