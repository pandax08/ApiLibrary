# Generated by Django 3.1.6 on 2021-02-10 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=30)),
                ('editorial', models.CharField(max_length=30)),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tomos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comicfile', models.FileField(null=True, upload_to='comics_files/files')),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tomos', to='Comics.comics')),
            ],
        ),
        migrations.CreateModel(
            name='Portada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portada', models.FileField(null=True, upload_to='comics_files/portadas')),
                ('comic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Comics.comics')),
            ],
        ),
        migrations.AddField(
            model_name='comics',
            name='tags',
            field=models.ManyToManyField(to='Comics.Tag'),
        ),
    ]
