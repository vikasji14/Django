# Generated by Django 5.1.2 on 2024-10-26 12:03

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0002_chaivarity_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_until', models.DateTimeField()),
                ('chai', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='chai.chaivarity')),
            ],
        ),
        migrations.CreateModel(
            name='ChaiReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratting', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('chai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='chai.chaivarity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('chai_varities', models.ManyToManyField(related_name='stores', to='chai.chaivarity')),
            ],
        ),
    ]
