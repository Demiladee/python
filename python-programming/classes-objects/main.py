from user import User
from post import Post

app_user_one = User("xx@xx.com", "f-name l-name", "pwd", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("yy@yy.com", "name name", "spwd", "Developer")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()
