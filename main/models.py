from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# def articles_directory_path(instance, filename):      # TODO: Try to make it work
#     return 'article_{s}-{f}'.format(s=instance.Articles.title, f=filename)


class Articles(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish_at')

    body = models.TextField()
    image = models.ImageField(upload_to='articles/imgs/', blank=True)    # TODO: May be path should contain a slug mb
    # TODO: Image must be compressed by Pillow for example + unique name for imgs

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField(default=timezone.now)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_articles')
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_articles")   # TODO: Test it

    ARTICLE_SUBJECT = [
        ('politic', 'Political article'),
        ('economic', 'Economic article'),
        ('auto', 'Article about auto'),
        ('realty', 'Realty article'),
    ]
    article_subject = models.CharField(max_length=42, choices=ARTICLE_SUBJECT, default='politic')   # TODO: Try it without default

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:detailed_article',
                       args=[self.publish_at.year,
                             self.publish_at.month,
                             self.publish_at.day,
                             self.slug])


class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.article.title, self.name)
