from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    css_icon = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Projects(models.Model):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    project_link = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upload_file/', null=False, blank=False)
    gallery = models.ImageField(upload_to='upload_file/', null=False, blank=False)

    def __str__(self):
        return self.title

class SocialMedia(models.Model):
    link = models.CharField(max_length=200)
    icon = models.CharField(max_length=20)

    def __str__(self):
        return self.icon

class Client(models.Model):
    link = models.CharField(max_length=200)
    icon = models.FileField(upload_to='upload_file/', null=False, blank=False)

    def __str__(self):
        return self.link

class Testimonial(models.Model):
    say = models.TextField()
    author_img = models.ImageField(upload_to='upload_file/', null=False, blank=False)
    author = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)

    def __str__(self):
        return self.author
