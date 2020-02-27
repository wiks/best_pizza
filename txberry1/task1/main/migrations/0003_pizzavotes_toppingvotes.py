# Generated by Django 3.0.3 on 2020-02-22 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_pizza_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaVotes',
            fields=[
                ('pizza', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Pizza')),
                ('votes', models.IntegerField(default=0)),
                ('dt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ToppingVotes',
            fields=[
                ('topping', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Topping')),
                ('votes', models.IntegerField(default=0)),
                ('dt', models.DateTimeField()),
            ],
        ),
    ]