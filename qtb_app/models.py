from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Employee(BaseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    team = models.ForeignKey('Teams', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tasks(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Teams(BaseModel):
    team_leader = models.ForeignKey(Employee, on_delete=models.CASCADE)
    performance_rating = models.DecimalField(max_digits=3, decimal_places=2)
    compatibility_rating = models.DecimalField(max_digits=3, decimal_places=2)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team_leader.name}'s Team"


class Reports(BaseModel):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    sender = models.ForeignKey(Employee, on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField()
    time = models.TimeField(auto_now_add=True)


class Leaderboard(BaseModel):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    rank = models.IntegerField()
    year = models.IntegerField(db_index=True)

    def __str__(self):
        return f"{self.year} - Team {self.team} - Rank {self.rank}"
    