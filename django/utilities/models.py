from django.db import models
from django.core.files import File
from PIL import Image, ImageOps
import os
import io


# size_300 = (300,300)

# i = Image.open(file)
# fn, ext = os.path.splitext(file)
# i.thumbnail(size_300)
# i.save('dirname/{}_300x300{}'.format(fn, ext))


class BaseImage(models.Model):
    image = models.ImageField(
        verbose_name="image",
        upload_to="images/%Y/%m/%d/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name="Alternative text",
        max_length=255,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        im = Image.open(self.image)
        # Convert Image to RGB color mode
        im = im.convert('RGB')
        # auto_rotate image according to EXIF data
        im = ImageOps.exif_transpose(im)
        # save image to BytesIO object
        im_io = io.BytesIO() 
        # save image to BytesIO object
        im.save(im_io, 'JPEG', quality=70) 
        # create a django-friendly Files object
        new_image = File(im_io, name=self.image.name)
        # Change to new image
        self.image = new_image
        super().save(*args, **kwargs)