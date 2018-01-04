import datetime  # 时间处理
from django.test import TestCase
from django.utils import timezone  # 当前时区
from .models import User


# Create your tests here.

class UserModelTests(TestCase):
    def was_user_start_not_end(self):
        """
        was_user_start_not_end()判断用户是否有效，
        有效 返回True 否则返回False
        :return: True or False
        """
        pastDateTime = timezone.now() - datetime.timedelta(days=30)  # 生成一个过去时间
        nowDateTime = timezone.now()  # 当前时间
        futureDateTime = timezone.now() + datetime.timedelta(days=30)  # 未来的时间
        user_with_no_st = User()
        self.assertIs(user_with_no_st.was_user_start_not_end(), False)

        # user_past_st_no_ed = User(userStDatetime=pastDateTime)
        # self.assertIs(user_past_st_no_ed.was_user_start_not_end(), True)
        # user_past_st_past_ed = User(userStDatetime=pastDateTime, userEndDatetime=pastDateTime)
        # self.assertIs(user_past_st_past_ed.was_user_start_not_end(), False)
        # user_past_st_now_ed = User(userStDatetime=pastDateTime, userEndDatetime=nowDateTime)
        # self.assertIs(user_past_st_now_ed.was_user_start_not_end(), False)
        #
        # user_now_st_no_ed = User(userStDatetime=nowDateTime)
        # self.assertIs(user_now_st_no_ed.was_user_start_not_end(), True)
        # user_now_st_future_ed = User(userStDatetime=nowDateTime, userEndDatetime=futureDateTime)
        # self.assertIs(user_now_st_future_ed.was_user_start_not_end(), True)
        #
        # user_past_st_future_ed = User(userStDatetime=pastDateTime, userEndDatetime=futureDateTime)
        # user_future_st_no_ed = User(userStDatetime=futureDateTime)
        # self.assertIs(user_future_st_no_ed.was_user_start_not_end(), False)
