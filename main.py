from instabot import Bot
from time import sleep
import os
import glob


cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])


my_bot = Bot()

my_bot.login(username = 'Your email' , password = 'Your password')


# دریافت لیست فالوورهای کاربر هدف
target_username = "Your TARGET_USERNAME"
followers = my_bot.get_user_followers(target_username , 20)

username_list = []
for follower in followers:
    username_follower = my_bot.get_username_from_user_id(int(follower))
    username_list.append(username_follower)



with open(f'{target_username}_followers.txt', 'a') as file:
    file.write('\n'.join(username_list) + "\n")


# ارسال پیام به هر فالوور

message = "This just message"
for follower in followers:
   username = my_bot.get_username_from_user_id(follower)
   my_bot.send_message(message , [follower])




print("Done")