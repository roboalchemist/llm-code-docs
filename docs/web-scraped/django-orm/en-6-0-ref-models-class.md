# Source: https://docs.djangoproject.com/en/6.0/ref/models/class/

Title: Model class reference | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/models/class/

Markdown Content:
This document covers features of the [`Model`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model "django.db.models.Model") class. For more information about models, see [the complete list of Model reference guides](https://docs.djangoproject.com/en/6.0/ref/models/).

Attributes[¶](https://docs.djangoproject.com/en/6.0/ref/models/class/#attributes "Link to this heading")
--------------------------------------------------------------------------------------------------------

### `DoesNotExist`[¶](https://docs.djangoproject.com/en/6.0/ref/models/class/#doesnotexist "Link to this heading")

_exception_ Model.DoesNotExist[¶](https://docs.djangoproject.com/en/6.0/ref/models/class/#django.db.models.Model.DoesNotExist "Link to this definition")
This exception is raised by the ORM when an expected object is not found. For example, [`QuerySet.get()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") will raise it when no object is found for the given lookups.

Django provides a `DoesNotExist` exception as an attribute of each model class to identify the class of object that could not be found, allowing you to catch exceptions for a particular model class. The exception is a subclass of [`django.core.exceptions.ObjectDoesNotExist`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.ObjectDoesNotExist "django.core.exceptions.ObjectDoesNotExist").

### `MultipleObjectsReturned`[¶](https://docs.djangoproject.com/en/6.0/ref/models/class/#multipleobjectsreturned "Link to this heading")

_exception_ Model.MultipleObjectsReturned[¶](https://docs.djangoproject.com/en/6.0/ref/models/class/#django.db.models.Model.MultipleObjectsReturned "Link to this definition")
This exception is raised by [`QuerySet.get()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") when multiple objects are found for the given lookups.

Django provides a `MultipleObjectsReturned` exception as an attribute of each model class to identify the class of object for which multiple objects were found, allowing you to catch exceptions for a particular model class. The exception is a subclass of [`django.core.exceptions.MultipleObjectsReturned`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.MultipleObjectsReturned "django.core.exceptions.MultipleObjectsReturned").

### `NotUpdated`[¶](https://docs.djangoproject.com/en/6.0/ref/models/class/#notupdated "Link to this heading")

New in Django 6.0.

_exception_ Model.NotUpdated[¶](https://docs.djangoproject.com/en/6.0/ref/models/class/#django.db.models.Model.NotUpdated "Link to this definition")
This exception is raised when [a forced update](https://docs.djangoproject.com/en/6.0/ref/models/instances/#ref-models-force-insert) of a [`Model`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model "django.db.models.Model") instance does not affect any rows.

Django provides a `NotUpdated` exception as an attribute of each model class to identify the class of object that could not be updated, allowing you to catch exceptions for a particular model class. The exception is a subclass of [`django.core.exceptions.ObjectNotUpdated`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.core.exceptions.ObjectNotUpdated "django.core.exceptions.ObjectNotUpdated") and inherits from [`django.db.DatabaseError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.DatabaseError "django.db.DatabaseError") for backward compatibility reasons.

### `objects`[¶](https://docs.djangoproject.com/en/6.0/ref/models/class/#objects "Link to this heading")

Model.objects[¶](https://docs.djangoproject.com/en/6.0/ref/models/class/#django.db.models.Model.objects "Link to this definition")
Each non-abstract [`Model`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model "django.db.models.Model") class must have a [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") instance added to it. Django ensures that in your model class you have at least a default `Manager` specified. If you don’t add your own `Manager`, Django will add an attribute `objects` containing default [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") instance. If you add your own [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") instance attribute, the default one does not appear. Consider the following example:

from django.db import models

class Person(models.Model):
    # Add manager with another name
    people = models.Manager()

For more details on model managers see [Managers](https://docs.djangoproject.com/en/6.0/topics/db/managers/) and [Retrieving objects](https://docs.djangoproject.com/en/6.0/topics/db/queries/#retrieving-objects).
