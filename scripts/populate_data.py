import random
from django.db import connection
from faker import Faker
from django.utils import timezone
from qtb_app.models import Employee, Team, Task, Report, Leaderboard

fake = Faker()

with connection.cursor() as cursor:
    cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'qtb_app_employee';")
    cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'qtb_app_task';")
    cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'qtb_app_team';")
    cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'qtb_app_report';")
    cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'qtb_app_leaderboard';")

# Create 10 Tasks
tasks = []
for i in range(1, 11):
    task = Task.objects.create(
        id=i,  # Set the task id explicitly
        name=fake.word(),
        description=fake.text()
    )
    tasks.append(task)


teams = []
for _ in range(10):
    team = Team.objects.create(
        performance_rating=random.uniform(1, 5),
        compatibility_rating=random.uniform(1, 5)
    )
    teams.append(team)

    # Associate unique set of Tasks with each Team
    for team in teams:
        tasks_for_team = random.sample(tasks, len(tasks))
        for i, task in enumerate(tasks_for_team, start=1):
            task.team_id = team
            task.save()
            if i == 1:  # Set the first task as the team's main task
                team.task = task
                team.save()

# Create 10 Employees for each Team
employees = []
for team in teams:
    team_leader = Employee.objects.create(
        name=fake.name(),
        age=random.randint(20, 60),
        email=fake.email()
    )
    team_leader.team_id = team
    team_leader.save()
    employees.append(team_leader)

    # Add 9 members to each team
    for _ in range(9):
        member = Employee.objects.create(
            name=fake.name(),
            age=random.randint(20, 60),
            email=fake.email(),
            team_id=team
        )
        employees.append(member)

# Populate team_leader field for each team
for team in teams:
    team_leader = random.choice(team.employee_set.all())
    team.team_leader = team_leader
    team.save()

# Create 20 Reports with different times
for _ in range(20):
    team = random.choice(teams)
    sender = random.choice(employees)
    Report.objects.create(
        team=team,
        sender=sender,
        content=fake.text(),
        is_read=False,
        time=timezone.now() - timezone.timedelta(days=random.randint(1, 365))
    )

# Create Leaderboard for the top 10 Teams
leaderboard_teams = Team.objects.order_by('-performance_rating')[:10]
for i, team in enumerate(leaderboard_teams, start=1):
    Leaderboard.objects.create(
        team=team,
        rank=i,
        year=timezone.now().year
    )

print("Data populated successfully.")
