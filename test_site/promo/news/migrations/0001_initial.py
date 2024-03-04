
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Адрес')),
                ('anons', models.CharField(default='Неизвестно', max_length=100, verbose_name='Кто посещал')),
                ('full_text', models.TextField(verbose_name='Итоги акции')),
                ('date', models.DateTimeField(verbose_name='Дата посещения')),
            ],
        ),
    ]
