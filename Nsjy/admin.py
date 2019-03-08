#coding:utf-8
from django.contrib import admin
from .models import  Device,Room,Teacher,Flow,Post

# 设置后台标题
admin.site.site_header = '南山教育局运维系统'
admin.site.site_title = '南山教育局运维'

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    readonly_fields = ['dnum']
    list_display = ['dname','cpname','ip','mac','room']

    list_per_page = 10
    ordering = ('-room',)
    search_fields = ('dnum','dname','ip','mac','room')
    list_filter = ('room__flow',)
    list_display_links = ('ip',)
    list_editable = ['dname']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['postname','flow','roomnum','function']
    search_fields = ('roomnum',)
    list_filter = ('flow',)
    list_per_page = 10

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['tname','desc','tel','phone','room']
    search_fields = ('tname',)
    list_filter = ('room__flow',)
    list_per_page = 10


@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):
    list_display = ('id','flow',)
    list_display_links = None
    list_per_page = 10

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','postname',)
    list_display_links = None
    list_per_page = 10

