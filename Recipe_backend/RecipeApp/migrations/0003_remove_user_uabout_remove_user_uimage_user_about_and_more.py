# Generated by Django 4.1.6 on 2023-03-31 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeApp', '0002_user_upassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uAbout',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uImage',
        ),
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='uPassword',
            field=models.CharField(max_length=50),
        ),
    ]