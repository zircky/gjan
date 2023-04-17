# Generated by Django 4.1.7 on 2023-04-15 15:23

import demo.models
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Имя')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('photo_file', models.ImageField(blank=True, max_length=254, null=True, upload_to=demo.models.get_name_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])),
                ('year', models.IntegerField(blank=True, verbose_name='Год производства')),
                ('country', models.CharField(blank=True, max_length=254, verbose_name='Страна производства')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Стоимость')),
                ('count', models.IntegerField(default=1, verbose_name='Количество')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=254, verbose_name='Имя')),
                ('surname', models.CharField(max_length=254, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=254, verbose_name='Отчество')),
                ('username', models.CharField(max_length=254, unique=True, verbose_name='Логин')),
                ('email', models.CharField(max_length=254, unique=True, verbose_name='Почта')),
                ('password', models.CharField(max_length=254, verbose_name='Пароль')),
                ('role', models.CharField(choices=[('admin', 'Администратор'), ('user', 'Пользователь')], default='user', max_length=254, verbose_name='Роль')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
