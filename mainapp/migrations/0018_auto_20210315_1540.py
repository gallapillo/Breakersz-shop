# Generated by Django 3.1.7 on 2021-03-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_delete_console'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='device',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Устройство'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='related_order', to='mainapp.Order', verbose_name='Заказы покупателя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('payed', 'Заказ оплачен'), ('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('is_ready', 'Заказ готов'), ('completed', 'Заказ выполнен')], default='new', max_length=100, verbose_name='Статус заказ'),
        ),
    ]
