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
        self.render_response( 'mainpage.html')



app = webapp2.WSGIApplication( [ ('/', MainPageHandler )
                                ], debug=True )
