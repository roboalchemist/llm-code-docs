# Source: https://docs.djangoproject.com/en/6.0/howto/legacy-databases/

Title: How to integrate Django with a legacy database | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/howto/legacy-databases/

Markdown Content:
While Django is best suited for developing new applications, it’s quite possible to integrate it into legacy databases. Django includes a couple of utilities to automate as much of this process as possible.

This document assumes you know the Django basics, as covered in the [tutorial](https://docs.djangoproject.com/en/6.0/intro/tutorial01/).

Once you’ve got Django set up, you’ll follow this general process to integrate with an existing database.

Give Django your database parameters[¶](https://docs.djangoproject.com/en/6.0/howto/legacy-databases/#give-django-your-database-parameters "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

You’ll need to tell Django what your database connection parameters are, and what the name of the database is. Do that by editing the [`DATABASES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASES) setting and assigning values to the following keys for the `'default'` connection:

*   [`NAME`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-NAME)

*   [`ENGINE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DATABASE-ENGINE)

*   [`USER`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USER)

*   [`PASSWORD`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-PASSWORD)

*   [`HOST`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-HOST)

*   [`PORT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-PORT)

Auto-generate the models[¶](https://docs.djangoproject.com/en/6.0/howto/legacy-databases/#auto-generate-the-models "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

Django comes with a utility called [`inspectdb`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-inspectdb) that can create models by introspecting an existing database. You can view the output by running this command:

$ python manage.py inspectdb

Save this as a file by using standard Unix output redirection:

$ python manage.py inspectdb > models.py

This feature is meant as a shortcut, not as definitive model generation. See the [`documentation of inspectdb`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-inspectdb) for more information.

Once you’ve cleaned up your models, name the file `models.py` and put it in the Python package that holds your app. Then add the app to your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS) setting.

By default, [`inspectdb`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-inspectdb) creates unmanaged models. That is, `managed = False` in the model’s `Meta` class tells Django not to manage each table’s creation, modification, and deletion:

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = "CENSUS_PERSONS"

If you do want to allow Django to manage the table’s lifecycle, you’ll need to change the [`managed`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.managed "django.db.models.Options.managed") option above to `True` (or remove it because `True` is its default value).

Install the core Django tables[¶](https://docs.djangoproject.com/en/6.0/howto/legacy-databases/#install-the-core-django-tables "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------

Next, run the [`migrate`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-migrate) command to install any extra needed database records such as admin permissions and content types:

$ python manage.py migrate

Test and tweak[¶](https://docs.djangoproject.com/en/6.0/howto/legacy-databases/#test-and-tweak "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

Those are the basic steps – from here you’ll want to tweak the models Django generated until they work the way you’d like. Try accessing your data via the Django database API, and try editing objects via Django’s admin site, and edit the models file accordingly.
