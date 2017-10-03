

# from django.http import HttpResponse
from django.contrib import admin

from .models import UserProfile
from git_assignment import settings

class UserProfileAdmin(admin.ModelAdmin):

    class Meta:
    	model = UserProfile
    """data_record_created_at - time of data record creation"""
    list_display = ("login_name", "login_id", "url", "email", "created_at", "updated_at")
    list_filter = ("created_at", "email", "data_record_created_at")
    actions =  ['download_report']

    # def download_report(self, request, queryset):
    #     """
    #     Export data to excel sheet. Report can be generated for last year or one month or for user created today
    #     queryset : Selected query
    #     """
    #     wb = export_xlsx("Reimbursement Report", queryset, [
    #         (u"ID", 10),
    #         (u"UserName", 30),
    #         (u"Url", 15)

    #     ], row_map=lambda obj: [
    #         obj.pk,
    #         obj.login_name ,
    #         obj.url,
           
    #     ])
    #     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    #     response['Content-Disposition'] = 'attachment; filename=report.xlsx'
    #     wb.save(response)
    #     return response

admin.site.register(UserProfile, UserProfileAdmin)
