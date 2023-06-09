# Generated by Django 4.2.1 on 2023-05-14 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AllUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_user_first_name', models.CharField(max_length=200)),
                ('all_user_last_name', models.CharField(max_length=200)),
                ('all_user_user_name', models.CharField(max_length=200)),
                ('all_user_email_adress', models.CharField(max_length=200)),
                ('all_user_password', models.CharField(max_length=200)),
                ('normal_user_avatar', models.ImageField(upload_to='avatar')),
                ('all_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freelancer_first_name', models.CharField(max_length=200)),
                ('freelancer_last_name', models.CharField(max_length=200)),
                ('freelancer_user_name', models.CharField(max_length=200)),
                ('freelancer_email_address', models.CharField(max_length=200)),
                ('freelancer_password', models.CharField(max_length=200)),
                ('freelancer_avatar', models.ImageField(upload_to='freelancer_avatar')),
                ('freelancer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.alluser')),
            ],
        ),
    ]
