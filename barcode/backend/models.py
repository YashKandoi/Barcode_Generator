from django.db import models
from django.utils import timezone
import os

def input_file_path(instance, filename):
    return os.path.join('input_files', filename)

def output_file_path(instance, filename):
    return os.path.join('output_files', filename)

class MyModel(models.Model):
    input_file1 = models.FileField(upload_to=input_file_path)
    text_input1 = models.CharField(max_length=100)
    text_input2 = models.CharField(max_length=100)
    text_input3 = models.CharField(max_length=100)
    text_input4 = models.CharField(max_length=100)
    output_file = models.FileField(upload_to=output_file_path)
