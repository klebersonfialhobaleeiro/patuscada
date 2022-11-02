# Generated by Django 3.2.10 on 2022-11-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_onde_ficar_delete_contato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apoio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('falarCom', models.CharField(blank=True, max_length=50, null=True)),
                ('logomarca', models.ImageField(upload_to='')),
                ('grupo', models.CharField(choices=[('STD', 'Standart'), ('MTR', 'Master'), ('PRM', 'Premium'), ('PLT', 'Platinum')], max_length=3)),
            ],
        ),
        migrations.RenameModel(
            old_name='onde_ficar',
            new_name='OndeFicar',
        ),
    ]