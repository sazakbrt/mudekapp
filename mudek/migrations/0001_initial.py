# Generated by Django 4.2.1 on 2023-05-29 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MudekDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.CharField(max_length=120, verbose_name='Ders Adı')),
                ('period', models.CharField(max_length=120, verbose_name='Dönem Bilgileri')),
                ('vize', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Vize Değerlendirme Sayısı')),
                ('vize_percent', models.CharField(max_length=3, verbose_name='Vize %')),
                ('final', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Final Değerlendirme Sayısı')),
                ('final_percent', models.CharField(max_length=3, verbose_name='Final %')),
                ('homework', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Ödev Değerlendirme Sayısı')),
                ('homework_percent', models.CharField(max_length=3, verbose_name='Ödev %')),
                ('project', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Proje Değerlendirme Sayısı')),
                ('project_percent', models.CharField(max_length=3, verbose_name='Proje %')),
                ('uygulama', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Uygulama Değerlendirme Sayısı')),
                ('uygulama_percent', models.CharField(max_length=3, verbose_name='Uygulama %')),
                ('content', models.TextField(verbose_name='Değerlendirme Çıktısı Eleştirme')),
                ('publishing_date', models.DateTimeField(verbose_name='Eklenme Tarih')),
            ],
        ),
    ]
