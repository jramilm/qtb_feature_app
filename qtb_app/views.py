from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
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


def team_list(request):
    teams = Team.objects.all()

    search_query = request.GET.get('search', '')

    if 'refresh' in request.GET:
        search_query = ''

    team_data = []
    for team in teams:

        team_leader_match = team.team_leader.name.lower().find(search_query.lower()) != -1
        team_id_match = str(team.id).find(search_query) != -1

        member_name_match = Employee.objects.filter(
            team_id=team.id,
            name__icontains=search_query
        ).exists()

        if search_query and not (team_leader_match or team_id_match or member_name_match):
            continue

        team_data.append({
            'team': team,
            'team_leader': team.team_leader,
            'members': Employee.objects.filter(team_id=team.id),
        })

    context = {
        'teams': team_data,
    }
    return render(request, 'pages/team_page.html', context)


def get_report_details(request):
    report_id = request.GET.get('report_id')
    report = get_object_or_404(Report, pk=report_id)

    sender_name = report.sender.name if report.sender else 'Unknown'
    sender_email = report.sender.email if report.sender else 'Unknown'

    data = {
        'sender': sender_name,
        'sender_email': sender_email,
        'date': report.created_at.strftime('%Y-%m-%d %H:%M'),
        'content': report.content,
    }

    return JsonResponse(data)
