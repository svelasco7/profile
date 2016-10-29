import urllib2
import json


import webapp2
import logging
import jinja2
import os


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')

        url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=minions"
        result = urllib2.urlopen(url)
        kittygif = json.loads(result.read())
        cat_url = kittygif['data']['image_url']
        template_vars = {'cat_url': cat_url}

        # url="http://api.tumblr.com/v2/blog/maknae-t.tumblr.com/posts/text?api_key=fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4&notes_info=true"
        # result = urllib2.urlopen(url)
        # reblog = json.loads(result.read())
        # reblog_url = reblog['response']['posts']['reblog']
        # template_vars = {'reblog_url': reblog_url}


        self.response.write(template.render(template_vars))





jinja_environment = jinja2.Environment(loader =
    jinja2.FileSystemLoader(os.path.dirname(__file__)))



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
