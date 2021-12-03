"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({'title': 'Learning HTML', 'body': 'Going good!'})
        Blog.create({'title': 'Learning JavaScript', 'body': 'Going great!'})
        Blog.create({'title': 'Learning React', 'body': 'Going not so good.'})
        Blog.create({'title': 'Learning Python', 'body': 'Going good!'})
