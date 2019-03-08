#coding:utf-8
from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Device(models.Model):
    syslist = ((1, 'win7-64'),(2, 'win7-32'),(3, 'winxp'),(4, 'win10-32'),(5, 'win10-64'))
    dnamelist = ((1, '联想（Lenovo）'),(2, '戴尔（Dell）'),(3, '惠普（HP）'),(4, '兄弟（Brother）'),(5, '理光'))
    dtypelist = ((1, '计算机'),(2, '打印机'),(3, '自媒体设备'))

    dnum = models.CharField(max_length=20,verbose_name='设备编号')  # x00001
    dname = models.IntegerField(choices=dnamelist,default=1,verbose_name='设备品牌') # 品牌
    dtype = models.IntegerField(choices=dtypelist,default=1,verbose_name='设备类型') # 设备类型   打印机  计算机  交换机
    cpname = models.CharField(max_length=20,verbose_name='设备名称') # 设备名称
    ip = models.GenericIPAddressField(protocol='ipv4',verbose_name='IP地址') # IP
    mac = models.CharField(max_length=20,verbose_name='MAC地址') # mac
    disk = models.CharField(max_length=50,verbose_name='磁盘序列号') # disk
    systype = models.IntegerField(choices=syslist,default=1,verbose_name='系统型号') # systype
    dlocation = models.CharField(max_length=50,verbose_name='物理位置') # dlocation
    ctime = models.DateTimeField(default=timezone.now,verbose_name='创建时间') # dlocation
    room = models.ForeignKey("Room", on_delete=models.CASCADE,verbose_name='房间号')
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, verbose_name='所属人',default='')

    def __unicode__(self):
        return self.cpname

    class Meta:
        ordering = ['cpname']
        verbose_name = '设备信息'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    tname = models.CharField(max_length=20,verbose_name='职员')
    desc = models.CharField(max_length=30,verbose_name='职务',default='')
    tel = models.CharField(max_length=15,verbose_name='电话')
    phone = models.CharField(max_length=11,verbose_name='手机')
    room = models.ForeignKey("Room", on_delete=models.CASCADE,verbose_name='房号')
    # device = models.ManyToManyField("Device",verbose_name='拥有设备')

    def __unicode__(self):
        return self.tname

    class Meta:
        ordering = ['tname']
        verbose_name = '职工信息'
        verbose_name_plural = verbose_name

class Post(models.Model):
    postname = models.CharField(max_length=20,verbose_name='科室名称')

    def __unicode__(self):
        return self.postname

    class Meta:
        verbose_name = '科室信息'
        verbose_name_plural = verbose_name


class Flow(models.Model):
    flow = models.CharField(max_length=20,verbose_name='楼层')

    def __unicode__(self):
        return self.flow

    class Meta:
        verbose_name = '楼层信息'
        verbose_name_plural = verbose_name


class Room(models.Model):
    roomnum = models.CharField(max_length=5, verbose_name='房间号')
    # postname = models.CharField(max_length=20, verbose_name='科室名称')
    postname = models.ForeignKey(Post,verbose_name='科室名称',on_delete=models.CASCADE)
    function = models.CharField(max_length=10, verbose_name='房间功能')
    flow = models.ForeignKey(Flow, verbose_name='楼层',on_delete=models.CASCADE)

    def __unicode__(self):
        return self.roomnum

    class Meta:
        ordering = ['roomnum']
        verbose_name = '房间信息'
        verbose_name_plural = verbose_name