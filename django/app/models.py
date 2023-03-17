from django.db import models
from autoslug import AutoSlugField
from utilities.models import BaseImage

class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("app:test_models", args=[self.slug])

    def __str__(self):
        return self.name


class TestModelImage(BaseImage):
    test_model = models.ForeignKey(TestModel, related_name='images', on_delete=models.CASCADE)
    sort_order = models.SmallIntegerField(default=0)

    caption = models.CharField(max_length=191, default='', blank=True)

    class Meta:
        ordering = ('sort_order', 'pk')

    def __str__(self):
        return self.image.url
