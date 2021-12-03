""" A BlogController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Blog import Blog

class BlogController(Controller):
    
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        id = self.request.param('id')
        return Blog.find(id)


    def index(self):
        return Blog.all()

    def create(self):
        id = self.request.param('id')
        title = self.request.input('title')
        body = self.request.input('body')
        blogpost = Blog.create({'title': title, "body": body})
        return blogpost

    def update(self):
        id = self.request.param('id')
        title = self.request.input('title')
        body = self.request.input('body')
        Blog.where('id', id).update({'title': title, "body": body})
        return Blog.where('id', id).get()

    def destroy(self):
        id = self.request.param('id')
        blogpost = Blog.where('id', id).get()
        Blog.where('id', id).delete()
        return blogpost