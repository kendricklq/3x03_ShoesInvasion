from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import date

class UserTable(models.Model):    
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    # gender = models.CharField(max_length=10)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    verify_password = models.CharField(max_length=255, null=True)
    # Email
    email = models.EmailField(max_length=255)
    # Phone
    phone = models.IntegerField()
    # True = Banned, None/Null/False = Not Banned
    # bannedStatus = models.BooleanField(default=False)
    bannedStatus = models.BooleanField()
    # True = Verified, None/Null/False = Not Verified
    # verifiedStatus = models.BooleanField(default=False)
    verifiedStatus = models.BooleanField()
    # Used to store random generated verify code, empty it when account verified
    verificationCode = models.CharField(max_length=100, null=True)
    # True = Locked, None/Null/False = Not Locked
    lockedStatus = models.BooleanField()
    lockedCounter = models.PositiveSmallIntegerField(null=True)
    # User = Normal User, Editor = Editor, Admin = Administrator
    accountType = models.CharField(max_length=10, default="User")
    # Unique Identifier
    unique_id = models.CharField(max_length=255, unique=True, null=False, default="")
    # Secret Key for 2FA
    secret_key = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username