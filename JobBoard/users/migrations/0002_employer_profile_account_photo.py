# Generated by Django 4.1.2 on 2023-04-14 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.profile')),
                ('company_name', models.CharField(blank=True, max_length=75, null=True)),
            ],
            bases=('users.profile',),
        ),
        migrations.AddField(
            model_name='profile',
            name='account_photo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]