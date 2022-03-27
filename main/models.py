from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def articles_directory_path(instance, filename):
    return 'article_{s}-{f}'.format(s=instance.articles.title, f=filename)


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    body = models.TextField()
    image = models.ImageField(upload_to=articles_directory_path, blank=True)    # TODO: Path should contain a title

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField(default=timezone.now)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_articles")
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_articles")   # TODO: Test it

    ARTICLE_SUBJECT = [
        ('politic', 'Political article'),
        ('economic', 'Economic article'),
        ('auto', 'Article about auto'),
        ('realty', 'Realty article'),
    ]
    article_subject = models.CharField(max_length=42, choices=ARTICLE_SUBJECT, default='politic')   # TODO: Test without default

    def __str__(self):
        return self.title
