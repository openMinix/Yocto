import webapp2
import jinja2
import models.dbModels

jinja_env = jinja2.Environment( loader =
    jinja2.FileSystemLoader('./templates/'), autoescape = True )



class BaseHandler( webapp2.RequestHandler ):
    """Base class for handlers"""

    def render_response( self, template, **kwargs):
        """ Renders the template 'template' with the values from kwargs"""

        page_template = jinja_env.get_template( template )
        rendered_page = page_template.render( **kwargs )
        self.response.out.write( rendered_page )




class MainPageHandler( BaseHandler ):
    """Handler for the main page"""

    def get(self):
        self.render_response ( 'mainpage.html')



app = webapp2.WSGIApplication( [ ('/', MainPageHandler )
                                ], debug=True )
