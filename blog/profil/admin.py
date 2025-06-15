from django.contrib import admin
from .models import Barang, Jenis

# Register your models here.
class BarangAdmin(admin.ModelAdmin):
    list_display=['kdbrg', 'nama', 'stok', 'harga', 'link_gambar', 'waktu_posting', 'jenis_id']
    search_fields=['kdbrg', 'nama', 'jenis_id__nama']
    list_filter=('nama', 'jenis_id',)
    list_per_page=5

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)
