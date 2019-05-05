# Generated by Django 2.1.5 on 2019-03-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel_handler_app', '0004_auto_20190309_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatable',
            name='all',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='asp_ruk',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='base',
            field=models.CharField(blank=True, choices=[('B', 'Budget'), ('C', 'Contract')], max_length=1),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='course_work',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='credit',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='exam',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='exam_consultation',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='gos_exam',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='lab_works',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='lectures',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='modular_control',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='other',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='practise_less',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='practise_ruk',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='rez_vkr',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='term_consultation',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='vkr_bac',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='vkr_mag',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='vkr_spec',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='zach_vkr',
            field=models.FloatField(default=0),
        ),
    ]