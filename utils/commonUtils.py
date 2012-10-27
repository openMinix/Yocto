import yocto
import re
import json
import urllib2
import simplejson

def render_template( template, **kwargs):
    """Renders the template with the given parameters """

    page_template = yocto.jinja_env.get_template( template )
    rendered_page = page_template.render ( **kwargs )

    return rendered_page


class Request(object):
    def __init__(self, textS):
        self.text = textS

    def create_list(self):
        re.sub(' +', ' ', self.text)
        if self.text[0] == ' ':
            self.text = self.text[1 : len(self.text)]
        if self.text[-1] == ' ':
            self.text = self.text[0 : len(self.text) - 1]

        self.list_args = self.text.split()

    def create_request(self):
        question = ""
        for i in range(len(self.list_args) - 1):
            question = question + str(self.list_args[i]) + '%20'
        question = question + str(self.list_args[len(self.list_args) - 1])
        self.url = ('https://ajax.googleapis.com/ajax/services/search/web'
                    '?v=1.0&q=' + question + '&userip=USERS-IP-ADDRESS')

    def get_results(self):
        request = urllib2.Request(self.url)
        response = urllib2.urlopen(request)
        self.links = []

        results = simplejson.load(response)
        for value in results["responseData"]["results"]:
            self.links.append(value["url"])

    def get_links(self):
        self.create_list()
        self.create_request()
        self.get_results()

        return self.links








