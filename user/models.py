import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class Rank(models.Model):
    rankID = models.CharField(max_length=200)
    rankName = models.CharField(max_length=200)
    rankStDatetime = models.DateTimeField('开始时间', default=timezone.now)
    rankEndDatetime = models.DateTimeField('结束时间')


class Dept(models.Model):
    deptID = models.CharField(max_length=200)
    deptName = models.CharField(max_length=200)
    deptStDatetime = models.DateTimeField('开始时间', default=timezone.now)
    deptEndDatetime = models.DateTimeField('结束时间')


class Group(models.Model):
    groupID = models.CharField(max_length=200)
    groupName = models.CharField(max_length=200)
    groupStDatetime = models.DateTimeField('开始时间', default=timezone.now)
    groupEndDatetime = models.DateTimeField('结束时间')


class Type(models.Model):
    typeID = models.CharField(max_length=200)
    typeName = models.CharField(max_length=200)
    typeStDatetime = models.DateTimeField('开始时间', default=timezone.now)
    typeEndDatetime = models.DateTimeField('结束时间')


class User(models.Model):
    userID = models.CharField('工号', max_length=200)
    userName = models.CharField('用户名', max_length=200)
    userPassword = models.CharField('密码', max_length=200)
    userStDatetime = models.DateTimeField('开始时间', default=timezone.now)
    userEndDatetime = models.DateTimeField('结束时间')
    userRankDR = models.OneToOneField(Rank, on_delete=models.CASCADE, primary_key=True)
    userDeptDR = models.OneToOneField(Dept, on_delete=models.CASCADE, primary_key=True)
    userGroupDR = models.OneToOneField(Group, on_delete=models.CASCADE, primary_key=True)
    userTypeDR = models.OneToOneField(Type, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return 'userID:' + self.userID + ',userName:' + self.userName

    def was_user_end(self):
        return self.userEndDatetime == ""

    def was_user_start_not_end(self):
        return self.userStDatetime != "" & (self.userEndDatetime == "" | self.userEndDatetime > timezone.now())

    was_user_start_not_end.admin_order_field = 'userEndDatetime'
    was_user_start_not_end.boolean = True
    was_user_start_not_end.shor_description = '用户是否有效'
