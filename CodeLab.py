import itchat

# 导入itchat 包

itchat.auto_login(enableCmdQR=2, hotReload=True)

# 登录微信

itchat.send('Hello, filehelper', toUserName='filehelper')

# 发送消息