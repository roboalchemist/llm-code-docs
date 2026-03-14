# Source: https://docs.djangoproject.com/en/6.0/ref/models/expressions/

Title: Query Expressions | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/models/expressions/

Markdown Content:
Query expressions describe a value or a computation that can be used as part of an update, create, filter, order by, annotation, or aggregate. When an expression outputs a boolean value, it may be used directly in filters. There are a number of built-in expressions (documented below) that can be used to help you write queries. Expressions can be combined, or in some cases nested, to form more complex computations.

Supported arithmetic[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#supported-arithmetic "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

Django supports negation, addition, subtraction, multiplication, division, modulo arithmetic, and the power operator on query expressions, using Python constants, variables, and even other expressions.

Output field[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#output-field "Link to this heading")
------------------------------------------------------------------------------------------------------------------

Many of the expressions documented in this section support an optional `output_field` parameter. If given, Django will load the value into that field after retrieving it from the database.

`output_field` takes a model field instance, like `IntegerField()` or `BooleanField()`. Usually, the field doesn’t need any arguments, like `max_length`, since field arguments relate to data validation which will not be performed on the expression’s output value.

`output_field` is only required when Django is unable to automatically determine the result’s field type, such as complex expressions that mix field types. For example, adding a `DecimalField()` and a `FloatField()` requires an output field, like `output_field=FloatField()`.

`output_field` also allows using custom fields that perform type conversions outside a specific model field context. For example, if you frequently need to perform date arithmetic with `timedelta`, you can create a custom field that handles the conversion, ensuring consistent results across databases. See [How to create custom model fields](https://docs.djangoproject.com/en/6.0/howto/custom-model-fields/).

Some examples[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#some-examples "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

>>> from django.db.models import Count, F, Value
>>> from django.db.models.functions import Length, Upper
>>> from django.db.models.lookups import GreaterThan

# Find companies that have more employees than chairs.
>>> Company.objects.filter(num_employees__gt=F("num_chairs"))

# Find companies that have at least twice as many employees
# as chairs. Both the querysets below are equivalent.
>>> Company.objects.filter(num_employees__gt=F("num_chairs") * 2)
>>> Company.objects.filter(num_employees__gt=F("num_chairs") + F("num_chairs"))

# How many chairs are needed for each company to seat all employees?
>>> company = (
...     Company.objects.filter(num_employees__gt=F("num_chairs"))
...     .annotate(chairs_needed=F("num_employees") - F("num_chairs"))
...     .first()
... )
>>> company.num_employees
120
>>> company.num_chairs
50
>>> company.chairs_needed
70

# Create a new company using expressions.
>>> company = Company.objects.create(name="Google", ticker=Upper(Value("goog")))
>>> company.ticker
'GOOG'

# Annotate models with an aggregated value. Both forms
# below are equivalent.
>>> Company.objects.annotate(num_products=Count("products"))
>>> Company.objects.annotate(num_products=Count(F("products")))

# Aggregates can contain complex computations also
>>> Company.objects.annotate(num_offerings=Count(F("products") + F("services")))

# Expressions can also be used in order_by(), either directly
>>> Company.objects.order_by(Length("name").asc())
>>> Company.objects.order_by(Length("name").desc())
# or using the double underscore lookup syntax.
>>> from django.db.models import CharField
>>> from django.db.models.functions import Length
>>> CharField.register_lookup(Length)
>>> Company.objects.order_by("name__length")

# Boolean expression can be used directly in filters.
>>> from django.db.models import Exists, OuterRef
>>> Company.objects.filter(
...     Exists(Employee.objects.filter(company=OuterRef("pk"), salary__gt=10))
... )

# Lookup expressions can also be used directly in filters
>>> Company.objects.filter(GreaterThan(F("num_employees"), F("num_chairs")))
# or annotations.
>>> Company.objects.annotate(
...     need_chairs=GreaterThan(F("num_employees"), F("num_chairs")),
... )

Built-in Expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#built-in-expressions "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

Note

These expressions are defined in `django.db.models.expressions` and `django.db.models.aggregates`, but for convenience they’re available and usually imported from [`django.db.models`](https://docs.djangoproject.com/en/6.0/topics/db/models/#module-django.db.models "django.db.models").

### `F()` expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#f-expressions "Link to this heading")

_class_ F[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L878)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.F "Link to this definition")
An `F()` object represents the value of a model field, transformed value of a model field, or annotated column. It makes it possible to refer to model field values and perform database operations using them without actually having to pull them out of the database into Python memory.

Instead, Django uses the `F()` object to generate an SQL expression that describes the required operation at the database level.

Let’s try this with an example. Normally, one might do something like this:

# Tintin filed a news story!
reporter = Reporters.objects.get(name="Tintin")
reporter.stories_filed += 1
reporter.save()

Here, we have pulled the value of `reporter.stories_filed` from the database into memory and manipulated it using familiar Python operators, and then saved the object back to the database. But instead we could also have done:

from django.db.models import F

reporter = Reporters.objects.get(name="Tintin")
reporter.stories_filed = F("stories_filed") + 1
reporter.save()

Although `reporter.stories_filed = F('stories_filed') + 1` looks like a normal Python assignment of value to an instance attribute, in fact it’s an SQL construct describing an operation on the database.

When Django encounters an instance of `F()`, it overrides the standard Python operators to create an encapsulated SQL expression; in this case, one which instructs the database to increment the database field represented by `reporter.stories_filed`.

Whatever value is or was on `reporter.stories_filed`, Python never gets to know about it - it is dealt with entirely by the database. All Python does, through Django’s `F()` class, is create the SQL syntax to refer to the field and describe the operation.

As well as being used in operations on single instances as above, `F()` can be used with `update()` to perform bulk updates on a `QuerySet`. This reduces the two queries we were using above - the `get()` and the [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") - to just one:

reporter = Reporters.objects.filter(name="Tintin")
reporter.update(stories_filed=F("stories_filed") + 1)

We can also use [`update()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.update "django.db.models.query.QuerySet.update") to increment the field value on multiple objects - which could be very much faster than pulling them all into Python from the database, looping over them, incrementing the field value of each one, and saving each one back to the database:

Reporter.objects.update(stories_filed=F("stories_filed") + 1)

`F()` therefore can offer performance advantages by:

*   getting the database, rather than Python, to do work

*   reducing the number of queries some operations require

#### Slicing `F()` expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#slicing-f-expressions "Link to this heading")

For string-based fields, text-based fields, and [`ArrayField`](https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/fields/#django.contrib.postgres.fields.ArrayField "django.contrib.postgres.fields.ArrayField"), you can use Python’s array-slicing syntax. The indices are 0-based. The `step` argument to `slice` and negative indexing are not supported. For example:

>>> # Replacing a name with a substring of itself.
>>> writer = Writers.objects.get(name="Priyansh")
>>> writer.name = F("name")[1:5]
>>> writer.save()
>>> writer.name
'riya'

#### Avoiding race conditions using `F()`[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#avoiding-race-conditions-using-f "Link to this heading")

Another useful benefit of `F()` is that having the database - rather than Python - update a field’s value avoids a _race condition_.

If two Python threads execute the code in the first example above, one thread could retrieve, increment, and save a field’s value after the other has retrieved it from the database. The value that the second thread saves will be based on the original value; the work of the first thread will be lost.

If the database is responsible for updating the field, the process is more robust: it will only ever update the field based on the value of the field in the database when the [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") or `update()` is executed, rather than based on its value when the instance was retrieved.

#### `F()` assignments are refreshed after `Model.save()`[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#f-assignments-are-refreshed-after-model-save "Link to this heading")

`F()` objects assigned to model fields are refreshed from the database on [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") on backends that support it without incurring a subsequent query (SQLite, PostgreSQL, and Oracle) and deferred otherwise (MySQL or MariaDB). For example:

>>> reporter = Reporters.objects.get(name="Tintin")
>>> reporter.stories_filed = F("stories_filed") + 1
>>> reporter.save()
>>> reporter.stories_filed  # This triggers a refresh query on MySQL/MariaDB.
14 # Assuming the database value was 13 when the object was saved.

Changed in Django 6.0:

In previous versions of Django, `F()` objects were not refreshed from the database on [`save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") which resulted in them being evaluated and persisted every time the instance was saved.

#### Using `F()` in filters[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#using-f-in-filters "Link to this heading")

`F()` is also very useful in `QuerySet` filters, where they make it possible to filter a set of objects against criteria based on their field values, rather than on Python values.

This is documented in [using F() expressions in queries](https://docs.djangoproject.com/en/6.0/topics/db/queries/#using-f-expressions-in-filters).

#### Using `F()` with annotations[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#using-f-with-annotations "Link to this heading")

`F()` can be used to create dynamic fields on your models by combining different fields with arithmetic:

company = Company.objects.annotate(chairs_needed=F("num_employees") - F("num_chairs"))

If the fields that you’re combining are of different types you’ll need to tell Django what kind of field will be returned. Most expressions support [output_field](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#output-field) for this case, but since `F()` does not, you will need to wrap the expression with [`ExpressionWrapper`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.ExpressionWrapper "django.db.models.ExpressionWrapper"):

from django.db.models import DateTimeField, ExpressionWrapper, F

Ticket.objects.annotate(
    expires=ExpressionWrapper(
        F("active_at") + F("duration"), output_field=DateTimeField()
    )
)

When referencing relational fields such as `ForeignKey`, `F()` returns the primary key value rather than a model instance:

>>> car = Company.objects.annotate(built_by=F("manufacturer"))[0]
>>> car.manufacturer
<Manufacturer: Toyota>
>>> car.built_by
3

#### Using `F()` to sort null values[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#using-f-to-sort-null-values "Link to this heading")

Use `F()` and the `nulls_first` or `nulls_last` keyword argument to [`Expression.asc()`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.asc "django.db.models.Expression.asc") or [`desc()`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.desc "django.db.models.Expression.desc") to control the ordering of a field’s null values. By default, the ordering depends on your database.

For example, to sort companies that haven’t been contacted (`last_contacted` is null) after companies that have been contacted:

from django.db.models import F

Company.objects.order_by(F("last_contacted").desc(nulls_last=True))

#### Using `F()` with logical operations[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#using-f-with-logical-operations "Link to this heading")

`F()` expressions that output `BooleanField` can be logically negated with the inversion operator `~F()`. For example, to swap the activation status of companies:

from django.db.models import F

Company.objects.update(is_active=~F("is_active"))

### `Func()` expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#func-expressions "Link to this heading")

`Func()` expressions are the base type of all expressions that involve database functions like `COALESCE` and `LOWER`, or aggregates like `SUM`. They can be used directly:

from django.db.models import F, Func

queryset.annotate(field_lower=Func(F("field"), function="LOWER"))

or they can be used to build a library of database functions:

class Lower(Func):
    function = "LOWER"

queryset.annotate(field_lower=Lower("field"))

But both cases will result in a queryset where each model is annotated with an extra attribute `field_lower` produced, roughly, from the following SQL:

SELECT
 ...
 LOWER("db_table"."field") as "field_lower"

See [Database Functions](https://docs.djangoproject.com/en/6.0/ref/models/database-functions/) for a list of built-in database functions.

The `Func` API is as follows:

_class_ Func(_*expressions_, _**extra_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L1050)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Func "Link to this definition")function[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Func.function "Link to this definition")
A class attribute describing the function that will be generated. Specifically, the `function` will be interpolated as the `function` placeholder within [`template`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Func.template "django.db.models.Func.template"). Defaults to `None`.

template[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Func.template "Link to this definition")
A class attribute, as a format string, that describes the SQL that is generated for this function. Defaults to `'%(function)s(%(expressions)s)'`.

If you’re constructing SQL like `strftime('%W', 'date')` and need a literal `%` character in the query, quadruple it (`%%%%`) in the `template` attribute because the string is interpolated twice: once during the template interpolation in `as_sql()` and once in the SQL interpolation with the query parameters in the database cursor.

arg_joiner[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Func.arg_joiner "Link to this definition")
A class attribute that denotes the character used to join the list of `expressions` together. Defaults to `', '`.

arity[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Func.arity "Link to this definition")
A class attribute that denotes the number of arguments the function accepts. If this attribute is set and the function is called with a different number of expressions, `TypeError` will be raised. Defaults to `None`.

as_sql(_compiler_, _connection_, _function=None_, _template=None_, _arg\_joiner=None_, _**extra\_context_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L1093)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Func.as_sql "Link to this definition")
Generates the SQL fragment for the database function. Returns a tuple `(sql, params)`, where `sql` is the SQL string, and `params` is the list or tuple of query parameters.

The `as_vendor()` methods should use the `function`, `template`, `arg_joiner`, and any other `**extra_context` parameters to customize the SQL as needed. For example:

`django/db/models/functions.py`[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#id7 "Link to this code")

class ConcatPair(Func):
    ...
    function = "CONCAT"
    ...

    def as_mysql(self, compiler, connection, **extra_context):
        return super().as_sql(
            compiler,
            connection,
            function="CONCAT_WS",
            template="%(function)s('', %(expressions)s)",
            **extra_context
        )

To avoid an SQL injection vulnerability, `extra_context`[must not contain untrusted user input](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#avoiding-sql-injection-in-query-expressions) as these values are interpolated into the SQL string rather than passed as query parameters, where the database driver would escape them.

The `*expressions` argument is a list of positional expressions that the function will be applied to. The expressions will be converted to strings, joined together with `arg_joiner`, and then interpolated into the `template` as the `expressions` placeholder.

Positional arguments can be expressions or Python values. Strings are assumed to be column references and will be wrapped in `F()` expressions while other values will be wrapped in `Value()` expressions.

The `**extra` kwargs are `key=value` pairs that can be interpolated into the `template` attribute. To avoid an SQL injection vulnerability, `extra`[must not contain untrusted user input](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#avoiding-sql-injection-in-query-expressions) as these values are interpolated into the SQL string rather than passed as query parameters, where the database driver would escape them.

The `function`, `template`, and `arg_joiner` keywords can be used to replace the attributes of the same name without having to define your own class. [output_field](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#output-field) can be used to define the expected return type.

Sanitize input used to configure a query expression

Built-in database functions (such as [`Cast`](https://docs.djangoproject.com/en/6.0/ref/models/database-functions/#django.db.models.functions.Cast "django.db.models.functions.Cast")) vary in whether arguments such as `output_field` can be supplied positionally or only by keyword. For `output_field` and several other cases, the input ultimately reaches `Func()` as a keyword argument, so the advice to avoid constructing keyword arguments from untrusted user input applies as equally to these arguments as it does to `**extra`.

### `Aggregate()` expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#aggregate-expressions "Link to this heading")

An aggregate expression is a special case of a [Func() expression](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#func-expressions) that informs the query that a `GROUP BY` clause is required. All of the [aggregate functions](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#aggregation-functions), like `Sum()` and `Count()`, inherit from `Aggregate()`.

Since `Aggregate`s are expressions and wrap expressions, you can represent some complex computations:

from django.db.models import Count

Company.objects.annotate(
    managers_required=(Count("num_employees") / 4) + Count("num_managers")
)

The `Aggregate` API is as follows:

_class_ Aggregate(_*expressions_, _output\_field=None_, _distinct=False_, _filter=None_, _default=None_, _order\_by=None_, _**extra_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/aggregates.py#L72)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Aggregate "Link to this definition")template[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Aggregate.template "Link to this definition")
A class attribute, as a format string, that describes the SQL that is generated for this aggregate. Defaults to `'%(function)s(%(distinct)s%(expressions)s)'`.

function[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Aggregate.function "Link to this definition")
A class attribute describing the aggregate function that will be generated. Specifically, the `function` will be interpolated as the `function` placeholder within [`template`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Aggregate.template "django.db.models.Aggregate.template"). Defaults to `None`.

window_compatible[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Aggregate.window_compatible "Link to this definition")
Defaults to `True` since most aggregate functions can be used as the source expression in [`Window`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.Window "django.db.models.expressions.Window").

allow_distinct[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Aggregate.allow_distinct "Link to this definition")
A class attribute determining whether or not this aggregate function allows passing a `distinct` keyword argument. If set to `False` (default), `TypeError` is raised if `distinct=True` is passed.

allow_order_by[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Aggregate.allow_order_by "Link to this definition")
New in Django 6.0.

A class attribute determining whether or not this aggregate function allows passing a `order_by` keyword argument. If set to `False` (default), `TypeError` is raised if `order_by` is passed as a value other than `None`.

empty_result_set_value[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Aggregate.empty_result_set_value "Link to this definition")
Defaults to `None` since most aggregate functions result in `NULL` when applied to an empty result set.

The `expressions` positional arguments can include expressions, transforms of the model field, or the names of model fields. They will be converted to a string and used as the `expressions` placeholder within the `template`.

The `distinct` argument determines whether or not the aggregate function should be invoked for each distinct value of `expressions` (or set of values, for multiple `expressions`). The argument is only supported on aggregates that have [`allow_distinct`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Aggregate.allow_distinct "django.db.models.Aggregate.allow_distinct") set to `True`.

The `filter` argument takes a [`Q object`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.Q "django.db.models.Q") that’s used to filter the rows that are aggregated. See [Conditional aggregation](https://docs.djangoproject.com/en/6.0/ref/models/conditional-expressions/#conditional-aggregation) and [Filtering on annotations](https://docs.djangoproject.com/en/6.0/topics/db/aggregation/#filtering-on-annotations) for example usage.

The `order_by` argument behaves similarly to the `field_names` input of the [`order_by()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.order_by "django.db.models.query.QuerySet.order_by") function, accepting a field name (with an optional `"-"` prefix which indicates descending order) or an expression (or a tuple or list of strings and/or expressions) that specifies the ordering of the elements in the result.

The `default` argument takes a value that will be passed along with the aggregate to [`Coalesce`](https://docs.djangoproject.com/en/6.0/ref/models/database-functions/#django.db.models.functions.Coalesce "django.db.models.functions.Coalesce"). This is useful for specifying a value to be returned other than `None` when the queryset (or grouping) contains no entries.

The `**extra` kwargs are `key=value` pairs that can be interpolated into the `template` attribute.

Changed in Django 6.0:

The `order_by` argument was added.

### Creating your own Aggregate Functions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#creating-your-own-aggregate-functions "Link to this heading")

You can create your own aggregate functions, too. At a minimum, you need to define `function`, but you can also completely customize the SQL that is generated. Here’s a brief example:

from django.db.models import Aggregate

class Sum(Aggregate):
    # Supports SUM(ALL field).
    function = "SUM"
    template = "%(function)s(%(all_values)s%(expressions)s)"
    allow_distinct = False
    arity = 1

    def  __init__ (self, expression, all_values=False, **extra):
        super(). __init__ (expression, all_values="ALL " if all_values else "", **extra)

### `Value()` expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#value-expressions "Link to this heading")

_class_ Value(_value_, _output\_field=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L1144)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Value "Link to this definition")
A `Value()` object represents the smallest possible component of an expression: a simple value. When you need to represent the value of an integer, boolean, or string within an expression, you can wrap that value within a `Value()`.

You will rarely need to use `Value()` directly. When you write the expression `F('field') + 1`, Django implicitly wraps the `1` in a `Value()`, allowing simple values to be used in more complex expressions. You will need to use `Value()` when you want to pass a string to an expression. Most expressions interpret a string argument as the name of a field, like `Lower('name')`.

The `value` argument describes the value to be included in the expression, such as `1`, `True`, or `None`. Django knows how to convert these Python values into their corresponding database type.

If no [output_field](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#output-field) is specified, it will be inferred from the type of the provided `value` for many common types. For example, passing an instance of [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") as `value` defaults `output_field` to [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField").

### `ExpressionWrapper()` expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#expressionwrapper-expressions "Link to this heading")

_class_ ExpressionWrapper(_expression_, _output\_field_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L1504)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.ExpressionWrapper "Link to this definition")
`ExpressionWrapper` surrounds another expression and provides access to properties, such as [output_field](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#output-field), that may not be available on other expressions. `ExpressionWrapper` is necessary when using arithmetic on `F()` expressions with different types as described in [Using F() with annotations](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#using-f-with-annotations).

Database casting not performed

`ExpressionWrapper` only sets the output field for the ORM and does not perform any database-level casting. To ensure a specific type is returned from the database, use [`Cast`](https://docs.djangoproject.com/en/6.0/ref/models/database-functions/#django.db.models.functions.Cast "django.db.models.functions.Cast") instead.

### Conditional expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#conditional-expressions "Link to this heading")

Conditional expressions allow you to use [`if`](https://docs.python.org/3/reference/compound_stmts.html#if "(in Python v3.14)") … [`elif`](https://docs.python.org/3/reference/compound_stmts.html#elif "(in Python v3.14)") … [`else`](https://docs.python.org/3/reference/compound_stmts.html#else "(in Python v3.14)") logic in queries. Django natively supports SQL `CASE` expressions. For more details see [Conditional Expressions](https://docs.djangoproject.com/en/6.0/ref/models/conditional-expressions/).

### `Subquery()` expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#subquery-expressions "Link to this heading")

_class_ Subquery(_queryset_, _output\_field=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L1769)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Subquery "Link to this definition")
You can add an explicit subquery to a `QuerySet` using the `Subquery` expression.

For example, to annotate each post with the email address of the author of the newest comment on that post:

>>> from django.db.models import OuterRef, Subquery
>>> newest = Comment.objects.filter(post=OuterRef("pk")).order_by("-created_at")
>>> Post.objects.annotate(newest_commenter_email=Subquery(newest.values("email")[:1]))

On PostgreSQL, the SQL looks like:

SELECT "post"."id", (
 SELECT U0."email"
 FROM "comment" U0
 WHERE U0."post_id" = ("post"."id")
 ORDER BY U0."created_at" DESC LIMIT 1
) AS "newest_commenter_email" FROM "post"

Note

The examples in this section are designed to show how to force Django to execute a subquery. In some cases it may be possible to write an equivalent queryset that performs the same task more clearly or efficiently.

#### Referencing columns from the outer queryset[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#referencing-columns-from-the-outer-queryset "Link to this heading")

_class_ OuterRef(_field_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L979)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.OuterRef "Link to this definition")
Use `OuterRef` when a queryset in a `Subquery` needs to refer to a field from the outer query or its transform. It acts like an [`F`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.F "django.db.models.F") expression except that the check to see if it refers to a valid field isn’t made until the outer queryset is resolved.

Instances of `OuterRef` may be used in conjunction with nested instances of `Subquery` to refer to a containing queryset that isn’t the immediate parent. For example, this queryset would need to be within a nested pair of `Subquery` instances to resolve correctly:

>>> Book.objects.filter(author=OuterRef(OuterRef("pk")))

#### Limiting a subquery to a single column[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#limiting-a-subquery-to-a-single-column "Link to this heading")

There are times when a single column must be returned from a `Subquery`, for instance, to use a `Subquery` as the target of an `__in` lookup. To return all comments for posts published within the last day:

>>> from datetime import timedelta
>>> from django.utils import timezone
>>> one_day_ago = timezone.now() - timedelta(days=1)
>>> posts = Post.objects.filter(published_at__gte=one_day_ago)
>>> Comment.objects.filter(post__in=Subquery(posts.values("pk")))

In this case, the subquery must use [`values()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.values "django.db.models.query.QuerySet.values") to return only a single column: the primary key of the post.

#### Limiting the subquery to a single row[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#limiting-the-subquery-to-a-single-row "Link to this heading")

To prevent a subquery from returning multiple rows, a slice (`[:1]`) of the queryset is used:

>>> subquery = Subquery(newest.values("email")[:1])
>>> Post.objects.annotate(newest_commenter_email=subquery)

In this case, the subquery must only return a single column _and_ a single row: the email address of the most recently created comment.

(Using [`get()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") instead of a slice would fail because the `OuterRef` cannot be resolved until the queryset is used within a `Subquery`.)

#### `Exists()` subqueries[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#exists-subqueries "Link to this heading")

_class_ Exists(_queryset_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L1840)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Exists "Link to this definition")
`Exists` is a `Subquery` subclass that uses an SQL `EXISTS` statement. In many cases it will perform better than a subquery since the database is able to stop evaluation of the subquery when a first matching row is found.

For example, to annotate each post with whether or not it has a comment from within the last day:

>>> from django.db.models import Exists, OuterRef
>>> from datetime import timedelta
>>> from django.utils import timezone
>>> one_day_ago = timezone.now() - timedelta(days=1)
>>> recent_comments = Comment.objects.filter(
...     post=OuterRef("pk"),
...     created_at__gte=one_day_ago,
... )
>>> Post.objects.annotate(recent_comment=Exists(recent_comments))

On PostgreSQL, the SQL looks like:

SELECT "post"."id", "post"."published_at", EXISTS(
 SELECT (1) as "a"
 FROM "comment" U0
 WHERE (
 U0."created_at" >= YYYY-MM-DD HH:MM:SS AND
 U0."post_id" = "post"."id"
 )
 LIMIT 1
) AS "recent_comment" FROM "post"

It’s unnecessary to force `Exists` to refer to a single column, since the columns are discarded and a boolean result is returned. Similarly, since ordering is unimportant within an SQL `EXISTS` subquery and would only degrade performance, it’s automatically removed.

You can query using `NOT EXISTS` with `~Exists()`.

#### Filtering on a `Subquery()` or `Exists()` expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#filtering-on-a-subquery-or-exists-expressions "Link to this heading")

`Subquery()` that returns a boolean value and `Exists()` may be used as a `condition` in [`When`](https://docs.djangoproject.com/en/6.0/ref/models/conditional-expressions/#django.db.models.expressions.When "django.db.models.expressions.When") expressions, or to directly filter a queryset:

>>> recent_comments = Comment.objects.filter(...)  # From above
>>> Post.objects.filter(Exists(recent_comments))

This will ensure that the subquery will not be added to the `SELECT` columns, which may result in a better performance.

#### Using aggregates within a `Subquery` expression[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#using-aggregates-within-a-subquery-expression "Link to this heading")

Aggregates may be used within a `Subquery`, but they require a specific combination of [`filter()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter"), [`values()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.values "django.db.models.query.QuerySet.values"), and [`annotate()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.annotate "django.db.models.query.QuerySet.annotate") to get the subquery grouping correct.

Assuming both models have a `length` field, to find posts where the post length is greater than the total length of all combined comments:

>>> from django.db.models import OuterRef, Subquery, Sum
>>> comments = Comment.objects.filter(post=OuterRef("pk")).order_by().values("post")
>>> total_comments = comments.annotate(total=Sum("length")).values("total")
>>> Post.objects.filter(length__gt=Subquery(total_comments))

The initial `filter(...)` limits the subquery to the relevant parameters. `order_by()` removes the default [`ordering`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.ordering "django.db.models.Options.ordering") (if any) on the `Comment` model. `values('post')` aggregates comments by `Post`. Finally, `annotate(...)` performs the aggregation. The order in which these queryset methods are applied is important. In this case, since the subquery must be limited to a single column, `values('total')` is required.

This is the only way to perform an aggregation within a `Subquery`, as using [`aggregate()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.aggregate "django.db.models.query.QuerySet.aggregate") attempts to evaluate the queryset (and if there is an `OuterRef`, this will not be possible to resolve).

### Raw SQL expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#raw-sql-expressions "Link to this heading")

_class_ RawSQL(_sql_, _params_, _output\_field=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L1224)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.RawSQL "Link to this definition")
Sometimes database expressions can’t easily express a complex `WHERE` clause. In these edge cases, use the `RawSQL` expression. For example:

>>> from django.db.models.expressions import RawSQL
>>> queryset.annotate(val=RawSQL("select col from sometable where othercol = %s", (param,)))

These extra lookups may not be portable to different database engines (because you’re explicitly writing SQL code) and violate the DRY principle, so you should avoid them if possible.

`RawSQL` expressions can also be used as the target of `__in` filters:

>>> queryset.filter(id__in=RawSQL("select id from sometable where col = %s", (param,)))

Warning

To protect against [SQL injection attacks](https://en.wikipedia.org/wiki/SQL_injection), you must escape any parameters that the user can control by using `params`. `params` is a required argument to force you to acknowledge that you’re not interpolating your SQL with user-provided data.

You also must not quote placeholders in the SQL string. This example is vulnerable to SQL injection because of the quotes around `%s`:

RawSQL("select col from sometable where othercol = '%s'")  # unsafe!

You can read more about how Django’s [SQL injection protection](https://docs.djangoproject.com/en/6.0/topics/security/#sql-injection-protection) works.

### Window functions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#window-functions "Link to this heading")

Window functions provide a way to apply functions on partitions. Unlike a normal aggregation function which computes a final result for each set defined by the group by, window functions operate on [frames](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#window-frames) and partitions, and compute the result for each row.

You can specify multiple windows in the same query which in Django ORM would be equivalent to including multiple expressions in a [QuerySet.annotate()](https://docs.djangoproject.com/en/6.0/topics/db/aggregation/) call. The ORM doesn’t make use of named windows, instead they are part of the selected columns.

_class_ Window(_expression_, _partition\_by=None_, _order\_by=None_, _frame=None_, _output\_field=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L1973)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.Window "Link to this definition")template[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.Window.template "Link to this definition")
Defaults to `%(expression)s OVER (%(window)s)`. If only the `expression` argument is provided, the window clause will be blank.

The `Window` class is the main expression for an `OVER` clause.

The `expression` argument is either a [window function](https://docs.djangoproject.com/en/6.0/ref/models/database-functions/#window-functions), an [aggregate function](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#aggregation-functions), or an expression that’s compatible in a window clause.

The `partition_by` argument accepts an expression or a sequence of expressions (column names should be wrapped in an `F`-object) that control the partitioning of the rows. Partitioning narrows which rows are used to compute the result set.

The [output_field](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#output-field) is specified either as an argument or by the expression.

The `order_by` argument accepts an expression on which you can call [`asc()`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.asc "django.db.models.Expression.asc") and [`desc()`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.desc "django.db.models.Expression.desc"), a string of a field name (with an optional `"-"` prefix which indicates descending order), or a tuple or list of strings and/or expressions. The ordering controls the order in which the expression is applied. For example, if you sum over the rows in a partition, the first result is the value of the first row, the second is the sum of first and second row.

The `frame` parameter specifies which other rows that should be used in the computation. See [Frames](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#window-frames) for details.

For example, to annotate each movie with the average rating for the movies by the same studio in the same genre and release year:

>>> from django.db.models import Avg, F, Window
>>> Movie.objects.annotate(
...     avg_rating=Window(
...         expression=Avg("rating"),
...         partition_by=[F("studio"), F("genre")],
...         order_by="released__year",
...     ),
... )

This allows you to check if a movie is rated better or worse than its peers.

You may want to apply multiple expressions over the same window, i.e., the same partition and frame. For example, you could modify the previous example to also include the best and worst rating in each movie’s group (same studio, genre, and release year) by using three window functions in the same query. The partition and ordering from the previous example is extracted into a dictionary to reduce repetition:

>>> from django.db.models import Avg, F, Max, Min, Window
>>> window = {
...     "partition_by": [F("studio"), F("genre")],
...     "order_by": "released__year",
... }
>>> Movie.objects.annotate(
...     avg_rating=Window(
...         expression=Avg("rating"),
...         **window,
...     ),
...     best=Window(
...         expression=Max("rating"),
...         **window,
...     ),
...     worst=Window(
...         expression=Min("rating"),
...         **window,
...     ),
... )

Filtering against window functions is supported as long as lookups are not disjunctive (not using `OR` or `XOR` as a connector) and against a queryset performing aggregation.

For example, a query that relies on aggregation and has an `OR`-ed filter against a window function and a field is not supported. Applying combined predicates post-aggregation could cause rows that would normally be excluded from groups to be included:

>>> qs = Movie.objects.annotate(
...     category_rank=Window(Rank(), partition_by="category", order_by="-rating"),
...     scenes_count=Count("actors"),
... ).filter(Q(category_rank__lte=3) | Q(title__contains="Batman"))
>>> list(qs)
NotImplementedError: Heterogeneous disjunctive predicates against window functions
are not implemented when performing conditional aggregation.

Among Django’s built-in database backends, MySQL, PostgreSQL, and Oracle support window expressions. Support for different window expression features varies among the different databases. For example, the options in [`asc()`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.asc "django.db.models.Expression.asc") and [`desc()`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.desc "django.db.models.Expression.desc") may not be supported. Consult the documentation for your database as needed.

#### Frames[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#frames "Link to this heading")

For a window frame, you can choose either a range-based sequence of rows or an ordinary sequence of rows.

_class_ ValueRange(_start=None_, _end=None_, _exclusion=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L2184)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.ValueRange "Link to this definition")frame_type[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.ValueRange.frame_type "Link to this definition")
This attribute is set to `'RANGE'`.

PostgreSQL has limited support for `ValueRange` and only supports use of the standard start and end points, such as `CURRENT ROW` and 
```
UNBOUNDED
FOLLOWING
```
.

_class_ RowRange(_start=None_, _end=None_, _exclusion=None_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L2177)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.RowRange "Link to this definition")frame_type[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.RowRange.frame_type "Link to this definition")
This attribute is set to `'ROWS'`.

Both classes return SQL with the template:

%(frame_type)s BETWEEN %(start)s AND %(end)s

_class_ WindowFrameExclusion[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L2080)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.WindowFrameExclusion "Link to this definition")CURRENT_ROW[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.WindowFrameExclusion.CURRENT_ROW "Link to this definition")GROUP[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.WindowFrameExclusion.GROUP "Link to this definition")TIES[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.WindowFrameExclusion.TIES "Link to this definition")NO_OTHERS[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.WindowFrameExclusion.NO_OTHERS "Link to this definition")
The `exclusion` argument allows excluding rows ([`CURRENT_ROW`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.WindowFrameExclusion.CURRENT_ROW "django.db.models.expressions.WindowFrameExclusion.CURRENT_ROW")), groups ([`GROUP`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.WindowFrameExclusion.GROUP "django.db.models.expressions.WindowFrameExclusion.GROUP")), and ties ([`TIES`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.WindowFrameExclusion.TIES "django.db.models.expressions.WindowFrameExclusion.TIES")) from the window frames on supported databases:

%(frame_type)s BETWEEN %(start)s AND %(end)s EXCLUDE %(exclusion)s

Frames narrow the rows that are used for computing the result. They shift from some start point to some specified end point. Frames can be used with and without partitions, but it’s often a good idea to specify an ordering of the window to ensure a deterministic result. In a frame, a peer in a frame is a row with an equivalent value, or all rows if an ordering clause isn’t present.

The default starting point for a frame is `UNBOUNDED PRECEDING` which is the first row of the partition. The end point is always explicitly included in the SQL generated by the ORM and is by default `UNBOUNDED FOLLOWING`. The default frame includes all rows from the partition to the last row in the set.

The accepted values for the `start` and `end` arguments are `None`, an integer, or zero. A negative integer for `start` results in `N PRECEDING`, while `None` yields `UNBOUNDED PRECEDING`. In `ROWS` mode, a positive integer can be used for `start` resulting in `N FOLLOWING`. Positive integers are accepted for `end` and results in `N FOLLOWING`. In `ROWS` mode, a negative integer can be used for `end` resulting in `N PRECEDING`. For both `start` and `end`, zero will return `CURRENT ROW`.

There’s a difference in what `CURRENT ROW` includes. When specified in `ROWS` mode, the frame starts or ends with the current row. When specified in `RANGE` mode, the frame starts or ends at the first or last peer according to the ordering clause. Thus, `RANGE CURRENT ROW` evaluates the expression for rows which have the same value specified by the ordering. Because the template includes both the `start` and `end` points, this may be expressed with:

ValueRange(start=0, end=0)

If a movie’s “peers” are described as movies released by the same studio in the same genre in the same year, this `RowRange` example annotates each movie with the average rating of a movie’s two prior and two following peers:

>>> from django.db.models import Avg, F, RowRange, Window
>>> Movie.objects.annotate(
...     avg_rating=Window(
...         expression=Avg("rating"),
...         partition_by=[F("studio"), F("genre")],
...         order_by="released__year",
...         frame=RowRange(start=-2, end=2),
...     ),
... )

If the database supports it, you can specify the start and end points based on values of an expression in the partition. If the `released` field of the `Movie` model stores the release month of each movie, this `ValueRange` example annotates each movie with the average rating of a movie’s peers released between twelve months before and twelve months after each movie:

>>> from django.db.models import Avg, F, ValueRange, Window
>>> Movie.objects.annotate(
...     avg_rating=Window(
...         expression=Avg("rating"),
...         partition_by=[F("studio"), F("genre")],
...         order_by="released__year",
...         frame=ValueRange(start=-12, end=12),
...     ),
... )

Technical Information[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#technical-information "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

Below you’ll find technical implementation details that may be useful to library authors. The technical API and examples below will help with creating generic query expressions that can extend the built-in functionality that Django provides.

### Expression API[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#expression-api "Link to this heading")

Query expressions implement the [query expression API](https://docs.djangoproject.com/en/6.0/ref/models/lookups/#query-expression), but also expose a number of extra methods and attributes listed below. All query expressions must inherit from `Expression()` or a relevant subclass.

When a query expression wraps another expression, it is responsible for calling the appropriate methods on the wrapped expression.

_class_ Expression[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/models/expressions.py#L520)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression "Link to this definition")allowed_default[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.allowed_default "Link to this definition")
Tells Django that this expression can be used in [`Field.db_default`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_default "django.db.models.Field.db_default"). Defaults to `False`.

constraint_validation_compatible[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.constraint_validation_compatible "Link to this definition")
Tells Django that this expression can be used during a constraint validation. Expressions with `constraint_validation_compatible` set to `False` must have only one source expression. Defaults to `True`.

contains_aggregate[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.contains_aggregate "Link to this definition")
Tells Django that this expression contains an aggregate and that a `GROUP BY` clause needs to be added to the query.

contains_over_clause[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.contains_over_clause "Link to this definition")
Tells Django that this expression contains a [`Window`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.Window "django.db.models.expressions.Window") expression. It’s used, for example, to disallow window function expressions in queries that modify data.

filterable[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.filterable "Link to this definition")
Tells Django that this expression can be referenced in [`QuerySet.filter()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter"). Defaults to `True`.

window_compatible[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.window_compatible "Link to this definition")
Tells Django that this expression can be used as the source expression in [`Window`](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.expressions.Window "django.db.models.expressions.Window"). Defaults to `False`.

empty_result_set_value[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.empty_result_set_value "Link to this definition")
Tells Django which value should be returned when the expression is used to apply a function over an empty result set. Defaults to [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "(in Python v3.14)") which forces the expression to be computed on the database.

set_returning[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.set_returning "Link to this definition")
New in Django 5.2.

Tells Django that this expression contains a set-returning function, enforcing subquery evaluation. It’s used, for example, to allow some Postgres set-returning functions (e.g. `JSONB_PATH_QUERY`, `UNNEST`, etc.) to skip optimization and be properly evaluated when annotations spawn rows themselves. Defaults to `False`.

allows_composite_expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.allows_composite_expressions "Link to this definition")
New in Django 5.2.

Tells Django that this expression allows composite expressions, for example, to support [composite primary keys](https://docs.djangoproject.com/en/6.0/topics/composite-primary-key/#cpk-and-database-functions). Defaults to `False`.

resolve_expression(_query=None_, _allow\_joins=True_, _reuse=None_, _summarize=False_, _for\_save=False_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.resolve_expression "Link to this definition")
Provides the chance to do any preprocessing or validation of the expression before it’s added to the query. `resolve_expression()` must also be called on any nested expressions. A `copy()` of `self` should be returned with any necessary transformations.

`query` is the backend query implementation.

`allow_joins` is a boolean that allows or denies the use of joins in the query.

`reuse` is a set of reusable joins for multi-join scenarios.

`summarize` is a boolean that, when `True`, signals that the query being computed is a terminal aggregate query.

`for_save` is a boolean that, when `True`, signals that the query being executed is performing a create or update.

get_source_expressions()[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.get_source_expressions "Link to this definition")
Returns an ordered list of inner expressions. For example:

>>> Sum(F("foo")).get_source_expressions()
[F('foo')]

set_source_expressions(_expressions_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.set_source_expressions "Link to this definition")
Takes a list of expressions and stores them such that `get_source_expressions()` can return them.

relabeled_clone(_change\_map_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.relabeled_clone "Link to this definition")
Returns a clone (copy) of `self`, with any column aliases relabeled. Column aliases are renamed when subqueries are created. `relabeled_clone()` should also be called on any nested expressions and assigned to the clone.

`change_map` is a dictionary mapping old aliases to new aliases.

Example:

def relabeled_clone(self, change_map):
    clone = copy.copy(self)
    clone.expression = self.expression.relabeled_clone(change_map)
    return clone

convert_value(_value_, _expression_, _connection_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.convert_value "Link to this definition")
A hook allowing the expression to coerce `value` into a more appropriate type.

`expression` is the same as `self`.

get_group_by_cols()[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.get_group_by_cols "Link to this definition")
Responsible for returning the list of columns references by this expression. `get_group_by_cols()` should be called on any nested expressions. `F()` objects, in particular, hold a reference to a column.

asc(_nulls\_first=None_, _nulls\_last=None_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.asc "Link to this definition")
Returns the expression ready to be sorted in ascending order.

`nulls_first` and `nulls_last` define how null values are sorted. See [Using F() to sort null values](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#using-f-to-sort-null-values) for example usage.

desc(_nulls\_first=None_, _nulls\_last=None_)[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.desc "Link to this definition")
Returns the expression ready to be sorted in descending order.

`nulls_first` and `nulls_last` define how null values are sorted. See [Using F() to sort null values](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#using-f-to-sort-null-values) for example usage.

reverse_ordering()[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#django.db.models.Expression.reverse_ordering "Link to this definition")
Returns `self` with any modifications required to reverse the sort order within an `order_by` call. As an example, an expression implementing `NULLS LAST` would change its value to be `NULLS FIRST`. Modifications are only required for expressions that implement sort order like `OrderBy`. This method is called when [`reverse()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.reverse "django.db.models.query.QuerySet.reverse") is called on a queryset.

### Writing your own Query Expressions[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#writing-your-own-query-expressions "Link to this heading")

You can write your own query expression classes that use, and can integrate with, other query expressions. Let’s step through an example by writing an implementation of the `COALESCE` SQL function, without using the built-in [Func() expressions](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#func-expressions).

The `COALESCE` SQL function is defined as taking a list of columns or values. It will return the first column or value that isn’t `NULL`.

We’ll start by defining the template to be used for SQL generation and an `__init__()` method to set some attributes:

from django.db.models import Expression

class Coalesce(Expression):
    template = "COALESCE( %(expressions)s )"

    def  __init__ (self, expressions, output_field):
        super(). __init__ (output_field=output_field)
        if len(expressions) < 2:
            raise ValueError("expressions must have at least 2 elements")
        for expression in expressions:
            if not hasattr(expression, "resolve_expression"):
                raise TypeError("%r is not an Expression" % expression)
        self.expressions = expressions

We do some basic validation on the parameters, including requiring at least 2 columns or values, and ensuring they are expressions. We are requiring [output_field](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#output-field) here so that Django knows what kind of model field to assign the eventual result to.

Now we implement the preprocessing and validation. Since we do not have any of our own validation at this point, we delegate to the nested expressions:

def resolve_expression(
    self, query=None, allow_joins=True, reuse=None, summarize=False, for_save=False
):
    c = self.copy()
    c.is_summary = summarize
    for pos, expression in enumerate(self.expressions):
        c.expressions[pos] = expression.resolve_expression(
            query, allow_joins, reuse, summarize, for_save
        )
    return c

Next, we write the method responsible for generating the SQL:

def as_sql(self, compiler, connection, template=None):
    sql_expressions, sql_params = [], []
    for expression in self.expressions:
        sql, params = compiler.compile(expression)
        sql_expressions.append(sql)
        sql_params.extend(params)
    template = template or self.template
    data = {"expressions": ",".join(sql_expressions)}
    return template % data, tuple(sql_params)

def as_oracle(self, compiler, connection):
 """
 Example of vendor specific handling (Oracle in this case).
 Let's make the function name lowercase.
 """
    return self.as_sql(compiler, connection, template="coalesce( %(expressions)s )")

`as_sql()` methods can support custom keyword arguments, allowing `as_vendorname()` methods to override data used to generate the SQL string. Using `as_sql()` keyword arguments for customization is preferable to mutating `self` within `as_vendorname()` methods as the latter can lead to errors when running on different database backends. If your class relies on class attributes to define data, consider allowing overrides in your `as_sql()` method.

We generate the SQL for each of the `expressions` by using the `compiler.compile()` method, and join the result together with commas. Then the template is filled out with our data and the SQL and parameters are returned.

We’ve also defined a custom implementation that is specific to the Oracle backend. The `as_oracle()` function will be called instead of `as_sql()` if the Oracle backend is in use.

Finally, we implement the rest of the methods that allow our query expression to play nice with other query expressions:

def get_source_expressions(self):
    return self.expressions

def set_source_expressions(self, expressions):
    self.expressions = expressions

Let’s see how it works:

>>> from django.db.models import F, Value, CharField
>>> qs = Company.objects.annotate(
...     tagline=Coalesce(
...         [F("motto"), F("ticker_name"), F("description"), Value("No Tagline")],
...         output_field=CharField(),
...     )
... )
>>> for c in qs:
...     print("%s: %s" % (c.name, c.tagline))
...
Google: Do No Evil
Apple: AAPL
Yahoo: Internet Company
Django Software Foundation: No Tagline

#### Avoiding SQL injection[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#avoiding-sql-injection "Link to this heading")

Since a `Func`’s keyword arguments for `__init__()` (`**extra`) and `as_sql()` (`**extra_context`) are interpolated into the SQL string rather than passed as query parameters (where the database driver would escape them), they must not contain untrusted user input.

For example, if `substring` is user-provided, this function is vulnerable to SQL injection:

from django.db.models import Func

class Position(Func):
    function = "POSITION"
    template = "%(function)s('%(substring)s' in %(expressions)s)"

    def  __init__ (self, expression, substring):
        # substring=substring is an SQL injection vulnerability!
        super(). __init__ (expression, substring=substring)

This function generates an SQL string without any parameters. Since `substring` is passed to `super().__init__()` as a keyword argument, it’s interpolated into the SQL string before the query is sent to the database.

Here’s a corrected rewrite:

class Position(Func):
    function = "POSITION"
    arg_joiner = " IN "

    def  __init__ (self, expression, substring):
        super(). __init__ (substring, expression)

With `substring` instead passed as a positional argument, it’ll be passed as a parameter in the database query.

### Adding support in third-party database backends[¶](https://docs.djangoproject.com/en/6.0/ref/models/expressions/#adding-support-in-third-party-database-backends "Link to this heading")

If you’re using a database backend that uses a different SQL syntax for a certain function, you can add support for it by monkey patching a new method onto the function’s class.

Let’s say we’re writing a backend for Microsoft’s SQL Server which uses the SQL `LEN` instead of `LENGTH` for the [`Length`](https://docs.djangoproject.com/en/6.0/ref/models/database-functions/#django.db.models.functions.Length "django.db.models.functions.Length") function. We’ll monkey patch a new method called `as_sqlserver()` onto the `Length` class:

from django.db.models.functions import Length

def sqlserver_length(self, compiler, connection):
    return self.as_sql(compiler, connection, function="LEN")

Length.as_sqlserver = sqlserver_length

You can also customize the SQL using the `template` parameter of `as_sql()`.

We use `as_sqlserver()` because `django.db.connection.vendor` returns `sqlserver` for the backend.

Third-party backends can register their functions in the top level `__init__.py` file of the backend package or in a top level `expressions.py` file (or package) that is imported from the top level `__init__.py`.

For user projects wishing to patch the backend that they’re using, this code should live in an [`AppConfig.ready()`](https://docs.djangoproject.com/en/6.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready") method.
