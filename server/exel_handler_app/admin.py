from django.contrib import admin

from .models import FileUploadModel, Group, Subject, LearningBase, DataTable
# Register your models here.


class FileAdmin(admin.ModelAdmin):
	pass


class GroupAdmin(admin.ModelAdmin):
	pass


class SubjectAdmin(admin.ModelAdmin):
	pass


class LearningBaseAdmin(admin.ModelAdmin):
	pass


class DataTableAdmin(admin.ModelAdmin):
	pass


admin.site.register(FileUploadModel, FileAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(LearningBase, LearningBaseAdmin)
admin.site.register(DataTable, DataTableAdmin)
