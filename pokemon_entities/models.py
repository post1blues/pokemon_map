from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='покемон')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='покемон (англ.)')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='покемон (япон.)')
    image = models.ImageField(null=True, verbose_name='изображение')
    description = models.TextField(blank=True, verbose_name='описание')

    previous_evolution = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='предыдущее поколение',
        related_name='next_evolutions'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='покемон',
        related_name='pokemon_entities'
    )
    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')
    appeared_at = models.DateTimeField(verbose_name='время появления')
    disappeared_at = models.DateTimeField(verbose_name='время исчезновения', blank=True, null=True)
    level = models.IntegerField(verbose_name='уровень', blank=True, null=True)
    health = models.IntegerField(verbose_name='здоровье', blank=True, null=True)
    strength = models.IntegerField(verbose_name='сила', blank=True, null=True)
    defence = models.IntegerField(verbose_name='защита', blank=True, null=True)
    stamina = models.IntegerField(verbose_name='выносливость', blank=True, null=True)

    def __str__(self):
        return f'{self.pokemon.title} - {self.level}'

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'
