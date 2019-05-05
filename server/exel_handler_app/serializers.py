from .models import Group, Subject, LearningBase, DataTable

from rest_framework import serializers



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_name',)
        extra_kwargs = {
            'group_name': {'validators': []},
        }


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject_name',)
        extra_kwargs = {
            'subject_name': {'validators': []},
        }


class LearningBaseSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=[('B', 'Budget'),('C', 'Contract')], allow_blank=True)

    class Meta:
        model = LearningBase
        fields = '__all__'


# TODO: Choice field with normal display
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTable
        # fields = '__all__'
        exclude = ['added_by']

    # added_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    group = GroupSerializer()
    subject = SubjectSerializer()

    def create(self, validated_data):
        # TODO: can't sent null date
        group_data = validated_data.pop('group')['group_name']
        subject_data = validated_data.pop('subject')['subject_name']
        usr = self.context['request'].user
        grp, _ = Group.objects.get_or_create(group_name=group_data)
        subject, _ = Subject.objects.get_or_create(subject_name=subject_data)
        data = DataTable.objects.create(added_by=usr, group=grp, subject=subject, **validated_data)
        return data

    def update(self, instance, validated_data):
        group_data_dict = validated_data.pop('group')
        group_data = group_data_dict.get('group_name', instance.group.group_name)
        subject_data_dict = validated_data.pop('subject')
        subject_data = subject_data_dict.get('subject_name', instance.subject.subject_name)
        group, _ = Group.objects.get_or_create(group_name=group_data)
        subject, _ = Subject.objects.get_or_create(subject_name=subject_data)
        instance.term = validated_data.get('term', instance.term)
        instance.date = validated_data.get('date', instance.date)
        instance.course = validated_data.get('course', instance.course)
        instance.group = group
        instance.base = validated_data.get('base', instance.base)
        instance.subject = subject
        instance.lectures = validated_data.get('lectures', instance.lectures)
        instance.practise_less = validated_data.get('practise_less', instance.practise_less)
        instance.lab_works = validated_data.get('lab_works', instance.lab_works)
        instance.modular_control = validated_data.get('modular_control', instance.modular_control)
        instance.term_consultation = validated_data.get('term_consultation', instance.term_consultation)
        instance.exam_consultation = validated_data.get('exam_consultation', instance.exam_consultation)
        instance.credit = validated_data.get('credit', instance.credit)
        instance.exam = validated_data.get('exam', instance.exam)
        instance.course_work = validated_data.get('course_work', instance.course_work)
        instance.vkr_bac = validated_data.get('vkr_bac', instance.vkr_bac)
        instance.vkr_spec = validated_data.get('vkr_spec', instance.vkr_spec)
        instance.vkr_mag = validated_data.get('vkr_mag', instance.vkr_mag)
        instance.practise_ruk = validated_data.get('practise_ruk', instance.practise_ruk)
        instance.gos_exam = validated_data.get('gos_exam', instance.gos_exam)
        instance.rez_vkr = validated_data.get('rez_vkr', instance.rez_vkr)
        instance.zach_vkr = validated_data.get('zach_vkr', instance.zach_vkr)
        instance.asp_ruk = validated_data.get('asp_ruk', instance.asp_ruk)
        instance.other = validated_data.get('other', instance.other)
        instance.all = validated_data.get('all', instance.all)
        instance.save()
        return instance
