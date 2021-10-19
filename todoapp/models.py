from django.db import models

# Create your models here.

# Options Menu
PRIORITIES = (
    ('adanger', 'Prioritu High'),
    ('bwarning', 'Priority Medium'),
    ('csuccess', 'Priority Low')
)


class Username(models.Model):
    username = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.username


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Username, on_delete=models.CASCADE)
    title = models.CharField(max_length=207)
    description = models.CharField(max_length=5000, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=30,
                                choices=PRIORITIES,
                                default=PRIORITIES[0])
    complete = models.IntegerField(default=0)

    def __str__(self):
        return self.username + ' ' + self.title
