from django.db import models
from datetime import date


class User(models.Model):
    userId = models.AutoField(primary_key=True, db_column='user_id')
    userName = models.CharField(unique=True,
                                max_length=255, default="", blank=True, null=True, db_column='user_name')
    userUpass = models.CharField(
        max_length=64, default="", blank=True, null=True, db_column='user_upass')
    userAddress = models.CharField(
        max_length=100, default="", blank=True, null=True, db_column='user_address')
    userMobile = models.CharField(
        max_length=18, default="", unique=True, blank=True, null=True, db_column='user_mobile')
    userEmail = models.EmailField(
        max_length=100, default="", unique=True, blank=True, null=True, db_column='user_email')
    userRoleId = models.IntegerField(
        default=0, blank=True, null=True, db_column='user_role_id')
    userActive = models.CharField(
        max_length=1, default='1', blank=True, null=True, db_column='user_active')
    userEntryId = models.IntegerField(
        blank=True, default=0, null=True, db_column='user_entry_id')
    userEntryDate = models.DateField(default=date.today().isoformat(),
                                     blank=True, null=True, db_column='user_entry_date', editable=False)
    userModifiedId = models.IntegerField(
        blank=True, default=0, null=True, db_column='user_modified_id')
    userModifiedDate = models.DateField(
        blank=True, null=True, db_column='user_modified_date', editable=True)

    class Meta:
        managed = True
        db_table = 'user'
