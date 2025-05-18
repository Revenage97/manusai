from django.contrib import admin
from .models import Inventory, ActivityLog, ExcelFile, BackupFile

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('kode', 'nama_barang', 'kategori', 'harga_jual', 'total_stok')
    search_fields = ('kode', 'nama_barang', 'kategori')
    list_filter = ('kategori',)

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp', 'details')
    list_filter = ('action', 'user', 'timestamp')
    search_fields = ('user__username', 'details')
    readonly_fields = ('user', 'action', 'timestamp', 'details')

@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'uploaded_by', 'uploaded_at')
    list_filter = ('uploaded_at', 'uploaded_by')
    search_fields = ('filename', 'uploaded_by__username')
    readonly_fields = ('uploaded_at', 'uploaded_by')

@admin.register(BackupFile)
class BackupFileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'created_by', 'created_at')
    list_filter = ('created_at', 'created_by')
    search_fields = ('filename', 'created_by__username')
    readonly_fields = ('created_at', 'created_by')
