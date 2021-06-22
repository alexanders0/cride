# Generated by Django 3.1.7 on 2021-06-22 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on wich the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on wich the object was last modified.', verbose_name='modified at')),
                ('comments', models.TextField(blank=True)),
                ('rating', models.IntegerField(default=1)),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circles.circle')),
                ('rated_user', models.ForeignKey(help_text='User that receives the rating.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rated_user', to=settings.AUTH_USER_MODEL)),
                ('rating_user', models.ForeignKey(help_text='User that emits the rating', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rating_user', to=settings.AUTH_USER_MODEL)),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_ride', to='rides.ride')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
