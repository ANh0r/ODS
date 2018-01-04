# Generated by Django 2.0.1 on 2018-01-04 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptID', models.CharField(max_length=200)),
                ('deptName', models.CharField(max_length=200)),
                ('deptStDatetime', models.DateTimeField(verbose_name='开始时间')),
                ('deptEndDatetime', models.DateTimeField(verbose_name='结束时间')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupID', models.CharField(max_length=200)),
                ('groupName', models.CharField(max_length=200)),
                ('groupStDatetime', models.DateTimeField(verbose_name='开始时间')),
                ('groupEndDatetime', models.DateTimeField(verbose_name='结束时间')),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rankID', models.CharField(max_length=200)),
                ('rankName', models.CharField(max_length=200)),
                ('rankStDatetime', models.DateTimeField(verbose_name='开始时间')),
                ('rankEndDatetime', models.DateTimeField(verbose_name='结束时间')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeID', models.CharField(max_length=200)),
                ('typeName', models.CharField(max_length=200)),
                ('typeStDatetime', models.DateTimeField(verbose_name='开始时间')),
                ('typeEndDatetime', models.DateTimeField(verbose_name='结束时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=200, verbose_name='工号')),
                ('userName', models.CharField(max_length=200, verbose_name='用户名')),
                ('userPassword', models.CharField(max_length=200, verbose_name='密码')),
                ('userStDatetime', models.DateTimeField(verbose_name='开始时间')),
                ('userEndDatetime', models.DateTimeField(verbose_name='结束时间')),
                ('userDeptDR', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Dept')),
                ('userGroupDR', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Group')),
                ('userRankDR', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Rank')),
                ('userTypeDR', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Type')),
            ],
        ),
    ]