import os
from django.db import models

# Create your models here.
class DigitAssoc(models.Model):
    def get_user_filename(self, instance, filename):
        filename, filext = os.path.splitext(filename)
        filename = self.digit+filext
        return "user_{0}/{1}".format(instance.user.id, filename)


    digit = models.CharField(max_length=2, unique = True, verbose_name="Число")
    word = models.CharField(max_length=100, verbose_name="Ассоциация", blank=True)
    foto = models.ImageField(upload_to=get_user_filename)
    
    
    def __str__(self):
        return self.digit+" - "+self.word