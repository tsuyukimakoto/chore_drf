# Generated by Django 2.1.5 on 2019-03-30 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_add_comment_model'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('todo', 'title')},
        ),
    ]
