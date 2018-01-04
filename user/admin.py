from django.contrib import admin

from .models import User, Rank, Group, Type, Dept


# Register your models here.

class RankAdmin(admin.ModelAdmin):
    model = Rank


class GroupAdmin(admin.ModelAdmin):
    model = Group


class TypeAdmin(admin.ModelAdmin):
    model = Type


class DeptAdmin(admin.ModelAdmin):
    model = Dept


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('基本信息', {'fields': ['userID', 'userName', 'userRankDR', 'userDeptDR', 'userGroupDR', 'userTypeDR']}),
        ('开始时间', {'fields': ['userStDatetime']}),
        ('结束时间', {'fields': ['userEndDatetime']}),

    ]
    list_display = (
        'userID', 'userName', 'userName', 'userPassword', 'userStDatetime', 'userEndDatetime', 'userRankDR',
        'userDeptDR',
        'userGroupDR', 'userTypeDR')
    list_filter = [ 'userID', 'userName', 'userName', 'userPassword', 'userStDatetime', 'userEndDatetime', 'userRankDR',
        'userDeptDR',
        'userGroupDR', 'userTypeDR']
    search_fields = ['userID', 'userName', 'userName', 'userPassword', 'userStDatetime', 'userEndDatetime',
                   ]


admin.site.register(Rank, RankAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Dept, DeptAdmin)
admin.site.register(User, UserAdmin)
