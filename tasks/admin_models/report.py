from django.contrib import admin

from tasks.models.report_in_task import ReportInTask


class ReportInTaskInline(admin.TabularInline):
    model = ReportInTask
    extra = 1
    fk_name = "report"


class ReportAdmin(admin.ModelAdmin):
    list_display = ('date', 'user')

class MyReportAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    list_display = ('date', 'user')
    # fieldsets = [
    #     (None,               {'fields': ['ReportInTask']}),
    #     #('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [ReportInTaskInline]

    def get_queryset(self, request):
        return super(MyReportAdmin, self).get_queryset(request).filter(user_id=request.user.id)
