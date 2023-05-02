# Get instance
import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException

bot = instaloader.Instaloader()

# Login or load session
username = "username"
password = r'password'
try:
    bot.login(username, password)
except TwoFactorAuthRequiredException:
    bot.two_factor_login(int(input("Please 2FA Code:")))

# Obtain profile metadata
profile = instaloader.Profile.from_username(bot.context, username)

# Print list of followers
followers_list = []
followees_list = []
count = 0
for followers in profile.get_followers():
    followers_list.append(followers.username)
    file = open("profile_followers.txt", "a+")
    file.write(followers_list[count])
    file.write("\n")
    file.close()
    print(followers_list[count])
    count = count + 1

# Print list of followees
for followees in profile.get_followees():
    followees_list.append(followees.username)
    file = open("profile_followees.txt", "a+")
    file.write(followees_list[count])
    file.write("\n")
    file.close()
    print(followees_list[count])
    count = count + 1