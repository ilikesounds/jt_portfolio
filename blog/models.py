from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from aboutme.models import Profile
# from django.utils.text import slugify


@python_2_unicode_compatible
class Blog(models.Model):
    """
    This model establishes the structure of the blog article for jt_portfolio.
    """

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='blog',
    )

    PRIVATE, PUBLIC = 'Prv', 'Pub'

    PUBLISHED_CHOICES = (
        (PRIVATE, 'Private'),
        (PUBLIC, 'Public')
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


class BlogManager(models.Manager):
    def get_queryset(self):
        queryset = super(BlogManager, self).get_queryset().filter(
            published_status='Pub'
            )
        queryset = queryset.order_by('-date_created')
        return queryset
