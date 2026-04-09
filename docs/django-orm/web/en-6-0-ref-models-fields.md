# Source: https://docs.djangoproject.com/en/6.0/ref/models/fields/

Title: Model field reference | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/models/fields/

Markdown Content:
Model field reference | Django documentation | Django
===============
[Skip to main content](https://docs.djangoproject.com/en/6.0/ref/models/fields/#main-content)

[Django](https://www.djangoproject.com/)
The web framework for perfectionists with deadlines.

Menu Main navigation
*   [Overview](https://www.djangoproject.com/start/overview/)
*   [Download](https://www.djangoproject.com/download/)
*   [Documentation](https://docs.djangoproject.com/)
*   [News](https://www.djangoproject.com/weblog/)
*   [Code](https://github.com/django/django)
*   [Issues](https://code.djangoproject.com/)
*   [Community](https://www.djangoproject.com/community/)
*   [Foundation](https://www.djangoproject.com/foundation/)
*   [♥ Donate](https://www.djangoproject.com/fundraising/)

Search Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

[Documentation](https://docs.djangoproject.com/en/6.0/)

*   [Getting Help](https://docs.djangoproject.com/en/6.0/faq/help/)

*   Language: **en**
*   [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/models/fields/)
*   [sv](https://docs.djangoproject.com/sv/6.0/ref/models/fields/)
*   [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/models/fields/)
*   [pl](https://docs.djangoproject.com/pl/6.0/ref/models/fields/)
*   [ko](https://docs.djangoproject.com/ko/6.0/ref/models/fields/)
*   [ja](https://docs.djangoproject.com/ja/6.0/ref/models/fields/)
*   [it](https://docs.djangoproject.com/it/6.0/ref/models/fields/)
*   [id](https://docs.djangoproject.com/id/6.0/ref/models/fields/)
*   [fr](https://docs.djangoproject.com/fr/6.0/ref/models/fields/)
*   [es](https://docs.djangoproject.com/es/6.0/ref/models/fields/)
*   [el](https://docs.djangoproject.com/el/6.0/ref/models/fields/)

*   Documentation version: **6.0**
*   [dev](https://docs.djangoproject.com/en/dev/ref/models/fields/)
*   [5.2](https://docs.djangoproject.com/en/5.2/ref/models/fields/)
*   [5.1](https://docs.djangoproject.com/en/5.1/ref/models/fields/)
*   [5.0](https://docs.djangoproject.com/en/5.0/ref/models/fields/)
*   [4.2](https://docs.djangoproject.com/en/4.2/ref/models/fields/)
*   [4.1](https://docs.djangoproject.com/en/4.1/ref/models/fields/)
*   [4.0](https://docs.djangoproject.com/en/4.0/ref/models/fields/)
*   [3.2](https://docs.djangoproject.com/en/3.2/ref/models/fields/)
*   [3.1](https://docs.djangoproject.com/en/3.1/ref/models/fields/)
*   [3.0](https://docs.djangoproject.com/en/3.0/ref/models/fields/)
*   [2.2](https://docs.djangoproject.com/en/2.2/ref/models/fields/)
*   [2.1](https://docs.djangoproject.com/en/2.1/ref/models/fields/)
*   [2.0](https://docs.djangoproject.com/en/2.0/ref/models/fields/)
*   [1.11](https://docs.djangoproject.com/en/1.11/ref/models/fields/)
*   [1.10](https://docs.djangoproject.com/en/1.10/ref/models/fields/)
*   [1.8](https://docs.djangoproject.com/en/1.8/ref/models/fields/)

*   [](https://docs.djangoproject.com/en/6.0/ref/models/fields/#top)

Model field reference[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#module-django.db.models.fields "Link to this heading")
========================================================================================================================================

This document contains all the API references of [`Field`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field "django.db.models.Field") including the [field options](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-options) and [field types](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-types) Django offers.

See also

If the built-in fields don’t do the trick, you can try [django-localflavor](https://pypi.org/project/django-localflavor/) ([documentation](https://django-localflavor.readthedocs.io/)), which contains assorted pieces of code that are useful for particular countries and cultures.

Also, you can easily [write your own custom model fields](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/).

Note

Fields are defined in [`django.db.models.fields`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#module-django.db.models.fields "django.db.models.fields: Built-in field types."), but for convenience they’re imported into [`django.db.models`](https://docs.djangoproject.com/en/6.0/topics/db/models/#module-django.db.models "django.db.models"). The standard convention is to use `from django.db import models` and refer to fields as `models.<Foo>Field`.

Field options[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-options "Link to this heading")
---------------------------------------------------------------------------------------------------------------

The following arguments are available to all field types. All are optional.

### `null`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#null "Link to this heading")

Field.null[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.null "Link to this definition")
If `True`, Django will store empty values as `NULL` in the database. Default is `False`.

Avoid using [`null`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null") on string-based fields such as [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField") and [`TextField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.TextField "django.db.models.TextField"). The Django convention is to use an empty string, not `NULL`, as the “no data” state for string-based fields. If a string-based field has `null=False`, empty strings can still be saved for “no data”. If a string-based field has `null=True`, that means it has two possible values for “no data”: `NULL`, and the empty string. In most cases, it’s redundant to have two possible values for “no data”. One exception is when a [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField") has both `unique=True` and `blank=True` set. In this situation, `null=True` is required to avoid unique constraint violations when saving multiple objects with blank values.

For both string-based and non-string-based fields, you will also need to set `blank=True` if you wish to permit empty values in forms, as the [`null`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null") parameter only affects database storage (see [`blank`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.blank "django.db.models.Field.blank")).

Note

When using the Oracle database backend, the value `NULL` will be stored to denote the empty string regardless of this attribute.

### `blank`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#blank "Link to this heading")

Field.blank[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.blank "Link to this definition")
If `True`, the field is allowed to be blank. Default is `False`.

Note that this is different than [`null`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null"). [`null`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null") is purely database-related, whereas [`blank`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.blank "django.db.models.Field.blank") is validation-related. If a field has `blank=True`, form validation will allow entry of an empty value. If a field has `blank=False`, the field will be required.

Supplying missing values

`blank=True` can be used with fields having `null=False`, but this will require implementing [`clean()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.clean "django.db.models.Model.clean") on the model in order to programmatically supply any missing values.

### `choices`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#choices "Link to this heading")

Field.choices[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L553)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.choices "Link to this definition")
A mapping or iterable in the format described below to use as choices for this field. If choices are given, they’re enforced by [model validation](https://docs.djangoproject.com/en/6.0/ref/models/instances/#validating-objects) and the default form widget will be a select box with these choices instead of the standard text field.

If a mapping is given, the key element is the actual value to be set on the model, and the second element is the human readable name. For example:

YEAR_IN_SCHOOL_CHOICES = {
    "FR": "Freshman",
    "SO": "Sophomore",
    "JR": "Junior",
    "SR": "Senior",
    "GR": "Graduate",
}

You can also pass a [sequence](https://docs.python.org/3/glossary.html#term-sequence "(in Python v3.14)") consisting itself of iterables of exactly two items (e.g. `[(A1, B1), (A2, B2), …]`). The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name. For example:

YEAR_IN_SCHOOL_CHOICES = [
    ("FR", "Freshman"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    ("GR", "Graduate"),
]

`choices` can also be defined as a callable that expects no arguments and returns any of the formats described above. For example:

def get_currencies():
    return {i: i for i in settings.CURRENCIES}

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=get_currencies)

Passing a callable for `choices` can be particularly handy when, for example, the choices are:

*   the result of I/O-bound operations (which could potentially be cached), such as querying a table in the same or an external database, or accessing the choices from a static file.

*   a list that is mostly stable but could vary from time to time or from project to project. Examples in this category are using third-party apps that provide a well-known inventory of values, such as currencies, countries, languages, time zones, etc.

Generally, it’s best to define choices inside a model class, and to define a suitably-named constant for each value:

from django.db import models

class Student(models.Model):
    FRESHMAN = "FR"
    SOPHOMORE = "SO"
    JUNIOR = "JR"
    SENIOR = "SR"
    GRADUATE = "GR"
    YEAR_IN_SCHOOL_CHOICES = {
        FRESHMAN: "Freshman",
        SOPHOMORE: "Sophomore",
        JUNIOR: "Junior",
        SENIOR: "Senior",
        GRADUATE: "Graduate",
    }
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}

Though you can define a choices list outside of a model class and then refer to it, defining the choices and names for each choice inside the model class keeps all of that information with the class that uses it, and helps reference the choices (e.g, `Student.SOPHOMORE` will work anywhere that the `Student` model has been imported).

You can also collect your available choices into named groups that can be used for organizational purposes:

MEDIA_CHOICES = {
    "Audio": {
        "vinyl": "Vinyl",
        "cd": "CD",
    },
    "Video": {
        "vhs": "VHS Tape",
        "dvd": "DVD",
    },
    "unknown": "Unknown",
}

The key of the mapping is the name to apply to the group and the value is the choices inside that group, consisting of the field value and a human-readable name for an option. Grouped options may be combined with ungrouped options within a single mapping (such as the `"unknown"` option in this example).

You can also use a sequence, e.g. a list of 2-tuples:

MEDIA_CHOICES = [
    (
        "Audio",
        (
            ("vinyl", "Vinyl"),
            ("cd", "CD"),
        ),
    ),
    (
        "Video",
        (
            ("vhs", "VHS Tape"),
            ("dvd", "DVD"),
        ),
    ),
    ("unknown", "Unknown"),
]

Note that choices can be any sequence object – not necessarily a list or tuple. This lets you construct choices dynamically. But if you find yourself hacking [`choices`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.choices "django.db.models.Field.choices") to be dynamic, you’re probably better off using a proper database table with a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"). [`choices`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.choices "django.db.models.Field.choices") is meant for static data that doesn’t change much, if ever.

Note

A new migration is created each time the order of `choices` changes.

For each model field that has [`choices`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.choices "django.db.models.Field.choices") set, Django will normalize the choices to a list of 2-tuples and add a method to retrieve the human-readable name for the field’s current value. See [`get_FOO_display()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.get_FOO_display "django.db.models.Model.get_FOO_display") in the database API documentation.

Unless [`blank=False`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.blank "django.db.models.Field.blank") is set on the field along with a [`default`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.default "django.db.models.Field.default") then a label containing `"---------"` will be rendered with the select box. To override this behavior, add a tuple to `choices` containing `None`; e.g. `(None, 'Your String For Display')`. Alternatively, you can use an empty string instead of `None` where this makes sense - such as on a [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField").

#### Enumeration types[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#enumeration-types "Link to this heading")

In addition, Django provides enumeration types that you can subclass to define choices in a concise way:

from django.utils.translation import gettext_lazy as _

class Student(models.Model):
    class YearInSchool(models.TextChoices):
        FRESHMAN = "FR", _("Freshman")
        SOPHOMORE = "SO", _("Sophomore")
        JUNIOR = "JR", _("Junior")
        SENIOR = "SR", _("Senior")
        GRADUATE = "GR", _("Graduate")

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool,
        default=YearInSchool.FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR,
        }

These work similar to [`enum`](https://docs.python.org/3/library/enum.html#module-enum "(in Python v3.14)") from Python’s standard library, but with some modifications:

*   Enum member values are a tuple of arguments to use when constructing the concrete data type. Django supports adding an extra string value to the end of this tuple to be used as the human-readable name, or `label`. The `label` can be a lazy translatable string. Thus, in most cases, the member value will be a `(value, label)` 2-tuple. See below for [an example of subclassing choices](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-choices-enum-subclassing) using a more complex data type. If a tuple is not provided, or the last item is not a (lazy) string, the `label` is [automatically generated](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-choices-enum-auto-label) from the member name.

*   A `.label` property is added on values, to return the human-readable name.

*   A number of custom properties are added to the enumeration classes – `.choices`, `.labels`, `.values`, and `.names` – to make it easier to access lists of those separate parts of the enumeration.

Warning

These property names cannot be used as member names as they would conflict. 
*   The use of [`enum.unique()`](https://docs.python.org/3/library/enum.html#enum.unique "(in Python v3.14)") is enforced to ensure that values cannot be defined multiple times. This is unlikely to be expected in choices for a field.

Note that using `YearInSchool.SENIOR`, `YearInSchool['SENIOR']`, or `YearInSchool('SR')` to access or lookup enum members work as expected, as do the `.name` and `.value` properties on the members.

If you don’t need to have the human-readable names translated, you can have them inferred from the member name (replacing underscores with spaces and using title-case):

>>> class Vehicle(models.TextChoices):
...     CAR = "C"
...     TRUCK = "T"
...     JET_SKI = "J"
...
>>> Vehicle.JET_SKI.label
'Jet Ski'

Since the case where the enum values need to be integers is extremely common, Django provides an `IntegerChoices` class. For example:

class Card(models.Model):
    class Suit(models.IntegerChoices):
        DIAMOND = 1
        SPADE = 2
        HEART = 3
        CLUB = 4

    suit = models.IntegerField(choices=Suit)

It is also possible to make use of the [Enum Functional API](https://docs.python.org/3/howto/enum.html#functional-api) with the caveat that labels are automatically generated as highlighted above:

>>> MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
>>> MedalType.choices
[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')]
>>> Place = models.IntegerChoices("Place", "FIRST SECOND THIRD")
>>> Place.choices
[(1, 'First'), (2, 'Second'), (3, 'Third')]

If you require support for a concrete data type other than `int` or `str`, you can subclass `Choices` and the required concrete data type, e.g. [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)") for use with [`DateField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField "django.db.models.DateField"):

class MoonLandings(datetime.date, models.Choices):
    APOLLO_11 = 1969, 7, 20, "Apollo 11 (Eagle)"
    APOLLO_12 = 1969, 11, 19, "Apollo 12 (Intrepid)"
    APOLLO_14 = 1971, 2, 5, "Apollo 14 (Antares)"
    APOLLO_15 = 1971, 7, 30, "Apollo 15 (Falcon)"
    APOLLO_16 = 1972, 4, 21, "Apollo 16 (Orion)"
    APOLLO_17 = 1972, 12, 11, "Apollo 17 (Challenger)"

There are some additional caveats to be aware of:

*   Enumeration types do not support [named groups](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-choices-named-groups).

*   Because an enumeration with a concrete data type requires all values to match the type, overriding the [blank label](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-choices-blank-label) cannot be achieved by creating a member with a value of `None`. Instead, set the `__empty__` attribute on the class:

class Answer(models.IntegerChoices):
    NO = 0, _("No")
    YES = 1, _("Yes")

     __empty__  = _("(Unknown)")  

### `db_column`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#db-column "Link to this heading")

Field.db_column[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_column "Link to this definition")
The name of the database column to use for this field. If this isn’t given, Django will use the field’s name.

If your database column name is an SQL reserved word, or contains characters that aren’t allowed in Python variable names – notably, the hyphen – that’s OK. Django quotes column and table names behind the scenes.

### `db_comment`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#db-comment "Link to this heading")

Field.db_comment[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_comment "Link to this definition")
The comment on the database column to use for this field. It is useful for documenting fields for individuals with direct database access who may not be looking at your Django code. For example:

pub_date = models.DateTimeField(
    db_comment="Date and time when the article was published",
)

### `db_default`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#db-default "Link to this heading")

Field.db_default[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_default "Link to this definition")
The database-computed default value for this field. This can be a literal value or a database function, such as [`Now`](https://docs.djangoproject.com/en/6.0/ref/models/database-functions/#django.db.models.functions.Now "django.db.models.functions.Now"):

created = models.DateTimeField(db_default=Now())

More complex expressions can be used, as long as they are made from literals and database functions:

month_due = models.DateField(
    db_default=TruncMonth(
        Now() + timedelta(days=90),
        output_field=models.DateField(),
    )
)

Database defaults cannot reference other fields or models. For example, this is invalid:

end = models.IntegerField(db_default=F("start") + 50)

If both `db_default` and [`Field.default`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.default "django.db.models.Field.default") are set, `default` will take precedence when creating instances in Python code. `db_default` will still be set at the database level and will be used when inserting rows outside of the ORM or when adding a new field in a migration.

If a field has a `db_default` without a `default` set and no value is assigned to the field, a `DatabaseDefault` object is returned as the field value on unsaved model instances. The actual value for the field is determined by the database when the model instance is saved.

### `db_index`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#db-index "Link to this heading")

Field.db_index[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_index "Link to this definition")
If `True`, a database index will be created for this field.

Use the [`indexes`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.indexes "django.db.models.Options.indexes") option instead.

Where possible, use the [`Meta.indexes`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.indexes "django.db.models.Options.indexes") option instead. In nearly all cases, [`indexes`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.indexes "django.db.models.Options.indexes") provides more functionality than `db_index`. `db_index` may be deprecated in the future.

### `db_tablespace`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#db-tablespace "Link to this heading")

Field.db_tablespace[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L929)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_tablespace "Link to this definition")
The name of the [database tablespace](https://docs.djangoproject.com/en/6.0/topics/db/tablespaces/) to use for this field’s index, if this field is indexed. The default is the project’s [`DEFAULT_INDEX_TABLESPACE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_INDEX_TABLESPACE) setting, if set, or the [`db_tablespace`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.db_tablespace "django.db.models.Options.db_tablespace") of the model, if any. If the backend doesn’t support tablespaces for indexes, this option is ignored.

### `default`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#default "Link to this heading")

Field.default[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.default "Link to this definition")
The default value for the field. This can be a value or a callable object. If callable it will be called every time a new object is created.

The default can’t be a mutable object (model instance, `list`, `set`, etc.), as a reference to the same instance of that object would be used as the default value in all new model instances. Instead, wrap the desired default in a callable. For example, if you want to specify a default `dict` for [`JSONField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.JSONField "django.db.models.JSONField"), use a function:

def contact_default():
    return {"email": "to1@example.com"}

contact_info = JSONField("ContactInfo", default=contact_default)

`lambda`s can’t be used for field options like `default` because they can’t be [serialized by migrations](https://docs.djangoproject.com/en/6.0/topics/migrations/#migration-serializing). See that documentation for other caveats.

For fields like [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") that map to model instances, defaults should be the value of the field they reference (`pk` unless [`to_field`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.to_field "django.db.models.ForeignKey.to_field") is set) instead of model instances.

The default value is used when new model instances are created and a value isn’t provided for the field. When the field is a primary key, the default is also used when the field is set to `None`.

The default value can also be set at the database level with [`Field.db_default`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_default "django.db.models.Field.db_default").

### `editable`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#editable "Link to this heading")

Field.editable[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.editable "Link to this definition")
If `False`, the field will not be displayed in the admin or any other [`ModelForm`](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm"). It will also be skipped during [model validation](https://docs.djangoproject.com/en/6.0/ref/models/instances/#validating-objects). Default is `True`.

### `error_messages`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#error-messages "Link to this heading")

Field.error_messages[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L767)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.error_messages "Link to this definition")
The `error_messages` argument lets you override the default messages that the field will raise. Pass in a dictionary with keys matching the error messages you want to override.

Error message keys include `null`, `blank`, `invalid`, `invalid_choice`, `unique`, and `unique_for_date`. Additional error message keys are specified for each field in the [Field types](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-types) section below.

These error messages often don’t propagate to forms. See [Considerations regarding model’s error_messages](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#considerations-regarding-model-errormessages).

### `help_text`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#help-text "Link to this heading")

Field.help_text[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.help_text "Link to this definition")
Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form.

Note that this value is _not_ HTML-escaped in automatically-generated forms. This lets you include HTML in [`help_text`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.help_text "django.db.models.Field.help_text") if you so desire. For example:

help_text = "Please use the following format: <em>YYYY-MM-DD</em>."

Alternatively you can use plain text and [`django.utils.html.escape()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.html.escape "django.utils.html.escape") to escape any HTML special characters. Ensure that you escape any help text that may come from untrusted users to avoid a cross-site scripting attack.

### `primary_key`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#primary-key "Link to this heading")

Field.primary_key[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.primary_key "Link to this definition")
If `True`, this field is the primary key for the model.

If you don’t specify `primary_key=True` for any field in your model and have not defined a composite primary key, Django will automatically add a field to hold the primary key. So, you don’t need to set `primary_key=True` on any of your fields unless you want to override the default primary-key behavior. The type of auto-created primary key fields can be specified per app in [`AppConfig.default_auto_field`](https://docs.djangoproject.com/en/6.0/ref/applications/#django.apps.AppConfig.default_auto_field "django.apps.AppConfig.default_auto_field") or globally in the [`DEFAULT_AUTO_FIELD`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_AUTO_FIELD) setting. For more, see [Automatic primary key fields](https://docs.djangoproject.com/en/6.0/topics/db/models/#automatic-primary-key-fields).

`primary_key=True` implies [`null=False`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null") and [`unique=True`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique "django.db.models.Field.unique"). Only one field per model can set `primary_key=True`. Composite primary keys must be defined using [`CompositePrimaryKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CompositePrimaryKey "django.db.models.CompositePrimaryKey") instead of setting this flag to `True` for all fields to maintain this invariant.

The primary key field is read-only. If you change the value of the primary key on an existing object and then save it, a new object will be created alongside the old one.

The primary key field is set to `None` when [`deleting`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.delete "django.db.models.Model.delete") an object.

Changed in Django 5.2:
The `CompositePrimaryKey` field was added.

### `unique`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#unique "Link to this heading")

Field.unique[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L925)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique "Link to this definition")
If `True`, this field must be unique throughout the table.

This is enforced at the database level and by model validation. If you try to save a model with a duplicate value in a [`unique`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique "django.db.models.Field.unique") field, a [`django.db.IntegrityError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.IntegrityError "django.db.IntegrityError") will be raised by the model’s [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") method.

This option is valid on all field types except [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") and [`OneToOneField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.OneToOneField "django.db.models.OneToOneField").

Note that when `unique` is `True`, you don’t need to specify [`db_index`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_index "django.db.models.Field.db_index"), because `unique` implies the creation of an index.

### `unique_for_date`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#unique-for-date "Link to this heading")

Field.unique_for_date[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique_for_date "Link to this definition")
Set this to the name of a [`DateField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField "django.db.models.DateField") or [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField") to require that this field be unique for the value of the date field.

For example, if you have a field `title` that has `unique_for_date="pub_date"`, then Django wouldn’t allow the entry of two records with the same `title` and `pub_date`.

Note that if you set this to point to a [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField"), only the date portion of the field will be considered. Besides, when [`USE_TZ`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-USE_TZ) is `True`, the check will be performed in the [current time zone](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#default-current-time-zone) at the time the object gets saved.

This is enforced by [`Model.validate_unique()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.validate_unique "django.db.models.Model.validate_unique") during model validation but not at the database level. If any [`unique_for_date`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique_for_date "django.db.models.Field.unique_for_date") constraint involves fields that are not part of a [`ModelForm`](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm") (for example, if one of the fields is listed in `exclude` or has [`editable=False`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.editable "django.db.models.Field.editable")), [`Model.validate_unique()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.validate_unique "django.db.models.Model.validate_unique") will skip validation for that particular constraint.

### `unique_for_month`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#unique-for-month "Link to this heading")

Field.unique_for_month[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique_for_month "Link to this definition")
Like [`unique_for_date`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique_for_date "django.db.models.Field.unique_for_date"), but requires the field to be unique with respect to the month.

### `unique_for_year`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#unique-for-year "Link to this heading")

Field.unique_for_year[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique_for_year "Link to this definition")
Like [`unique_for_date`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique_for_date "django.db.models.Field.unique_for_date") and [`unique_for_month`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique_for_month "django.db.models.Field.unique_for_month").

### `verbose_name`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#verbose-name "Link to this heading")

Field.verbose_name[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.verbose_name "Link to this definition")
A human-readable name for the field. If the verbose name isn’t given, Django will automatically create it using the field’s attribute name, converting underscores to spaces. See [Verbose field names](https://docs.djangoproject.com/en/6.0/topics/db/models/#verbose-field-names).

### `validators`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#validators "Link to this heading")

Field.validators[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L775)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.validators "Link to this definition")
A list of validators to run for this field. See the [validators documentation](https://docs.djangoproject.com/en/6.0/ref/validators/) for more information.

Field types[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-types "Link to this heading")
-----------------------------------------------------------------------------------------------------------

### `AutoField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#autofield "Link to this heading")

_class_ AutoField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2869)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.AutoField "Link to this definition")
An [`IntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.IntegerField "django.db.models.IntegerField") that automatically increments according to available IDs. You usually won’t need to use this directly; a primary key field will automatically be added to your model if you don’t specify otherwise. See [Automatic primary key fields](https://docs.djangoproject.com/en/6.0/topics/db/models/#automatic-primary-key-fields).

### `BigAutoField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#bigautofield "Link to this heading")

_class_ BigAutoField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2877)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.BigAutoField "Link to this definition")
A 64-bit integer, much like an [`AutoField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.AutoField "django.db.models.AutoField") except that it is guaranteed to fit numbers from `1` to `9223372036854775807`.

### `BigIntegerField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#bigintegerfield "Link to this heading")

_class_ BigIntegerField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2162)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.BigIntegerField "Link to this definition")
A 64-bit integer, much like an [`IntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.IntegerField "django.db.models.IntegerField") except that it is guaranteed to fit numbers from `-9223372036854775808` to `9223372036854775807`. The default form widget for this field is a [`NumberInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.NumberInput "django.forms.NumberInput").

### `BinaryField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#binaryfield "Link to this heading")

_class_ BinaryField(_max\_length=None_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2665)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.BinaryField "Link to this definition")
A field to store raw binary data. It can be assigned [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)"), [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "(in Python v3.14)"), or [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "(in Python v3.14)").

By default, `BinaryField` sets [`editable`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.editable "django.db.models.Field.editable") to `False`, in which case it can’t be included in a [`ModelForm`](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm").

BinaryField.max_length[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.BinaryField.max_length "Link to this definition")
Optional. The maximum length (in bytes) of the field. The maximum length is enforced in Django’s validation using [`MaxLengthValidator`](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.MaxLengthValidator "django.core.validators.MaxLengthValidator").

Abusing `BinaryField`

Although you might think about storing files in the database, consider that it is bad design in 99% of the cases. This field is _not_ a replacement for proper [static files](https://docs.djangoproject.com/en/6.0/howto/static-files/) handling.

### `BooleanField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#booleanfield "Link to this heading")

_class_ BooleanField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1158)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.BooleanField "Link to this definition")
A true/false field.

The default form widget for this field is [`CheckboxInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.CheckboxInput "django.forms.CheckboxInput"), or [`NullBooleanSelect`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.NullBooleanSelect "django.forms.NullBooleanSelect") if [`null=True`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null").

The default value of `BooleanField` is `None` when [`Field.default`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.default "django.db.models.Field.default") isn’t defined.

### `CompositePrimaryKey`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#compositeprimarykey "Link to this heading")

New in Django 5.2.

_class_ CompositePrimaryKey(_*field\_names_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/composite.py#L50)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CompositePrimaryKey "Link to this definition")
A virtual field used for defining a composite primary key.

This field must be defined as the model’s `pk` attribute. If present, Django will create the underlying model table with a composite primary key.

The `*field_names` argument is a list of positional field names that compose the primary key.

See [Composite primary keys](https://docs.djangoproject.com/en/6.0/topics/composite-primary-key/) for more details.

### `CharField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#charfield "Link to this heading")

_class_ CharField(_max\_length=None_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1204)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "Link to this definition")
A string field, for small- to large-sized strings.

For large amounts of text, use [`TextField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.TextField "django.db.models.TextField").

The default form widget for this field is a [`TextInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.TextInput "django.forms.TextInput").

[`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField") has the following extra arguments:

CharField.max_length[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField.max_length "Link to this definition")
The maximum length (in characters) of the field. The `max_length` is enforced at the database level and in Django’s validation using [`MaxLengthValidator`](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.MaxLengthValidator "django.core.validators.MaxLengthValidator"). It’s required for all database backends included with Django except PostgreSQL and SQLite, which supports unlimited `VARCHAR` columns.

Note

If you are writing an application that must be portable to multiple database backends, you should be aware that there are restrictions on `max_length` for some backends. Refer to the [database backend notes](https://docs.djangoproject.com/en/6.0/ref/databases/) for details.

Changed in Django 5.2:
Support for unlimited `VARCHAR` columns was added on SQLite.

CharField.db_collation[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField.db_collation "Link to this definition")
Optional. The database collation name of the field.

Note

Collation names are not standardized. As such, this will not be portable across multiple database backends.

Oracle

Oracle supports collations only when the `MAX_STRING_SIZE` database initialization parameter is set to `EXTENDED`.

### `DateField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#datefield "Link to this heading")

_class_ DateField(_auto\_now=False_, _auto\_now\_add=False_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1422)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField "Link to this definition")
A date, represented in Python by a `datetime.date` instance. Has a few extra, optional arguments:

DateField.auto_now[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField.auto_now "Link to this definition")
Automatically set the field to now every time the object is saved. Useful for “last-modified” timestamps. Note that the current date is _always_ used; it’s not just a default value that you can override.

The field is only automatically updated when calling [`Model.save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save"). The field isn’t updated when making updates to other fields in other ways such as [`QuerySet.update()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.update "django.db.models.query.QuerySet.update"), though you can specify a custom value for the field in an update like that.

DateField.auto_now_add[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField.auto_now_add "Link to this definition")
Automatically set the field to now when the object is first created. Useful for creation of timestamps. Note that the current date is _always_ used; it’s not just a default value that you can override. So even if you set a value for this field when creating the object, it will be ignored. If you want to be able to modify this field, set the following instead of `auto_now_add=True`:

*   For [`DateField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField "django.db.models.DateField"): `default=date.today` - from [`datetime.date.today()`](https://docs.python.org/3/library/datetime.html#datetime.date.today "(in Python v3.14)")

*   For [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField"): `default=timezone.now` - from [`django.utils.timezone.now()`](https://docs.djangoproject.com/en/6.0/ref/utils/#django.utils.timezone.now "django.utils.timezone.now")

The default form widget for this field is a [`DateInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.DateInput "django.forms.DateInput"). The admin adds a JavaScript calendar, and a shortcut for “Today”. Includes an additional `invalid_date` error message key.

The options `auto_now_add`, `auto_now`, and `default` are mutually exclusive. Any combination of these options will result in an error.

Note

As currently implemented, setting `auto_now` or `auto_now_add` to `True` will cause the field to have `editable=False` and `blank=True` set.

Note

The `auto_now` and `auto_now_add` options will always use the date in the [default timezone](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#default-current-time-zone) at the moment of creation or update. If you need something different, you may want to consider using your own callable default or overriding `save()` instead of using `auto_now` or `auto_now_add`; or using a `DateTimeField` instead of a `DateField` and deciding how to handle the conversion from datetime to date at display time.

Warning

Always use [`DateField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField "django.db.models.DateField") with a `datetime.date` instance.

If you have a `datetime.datetime` instance, it’s recommended to convert it to a `datetime.date` first. If you don’t, [`DateField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField "django.db.models.DateField") will localize the `datetime.datetime` to the [default timezone](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#default-current-time-zone) and convert it to a `datetime.date` instance, removing its time component. This is true for both storage and comparison.

Warning

On PostgreSQL and MySQL, arithmetic operations on a `DateField` with a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)") return a `datetime` instead of a `date`. This occurs because Python’s `timedelta` is converted to SQL `INTERVAL`, and the SQL operation `date +/- interval` returns a `timestamp` on these databases.

To ensure a `date` result, use one of the following approaches. Either explicitly cast the result to a date:

import datetime
from django.db.models import DateField, F
from django.db.models.functions import Cast

qs = MyModel.objects.annotate(
    previous_day=Cast(
        F("date_field") - datetime.timedelta(days=1),
        output_field=DateField(),
    )
)

Or on PostgreSQL only, use integer arithmetic to represent days:

from django.db.models import DateField, ExpressionWrapper, F

qs = MyModel.objects.annotate(
    previous_day=ExpressionWrapper(
        F("date_field") - 1,  # Subtract 1 day as integer
        output_field=DateField(),
    )
)

### `DateTimeField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#datetimefield "Link to this heading")

_class_ DateTimeField(_auto\_now=False_, _auto\_now\_add=False_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1557)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "Link to this definition")
A date and time, represented in Python by a `datetime.datetime` instance. Takes the same extra arguments as [`DateField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField "django.db.models.DateField").

The default form widget for this field is a single [`DateTimeInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.DateTimeInput "django.forms.DateTimeInput"). The admin uses two separate [`TextInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.TextInput "django.forms.TextInput") widgets with JavaScript shortcuts.

Warning

Always use [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField") with a `datetime.datetime` instance.

If you have a `datetime.date` instance, it’s recommended to convert it to a `datetime.datetime` first. If you don’t, [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField") will use midnight in the [default timezone](https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/#default-current-time-zone) for the time component. This is true for both storage and comparison. To compare the date portion of a [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField") with a `datetime.date` instance, use the [`date`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-date) lookup.

### `DecimalField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#decimalfield "Link to this heading")

_class_ DecimalField(_max\_digits=None_, _decimal\_places=None_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1698)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DecimalField "Link to this definition")
A fixed-precision decimal number, represented in Python by a [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.14)") instance. It validates the input using [`DecimalValidator`](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.DecimalValidator "django.core.validators.DecimalValidator").

Has the following **required** arguments:

DecimalField.max_digits[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DecimalField.max_digits "Link to this definition")
The maximum number of digits allowed in the number. Note that this number must be greater than or equal to `decimal_places`.

DecimalField.decimal_places[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DecimalField.decimal_places "Link to this definition")
The number of decimal places to store with the number.

For example, to store numbers up to `999.99` with a resolution of 2 decimal places, you’d use:

models.DecimalField(..., max_digits=5, decimal_places=2)

And to store numbers up to approximately one billion with a resolution of 10 decimal places:

models.DecimalField(..., max_digits=19, decimal_places=10)

The default form widget for this field is a [`NumberInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.NumberInput "django.forms.NumberInput") when [`localize`](https://docs.djangoproject.com/en/6.0/ref/forms/fields/#django.forms.Field.localize "django.forms.Field.localize") is `False` or [`TextInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.TextInput "django.forms.TextInput") otherwise.

Note

For more information about the differences between the [`FloatField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FloatField "django.db.models.FloatField") and [`DecimalField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DecimalField "django.db.models.DecimalField") classes, please see [FloatField vs. DecimalField](https://docs.djangoproject.com/en/6.0/ref/models/fields/#floatfield-vs-decimalfield). You should also be aware of [SQLite limitations](https://docs.djangoproject.com/en/6.0/ref/databases/#sqlite-decimal-handling) of decimal fields.

### `DurationField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#durationfield "Link to this heading")

_class_ DurationField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1853)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DurationField "Link to this definition")
A field for storing periods of time - modeled in Python by [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)"). When used on PostgreSQL, the data type used is an `interval` and on Oracle the data type is 
```
INTERVAL DAY(9) TO
SECOND(6)
```
. Otherwise a `bigint` of microseconds is used.

Note

Arithmetic with `DurationField` works in most cases. However on all databases other than PostgreSQL, comparing the value of a `DurationField` to arithmetic on `DateTimeField` instances will not work as expected.

### `EmailField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#emailfield "Link to this heading")

_class_ EmailField(_max\_length=254_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1918)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.EmailField "Link to this definition")
A [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField") that checks that the value is a valid email address using [`EmailValidator`](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.EmailValidator "django.core.validators.EmailValidator").

### `FileField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#filefield "Link to this heading")

_class_ FileField(_upload\_to=''_, _storage=None_, _max\_length=100_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/files.py#L236)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField "Link to this definition")
A file-upload field.

Note

The `primary_key` argument isn’t supported and will raise an error if used.

Has the following optional arguments:

FileField.upload_to[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField.upload_to "Link to this definition")
This attribute provides a way of setting the upload directory and file name, and can be set in two ways. In both cases, the value is passed to the [`Storage.save()`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.save "django.core.files.storage.Storage.save") method.

If you specify a string value or a [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)"), it may contain [`strftime()`](https://docs.python.org/3/library/time.html#time.strftime "(in Python v3.14)") formatting, which will be replaced by the date/time of the file upload (so that uploaded files don’t fill up the given directory). For example:

class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to="uploads/")
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to="uploads/%Y/%m/%d/")

If you are using the default [`FileSystemStorage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.FileSystemStorage "django.core.files.storage.FileSystemStorage"), the string value will be appended to your [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT) path to form the location on the local filesystem where uploaded files will be stored. If you are using a different storage, check that storage’s documentation to see how it handles `upload_to`.

`upload_to` may also be a callable, such as a function. This will be called to obtain the upload path, including the filename. This callable must accept two arguments and return a Unix-style path (with forward slashes) to be passed along to the storage system. The two arguments are:

| Argument | Description |
| --- | --- |
| `instance` | An instance of the model where the `FileField` is defined. More specifically, this is the particular instance where the current file is being attached. In most cases, this object will not have been saved to the database yet, so if it uses the default `AutoField`, _it might not yet have a value for its primary key field_. |
| `filename` | The filename that was originally given to the file. This may or may not be taken into account when determining the final destination path. |

For example:

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)

FileField.storage[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField.storage "Link to this definition")
A storage object, or a callable which returns a storage object. This handles the storage and retrieval of your files. See [Managing files](https://docs.djangoproject.com/en/6.0/topics/files/) for details on how to provide this object.

The default form widget for this field is a [`ClearableFileInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.ClearableFileInput "django.forms.ClearableFileInput").

Using a [`FileField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField "django.db.models.FileField") or an [`ImageField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ImageField "django.db.models.ImageField") (see below) in a model takes a few steps:

1.   In your settings file, you’ll need to define [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT) as the full path to a directory where you’d like Django to store uploaded files. (For performance, these files are not stored in the database.) Define [`MEDIA_URL`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_URL) as the base public URL of that directory. Make sure that this directory is writable by the web server’s user account.

2.   Add the [`FileField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField "django.db.models.FileField") or [`ImageField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ImageField "django.db.models.ImageField") to your model, defining the [`upload_to`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField.upload_to "django.db.models.FileField.upload_to") option to specify a subdirectory of [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT) to use for uploaded files.

3.   All that will be stored in your database is a path to the file (relative to [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT)). You’ll most likely want to use the convenience [`url`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.url "django.db.models.fields.files.FieldFile.url") attribute provided by Django. For example, if your [`ImageField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ImageField "django.db.models.ImageField") is called `mug_shot`, you can get the absolute path to your image in a template with `{{ object.mug_shot.url }}`.

For example, say your [`MEDIA_ROOT`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-MEDIA_ROOT) is set to `'/home/media'`, and [`upload_to`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField.upload_to "django.db.models.FileField.upload_to") is set to `'photos/%Y/%m/%d'`. The `'%Y/%m/%d'` part of [`upload_to`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField.upload_to "django.db.models.FileField.upload_to") is [`strftime()`](https://docs.python.org/3/library/time.html#time.strftime "(in Python v3.14)") formatting; `'%Y'` is the four-digit year, `'%m'` is the two-digit month and `'%d'` is the two-digit day. If you upload a file on Jan. 15, 2007, it will be saved in the directory `/home/media/photos/2007/01/15`.

If you wanted to retrieve the uploaded file’s on-disk filename, or the file’s size, you could use the [`name`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.name "django.core.files.File.name") and [`size`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File.size "django.core.files.File.size") attributes respectively; for more information on the available attributes and methods, see the [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") class reference and the [Managing files](https://docs.djangoproject.com/en/6.0/topics/files/) topic guide.

Note

The file is saved as part of saving the model in the database, so the actual file name used on disk cannot be relied on until after the model has been saved.

The uploaded file’s relative URL can be obtained using the [`url`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.url "django.db.models.fields.files.FieldFile.url") attribute. Internally, this calls the [`url()`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.url "django.core.files.storage.Storage.url") method of the underlying [`Storage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage "django.core.files.storage.Storage") class.

Note that whenever you deal with uploaded files, you should pay close attention to where you’re uploading them and what type of files they are, to avoid security holes. _Validate all uploaded files_ so that you’re sure the files are what you think they are. For example, if you blindly let somebody upload files, without validation, to a directory that’s within your web server’s document root, then somebody could upload a CGI or PHP script and execute that script by visiting its URL on your site. Don’t allow that.

Also note that even an uploaded HTML file, since it can be executed by the browser (though not by the server), can pose security threats that are equivalent to XSS or CSRF attacks.

[`FileField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField "django.db.models.FileField") instances are created in your database as `varchar` columns with a default max length of 100 characters. As with other fields, you can change the maximum length using the [`max_length`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField.max_length "django.db.models.CharField.max_length") argument.

#### `FileField` and `FieldFile`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#filefield-and-fieldfile "Link to this heading")

_class_ FieldFile[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/files.py#L19)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile "Link to this definition")
When you access a [`FileField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField "django.db.models.FileField") on a model, you are given an instance of [`FieldFile`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile "django.db.models.fields.files.FieldFile") as a proxy for accessing the underlying file.

The API of [`FieldFile`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile "django.db.models.fields.files.FieldFile") mirrors that of [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File"), with one key difference: _The object wrapped by the class is not necessarily a wrapper around Python’s built-in file object._ Instead, it is a wrapper around the result of the [`Storage.open()`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.open "django.core.files.storage.Storage.open") method, which may be a [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") object, or it may be a custom storage’s implementation of the [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") API.

In addition to the API inherited from [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") such as `read()` and `write()`, [`FieldFile`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile "django.db.models.fields.files.FieldFile") includes several methods that can be used to interact with the underlying file:

Warning

Two methods of this class, [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.save "django.db.models.fields.files.FieldFile.save") and [`delete()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.delete "django.db.models.fields.files.FieldFile.delete"), default to saving the model object of the associated `FieldFile` in the database.

FieldFile.name[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.name "Link to this definition")
The name of the file including the relative path from the root of the [`Storage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage "django.core.files.storage.Storage") of the associated [`FileField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField "django.db.models.FileField").

FieldFile.path[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/files.py#L62)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.path "Link to this definition")
A read-only property to access the file’s local filesystem path by calling the [`path()`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.path "django.core.files.storage.Storage.path") method of the underlying [`Storage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage "django.core.files.storage.Storage") class.

FieldFile.size[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/files.py#L72)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.size "Link to this definition")
The result of the underlying [`Storage.size()`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.size "django.core.files.storage.Storage.size") method.

FieldFile.url[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/files.py#L67)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.url "Link to this definition")
A read-only property to access the file’s relative URL by calling the [`url()`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage.url "django.core.files.storage.Storage.url") method of the underlying [`Storage`](https://docs.djangoproject.com/en/6.0/ref/files/storage/#django.core.files.storage.Storage "django.core.files.storage.Storage") class.

FieldFile.open(_mode='rb'_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/files.py#L78)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.open "Link to this definition")
Opens or reopens the file associated with this instance in the specified `mode`. Unlike the standard Python `open()` method, it doesn’t return a file descriptor.

Since the underlying file is opened implicitly when accessing it, it may be unnecessary to call this method except to reset the pointer to the underlying file or to change the `mode`.

FieldFile.close()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/files.py#L133)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.close "Link to this definition")
Behaves like the standard Python `file.close()` method and closes the file associated with this instance.

FieldFile.save(_name_, _content_, _save=True_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/files.py#L96)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.save "Link to this definition")
This method takes a filename and file contents and passes them to the storage class for the field, then associates the stored file with the model field. If you want to manually associate file data with [`FileField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField "django.db.models.FileField") instances on your model, the `save()` method is used to persist that file data.

Takes two required arguments: `name` which is the name of the file, and `content` which is an object containing the file’s contents. The optional `save` argument controls whether or not the model instance is saved after the file associated with this field has been altered. Defaults to `True`.

Note that the `content` argument should be an instance of [`django.core.files.File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File"), not Python’s built-in file object. You can construct a [`File`](https://docs.djangoproject.com/en/6.0/ref/files/file/#django.core.files.File "django.core.files.File") from an existing Python file object like this:

from django.core.files import File

# Open an existing file using Python's built-in open()
f = open("/path/to/hello.world")
myfile = File(f)

Or you can construct one from a Python string like this:

from django.core.files.base import ContentFile

myfile = ContentFile("hello world")

For more information, see [Managing files](https://docs.djangoproject.com/en/6.0/topics/files/).

FieldFile.delete(_save=True_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/files.py#L108)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.fields.files.FieldFile.delete "Link to this definition")
Deletes the file associated with this instance and clears all attributes on the field. Note: This method will close the file if it happens to be open when `delete()` is called.

The optional `save` argument controls whether or not the model instance is saved after the file associated with this field has been deleted. Defaults to `True`.

Note that when a model is deleted, related files are not deleted. If you need to cleanup orphaned files, you’ll need to handle it yourself (for instance, with a custom management command that can be run manually or scheduled to run periodically via e.g. cron).

### `FilePathField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#filepathfield "Link to this heading")

_class_ FilePathField(_path=''_, _match=None_, _recursive=False_, _allow\_files=True_, _allow\_folders=False_, _max\_length=100_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1944)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField "Link to this definition")
A [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField") whose choices are limited to the filenames in a certain directory on the filesystem. Has some special arguments, of which the first is **required**:

FilePathField.path[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField.path "Link to this definition")
Required. The absolute filesystem path to a directory from which this [`FilePathField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField "django.db.models.FilePathField") should get its choices. Example: `"/home/images"`.

`path` may also be a callable, such as a function to dynamically set the path at runtime. Example:

import os
from django.conf import settings
from django.db import models

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "images")

class MyModel(models.Model):
    file = models.FilePathField(path=images_path)

FilePathField.match[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField.match "Link to this definition")
Optional. A regular expression, as a string, that [`FilePathField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField "django.db.models.FilePathField") will use to filter filenames. Note that the regex will be applied to the base filename, not the full path. Example: `"foo.*\.txt$"`, which will match a file called `foo23.txt` but not `bar.txt` or `foo23.png`.

FilePathField.recursive[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField.recursive "Link to this definition")
Optional. Either `True` or `False`. Default is `False`. Specifies whether all subdirectories of [`path`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField.path "django.db.models.FilePathField.path") should be included

FilePathField.allow_files[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField.allow_files "Link to this definition")
Optional. Either `True` or `False`. Default is `True`. Specifies whether files in the specified location should be included. Either this or [`allow_folders`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField.allow_folders "django.db.models.FilePathField.allow_folders") must be `True`.

FilePathField.allow_folders[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField.allow_folders "Link to this definition")
Optional. Either `True` or `False`. Default is `False`. Specifies whether folders in the specified location should be included. Either this or [`allow_files`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField.allow_files "django.db.models.FilePathField.allow_files") must be `True`.

The one potential gotcha is that [`match`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField.match "django.db.models.FilePathField.match") applies to the base filename, not the full path. So, this example:

FilePathField(path="/home/images", match="foo.*", recursive=True)

…will match `/home/images/foo.png` but not `/home/images/foo/bar.png` because the [`match`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField.match "django.db.models.FilePathField.match") applies to the base filename (`foo.png` and `bar.png`).

[`FilePathField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FilePathField "django.db.models.FilePathField") instances are created in your database as `varchar` columns with a default max length of 100 characters. As with other fields, you can change the maximum length using the [`max_length`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField.max_length "django.db.models.CharField.max_length") argument.

### `FloatField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#floatfield "Link to this heading")

_class_ FloatField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2020)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FloatField "Link to this definition")
A floating-point number represented in Python by a `float` instance.

The default form widget for this field is a [`NumberInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.NumberInput "django.forms.NumberInput") when [`localize`](https://docs.djangoproject.com/en/6.0/ref/forms/fields/#django.forms.Field.localize "django.forms.Field.localize") is `False` or [`TextInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.TextInput "django.forms.TextInput") otherwise.

`FloatField` vs. `DecimalField`

The [`FloatField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FloatField "django.db.models.FloatField") class is sometimes mixed up with the [`DecimalField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DecimalField "django.db.models.DecimalField") class. Although they both represent real numbers, they represent those numbers differently. `FloatField` uses Python’s `float` type internally, while `DecimalField` uses Python’s `Decimal` type. For information on the difference between the two, see Python’s documentation for the [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "(in Python v3.14)") module.

### `GeneratedField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#generatedfield "Link to this heading")

_class_ GeneratedField(_*_, _expression_, _output\_field_, _db\_persist_, _**kwargs_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/generated.py#L11)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.GeneratedField "Link to this definition")
A field that is always computed based on other fields in the model. This field is managed and updated by the database itself. Uses the `GENERATED ALWAYS` SQL syntax.

There are two kinds of generated columns: stored and virtual. A stored generated column is computed when it is written (inserted or updated) and occupies storage as if it were a regular column. A virtual generated column occupies no storage and is computed when it is read. Thus, a virtual generated column is similar to a view and a stored generated column is similar to a materialized view.

GeneratedField.expression[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.GeneratedField.expression "Link to this definition")
An [`Expression`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression "django.db.models.Expression") used by the database to automatically set the field value each time the model is changed.

The expressions should be deterministic and only reference fields within the model (in the same database table). Generated fields cannot reference other generated fields. Database backends can impose further restrictions.

GeneratedField.output_field[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.GeneratedField.output_field "Link to this definition")
A model field instance to define the field’s data type.

GeneratedField.db_persist[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.GeneratedField.db_persist "Link to this definition")
Determines if the database column should occupy storage as if it were a real column. If `False`, the column acts as a virtual column and does not occupy database storage space.

PostgreSQL only supports persisted columns. Oracle only supports virtual columns.

Database limitations

There are many database-specific restrictions on generated fields that Django doesn’t validate and the database may raise an error e.g. PostgreSQL requires functions and operators referenced in a generated column to be marked as `IMMUTABLE`.

You should always check that `expression` is supported on your database. Check out [MariaDB](https://mariadb.com/kb/en/generated-columns/#expression-support), [MySQL](https://dev.mysql.com/doc/refman/en/create-table-generated-columns.html), [Oracle](https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6__BABIIGBD), [PostgreSQL](https://www.postgresql.org/docs/current/ddl-generated-columns.html), or [SQLite](https://www.sqlite.org/gencol.html#limitations) docs.

Changed in Django 6.0:
`GeneratedField`s are now automatically refreshed from the database on backends that support it (SQLite, PostgreSQL, and Oracle) and marked as deferred otherwise.

### `GenericIPAddressField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#genericipaddressfield "Link to this heading")

_class_ GenericIPAddressField(_protocol='both'_, _unpack\_ipv4=False_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2217)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.GenericIPAddressField "Link to this definition")
An IPv4 or IPv6 address, in string format (e.g. `192.0.2.30` or `2a02:42fe::4`). The default form widget for this field is a [`TextInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.TextInput "django.forms.TextInput").

The IPv6 address normalization follows [**RFC 4291 Section 2.2**](https://datatracker.ietf.org/doc/html/rfc4291.html#section-2.2) section 2.2, including using the IPv4 format suggested in paragraph 3 of that section, like `::ffff:192.0.2.0`. For example, `2001:0::0:01` would be normalized to `2001::1`, and `::ffff:0a0a:0a0a` to `::ffff:10.10.10.10`. All characters are converted to lowercase.

GenericIPAddressField.protocol[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.GenericIPAddressField.protocol "Link to this definition")
Limits valid inputs to the specified protocol. Accepted values are `'both'` (default), `'IPv4'` or `'IPv6'`. Matching is case insensitive.

GenericIPAddressField.unpack_ipv4[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.GenericIPAddressField.unpack_ipv4 "Link to this definition")
Unpacks IPv4 mapped addresses like `::ffff:192.0.2.1`. If this option is enabled that address would be unpacked to `192.0.2.1`. Default is disabled. Can only be used when `protocol` is set to `'both'`.

If you allow for blank values, you have to allow for null values since blank values are stored as null.

### `ImageField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#imagefield "Link to this heading")

_class_ ImageField(_upload\_to=None_, _height\_field=None_, _width\_field=None_, _max\_length=100_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/files.py#L417)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ImageField "Link to this definition")
Inherits all attributes and methods from [`FileField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField "django.db.models.FileField"), but also validates that the uploaded object is a valid image.

In addition to the special attributes that are available for [`FileField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.FileField "django.db.models.FileField"), an [`ImageField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ImageField "django.db.models.ImageField") also has `height` and `width` attributes.

To facilitate querying on those attributes, [`ImageField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ImageField "django.db.models.ImageField") has the following optional arguments:

ImageField.height_field[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ImageField.height_field "Link to this definition")
Name of a model field which is auto-populated with the height of the image each time an image object is set.

ImageField.width_field[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ImageField.width_field "Link to this definition")
Name of a model field which is auto-populated with the width of the image each time an image object is set.

Requires the [pillow](https://pypi.org/project/pillow/) library.

[`ImageField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ImageField "django.db.models.ImageField") instances are created in your database as `varchar` columns with a default max length of 100 characters. As with other fields, you can change the maximum length using the [`max_length`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField.max_length "django.db.models.CharField.max_length") argument.

The default form widget for this field is a [`ClearableFileInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.ClearableFileInput "django.forms.ClearableFileInput").

### `IntegerField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#integerfield "Link to this heading")

_class_ IntegerField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2062)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.IntegerField "Link to this definition")
An integer. Values are only allowed between certain (database-dependent) points. Values from `-2147483648` to `2147483647` are compatible in all databases supported by Django.

It uses [`MinValueValidator`](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.MinValueValidator "django.core.validators.MinValueValidator") and [`MaxValueValidator`](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.MaxValueValidator "django.core.validators.MaxValueValidator") to validate the input based on the values that the default database supports.

The default form widget for this field is a [`NumberInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.NumberInput "django.forms.NumberInput") when [`localize`](https://docs.djangoproject.com/en/6.0/ref/forms/fields/#django.forms.Field.localize "django.forms.Field.localize") is `False` or [`TextInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.TextInput "django.forms.TextInput") otherwise.

### `JSONField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#jsonfield "Link to this heading")

_class_ JSONField(_encoder=None_, _decoder=None_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/json.py#L22)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.JSONField "Link to this definition")
A field for storing JSON encoded data. In Python the data is represented in its Python native format: dictionaries, lists, strings, numbers, booleans and `None`.

`JSONField` is supported on MariaDB, MySQL, Oracle, PostgreSQL, and SQLite (with the [JSON1 extension enabled](https://docs.djangoproject.com/en/6.0/ref/databases/#sqlite-json1)).

JSONField.encoder[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.JSONField.encoder "Link to this definition")
An optional [`json.JSONEncoder`](https://docs.python.org/3/library/json.html#json.JSONEncoder "(in Python v3.14)") subclass to serialize data types not supported by the standard JSON serializer (e.g. `datetime.datetime` or [`UUID`](https://docs.python.org/3/library/uuid.html#uuid.UUID "(in Python v3.14)")). For example, you can use the [`DjangoJSONEncoder`](https://docs.djangoproject.com/en/6.0/topics/serialization/#django.core.serializers.json.DjangoJSONEncoder "django.core.serializers.json.DjangoJSONEncoder") class.

Defaults to `json.JSONEncoder`.

JSONField.decoder[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.JSONField.decoder "Link to this definition")
An optional [`json.JSONDecoder`](https://docs.python.org/3/library/json.html#json.JSONDecoder "(in Python v3.14)") subclass to deserialize the value retrieved from the database. The value will be in the format chosen by the custom encoder (most often a string). Your deserialization may need to account for the fact that you can’t be certain of the input type. For example, you run the risk of returning a `datetime` that was actually a string that just happened to be in the same format chosen for `datetime`s.

Defaults to `json.JSONDecoder`.

To query `JSONField` in the database, see [Querying JSONField](https://docs.djangoproject.com/en/6.0/topics/db/queries/#querying-jsonfield).

Default value

If you give the field a [`default`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.default "django.db.models.Field.default"), ensure it’s a callable such as the [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") class or a function that returns a fresh object each time. Incorrectly using a mutable object like `default={}` or `default=[]` creates a mutable default that is shared between all instances.

Indexing

[`Index`](https://docs.djangoproject.com/en/6.0/ref/models/indexes/#django.db.models.Index "django.db.models.Index") and [`Field.db_index`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_index "django.db.models.Field.db_index") both create a B-tree index, which isn’t particularly helpful when querying `JSONField`. On PostgreSQL only, you can use [`GinIndex`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/indexes/#django.contrib.postgres.indexes.GinIndex "django.contrib.postgres.indexes.GinIndex") that is better suited.

PostgreSQL users

PostgreSQL has two native JSON based data types: `json` and `jsonb`. The main difference between them is how they are stored and how they can be queried. PostgreSQL’s `json` field is stored as the original string representation of the JSON and must be decoded on the fly when queried based on keys. The `jsonb` field is stored based on the actual structure of the JSON which allows indexing. The trade-off is a small additional cost on writing to the `jsonb` field. `JSONField` uses `jsonb`.

Oracle users

Oracle Database does not support storing JSON scalar values. Only JSON objects and arrays (represented in Python using [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") and [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) are supported.

### `PositiveBigIntegerField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#positivebigintegerfield "Link to this heading")

_class_ PositiveBigIntegerField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2363)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.PositiveBigIntegerField "Link to this definition")
Like a [`PositiveIntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.PositiveIntegerField "django.db.models.PositiveIntegerField"), but only allows values under a certain (database-dependent) point. Values from `0` to `9223372036854775807` are compatible in all databases supported by Django.

### `PositiveIntegerField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#positiveintegerfield "Link to this heading")

_class_ PositiveIntegerField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2378)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.PositiveIntegerField "Link to this definition")
Like an [`IntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.IntegerField "django.db.models.IntegerField"), but must be either positive or zero (`0`). Values are only allowed under a certain (database-dependent) point. Values from `0` to `2147483647` are compatible in all databases supported by Django. The value `0` is accepted for backward compatibility reasons.

### `PositiveSmallIntegerField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#positivesmallintegerfield "Link to this heading")

_class_ PositiveSmallIntegerField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2393)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.PositiveSmallIntegerField "Link to this definition")
Like a [`PositiveIntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.PositiveIntegerField "django.db.models.PositiveIntegerField"), but only allows values under a certain (database-dependent) point. Values from `0` to `32767` are compatible in all databases supported by Django.

### `SlugField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#slugfield "Link to this heading")

_class_ SlugField(_max\_length=50_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2408)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.SlugField "Link to this definition")
[Slug](https://docs.djangoproject.com/en/6.0/glossary/#term-slug) is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.

Like a CharField, you can specify [`max_length`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField.max_length "django.db.models.CharField.max_length") (read the note about database portability and [`max_length`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField.max_length "django.db.models.CharField.max_length") in that section, too). If [`max_length`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField.max_length "django.db.models.CharField.max_length") is not specified, Django will use a default length of 50.

Implies setting [`Field.db_index`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_index "django.db.models.Field.db_index") to `True`.

It is often useful to automatically prepopulate a SlugField based on the value of some other value. You can do this automatically in the admin using [`prepopulated_fields`](https://docs.djangoproject.com/en/6.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields "django.contrib.admin.ModelAdmin.prepopulated_fields").

It uses [`validate_slug`](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.validate_slug "django.core.validators.validate_slug") or [`validate_unicode_slug`](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.validate_unicode_slug "django.core.validators.validate_unicode_slug") for validation.

SlugField.allow_unicode[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.SlugField.allow_unicode "Link to this definition")
If `True`, the field accepts Unicode letters in addition to ASCII letters. Defaults to `False`.

### `SmallAutoField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#smallautofield "Link to this heading")

_class_ SmallAutoField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2885)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.SmallAutoField "Link to this definition")
Like an [`AutoField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.AutoField "django.db.models.AutoField"), but only allows values under a certain (database-dependent) limit. Values from `1` to `32767` are compatible in all databases supported by Django.

### `SmallIntegerField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#smallintegerfield "Link to this heading")

_class_ SmallIntegerField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2179)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.SmallIntegerField "Link to this definition")
Like an [`IntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.IntegerField "django.db.models.IntegerField"), but only allows values under a certain (database-dependent) point. Values from `-32768` to `32767` are compatible in all databases supported by Django.

### `TextField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#textfield "Link to this heading")

_class_ TextField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2445)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.TextField "Link to this definition")
A large text field. The default form widget for this field is a [`Textarea`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.Textarea "django.forms.Textarea").

If you specify a `max_length` attribute, it will be reflected in the [`Textarea`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.Textarea "django.forms.Textarea") widget of the auto-generated form field. However it is not enforced at the model or database level. Use a [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField") for that.

TextField.db_collation[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.TextField.db_collation "Link to this definition")
Optional. The database collation name of the field.

Note

Collation names are not standardized. As such, this will not be portable across multiple database backends.

Oracle

Oracle does not support collations for a `TextField`.

### `TimeField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#timefield "Link to this heading")

_class_ TimeField(_auto\_now=False_, _auto\_now\_add=False_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2522)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.TimeField "Link to this definition")
A time, represented in Python by a `datetime.time` instance. Accepts the same auto-population options as [`DateField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField "django.db.models.DateField").

The default form widget for this field is a [`TimeInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.TimeInput "django.forms.TimeInput"). The admin adds some JavaScript shortcuts.

### `URLField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#urlfield "Link to this heading")

_class_ URLField(_max\_length=200_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2640)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.URLField "Link to this definition")
A [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField") for a URL, validated by [`URLValidator`](https://docs.djangoproject.com/en/6.0/ref/validators/#django.core.validators.URLValidator "django.core.validators.URLValidator").

The default form widget for this field is a [`URLInput`](https://docs.djangoproject.com/en/6.0/ref/forms/widgets/#django.forms.URLInput "django.forms.URLInput").

Like all [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField") subclasses, [`URLField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.URLField "django.db.models.URLField") takes the optional [`max_length`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField.max_length "django.db.models.CharField.max_length") argument. If you don’t specify [`max_length`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField.max_length "django.db.models.CharField.max_length"), a default of 200 is used.

### `UUIDField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#uuidfield "Link to this heading")

_class_ UUIDField(_**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L2729)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.UUIDField "Link to this definition")
A field for storing universally unique identifiers. Uses Python’s [`UUID`](https://docs.python.org/3/library/uuid.html#uuid.UUID "(in Python v3.14)") class. When used on PostgreSQL and MariaDB 10.7+, this stores in a `uuid` datatype, otherwise in a `char(32)`.

Universally unique identifiers are a good alternative to [`AutoField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.AutoField "django.db.models.AutoField") for [`primary_key`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.primary_key "django.db.models.Field.primary_key"). The database will not generate the UUID for you, so it is recommended to use [`default`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.default "django.db.models.Field.default"):

import uuid
from django.db import models

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # other fields

Note that a callable (with the parentheses omitted) is passed to `default`, not an instance of `UUID`.

Lookups on PostgreSQL and MariaDB 10.7+

Using [`iexact`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-iexact), [`contains`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-contains), [`icontains`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-icontains), [`startswith`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-startswith), [`istartswith`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-istartswith), [`endswith`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-endswith), or [`iendswith`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#std-fieldlookup-iendswith) lookups on PostgreSQL don’t work for values without hyphens, because PostgreSQL and MariaDB 10.7+ store them in a hyphenated uuid datatype type.

Relationship fields[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#module-django.db.models.fields.related "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Django also defines a set of fields that represent relations.

### `ForeignKey`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#foreignkey "Link to this heading")

_class_ ForeignKey(_to_, _on\_delete_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/related.py#L957)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "Link to this definition")
A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the [`on_delete`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.on_delete "django.db.models.ForeignKey.on_delete") option:

from django.db import models

class Manufacturer(models.Model):
    name = models.TextField()

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

The first positional argument can be either a concrete model class or a [lazy reference](https://docs.djangoproject.com/en/6.0/ref/models/fields/#lazy-relationships) to a model class. [Recursive relationships](https://docs.djangoproject.com/en/6.0/ref/models/fields/#recursive-relationships), where a model has a relationship with itself, are also supported.

See [`ForeignKey.on_delete`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.on_delete "django.db.models.ForeignKey.on_delete") for details on the second positional argument.

A database index is automatically created on the `ForeignKey`. You can disable this by setting [`db_index`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_index "django.db.models.Field.db_index") to `False`. You may want to avoid the overhead of an index if you are creating a foreign key for consistency rather than joins, or if you will be creating an alternative index like a partial or multiple column index.

#### Database Representation[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#database-representation "Link to this heading")

Behind the scenes, Django appends `"_id"` to the field name to create its database column name. In the above example, the database table for the `Car` model will have a `manufacturer_id` column. You can change this explicitly by specifying [`db_column`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_column "django.db.models.Field.db_column"), however, your code should never have to deal with the database column name (unless you write custom SQL). You’ll always deal with the field names of your model object.

#### Arguments[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#arguments "Link to this heading")

[`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") accepts other arguments that define the details of how the relation works.

ForeignKey.on_delete[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.on_delete "Link to this definition")
When an object referenced by a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") is deleted, Django will emulate the behavior of the SQL constraint specified by the [`on_delete`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.on_delete "django.db.models.ForeignKey.on_delete") argument. For example, if you have a nullable [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") and you want it to be set null when the referenced object is deleted:

user = models.ForeignKey(
    User,
    models.SET_NULL,
    blank=True,
    null=True,
)

`on_delete` doesn’t create an SQL constraint in the database. Support for database-level cascade options [may be implemented later](https://code.djangoproject.com/ticket/21961).

The possible values for [`on_delete`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.on_delete "django.db.models.ForeignKey.on_delete") are found in [`django.db.models`](https://docs.djangoproject.com/en/6.0/topics/db/models/#module-django.db.models "django.db.models"):

*   CASCADE[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/deletion.py#L22)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CASCADE "Link to this definition")
Cascade deletes. Django emulates the behavior of the SQL constraint 
```
ON
DELETE CASCADE
```
 and also deletes the object containing the [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey").

[`Model.delete()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.delete "django.db.models.Model.delete") isn’t called on related models, but the [`pre_delete`](https://docs.djangoproject.com/en/6.0/ref/signals/#django.db.models.signals.pre_delete "django.db.models.signals.pre_delete") and [`post_delete`](https://docs.djangoproject.com/en/6.0/ref/signals/#django.db.models.signals.post_delete "django.db.models.signals.post_delete") signals are sent for all deleted objects.

*   PROTECT[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/deletion.py#L34)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.PROTECT "Link to this definition")
Prevent deletion of the referenced object by raising [`ProtectedError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.models.ProtectedError "django.db.models.ProtectedError"), a subclass of [`django.db.IntegrityError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.IntegrityError "django.db.IntegrityError").

*   RESTRICT[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/deletion.py#L47)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.RESTRICT "Link to this definition")
Prevent deletion of the referenced object by raising [`RestrictedError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.models.RestrictedError "django.db.models.RestrictedError") (a subclass of [`django.db.IntegrityError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.IntegrityError "django.db.IntegrityError")). Unlike [`PROTECT`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.PROTECT "django.db.models.PROTECT"), deletion of the referenced object is allowed if it also references a different object that is being deleted in the same operation, but via a [`CASCADE`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CASCADE "django.db.models.CASCADE") relationship.

Consider this set of models:

class Artist(models.Model):
    name = models.CharField(max_length=10)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)  
`Artist` can be deleted even if that implies deleting an `Album` which is referenced by a `Song`, because `Song` also references `Artist` itself through a cascading relationship. For example:

>>> artist_one = Artist.objects.create(name="artist one")
>>> artist_two = Artist.objects.create(name="artist two")
>>> album_one = Album.objects.create(artist=artist_one)
>>> album_two = Album.objects.create(artist=artist_two)
>>> song_one = Song.objects.create(artist=artist_one, album=album_one)
>>> song_two = Song.objects.create(artist=artist_one, album=album_two)
>>> album_one.delete()
# Raises RestrictedError.
>>> artist_two.delete()
# Raises RestrictedError.
>>> artist_one.delete()
(4, {'Song': 2, 'Album': 1, 'Artist': 1})  
*   SET_NULL[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/deletion.py#L69)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.SET_NULL "Link to this definition")
Set the [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") null; this is only possible if [`null`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null") is `True`.

*   SET_DEFAULT[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/deletion.py#L76)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.SET_DEFAULT "Link to this definition")
Set the [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") to its default value; a default for the [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") must be set.

*   SET()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/deletion.py#L52)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.SET "Link to this definition")
Set the [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") to the value passed to [`SET()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.SET "django.db.models.SET"), or if a callable is passed in, the result of calling it. In most cases, passing a callable will be necessary to avoid executing queries at the time your `models.py` is imported:

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]

class MyModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )  
*   DO_NOTHING[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/deletion.py#L80)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DO_NOTHING "Link to this definition")
Take no action. If your database backend enforces referential integrity, this will cause an [`IntegrityError`](https://docs.djangoproject.com/en/6.0/ref/exceptions/#django.db.IntegrityError "django.db.IntegrityError") unless you manually add an SQL `ON DELETE` constraint to the database field.

ForeignKey.limit_choices_to[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.limit_choices_to "Link to this definition")
Sets a limit to the available choices for this field when this field is rendered using a `ModelForm` or the admin (by default, all objects in the queryset are available to choose). Either a dictionary, a [`Q`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.Q "django.db.models.Q") object, or a callable returning a dictionary or [`Q`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.Q "django.db.models.Q") object can be used.

For example:

staff_member = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    limit_choices_to={"is_staff": True},
)

causes the corresponding field on the `ModelForm` to list only `User` instances that have `is_staff=True`. This may be helpful in the Django admin.

The callable form can be helpful, for instance, when used in conjunction with the Python `datetime` module to limit selections by date range. For example:

def limit_pub_date_choices():
    return {"pub_date__lte": datetime.date.today()}

limit_choices_to = limit_pub_date_choices

If `limit_choices_to` is or returns a [`Q object`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.Q "django.db.models.Q"), which is useful for [complex queries](https://docs.djangoproject.com/en/6.0/topics/db/queries/#complex-lookups-with-q), then it will only have an effect on the choices available in the admin when the field is not listed in [`raw_id_fields`](https://docs.djangoproject.com/en/6.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.raw_id_fields "django.contrib.admin.ModelAdmin.raw_id_fields") in the `ModelAdmin` for the model.

Note

If a callable is used for `limit_choices_to`, it will be invoked every time a new form is instantiated. It may also be invoked when a model is validated, for example by management commands or the admin. The admin constructs querysets to validate its form inputs in various edge cases multiple times, so there is a possibility your callable may be invoked several times.

ForeignKey.related_name[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_name "Link to this definition")
The name to use for the relation from the related object back to this one. It’s also the default value for [`related_query_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_query_name "django.db.models.ForeignKey.related_query_name") (the name to use for the reverse filter name from the target model). See the [related objects documentation](https://docs.djangoproject.com/en/6.0/topics/db/queries/#backwards-related-objects) for a full explanation and example. Note that you must set this value when defining relations on [abstract models](https://docs.djangoproject.com/en/6.0/topics/db/models/#abstract-base-classes); and when you do so [some special syntax](https://docs.djangoproject.com/en/6.0/topics/db/models/#abstract-related-name) is available.

If you’d prefer Django not to create a backwards relation, set `related_name` to `'+'` or end it with `'+'`. For example, this will ensure that the `User` model won’t have a backwards relation to this model:

user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="+",
)

ForeignKey.related_query_name[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_query_name "Link to this definition")
The name to use for the reverse filter name from the target model. It defaults to the value of [`related_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") or [`default_related_name`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.default_related_name "django.db.models.Options.default_related_name") if set, otherwise it defaults to the name of the model:

# Declare the ForeignKey with related_query_name
class Tag(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="tags",
        related_query_name="tag",
    )
    name = models.CharField(max_length=255)

# That's now the name of the reverse filter
Article.objects.filter(tag__name="important")

Like [`related_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name"), `related_query_name` supports app label and class interpolation via [some special syntax](https://docs.djangoproject.com/en/6.0/topics/db/models/#abstract-related-name).

ForeignKey.to_field[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.to_field "Link to this definition")
The field on the related object that the relation is to. By default, Django uses the primary key of the related object. If you reference a different field, that field must have `unique=True`.

ForeignKey.db_constraint[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.db_constraint "Link to this definition")
Controls whether or not a constraint should be created in the database for this foreign key. The default is `True`, and that’s almost certainly what you want; setting this to `False` can be very bad for data integrity. That said, here are some scenarios where you might want to do this:

*   You have legacy data that is not valid.

*   You’re sharding your database.

If this is set to `False`, accessing a related object that doesn’t exist will raise its `DoesNotExist` exception.

ForeignKey.swappable[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.swappable "Link to this definition")
Controls the migration framework’s reaction if this [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") is pointing at a swappable model. If it is `True` - the default - then if the [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") is pointing at a model which matches the current value of `settings.AUTH_USER_MODEL` (or another swappable model setting) the relationship will be stored in the migration using a reference to the setting, not to the model directly.

You only want to override this to be `False` if you are sure your model should always point toward the swapped-in model - for example, if it is a profile model designed specifically for your custom user model.

Setting it to `False` does not mean you can reference a swappable model even if it is swapped out - `False` means that the migrations made with this [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") will always reference the exact model you specify (so it will fail hard if the user tries to run with a `User` model you don’t support, for example).

If in doubt, leave it to its default of `True`.

### `ManyToManyField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#manytomanyfield "Link to this heading")

_class_ ManyToManyField(_to_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/related.py#L1364)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "Link to this definition")
A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does for [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), including [recursive](https://docs.djangoproject.com/en/6.0/ref/models/fields/#recursive-relationships) and [lazy](https://docs.djangoproject.com/en/6.0/ref/models/fields/#lazy-relationships) relationships.

Related objects can be added, removed, or created with the field’s [`RelatedManager`](https://docs.djangoproject.com/en/6.0/ref/models/relations/#django.db.models.fields.related.RelatedManager "django.db.models.fields.related.RelatedManager").

#### Database Representation[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#id2 "Link to this heading")

Behind the scenes, Django creates an intermediary join table to represent the many-to-many relationship. By default, this table name is generated using the name of the many-to-many field and the name of the table for the model that contains it. Since some databases don’t support table names above a certain length, these table names will be automatically truncated and a uniqueness hash will be used, e.g. `author_books_9cdf`. You can manually provide the name of the join table using the [`db_table`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.db_table "django.db.models.ManyToManyField.db_table") option.

#### Arguments[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#manytomany-arguments "Link to this heading")

[`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") accepts an extra set of arguments – all optional – that control how the relationship functions.

ManyToManyField.related_name[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.related_name "Link to this definition")
Same as [`ForeignKey.related_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name").

ManyToManyField.related_query_name[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.related_query_name "Link to this definition")
Same as [`ForeignKey.related_query_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_query_name "django.db.models.ForeignKey.related_query_name").

ManyToManyField.limit_choices_to[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.limit_choices_to "Link to this definition")
Same as [`ForeignKey.limit_choices_to`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.limit_choices_to "django.db.models.ForeignKey.limit_choices_to").

ManyToManyField.symmetrical[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.symmetrical "Link to this definition")
Only used in the definition of ManyToManyFields on self. Consider the following model:

from django.db import models

class Person(models.Model):
    friends = models.ManyToManyField("self")

When Django processes this model, it identifies that it has a [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") on itself, and as a result, it doesn’t add a `person_set` attribute to the `Person` class. Instead, the [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") is assumed to be symmetrical – that is, if I am your friend, then you are my friend.

If you do not want symmetry in many-to-many relationships with `self`, set [`symmetrical`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.symmetrical "django.db.models.ManyToManyField.symmetrical") to `False`. This will force Django to add the descriptor for the reverse relationship, allowing [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") relationships to be non-symmetrical.

ManyToManyField.through[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.through "Link to this definition")
Django will automatically generate a table to manage many-to-many relationships. However, if you want to manually specify the intermediary table, you can use the [`through`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.through "django.db.models.ManyToManyField.through") option to specify the Django model that represents the intermediate table that you want to use.

The `through` model can be specified using either the model class directly or a [lazy reference](https://docs.djangoproject.com/en/6.0/ref/models/fields/#lazy-relationships) to the model class.

The most common use for this option is when you want to associate [extra data with a many-to-many relationship](https://docs.djangoproject.com/en/6.0/topics/db/models/#intermediary-manytomany).

Note

Recursive relationships using an intermediary model can’t determine the reverse accessors names, as they would be the same. You need to set a [`related_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") to at least one of them. If you’d prefer Django not to create a backwards relation, set `related_name` to `'+'`.

Foreign key order in intermediary models

When defining an asymmetric many-to-many relationship from a model to itself using an intermediary model without defining [`through_fields`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.through_fields "django.db.models.ManyToManyField.through_fields"), the first foreign key in the intermediary model will be treated as representing the source side of the `ManyToManyField`, and the second as the target side. For example:

from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    clients = models.ManyToManyField(
        "self", symmetrical=False, related_name="suppliers", through="Supply"
    )

class Supply(models.Model):
    supplier = models.ForeignKey(
        Manufacturer, models.CASCADE, related_name="supplies_given"
    )
    client = models.ForeignKey(
        Manufacturer, models.CASCADE, related_name="supplies_received"
    )
    product = models.CharField(max_length=255)

Here, the `Manufacturer` model defines the many-to-many relationship with `clients` in its role as a supplier. Therefore, the `supplier` foreign key (the source) must come before the `client` foreign key (the target) in the intermediary `Supply` model.

Specifying [`through_fields=("supplier", "client")`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.through_fields "django.db.models.ManyToManyField.through_fields") on the `ManyToManyField` makes the order of foreign keys on the `through` model irrelevant.

If you don’t specify an explicit `through` model, there is still an implicit `through` model class you can use to directly access the table created to hold the association. It has three fields to link the models, a primary key and two foreign keys. There is a unique constraint on the two foreign keys.

If the source and target models differ, the following fields are generated:

*   `id`: the primary key of the relation.

*   `<containing_model>_id`: the `id` of the model that declares the `ManyToManyField`.

*   `<other_model>_id`: the `id` of the model that the `ManyToManyField` points to.

If the `ManyToManyField` points from and to the same model, the following fields are generated:

*   `id`: the primary key of the relation.

*   `from_<model>_id`: the `id` of the instance which points at the model (i.e. the source instance).

*   `to_<model>_id`: the `id` of the instance to which the relationship points (i.e. the target model instance).

This class can be used to query associated records for a given model instance like a normal model:

Model.m2mfield.through.objects.all()

ManyToManyField.through_fields[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.through_fields "Link to this definition")
Only used when a custom intermediary model is specified. Django will normally determine which fields of the intermediary model to use in order to establish a many-to-many relationship automatically. However, consider the following models:

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through="Membership",
        through_fields=("group", "person"),
    )

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)

`Membership` has _two_ foreign keys to `Person` (`person` and `inviter`), which makes the relationship ambiguous and Django can’t know which one to use. In this case, you must explicitly specify which foreign keys Django should use using `through_fields`, as in the example above.

`through_fields` accepts a 2-tuple `('field1', 'field2')`, where `field1` is the name of the foreign key to the model the [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") is defined on (`group` in this case), and `field2` the name of the foreign key to the target model (`person` in this case).

When you have more than one foreign key on an intermediary model to any (or even both) of the models participating in a many-to-many relationship, you _must_ specify `through_fields`. This also applies to [recursive relationships](https://docs.djangoproject.com/en/6.0/ref/models/fields/#recursive-relationships) when an intermediary model is used and there are more than two foreign keys to the model, or you want to explicitly specify which two Django should use.

ManyToManyField.db_table[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.db_table "Link to this definition")
The name of the table to create for storing the many-to-many data. If this is not provided, Django will assume a default name based upon the names of: the table for the model defining the relationship and the name of the field itself.

ManyToManyField.db_constraint[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.db_constraint "Link to this definition")
Controls whether or not constraints should be created in the database for the foreign keys in the intermediary table. The default is `True`, and that’s almost certainly what you want; setting this to `False` can be very bad for data integrity. That said, here are some scenarios where you might want to do this:

*   You have legacy data that is not valid.

*   You’re sharding your database.

It is an error to pass both `db_constraint` and `through`.

ManyToManyField.swappable[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.swappable "Link to this definition")
Controls the migration framework’s reaction if this [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") is pointing at a swappable model. If it is `True` - the default - then if the [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") is pointing at a model which matches the current value of `settings.AUTH_USER_MODEL` (or another swappable model setting) the relationship will be stored in the migration using a reference to the setting, not to the model directly.

You only want to override this to be `False` if you are sure your model should always point toward the swapped-in model - for example, if it is a profile model designed specifically for your custom user model.

If in doubt, leave it to its default of `True`.

[`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") does not support [`validators`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.validators "django.db.models.Field.validators").

[`null`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null") has no effect since there is no way to require a relationship at the database level.

### `OneToOneField`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#onetoonefield "Link to this heading")

_class_ OneToOneField(_to_, _on\_delete_, _parent\_link=False_, _**options_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/related.py#L1257)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.OneToOneField "Link to this definition")
A one-to-one relationship. Conceptually, this is similar to a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") with [`unique=True`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique "django.db.models.Field.unique"), but the “reverse” side of the relation will directly return a single object.

This is most useful as the primary key of a model which “extends” another model in some way; [Multi-table inheritance](https://docs.djangoproject.com/en/6.0/topics/db/models/#multi-table-inheritance) is implemented by adding an implicit one-to-one relation from the child model to the parent model, for example.

One positional argument is required: the class to which the model will be related. This works exactly the same as it does for [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), including all the options regarding [recursive](https://docs.djangoproject.com/en/6.0/ref/models/fields/#recursive-relationships) and [lazy](https://docs.djangoproject.com/en/6.0/ref/models/fields/#lazy-relationships) relationships.

If you do not specify the [`related_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_name "django.db.models.ForeignKey.related_name") argument for the `OneToOneField`, Django will use the lowercase name of the current model as default value.

With the following example:

from django.conf import settings
from django.db import models

class MySpecialUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    supervisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="supervisor_of",
    )

your resulting `User` model will have the following attributes:

>>> user = User.objects.get(pk=1)
>>> hasattr(user, "myspecialuser")
True
>>> hasattr(user, "supervisor_of")
True

A `RelatedObjectDoesNotExist` exception is raised when accessing the reverse relationship if an entry in the related table doesn’t exist. This is a subclass of the target model’s [`Model.DoesNotExist`](https://docs.djangoproject.com/en/6.0/ref/models/class/#django.db.models.Model.DoesNotExist "django.db.models.Model.DoesNotExist") exception and can be accessed as an attribute of the reverse accessor. For example, if a user doesn’t have a supervisor designated by `MySpecialUser`:

try:
    user.supervisor_of
except User.supervisor_of.RelatedObjectDoesNotExist:
    pass

Additionally, `OneToOneField` accepts all of the extra arguments accepted by [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey"), plus one extra argument:

OneToOneField.parent_link[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.OneToOneField.parent_link "Link to this definition")
When `True` and used in a model which inherits from another [concrete model](https://docs.djangoproject.com/en/6.0/glossary/#term-concrete-model), indicates that this field should be used as the link back to the parent class, rather than the extra `OneToOneField` which would normally be implicitly created by subclassing.

See [One-to-one relationships](https://docs.djangoproject.com/en/6.0/topics/db/examples/one_to_one/) for usage examples of `OneToOneField`.

### Lazy relationships[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#lazy-relationships "Link to this heading")

Lazy relationships allow referencing models by their names (as strings) or creating recursive relationships. Strings can be used as the first argument in any relationship field to reference models lazily. A lazy reference can be either [recursive](https://docs.djangoproject.com/en/6.0/ref/models/fields/#recursive-relationships), [relative](https://docs.djangoproject.com/en/6.0/ref/models/fields/#relative-relationships) or [absolute](https://docs.djangoproject.com/en/6.0/ref/models/fields/#absolute-relationships).

#### Recursive[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#recursive "Link to this heading")

To define a relationship where a model references itself, use `"self"` as the first argument of the relationship field:

from django.db import models

class Manufacturer(models.Model):
    name = models.TextField()
    suppliers = models.ManyToManyField("self", symmetrical=False)

When used in an [abstract model](https://docs.djangoproject.com/en/6.0/topics/db/models/#abstract-base-classes), the recursive relationship resolves such that each concrete subclass references itself.

#### Relative[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#relative "Link to this heading")

When a relationship needs to be created with a model that has not been defined yet, it can be referenced by its name rather than the model object itself:

from django.db import models

class Car(models.Model):
    manufacturer = models.ForeignKey(
        "Manufacturer",
        on_delete=models.CASCADE,
    )

class Manufacturer(models.Model):
    name = models.TextField()
    suppliers = models.ManyToManyField("self", symmetrical=False)

Relationships defined this way on [abstract models](https://docs.djangoproject.com/en/6.0/topics/db/models/#abstract-base-classes) are resolved when the model is subclassed as a concrete model and are not relative to the abstract model’s `app_label`:

`products/models.py`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#id5 "Link to this code")

from django.db import models

class AbstractCar(models.Model):
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)

    class Meta:
        abstract = True

`production/models.py`[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#id6 "Link to this code")

from django.db import models
from products.models import AbstractCar

class Manufacturer(models.Model):
    name = models.TextField()

class Car(AbstractCar):
    pass

In this example, the `Car.manufacturer` relationship will resolve to `production.Manufacturer`, as it points to the concrete model defined within the `production/models.py` file.

Reusable models with relative references

Relative references allow the creation of reusable abstract models with relationships that can resolve to different implementations of the referenced models in various subclasses across different applications.

#### Absolute[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#absolute "Link to this heading")

Absolute references specify a model using its `app_label` and class name, allowing for model references across different applications. This type of lazy relationship can also help resolve circular imports.

For example, if the `Manufacturer` model is defined in another application called `thirdpartyapp`, it can be referenced as:

class Car(models.Model):
    manufacturer = models.ForeignKey(
        "thirdpartyapp.Manufacturer",
        on_delete=models.CASCADE,
    )

Absolute references always point to the same model, even when used in an [abstract model](https://docs.djangoproject.com/en/6.0/topics/db/models/#abstract-base-classes).

Field API reference[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-api-reference "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

_class_ Field[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L119)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field "Link to this definition")
`Field` is an abstract class that represents a database table column. Django uses fields to create the database table ([`db_type()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_type "django.db.models.Field.db_type")), to map Python types to database ([`get_prep_value()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_prep_value "django.db.models.Field.get_prep_value")) and vice-versa ([`from_db_value()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.from_db_value "django.db.models.Field.from_db_value")).

A field is thus a fundamental piece in different Django APIs, notably, [`models`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model "django.db.models.Model") and [`querysets`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet").

In models, a field is instantiated as a class attribute and represents a particular table column, see [Models](https://docs.djangoproject.com/en/6.0/topics/db/models/). It has attributes such as [`null`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null") and [`unique`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.unique "django.db.models.Field.unique"), and methods that Django uses to map the field value to database-specific values.

A `Field` is a subclass of [`RegisterLookupMixin`](https://docs.djangoproject.com/en/6.0/ref/models/lookups/#django.db.models.lookups.RegisterLookupMixin "django.db.models.lookups.RegisterLookupMixin") and thus both [`Transform`](https://docs.djangoproject.com/en/6.0/ref/models/lookups/#django.db.models.Transform "django.db.models.Transform") and [`Lookup`](https://docs.djangoproject.com/en/6.0/ref/models/lookups/#django.db.models.Lookup "django.db.models.Lookup") can be registered on it to be used in `QuerySet`s (e.g. `field_name__exact="foo"`). All [built-in lookups](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#field-lookups) are registered by default.

All of Django’s built-in fields, such as [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField"), are particular implementations of `Field`. If you need a custom field, you can either subclass any of the built-in fields or write a `Field` from scratch. In either case, see [How to create custom model fields](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/).

description[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.description "Link to this definition")
A verbose description of the field, e.g. for the [`django.contrib.admindocs`](https://docs.djangoproject.com/en/6.0/ref/contrib/admin/admindocs/#module-django.contrib.admindocs "django.contrib.admindocs: Django's admin documentation generator.") application.

The description can be of the form:

description = _("String (up to %(max_length)s)")

where the arguments are interpolated from the field’s `__dict__`.

descriptor_class[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.descriptor_class "Link to this definition")
A class implementing the [descriptor protocol](https://docs.python.org/3/reference/datamodel.html#descriptors "(in Python v3.14)") that is instantiated and assigned to the model instance attribute. The constructor must accept a single argument, the `Field` instance. Overriding this class attribute allows for customizing the get and set behavior.

To map a `Field` to a database-specific type, Django exposes several methods:

get_internal_type()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L983)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_internal_type "Link to this definition")
Returns a string naming this field for backend specific purposes. By default, it returns the class name.

See [Emulating built-in field types](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/#emulating-built-in-field-types) for usage in custom fields.

db_type(_connection_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L857)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_type "Link to this definition")
Returns the database column data type for the [`Field`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field "django.db.models.Field"), taking into account the `connection`.

See [Custom database types](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/#custom-database-types) for usage in custom fields.

rel_db_type(_connection_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L888)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.rel_db_type "Link to this definition")
Returns the database column data type for fields such as `ForeignKey` and `OneToOneField` that point to the [`Field`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field "django.db.models.Field"), taking into account the `connection`.

See [Custom database types](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/#custom-database-types) for usage in custom fields.

There are three main situations where Django needs to interact with the database backend and fields:

*   when it queries the database (Python value -> database backend value)

*   when it loads data from the database (database backend value -> Python value)

*   when it saves to the database (Python value -> database backend value)

When querying, [`get_db_prep_value()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_db_prep_value "django.db.models.Field.get_db_prep_value") and [`get_prep_value()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_prep_value "django.db.models.Field.get_prep_value") are used:

get_prep_value(_value_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L990)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_prep_value "Link to this definition")
`value` is the current value of the model’s attribute, and the method should return data in a format that has been prepared for use as a parameter in a query.

See [Converting Python objects to query values](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/#converting-python-objects-to-query-values) for usage.

get_db_prep_value(_value_, _connection_, _prepared=False_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L996)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_db_prep_value "Link to this definition")
Converts `value` to a backend-specific value. By default it returns `value` if `prepared=True`, and [`get_prep_value(value)`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_prep_value "django.db.models.Field.get_prep_value") otherwise.

See [Converting query values to database values](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/#converting-query-values-to-database-values) for usage.

When loading data, [`from_db_value()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.from_db_value "django.db.models.Field.from_db_value") is used:

from_db_value(_value_, _expression_, _connection_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.from_db_value "Link to this definition")
Converts a value as returned by the database to a Python object. It is the reverse of [`get_prep_value()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_prep_value "django.db.models.Field.get_prep_value").

This method is not used for most built-in fields as the database backend already returns the correct Python type, or the backend itself does the conversion.

`expression` is the same as `self`.

See [Converting values to Python objects](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/#converting-values-to-python-objects) for usage.

Note

For performance reasons, `from_db_value` is not implemented as a no-op on fields which do not require it (all Django fields). Consequently you may not call `super` in your definition.

When saving, [`pre_save()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.pre_save "django.db.models.Field.pre_save") and [`get_db_prep_save()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_db_prep_save "django.db.models.Field.get_db_prep_save") are used:

get_db_prep_save(_value_, _connection_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1007)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_db_prep_save "Link to this definition")
Same as the [`get_db_prep_value()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_db_prep_value "django.db.models.Field.get_db_prep_value"), but called when the field value must be _saved_ to the database. By default returns [`get_db_prep_value()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_db_prep_value "django.db.models.Field.get_db_prep_value").

pre_save(_model\_instance_, _add_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L986)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.pre_save "Link to this definition")
Method called prior to [`get_db_prep_save()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.get_db_prep_save "django.db.models.Field.get_db_prep_save") to prepare the value before being saved (e.g. for [`DateField.auto_now`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField.auto_now "django.db.models.DateField.auto_now")).

`model_instance` is the instance this field belongs to and `add` is whether the instance is being saved to the database for the first time.

It should return the value of the appropriate attribute from `model_instance` for this field. The attribute name is in `self.attname` (this is set up by [`Field`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field "django.db.models.Field")).

See [Preprocessing values before saving](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/#preprocessing-values-before-saving) for usage.

Fields often receive their values as a different type, either from serialization or from forms.

to_python(_value_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L758)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.to_python "Link to this definition")
Converts the value into the correct Python object. It acts as the reverse of [`value_to_string()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.value_to_string "django.db.models.Field.value_to_string"), and is also called in [`clean()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.clean "django.db.models.Model.clean").

See [Converting values to Python objects](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/#converting-values-to-python-objects) for usage.

Besides saving to the database, the field also needs to know how to serialize its value:

value_from_object(_obj_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1149)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.value_from_object "Link to this definition")
Returns the field’s value for the given model instance.

This method is often used by [`value_to_string()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.value_to_string "django.db.models.Field.value_to_string").

value_to_string(_obj_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1085)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.value_to_string "Link to this definition")
Converts `obj` to a string. Used to serialize the value of the field.

See [Converting field data for serialization](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/#converting-model-field-to-serialization) for usage.

When using [`model forms`](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm"), the `Field` needs to know which form field it should be represented by:

formfield(_form\_class=None_, _choices\_form\_class=None_, _**kwargs_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L1100)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.formfield "Link to this definition")
Returns the default [`django.forms.Field`](https://docs.djangoproject.com/en/6.0/ref/forms/fields/#django.forms.Field "django.forms.Field") of this field for [`ModelForm`](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm").

If [`formfield()`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.formfield "django.db.models.Field.formfield") is overridden to return `None`, this field is excluded from the [`ModelForm`](https://docs.djangoproject.com/en/6.0/topics/forms/modelforms/#django.forms.ModelForm "django.forms.ModelForm").

By default, if both `form_class` and `choices_form_class` are `None`, it uses [`CharField`](https://docs.djangoproject.com/en/6.0/ref/forms/fields/#django.forms.CharField "django.forms.CharField"). If the field has [`choices`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.choices "django.db.models.Field.choices") and `choices_form_class` isn’t specified, it uses [`TypedChoiceField`](https://docs.djangoproject.com/en/6.0/ref/forms/fields/#django.forms.TypedChoiceField "django.forms.TypedChoiceField").

See [Specifying the form field for a model field](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/#specifying-form-field-for-model-field) for usage.

deconstruct()[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/fields/__init__.py#L570)[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.deconstruct "Link to this definition")
Returns a 4-tuple with enough information to recreate the field:

1.   The name of the field on the model.

2.   The import path of the field (e.g. `"django.db.models.IntegerField"`). This should be the most portable version, so less specific may be better.

3.   A list of positional arguments.

4.   A dict of keyword arguments.

This method must be added to fields prior to 1.7 to migrate its data using [Migrations](https://docs.djangoproject.com/en/6.0/topics/migrations/).

Registering and fetching lookups[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#registering-and-fetching-lookups "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

`Field` implements the [lookup registration API](https://docs.djangoproject.com/en/6.0/ref/models/lookups/#lookup-registration-api). The API can be used to customize which lookups are available for a field class and its instances, and how lookups are fetched from a field.

Field attribute reference[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-attribute-reference "Link to this heading")
=======================================================================================================================================

Every `Field` instance contains several attributes that allow introspecting its behavior. Use these attributes instead of `isinstance` checks when you need to write code that depends on a field’s functionality. These attributes can be used together with the [Model._meta API](https://docs.djangoproject.com/en/6.0/ref/models/meta/#model-meta-field-api) to narrow down a search for specific field types. Custom model fields should implement these flags.

Attributes for fields[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#attributes-for-fields "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

Field.auto_created[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.auto_created "Link to this definition")
Boolean flag that indicates if the field was automatically created, such as the `OneToOneField` used by model inheritance.

Field.concrete[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.concrete "Link to this definition")
Boolean flag that indicates if the field has a database column associated with it.

Field.hidden[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.hidden "Link to this definition")
Boolean flag that indicates if a field is hidden and should not be returned by [`Options.get_fields()`](https://docs.djangoproject.com/en/6.0/ref/models/meta/#django.db.models.options.Options.get_fields "django.db.models.options.Options.get_fields") by default. An example is the reverse field for a [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey "django.db.models.ForeignKey") with a `related_name` that starts with `'+'`.

Field.is_relation[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.is_relation "Link to this definition")
Boolean flag that indicates if a field contains references to one or more other models for its functionality (e.g. `ForeignKey`, `ManyToManyField`, `OneToOneField`, etc.).

Field.model[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.model "Link to this definition")
Returns the model on which the field is defined. If a field is defined on a superclass of a model, `model` will refer to the superclass, not the class of the instance.

Attributes for fields with relations[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#attributes-for-fields-with-relations "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

These attributes are used to query for the cardinality and other details of a relation. These attribute are present on all fields; however, they will only have boolean values (rather than `None`) if the field is a relation type ([`Field.is_relation=True`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.is_relation "django.db.models.Field.is_relation")).

Field.many_to_many[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.many_to_many "Link to this definition")
Boolean flag that is `True` if the field has a many-to-many relation; `False` otherwise. The only field included with Django where this is `True` is `ManyToManyField`.

Field.many_to_one[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.many_to_one "Link to this definition")
Boolean flag that is `True` if the field has a many-to-one relation, such as a `ForeignKey`; `False` otherwise.

Field.one_to_many[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.one_to_many "Link to this definition")
Boolean flag that is `True` if the field has a one-to-many relation, such as a `GenericRelation` or the reverse of a `ForeignKey`; `False` otherwise.

Field.one_to_one[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.one_to_one "Link to this definition")
Boolean flag that is `True` if the field has a one-to-one relation, such as a `OneToOneField`; `False` otherwise.

Field.related_model[¶](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.related_model "Link to this definition")
Points to the model the field relates to. For example, `Author` in `ForeignKey(Author, on_delete=models.CASCADE)`. The `related_model` for a `GenericForeignKey` is always `None`.

Previous page and next page

[Models](https://docs.djangoproject.com/en/6.0/ref/models/)

[Model index reference](https://docs.djangoproject.com/en/6.0/ref/models/indexes/)

[Back to Top](https://docs.djangoproject.com/en/6.0/ref/models/fields/#top)

Additional Information
----------------------

### Support Django!

![Image 1: Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

*   [Meros, Smith, Lazzara, Brennan & Brennan, P.A. donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Contents

*   [Model field reference](https://docs.djangoproject.com/en/6.0/ref/models/fields/#)
    *   [Field options](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-options)
        *   [`null`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#null)
        *   [`blank`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#blank)
        *   [`choices`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#choices)
            *   [Enumeration types](https://docs.djangoproject.com/en/6.0/ref/models/fields/#enumeration-types)

        *   [`db_column`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#db-column)
        *   [`db_comment`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#db-comment)
        *   [`db_default`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#db-default)
        *   [`db_index`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#db-index)
        *   [`db_tablespace`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#db-tablespace)
        *   [`default`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#default)
        *   [`editable`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#editable)
        *   [`error_messages`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#error-messages)
        *   [`help_text`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#help-text)
        *   [`primary_key`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#primary-key)
        *   [`unique`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#unique)
        *   [`unique_for_date`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#unique-for-date)
        *   [`unique_for_month`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#unique-for-month)
        *   [`unique_for_year`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#unique-for-year)
        *   [`verbose_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#verbose-name)
        *   [`validators`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#validators)

    *   [Field types](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-types)
        *   [`AutoField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#autofield)
        *   [`BigAutoField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#bigautofield)
        *   [`BigIntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#bigintegerfield)
        *   [`BinaryField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#binaryfield)
        *   [`BooleanField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#booleanfield)
        *   [`CompositePrimaryKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#compositeprimarykey)
        *   [`CharField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#charfield)
        *   [`DateField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#datefield)
        *   [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#datetimefield)
        *   [`DecimalField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#decimalfield)
        *   [`DurationField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#durationfield)
        *   [`EmailField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#emailfield)
        *   [`FileField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#filefield)
            *   [`FileField` and `FieldFile`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#filefield-and-fieldfile)

        *   [`FilePathField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#filepathfield)
        *   [`FloatField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#floatfield)
        *   [`GeneratedField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#generatedfield)
        *   [`GenericIPAddressField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#genericipaddressfield)
        *   [`ImageField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#imagefield)
        *   [`IntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#integerfield)
        *   [`JSONField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#jsonfield)
        *   [`PositiveBigIntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#positivebigintegerfield)
        *   [`PositiveIntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#positiveintegerfield)
        *   [`PositiveSmallIntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#positivesmallintegerfield)
        *   [`SlugField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#slugfield)
        *   [`SmallAutoField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#smallautofield)
        *   [`SmallIntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#smallintegerfield)
        *   [`TextField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#textfield)
        *   [`TimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#timefield)
        *   [`URLField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#urlfield)
        *   [`UUIDField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#uuidfield)

    *   [Relationship fields](https://docs.djangoproject.com/en/6.0/ref/models/fields/#module-django.db.models.fields.related)
        *   [`ForeignKey`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#foreignkey)
            *   [Database Representation](https://docs.djangoproject.com/en/6.0/ref/models/fields/#database-representation)
            *   [Arguments](https://docs.djangoproject.com/en/6.0/ref/models/fields/#arguments)

        *   [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#manytomanyfield)
            *   [Database Representation](https://docs.djangoproject.com/en/6.0/ref/models/fields/#id2)
            *   [Arguments](https://docs.djangoproject.com/en/6.0/ref/models/fields/#manytomany-arguments)

        *   [`OneToOneField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#onetoonefield)
        *   [Lazy relationships](https://docs.djangoproject.com/en/6.0/ref/models/fields/#lazy-relationships)
            *   [Recursive](https://docs.djangoproject.com/en/6.0/ref/models/fields/#recursive)
            *   [Relative](https://docs.djangoproject.com/en/6.0/ref/models/fields/#relative)
            *   [Absolute](https://docs.djangoproject.com/en/6.0/ref/models/fields/#absolute)

    *   [Field API reference](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-api-reference)
    *   [Registering and fetching lookups](https://docs.djangoproject.com/en/6.0/ref/models/fields/#registering-and-fetching-lookups)

*   [Field attribute reference](https://docs.djangoproject.com/en/6.0/ref/models/fields/#field-attribute-reference)
    *   [Attributes for fields](https://docs.djangoproject.com/en/6.0/ref/models/fields/#attributes-for-fields)
    *   [Attributes for fields with relations](https://docs.djangoproject.com/en/6.0/ref/models/fields/#attributes-for-fields-with-relations)

### Browse

*   Prev: [Models](https://docs.djangoproject.com/en/6.0/ref/models/)
*   Next: [Model index reference](https://docs.djangoproject.com/en/6.0/ref/models/indexes/)
*   [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
*   [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
*   [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)

### You are here:

*   [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    *   [API Reference](https://docs.djangoproject.com/en/6.0/ref/)
        *   [Models](https://docs.djangoproject.com/en/6.0/ref/models/)
            *   Model field reference

### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)Try the FAQ — it's got answers to many common questions.[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)Handy when looking for specific information.[Django Discord Server](https://chat.djangoproject.com/)Join the Django Discord Community.[Official Django Forum](https://forum.djangoproject.com/)Join the community on the Django Forum.[Ticket tracker](https://code.djangoproject.com/)Report bugs with Django or Django documentation in our ticket tracker.
### Download:

Offline (Django 6.0): [HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) | [PDF](https://media.readthedocs.org/pdf/django/6.0.x/django.pdf) | [ePub](https://media.readthedocs.org/epub/django/6.0.x/django.epub)

 Provided by [Read the Docs](https://readthedocs.org/).

### Diamond and Platinum Members

[![Image 2: JetBrains](https://media.djangoproject.com/cache/c0/ea/c0ea128467983e64aab91cd27e7918c0.png)](https://jb.gg/ybja10 "JetBrains")

*   **JetBrains**
*   [JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.](https://jb.gg/ybja10 "JetBrains")

[![Image 3: Sentry](https://media.djangoproject.com/cache/7a/f9/7af9c770dc49465739a82c91a0eb3d51.png)](https://sentry.io/for/django/ "Sentry")

*   **Sentry**
*   [Monitor your Django Code Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.](https://sentry.io/for/django/ "Sentry")

[![Image 4: Kraken Tech](https://media.djangoproject.com/cache/71/4b/714b3473ed0cf3665f6b894d3be9491e.png)](https://kraken.tech/ "Kraken Tech")

*   **Kraken Tech**
*   [Kraken is the most-loved operating system for energy. Powered by our Utility-Grade AI™ and deep industry know-how, we help utilities transform their technology and operations so they can lead the energy transition. Delivering better outcomes from generation through distribution to supply, Kraken powers 70+ million accounts worldwide, and is on a mission to make a big, green dent in the universe.](https://kraken.tech/ "Kraken Tech")

Django Links
------------

### Learn More

*   [About Django](https://www.djangoproject.com/start/overview/)
*   [Getting Started with Django](https://www.djangoproject.com/start/)
*   [Team Organization](https://www.djangoproject.com/foundation/teams/)
*   [Django Software Foundation](https://www.djangoproject.com/foundation/)
*   [Code of Conduct](https://www.djangoproject.com/conduct/)
*   [Diversity Statement](https://www.djangoproject.com/diversity/)

### Get Involved

*   [Join a Group](https://www.djangoproject.com/community/)
*   [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
*   [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
*   [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
*   [Individual membership](https://www.djangoproject.com/foundation/individual-members/)

### Get Help

*   [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
*   [Django Discord](https://chat.djangoproject.com/)
*   [Official Django Forum](https://forum.djangoproject.com/)

### Follow Us

*   [GitHub](https://github.com/django)
*   [X](https://x.com/djangoproject)
*   [Fediverse (Mastodon)](https://fosstodon.org/@django)
*   [Bluesky](https://bsky.app/profile/djangoproject.com)
*   [LinkedIn](https://www.linkedin.com/company/django-software-foundation)
*   [News RSS](https://www.djangoproject.com/rss/weblog/)

### Support Us

*   [Sponsor Django](https://www.djangoproject.com/fundraising/)
*   [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
*   [Official merchandise store](https://django.threadless.com/)
*   [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)

[Django](https://www.djangoproject.com/)

*   Hosting by[In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
*   Design by[Threespot](https://www.threespot.com/)&[andrevv](http://andrevv.com/)

© 2005-2026 [Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.
