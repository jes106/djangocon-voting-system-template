import uuid

from loguru import logger
from datetime import datetime, timedelta
from django.db import models
from django.utils.timezone import now

from src.votings.domain.exceptions import VotingDomainError
from src.users.models import Admin

class Voting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=7, choices=[("A", "Active"), ("D", "Draft"), ("R", "Deleted"), ("C", "Closed")])
    winners = models.IntegerField()
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField(default=datetime.now()+timedelta(days=1))
    voting_creator = models.ForeignKey(Admin, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, editable=False)
    last_update = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.last_update = now()
        super().update(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.status == "A":
            return VotingDomainError("Can't delete a voting that's active yet")
        
        if datetime.now() - self.created_at < timedelta(weeks=260): #We have to preserve a voting 5 years after it was done
            self.status = "Deleted"
            super().save(*args, **kwargs)
        else:
            super().delete(*args, **kwargs)

    def unactivate_voting(voting_id):
        try:
            voting = Voting.get(id=voting_id)
            voting.delete()
        except:
            logger.error(f"Erorr during unactivating the voting {voting_id}")

class Options(models.Model):
    voting = models.ForeignKey(Voting, related_name="options", on_delete=models.CASCADE)
    option = models.CharField(max_length=100)