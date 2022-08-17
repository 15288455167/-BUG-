from django import forms
from user import models
import random

from django.shortcuts import render, redirect, HttpResponse
from django_redis import get_redis_connection

from utils.tencent.SMS import send_sms_single
from django.conf import settings


# Create your views here.
# 操作redis数据库
def index(request):
    conn = get_redis_connection('default')
    conn.set('nickname', '军涛哥', ex=60)
    value = conn.get('nickname')
    print(value)
    return HttpResponse("OK")


# 用户注册、登录
class User_rigis(forms.ModelForm):
    code = forms.CharField(label='验证码', widget=forms.PasswordInput)
    confirm = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta:
        model = models.User_register
        fields = ['username', 'email', 'password', 'confirm', 'mobile_phone', 'code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                'class': "form-control",
                'placeholder': "请输入{}".format(field.label),
            }


def user_regis(request):
    form = User_rigis()
    return render(request, 'user_regis.html', {"form": form})


def send_code(request):
    """ 发送短信
        ?tpl=login  -> 548762
        ?tpl=register -> 548760
    """
    code = random.randrange(1000, 9999)
    res = send_sms_single('15288455167', 1511966, [code, ])
    if res['result'] == 0:
        return HttpResponse('成功')
    else:
        return HttpResponse(res['errmsg'])
