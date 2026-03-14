# Validation

To validate data in Schematics is to have both a data model and some input
data.  The data model describes what valid data looks like in different forms.

Here’s a quick glance and some of the ways you can tweak validation.

```
>>> from schematics.models import Model
>>> from schematics.types import StringType
>>> class Person(Model):
...     name = StringType()
...     bio = StringType(required=True)
...
>>> p = Person()
>>> p.name = 'Fiona Apple'
>>> p.validate()
Traceback (most recent call last):
...
ModelValidationError: {'bio': [u'This field is required.']}

```