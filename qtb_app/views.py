from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Employee, Task, Team, Report, Leaderboard


def view_items(request):
    employees = Employee.objects.all()
    teams = Team.objects.all()
    tasks = Task.objects.all()
    reports = Report.objects.all()
    leaderboards = Leaderboard.objects.all().order_by('rank')

    context = {
        'employees': employees,
        'tasks': tasks,
        'reports': reports,
        'teams': teams,
        'leaderboards': leaderboards
    }
    return render(request, 'dashboard.html', context)