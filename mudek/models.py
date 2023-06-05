from django.db import models

class MudekDocument(models.Model):
    lesson = models.CharField(max_length=120, verbose_name="Ders Adı")
    teacher = models.CharField(max_length=120, verbose_name="Öğretmen")
    period = models.CharField(max_length=120, verbose_name="Dönem Bilgileri")
    vize = models.DecimalField("Vize Değerlendirme Sayısı",
                                max_digits=2,
                                decimal_places=0)
    vize_percent = models.CharField(max_length=3, verbose_name="Vize %")
    final = models.DecimalField("Final Değerlendirme Sayısı",
                                max_digits=2,
                                decimal_places=0)
    final_percent = models.CharField(max_length=3, verbose_name="Final %")
    homework = models.DecimalField("Ödev Değerlendirme Sayısı",
                                max_digits=2,
                                decimal_places=0)
    homework_percent = models.CharField(max_length=3, verbose_name="Ödev %")
    project = models.DecimalField("Proje Değerlendirme Sayısı",
                                max_digits=2,
                                decimal_places=0)
    project_percent = models.CharField(max_length=3, verbose_name="Proje %")
    uygulama = models.DecimalField("Uygulama Değerlendirme Sayısı",
                                max_digits=2,
                                decimal_places=0)
    uygulama_percent = models.CharField(max_length=3, verbose_name="Uygulama %")
    content = models.TextField(verbose_name="Değerlendirme Çıktısı Eleştirme")
    publishing_date = models.DateTimeField(verbose_name="Eklenme Tarih")

    def __str__(self):
        return self.lesson
    