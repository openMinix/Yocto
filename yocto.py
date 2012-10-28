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
        posts = dbModels.Post.get_all_posts().order('-date')
        links = []
        contents = []

        results = ""
        for post in posts[0 : 3]:
            request = commonUtils.Request(post.title)
       #     tweets = commonUtils.search ( post.title )
            links += request.get_links()
            contents += request.get_content()
            results = commonUtils.render_template('google_results.html',
                links = links, contents = contents )

        self.render_response('mainpage.html', posts = posts,
            results = results )

    def post(self):
        title = self.request.get('title')
        content = self.request.get('content')
        author = self.request.get('author')

        if title and content and author:
            post_entry = dbModels.Post( title = title, content = content,
                            author = author )
            post_entry.put()

        self.redirect('/')


class VoteHandler( BaseHandler ):
    """Handles voting"""

    def get(self):
        post_id = int (self.request.get('post_id') )
        sign = self.request.get('sign')
        votes = self.request.get('votes')

        post = dbModels.Post.get_by_id( post_id )

        post.vote( sign )
        post.put()

        self.response.out.write( str( post.votes ) )


class UpdateHandler( BaseHandler ):
    """Handles posts update """

    def get(self):
        if self.request.get('links') == "yes":
            posts = dbModels.Post.get_all_posts().order('-date')
            links = []
            contents = []

            for post in posts[0 : 3]:
                request = commonUtils.Request(post.title)
                links += request.get_links()
                contents += request.get_content()

            self.render_response('google_results.html', 
            links = links, contents = contents)
   

        elif self.request.get('latest_post') == "":
            self.response.out.write("")
        else:
            latest_post_id = int( self.request.get('latest_post') )
            latest_post = dbModels.Post.get_by_id( latest_post_id )
        
        
            posts = dbModels.Post.all().filter(" date > ", latest_post.date ).order("-date")
        
            response_text = ""
        
            for post in posts:
                response_text += post.render()

            self.response.out.write( response_text )




app = webapp2.WSGIApplication( [ ('/', MainPageHandler ),
                                 ('/vote', VoteHandler ),
                                 ('/update', UpdateHandler)
                                ], debug=True )
