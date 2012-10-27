import webapp2
import jinja2


jinja_env = jinja2.Environment( loader =
    jinja2.FileSystemLoader('./templates/'), autoescape = True )


class MainPageHandler( webapp2.RequestHandler ):

    def get(self):

        self.template = jinja_env.get_template( 'extended.html' )
        self.rendered_template = self.template.render()
        self.response.out.write( self.rendered_template )








app = webapp2.WSGIApplication( [ ('/.*', MainPageHandler )
                                ], debug=True )
