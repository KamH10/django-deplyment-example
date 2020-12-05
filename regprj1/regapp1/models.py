from django.db import models
from django.contrib.auth.models import User
# SuperUserInformation
# Username: tyler3
# Email address: t3@gmail.com
# password: juliaN#789

# Create your models here.
class UserProfileInfo(models.Model):

    # **NOTE** (POS1) cross-ref with POS1 in 'views.py'
    # Create relationship (don't inherit from User!)
    # 1-1 relationship between UserForm and UserProfileInfo
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)

    # **NOTE** pip install pillow
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    profile_pic = models.ImageField(upload_to='regapp1/profile_pics', blank=True)

    # **NOTE** to print out the model
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
