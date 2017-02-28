from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
# from django.utils.text import slugify


@python_2_unicode_compatible
class Blog(models.Model):
    """
    This model establishes the structure of the blog article for jt_portfolio.
    """

    PRIVATE, SHARED, PUBLIC = 'Pri', 'Shr', 'Pub'

    PUBLISHED_CHOICES = (
        (PRIVATE, 'Private'),
        (SHARED, 'Shared'),
        (PUBLIC, 'Public')
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author'
    )

    title = models.CharField('Title',
                             max_length=128,
                             blank=False,
                             null=False
                             )

    date_created = models.DateTimeField('Date Created')
    date_modified = models.DateTimeField('Date Modified',
                                         blank=True,
                                         null=True)
    published_status = models.CharField('Published Status',
                                        max_length=3,
                                        choices=PUBLISHED_CHOICES,
                                        default=PRIVATE)

    body = models.TextField('Body')

    def __str__(self):
        """
        This will display in string format the blog object
        """

        blog = str(self.title)
        return blog
