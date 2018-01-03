from django.contrib import admin

from .models import User, Rank, Group, Type, Dept


# Register your models here.

class RankInline(admin.TabularInline):
    model = Rank


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('工号', {'fields': ['userID']}),
        ('姓名', {'fields': ['userName']}),
        ('密码', {'fields': ['userPassword']}),
        ('开始时间', {'fields': ['userStDatetime']}),
        ('结束时间', {'fields': ['userEndDatetime']}),
    ]
    list_display = ('userID', 'userName', 'userName', 'userPassword', 'userStDatetime', 'userEndDatetime', 'was_user_start_not_end')
    list_filter = ['userStDatetime']
    search_fields = ['userID', 'userName']


admin.site.register(User, UserAdmin)
