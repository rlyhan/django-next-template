from django.db import models
from autoslug import AutoSlugField

class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("app:test_models", args=[self.slug])

    def __str__(self):
        return self.name
