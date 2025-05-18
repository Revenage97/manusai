from django.db import models
from django.contrib.auth.models import User
import os
import datetime

class Inventory(models.Model):
    kode = models.CharField(max_length=50, unique=True)
    nama_barang = models.CharField(max_length=255)
    kategori = models.CharField(max_length=100)
    harga_jual = models.DecimalField(max_digits=12, decimal_places=2)
    total_stok = models.IntegerField()
    
    def __str__(self):
        return f"{self.kode} - {self.nama_barang}"
    
    class Meta:
        verbose_name_plural = "Inventory"

class ActivityLog(models.Model):
    ACTION_CHOICES = [
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('upload', 'Upload File'),
        ('backup', 'Backup File'),
        ('password', 'Change Password'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"
    
    class Meta:
        ordering = ['-timestamp']

class ExcelFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    
    def __str__(self):
        return self.filename
    
    def save(self, *args, **kwargs):
        if not self.filename and self.file:
            self.filename = os.path.basename(self.file.name)
        super().save(*args, **kwargs)

class BackupFile(models.Model):
    file = models.FileField(upload_to='backups/')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    
    def __str__(self):
        return self.filename
    
    def save(self, *args, **kwargs):
        if not self.filename and self.file:
            self.filename = os.path.basename(self.file.name)
        super().save(*args, **kwargs)
