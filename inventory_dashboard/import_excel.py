import os
import django
import sys

# Set up Django environment
sys.path.append('/home/ubuntu/new_django_project/inventory_dashboard')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_dashboard.settings')
django.setup()

import openpyxl
from dashboard.models import Inventory, ActivityLog
from django.contrib.auth.models import User

def import_excel_data():
    # Get admin user for logging
    try:
        admin_user = User.objects.get(username='kasir')
    except User.DoesNotExist:
        print("Admin user 'kasir' not found. Creating...")
        admin_user = User.objects.create_superuser('kasir', 'kasir@example.com', 'rascat')
    
    # Load Excel file
    excel_path = '/home/ubuntu/upload/Laporan_Manajemen_Barang_Cabang_2025_05_17_06_58_10.xlsx'
    print(f"Loading Excel file from: {excel_path}")
    
    wb = openpyxl.load_workbook(excel_path)
    sheet = wb.active
    
    # Skip header row
    rows = list(sheet.rows)[1:]
    
    # Clear existing inventory
    Inventory.objects.all().delete()
    print("Cleared existing inventory data")
    
    # Process rows
    count = 0
    for row in rows:
        kode = row[0].value
        nama_barang = row[1].value
        kategori = row[2].value
        harga_jual = row[3].value or 0
        total_stok = row[4].value or 0
        
        if kode and nama_barang:  # Ensure required fields exist
            Inventory.objects.create(
                kode=kode,
                nama_barang=nama_barang,
                kategori=kategori or '',
                harga_jual=harga_jual,
                total_stok=total_stok
            )
            count += 1
    
    # Log activity
    ActivityLog.objects.create(
        user=admin_user,
        action='upload',
        details=f"Import script: {count} items imported from {os.path.basename(excel_path)}"
    )
    
    print(f"Successfully imported {count} inventory items")
    return count

if __name__ == "__main__":
    import_excel_data()
