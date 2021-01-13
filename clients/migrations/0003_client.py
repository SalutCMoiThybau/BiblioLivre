# Generated by Django 3.1.4 on 2021-01-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0002_delete_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('adresse_mail', models.EmailField(max_length=100, null=True)),
                ('nombre_livres_possédés', models.IntegerField(null=True)),
            ],
        ),
    ]