import os

from django.db import models
from django.dispatch import receiver
from django.contrib.auth import get_user_model


UserModel = get_user_model()


def get_sentinel_user():
	return get_user_model().objects.get_or_create(username='deleted')[0]


def user_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	return 'user_{0}/{1}'.format(instance.owner.id, filename)


# Create your models here.
class FileUploadModel(models.Model):
	owner = models.ForeignKey(UserModel, on_delete=models.SET(get_sentinel_user))
	datafile = models.FileField(upload_to=user_directory_path)


@receiver(models.signals.post_delete, sender=FileUploadModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
	if instance.datafile:
		if os.path.isfile(instance.datafile.path):
			os.remove(instance.datafile.path)


class Group(models.Model):
	group_name = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return str(self.group_name)


class Subject(models.Model):
	subject_name = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return str(self.subject_name)


class LearningBase(models.Model):
	budget = ('B', 'Budget')
	contract = ('C', 'Contract')
	__all = dict([budget, contract])

	type = models.CharField(max_length=1, choices=__all.items())

	def __str__(self):
		return str(self.__all[self.type])


class DataTable(models.Model):
	LEARNING_BASE_CHOICES = (
		('B', 'Budget'),
		('C', 'Contract'),
	)

	added_by = models.ForeignKey(UserModel, on_delete=models.SET(get_sentinel_user))
	term = models.IntegerField()
	date = models.DateField(blank=True, null=True)
	course = models.IntegerField(blank=True, null=True)
	group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
	base = models.CharField(max_length=1, choices=LEARNING_BASE_CHOICES, blank=True)
	# base = models.ForeignKey(LearningBase, on_delete=models.CASCADE, blank=True, null=True)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	lectures = models.FloatField(default=0)
	practise_less = models.FloatField(default=0)
	lab_works = models.FloatField(default=0)
	modular_control = models.FloatField(default=0)
	term_consultation = models.FloatField(default=0)
	exam_consultation = models.FloatField(default=0)
	credit = models.FloatField(default=0)
	exam = models.FloatField(default=0)
	course_work = models.FloatField(default=0)
	vkr_bac = models.FloatField(default=0)
	vkr_spec = models.FloatField(default=0)
	vkr_mag = models.FloatField(default=0)
	practise_ruk = models.FloatField(default=0)
	gos_exam = models.FloatField(default=0)
	rez_vkr = models.FloatField(default=0)
	zach_vkr = models.FloatField(default=0)
	asp_ruk = models.FloatField(default=0)
	other = models.FloatField(default=0)
	all = models.FloatField()
