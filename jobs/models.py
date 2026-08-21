from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    )

    title = models.CharField(max_length=200)
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posted_jobs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')
    description = models.TextField()
    location = models.CharField(max_length=150)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='Full Time')
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title