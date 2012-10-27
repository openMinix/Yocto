import webapp2
import jinja2
import models.dbModels

jinja_env = jinja2.Environment( loader =
    jinja2.FileSystemLoader('./templates/'), autoescape = True )



class BaseHandler( webapp2.RequestHandler ):
    """Base class for handlers"""
    
    def render( self, template, **kwargs):
    """ Renders the template 'template' with the values from kwargs"""

        page_template = jinja_env.get_template( template )
        rendered_page = page_template( **kwargs )
        self.response.out( rendered_page )

    


class MainPageHandler( BaseHandler ):

    def get(self):
        self.render ( 'mainpage.html')






app = webapp2.WSGIApplication( [ ('/', MainPageHandler )
                                ], debug=True )
