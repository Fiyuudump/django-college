from django.contrib import admin
from . models import About, Client, Projects, Service, SocialMedia, Testimonial

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

# ----------------------------------------------------------------

class ProjectsAdmin(ModelAdmin):
    list_display=['category', 'title', 'project_link', 'desc', 'image']
    search_fields=['category', 'title']
    list_filter=('category', 'title')
    list_per_page=5

class AboutAdmin(ModelAdmin):
    list_display=['title', 'desc']
    search_fields=['title']
    list_filter=('title', 'desc')
    list_per_page=4

class ServiceAdmin(ModelAdmin):
    list_display=['title', 'desc', 'css_icon']
    search_fields=['title']
    list_filter=('title', 'desc')
    list_per_page=6

class SocialMediaAdmin(ModelAdmin):
    list_display=['link', 'icon']
    search_fields=['link']
    list_filter=('link', 'icon')
    list_per_page=4

class ClientAdmin(ModelAdmin):
    list_display=['link', 'icon']
    search_fields=['link']
    list_filter=('link',)
    list_per_page=8

class TestimonialAdmin(ModelAdmin):
    list_display=['say', 'author_img', 'author', 'job_title']
    search_fields=['author']
    list_filter=('author', 'job_title')
    list_per_page=3

admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Testimonial, TestimonialAdmin)

