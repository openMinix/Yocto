import webapp2
import jinja2
import models.dbModels
import utils.commonUtils

jinja_env = jinja2.Environment( loader =
    jinja2.FileSystemLoader('./templates/'), autoescape = True )



class BaseHandler( webapp2.RequestHandler ):
    """Base class for handlers"""

    def render_response( self, template, **kwargs):
        """ Renders the template 'template' with the values from kwargs"""

        self.response.out.write( commonUtils.render_template( template, **kwargs
) )



class MainPageHandler( BaseHandler ):
    """Handler for the main page"""

    def get(self):
        self.render_response ( 'mainpage.html')



app = webapp2.WSGIApplication( [ ('/', MainPageHandler )
                                ], debug=True )
