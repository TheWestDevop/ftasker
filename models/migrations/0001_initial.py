# Generated by Django 2.0 on 2019-06-27 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('sid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('jbtype', models.IntegerField()),
                ('jbcat', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('budgetmin', models.BigIntegerField()),
                ('budgetmax', models.BigIntegerField()),
                ('isawarded', models.IntegerField()),
                ('location', models.CharField(max_length=500)),
                ('duration', models.IntegerField(default=1)),
                ('startdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('enddate', models.DateTimeField(blank=True, null=True)),
                ('awarddate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('jid', models.IntegerField()),
                ('uid', models.IntegerField()),
                ('awarded', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('senderid', models.IntegerField(default=0)),
                ('uid', models.IntegerField()),
                ('status', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('isread', models.IntegerField()),
                ('createdate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('firstname', models.CharField(default='', max_length=200)),
                ('lastname', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('telephone', models.CharField(max_length=200)),
                ('address', models.CharField(default='', max_length=200)),
                ('address2', models.CharField(default='', max_length=200)),
                ('city', models.IntegerField(default=0)),
                ('state', models.IntegerField(default=0)),
                ('country', models.IntegerField(default=0)),
                ('createdate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('cid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('catid', models.IntegerField()),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=200)),
                ('secret', models.CharField(max_length=200)),
                ('usertype', models.IntegerField(default=1)),
                ('isemailverified', models.IntegerField(default=0)),
                ('isphoneverified', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('createdate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]