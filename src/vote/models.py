from django.db import models
from src.votings.models import Voting

class Vote(models.Model):
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    options = models.JSONField("options")