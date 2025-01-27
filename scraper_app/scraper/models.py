from django.db import models

class Task(models.Model):
    scenario = models.CharField(max_length=50)
    input_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

class ScrapedData(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='scraped_data')
    name = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

