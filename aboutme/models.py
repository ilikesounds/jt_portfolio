from django.db import models
from django.conf import settings


class Profile(models.Model):
    """
    This model establishes the structure of the Profile model.
    """

    def __str__(self):
        """
        This will display in string format the name of the edu object
        """

        fn = self.user.get_full_name().strip() or self.user.get_username()
        return "{}".format(fn)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='user'
    )

    street_addr = models.CharField('street address', max_length=128)
    unit = models.CharField('unit', max_length=8)
    city = models.CharField('city', max_length=64)
    state = models.CharField('state', max_length=4)
    post_code = models.CharField('postal code', max_length=5)
    mobile = models.CharField('mobile', max_length=10)
    email = models.CharField('email', max_length=64)
    repo = models.CharField('repo', max_length=64)


class Job(models.Model):
    """
    This model establishes the structure of the Job model.
    """

    def __str__(self):
        """
        This will display in string format the name of the job object
        """

        return str(self.title)

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='job',
    )

    title = models.CharField('title', max_length=64)
    company = models.CharField('company', max_length=64)
    location = models.CharField('location', max_length=64)
    date_start = models.DateField('start date')
    date_end = models.DateField('end date')
    short_desc = models.CharField('short description', max_length=128)
    description = models.TextField('description')


class Edu(models.Model):
    """
    This model establishes the structure of the Edu model.
    """

    def __str__(self):
        """
        This will display in string format the name of the edu object
        """

        return str(self.school)

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='school',
    )
    school = models.CharField('school', max_length=64)
    degree = models.CharField('degree', max_length=32)
    field_of_study = models.CharField('field of study', max_length=64)
    date_start = models.DateField('start date')
    date_end = models.DateField('end date')
    short_desc = models.CharField('short description', max_length=128)
    description = models.TextField('description')


class Skills(models.Model):
    """
    This models establishes the structure of Skills model.
    """

    def __str__(self):
        """
        This will display in string format the name of the Skill
        """

        return str(self.name)

    skill_type = models.CharField('skill type', max_length=16)
    skill_name = models.CharField('skill name', max_length=16)
    skill_description = models.TextField('skill description')
    skill_strength = models.IntegerField('skill_strength')
    
