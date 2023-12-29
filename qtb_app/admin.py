from django.contrib import admin
from django import forms
from .models import Employee, Team, Task, Report, Leaderboard


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'team_id')
    search_fields = ('name',)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'team_leader', 'task', 'performance_rating')
    search_fields =('id', 'team_leader', 'task',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


class ReportsAdminForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'team' in self.initial:
            team_id = self.initial['team']
            self.fields['sender'].queryset = Employee.objects.filter(team_id=team_id)
        else:
            self.fields['sender'].queryset = Employee.objects.all()


class ReportAdmin(admin.ModelAdmin):
    form = ReportsAdminForm
    list_display = ('team', 'sender', 'content', 'created_at')
    search_fields =('team', 'sender', 'content',)


class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('team', 'rank', 'year')
    search_fields = ('year', 'team')


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Leaderboard, LeaderboardAdmin)
