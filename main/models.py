from django.db import models

# Create your models here.


class Location(models.Model):
    """
        Места нахождения
    """

    name = models.CharField(verbose_name="Название", max_length=200)

    class Meta:
        verbose_name = "Место нахождения"
        verbose_name_plural = "Места нахождения"

    def __str__(self):
        return name


class TaraType(models.Model):
    """
        Тип упаковки
    """

    name = models.CharField(verbose_name="Название", max_length=200)

    class Meta:
        verbose_name = "Тип упаковки"
        verbose_name_plural = "Типы упаковки"

    def __str__(self):
        return name


class CollectPoint(models.Model):
    """
        Точка сбора продукции
    """

    name = models.CharField(verbose_name="Название", max_length=200)

    class Meta:
        verbose_name = "Точка сбора продукции"
        verbose_name_plural = "Точки сбора продукции"

    def __str__(self):
        return name


class NanoPowder(models.Model):
    """
        Выпуски нанопорошка с характеристиками
    """
    location = models.ForeignKey(Location, verbose_name="Местоположение",
        on_delete=models.CASCADE)
    tara_type = models.ForeignKey(TaraType, verbose_name="Тип тары",
        on_delete=models.CASCADE)
    tara_number = models.IntegerField(default=0, verbose_name="Номер тары")
    brutto_mass = models.FloatField(verbose_name="Масса брутто")
    material = models.CharField(verbose_name="Материал", max_length=200)
    prod_date = models.DateField(verbose_name="дата получения", null=True)
    prod_number = models.IntegerField(verbose_name="номер пуска", null=True)
    collect_point = models.ForeignKey(CollectPoint,verbose_name="точка сбора",
        on_delete=models.CASCADE)
    pack_date = models.DateField(verbose_name="дата фасовки", null=True)
    poverhn = models.FloatField(verbose_name="уд.поверхность", null=True)
    plotnost = models.FloatField(verbose_name="нас.плотность", null=True)
    label_text = models.TextField(verbose_name="Надпись на этикетке")
    comment = models.TextField(verbose_name="Служебное примечание", null=True, blank=True)
    mass_check_date = models.DateField(verbose_name="Дата проверки массы", null=True)
    plotnost_check_date = models.DateField(verbose_name="Дата пров. уд.плотн", null=True)
    netto_mass = models.FloatField(verbose_name="Масса нетто", null=True)

    class Meta:
        verbose_name = "Выпуск нанопорошка"
        verbose_name_plural = "Выпуски нанопорошка"

    def __str__(self):
        return label_text


