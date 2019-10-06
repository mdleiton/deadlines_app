from django.db import models
from users.models import Student
from tasks.models import Task
from apps.models import ModelWithTimeStamp

class Submission(ModelWithTimeStamp):
    ''' This model stores informations about academic task submissions '''
    
    students = models.ManyToManyField(Student, blank=False)

    task = models.ForeignKey(Task, on_delete=models.SET_NULL,  null=True)

    STATUS_CHOICES = (
        ("1", "Not yet defined"),
        ("2", "Under Revision"),
        ("3", "Accepted"),
        ("4", "Rejected"),
    )

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='1')