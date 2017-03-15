from django.db import models
from aboutme.models import Profile


class Project(models.Model):
    """
    This model establishes the structure of the Project model.
    """

    def __str__(self):
        """
        This will display in string format the name of the Project object.
        """

        return str(self.name)

    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name='project')

    name = models.CharField('project name', max_length=64)
    date_start = models.DateField('start date')
    date_end = models.DateField('end date')
    url = models.URLField('project url')
    short_desc = models.CharField('short description', max_length=128)
    description = models.TextField('description')
