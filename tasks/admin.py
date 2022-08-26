from django.contrib import admin

# Register your models here.
from tasks.admin_models import ReportAdmin, MyReportAdmin
from tasks.models import Report


class MyReport(Report):
    class Meta:
        proxy = True


admin.site.register(MyReport, MyReportAdmin)


admin.site.register(Report, ReportAdmin)
