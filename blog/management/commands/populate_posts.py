from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populate the database with initial blog posts"

    def handle(self, *args: Any, **options: Any):
        titles = [
            "Django Basics",
            "Understanding Models",
            "Creating Views",
            "Templates in Django",
            "Django Forms",
            "Static Files Management",
            "Django Admin Customization",
            "User Authentication",
            "Django Middleware",
            "Testing in Django"
        ]

        contents = [
            "Learn the basics of Django, a powerful web framework for Python.",
            "Understand how to create and manage models in Django.",
            "Learn how to create views to handle requests and responses.",
            "Discover how to use templates to render HTML in Django.",
            "Get familiar with Django forms for user input handling.",
            "Manage static files like CSS and JavaScript in your Django project.",
            "Customize the Django admin interface for better usability.",
            "Implement user authentication and authorization in Django.",
            "Explore middleware and its role in request/response processing.",
            "Learn how to write tests for your Django applications."
        ]

        img_urls = [
            f"https://picsum.photos/seed/{i}/800/400" for i in range(1, len(titles) + 1)
        ]

        for title, content, img_url in zip(titles, contents, img_urls):
            Post.objects.create(title=title, content=content, img_url=img_url)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database with initial blog posts."))