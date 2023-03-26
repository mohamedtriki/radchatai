from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete


class Profile(models.Model):
    plans=(("none","none"),("individual","individual"),("monthly","monthly"),("yearly","yearly"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=200,choices=plans,default="none")
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




class report(models.Model):
    author = models.TextField(default="",blank=True)
    report_image= models.ImageField(help_text="up to 20 reports",blank=True,default="")
    report_text=models.TextField(default="",blank=True)
    def __str__(self):
        return self.author

@receiver(pre_delete, sender=report)
def delete_image(sender, instance, **kwargs):
    instance.report_image.delete(False)



class feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    feedback=models.TextField(default="",blank=True)
    def __str__(self):
        return self.author.username