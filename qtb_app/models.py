from django.db import models
from phone_field import PhoneField


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        abstract = True


class Employee(BaseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone_num = PhoneField(blank=True)
    team_id = models.ForeignKey('Team', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - Team {self.team_id.id}'


class Task(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Team(BaseModel):
    team_leader = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    performance_rating = models.DecimalField(max_digits=5, decimal_places=2)
    compatibility_rating = models.DecimalField(max_digits=5, decimal_places=2)
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'


class Report(BaseModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    sender = models.ForeignKey(Employee, on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField()
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'Report {self.id} - Team: {self.team.id}'


class Leaderboard(BaseModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rank = models.IntegerField()
    year = models.IntegerField(db_index=True)

    def __str__(self):
        return f"{self.year} - Team {self.team} - Rank {self.rank}"
    