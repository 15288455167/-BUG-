LANGUAGE_CODE = 'zh-hans'

# SMS配置 ######################################
SMS_APP_KEY = "ac9b62723a0dde09411f53688658088b"  # API秘钥管理SecretKey
SMS_APPID = '1400724391'  # 应用列表SDK AppID
SMS_SIGN = '不知名鸽子'  # 签名管理的内容

# redis配置 ########################
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.43.53:6379",  # 安装redis的主机的 IP 和 端口
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                "encoding": 'utf-8'
            },
            "PASSWORD": "123456"  # redis密码
        }
    }
}