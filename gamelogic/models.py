from datetime import date
from django.db import models


class Game(models.Model):
    gameId = models.AutoField(primary_key=True, db_column='game_id')
    gameName = models.CharField(
        max_length=255, default="", blank=True, null=True, db_column='game_name')
    gameActive = models.CharField(
        max_length=1, default='1', blank=True, null=True, db_column='game_active')
    gameEntryId = models.IntegerField(db_column='game_entry_id', default=0)
    gameEntryDate = models.DateField(
        db_column='game_entry_date', default=date.today().isoformat(), editable=False)
    gameModifiedId = models.IntegerField(
        db_column='game_modified_id', default=0)
    gameModifiedDate = models.DateField(
        db_column='game_modified_date', blank=True, null=True, editable=True)

    class Meta:
        managed = True
        db_table = 'game'
