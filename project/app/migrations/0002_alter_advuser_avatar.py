
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='avatar',
            field=models.ImageField(upload_to='media'),
        ),
    ]
