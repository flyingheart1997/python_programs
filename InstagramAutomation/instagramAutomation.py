from instabot import Bot

i_bot = Bot()
i_bot.login(username='', password='')
i_bot.follow('')
i_bot.upload_photo('', caption='')
i_bot.unfollow('')
i_bot.send_message('message', ['fnd u_name', 'fnd u_name'])
followers = i_bot.get_user_followers('username')
for follower in followers:
    print(i_bot.get_user_info(follower))

followings = i_bot.get_user_following('username')
for following in followings:
    print(i_bot.get_user_info(following))
