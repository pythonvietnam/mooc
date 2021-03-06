from django.db import models
from django.conf import settings

from ars.core.models import UserProfile


class Teacher(models.Model):
    profile = models.OneToOneField(UserProfile,
                                default=None, related_name='teacher')

    class Meta:
        db_table = 'teacher'

    def __str__(self):
        return 'Teacher {}'.format(self.name)

    @property
    def username(self):
        return self.profile.user.username

    @property
    def avatar(self):
        if self.profile.avatar:
            return self.profile.avatar.url
        return None
