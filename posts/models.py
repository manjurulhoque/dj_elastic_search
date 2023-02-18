from django.db import models
from django.utils import timezone

from posts.es_search import PostDocument


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    posted_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def indexing(self):
        obj = PostDocument(
            meta={'id': self.id},
            posted_date=self.posted_date,
            title=self.title,
            body=self.body
        )
        obj.save()
        return obj.to_dict(include_meta=True)
