# Generated by Django 3.2.9 on 2021-12-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20211219_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, max_length=3000)),
                ('route', models.TextField(blank=True, max_length=300)),
                ('map_link', models.TextField(blank=True, max_length=300)),
                ('place_Img1', models.ImageField(blank=True, null=True, upload_to='')),
                ('place_Img2', models.ImageField(blank=True, null=True, upload_to='')),
                ('place_Img3', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='hotelName',
            field=models.CharField(choices=[('Pan Pacific Sonargoan', 'Pan_Pacific_Sonargoan'), ('Radisson Blu', 'Radisson_Blu'), ('Hotel De Meridian', 'Hotel_De_Meridian'), ('Grand Plaza Hotel', 'Grand_Plaza_Hotel'), ('Empyrean Hotel', 'Empyrean_Hotel'), ('The Raintree Dhaka', 'The_Raintree_Dhaka')], default=None, max_length=100, null=True),
        ),
    ]
