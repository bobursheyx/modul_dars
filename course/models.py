from django.db import models

class Speciality(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='course/speciality/')
    create_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"

class Course(models.Model):
    class PriceType(models.TextChoices):
        s = "USD", "$"
        sum = "UZS","so`m"

    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='course/course/')
    description = models.TextField()
    active_users = models.PositiveIntegerField(default=0)
    price = models.FloatField()
    price_type = models.CharField(max_length=10, choices=PriceType.choices,default=PriceType.sum, null=True)
    reyting = models.FloatField(default=0)
    speciality = models.ManyToManyField(Speciality)
    create_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
class Position(models.Model):
    name = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='course/teacher/')
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    x_link = models.URLField(null=True, blank=True)
    m_link = models.URLField(null=True, blank=True)
    l_link = models.URLField(null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} "