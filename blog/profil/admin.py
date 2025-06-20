from django.contrib import admin
from . models import Barang, Jenis, About, Project

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


class BarangAdmin(ModelAdmin):
    list_display=['kdbrg', 'nama', 'stok', 'harga', 'link_gambar', 'waktu_posting', 'jenis_id']
    search_fields=['kdbrg', 'nama', 'jenis_id__nama']
    list_filter=('nama', 'jenis_id',)
    list_per_page=5

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)
admin.site.register(About)
admin.site.register(Project)

