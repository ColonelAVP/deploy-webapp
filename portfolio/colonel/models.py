from django.db import models



# HOME section


class Home(models.Model):
    name = models.CharField(max_length=20)
    greeting1 = models.CharField(max_length=10)
    greeting2 = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# ABOUT section


class About(models.Model):
    heading = models.CharField(max_length=30)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)

# SKILLS Section


class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)

# PROJECTS Section


class Project(models.Model):
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Project {self.id}'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')

class Contact(models.Model):
    name= models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
