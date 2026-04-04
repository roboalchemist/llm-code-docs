# Source: https://docs.pylonsproject.org/projects/colander/en/latest/basics.html

Title: Colander Basics — colander 2.0 documentation

URL Source: https://docs.pylonsproject.org/projects/colander/en/latest/basics.html

Markdown Content:
Basics of using colander include defining a colander schema, deserializing a data structure using a schema, serializing a data structure using a schema, and dealing with [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exceptions.

Defining A Colander Schema[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#defining-a-colander-schema "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Imagine you want to deserialize and validate a serialization of data you've obtained by reading a YAML document. An example of such a data serialization might look something like this:

1{
2     'name': 'keith',
3     'age': '20',
4     'friends': [('1', 'jim'), ('2', 'bob'), ('3', 'joe'), ('4', 'fred')],
5     'phones': [{'location': 'home', 'number': '555-1212'},
6                {'location': 'work', 'number': '555-8989'}],
7}

Let's further imagine you'd like to make sure, on demand, that a particular serialization of this type read from this YAML document or another YAML document is "valid".

Notice that all the innermost values in the serialization are strings, even though some of them (such as age and the position of each friend) are more naturally integer-like. Let's define a schema which will attempt to convert a serialization to a data structure that has different types.

 1import colander
 2
 3class Friend(colander.TupleSchema):
 4    rank = colander.SchemaNode(colander.Int(),
 5                               validator=colander.Range(0, 9999))
 6    name = colander.SchemaNode(colander.String())
 7
 8class Phone(colander.MappingSchema):
 9    location = colander.SchemaNode(colander.String(),
10                                   validator=colander.OneOf(['home', 'work']))
11    number = colander.SchemaNode(colander.String())
12
13class Friends(colander.SequenceSchema):
14    friend = Friend()
15
16class Phones(colander.SequenceSchema):
17    phone = Phone()
18
19class Person(colander.MappingSchema):
20    name = colander.SchemaNode(colander.String())
21    age = colander.SchemaNode(colander.Int(),
22                              validator=colander.Range(0, 200))
23    friends = Friends()
24    phones = Phones()

For ease of reading, we've actually defined _five_ schemas above, but we coalesce them all into a single `Person` schema. As the result of our definitions, a `Person` represents:

*   A `name`, which must be a string.

*   An `age`, which must be deserializable to an integer; after deserialization happens, a validator ensures that the integer is between 0 and 200 inclusive.

*   A sequence of `friend` structures. Each friend structure is a two-element tuple. The first element represents an integer rank; it must be between 0 and 9999 inclusive. The second element represents a string name.

*   A sequence of `phone` structures. Each phone structure is a mapping. Each phone mapping has two keys: `location` and `number`. The `location` must be one of `work` or `home`. The number must be a string.

### Schema Node Objects[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#schema-node-objects "Link to this heading")

A schema is composed of one or more _schema node_ objects, each typically of the class [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode"), usually in a nested arrangement. Each schema node object has a required _type_, an optional _preparer_ for adjusting data after deserialization, an optional _validator_ for deserialized prepared data, an optional _default_, an optional _missing_, an optional _title_, an optional _description_, and a slightly less optional _name_. It also accepts _arbitrary_ keyword arguments, which are attached directly as attributes to the node instance.

The _type_ of a schema node indicates its data type (such as [`colander.Int`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Int "colander.Int") or [`colander.String`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.String "colander.String")).

The _preparer_ of a schema node is called after deserialization but before validation; it prepares a deserialized value for validation. Examples would be to prepend schemes that may be missing on url values or to filter html provided by a rich text editor. A preparer is not called during serialization, only during deserialization. You can also pass a schema node a list of preparers.

The _validator_ of a schema node is called after deserialization and preparation ; it makes sure the value matches a constraint. An example of such a validator is provided in the schema above: `validator=colander.Range(0, 200)`. A validator is not called after schema node serialization, only after node deserialization.

The _default_ of a schema node indicates the value to be serialized if a value for the schema node is not found in the input data during serialization. It should be the deserialized representation. If a schema node does not have a default, it is considered "serialization required".

The _missing_ of a schema node indicates the value if a value for the schema node is not found in the input data during deserialization. It should be the deserialized representation. If a schema node does not have a missing, it is considered "deserialization required". This value is never validated; it is considered pre-validated.

The _name_ of a schema node appears in error reports.

The _title_ of a schema node is metadata about a schema node that can be used by higher-level systems. By default, it is a capitalization of the _name_.

The _description_ of a schema node is metadata about a schema node that can be used by higher-level systems. By default, it is empty.

The _insert\_before_ of a schema node is a string: if supplied, it names a sibling defined by a superclass for its parent node; the current node will be inserted before the named node. It is not useful unless a mapping schema is inherited from another mapping schema, and you need to control the ordering of the resulting nodes.

Any other keyword arguments to a schema node constructor will be attached to the node unmolested (e.g. when `foo=1` is passed, the resulting schema node will have an attribute named `foo` with the value `1`).

Note

You may see some higher-level systems (such as Deform) pass a `widget` argument to a SchemaNode constructor. Such systems make use of the fact that a SchemaNode can be passed arbitrary keyword arguments for extension purposes. `widget` and other keyword arguments not enumerated here but which are passed during schema node construction by someone constructing a schema for a particular purpose are not used internally by Colander; they are instead only meaningful to higher-level systems which consume Colander schemas. Arbitrary keyword arguments are allowed to a schema node constructor in Colander 0.9+. Prior versions disallow them.

#### Subclassing SchemaNode[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#subclassing-schemanode "Link to this heading")

As of Colander 1.0a1+, it is possible and advisable to subclass [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") in order to create a bundle of default node behavior. The subclass can define the following methods and attributes: `preparer`, `validator`, `default`, `missing`, `name`, `title`, `description`, `widget`, and `after_bind`.

The imperative style that looks like this still works, of course:

ranged_int = colander.SchemaNode(
    typ=colander.Int(),
    validator=colander.Range(0, 10),
    default=10,
    title='Ranged Int'
    )

But in 1.0a1+, you can alternately now do something like this:

class RangedInt(colander.SchemaNode):
    schema_type = colander.Int
    validator = colander.Range(0, 10)
    default = 10
    title = 'Ranged Int'

ranged_int = RangedInt()

Values that are expected to be callables can now alternately be methods of the schemanode subclass instead of plain attributes:

class RangedInt(colander.SchemaNode):
    schema_type = colander.Int
    default = 10
    title = 'Ranged Int'

    def validator(self, node, cstruct):
       if not 0 < cstruct < 10:
           raise colander.Invalid(node, 'Must be between 0 and 10')

ranged_int = RangedInt()

Note that when implementing a method value such as `validator` that expects to receive a `node` argument, `node` must be provided in the call signature, even though `node` will almost always be the same as `self`. This is because Colander simply treats the method as another kind of callable, be it a method, or a function, or an instance that has a `__call__` method. It doesn't care that it happens to be a method of `self`, and it needs to support callables that are not methods, so it sends `node` in regardless.

You can't use _method_ definitions as `colander.deferred` callables. For example this will _not_ work:

class RangedInt(colander.SchemaNode):
    schema_type = colander.Int
    default = 10
    title = 'Ranged Int'

    @colander.deferred
    def validator(self, node, kw):
       request = kw['request']
       def avalidator(node, cstruct):
           if not 0 < cstruct < 10:
               if request.user != 'admin':
                   raise colander.Invalid(node, 'Must be between 0 and 10')
       return avalidator

ranged_int = RangedInt()
bound_ranged_int = ranged_int.bind(request=request)

This will result in:

TypeError: validator() takes exactly 3 arguments (2 given)

However, if you treat the thing being decorated as a function instead of a method (remove the `self` argument from the argument list), it will indeed work):

class RangedInt(colander.SchemaNode):
    schema_type = colander.Int
    default = 10
    title = 'Ranged Int'

    @colander.deferred
    def validator(node, kw):
       request = kw['request']
       def avalidator(node, cstruct):
           if not 0 < cstruct < 10:
               if request.user != 'admin':
                   raise colander.Invalid(node, 'Must be between 0 and 10')
       return avalidator

ranged_int = RangedInt()
bound_ranged_int = ranged_int.bind(request=request)

In releases of Colander before 1.0a1+, the only way to defer the computation of values was via the `colander.deferred` decorator. In this release, however, you can instead use the `bindings` attribute of `self` to obtain access to the bind parameters within values that are plain old methods:

class RangedInt(colander.SchemaNode):
    schema_type = colander.Int
    default = 10
    title = 'Ranged Int'

    def validator(self, node, cstruct):
       request = self.bindings['request']
       if not 0 < cstruct < 10:
           if request.user != 'admin':
               raise colander.Invalid(node, 'Must be between 0 and 10')

ranged_int = RangedInt()
bound_range_int = ranged_int.bind(request=request)

If the things you're trying to defer aren't callables like `validator`, but they're instead just plain attributes like `missing` or `default`, instead of using a `colander.deferred`, you can use `after_bind` to set attributes of the schemanode that rely on binding variables:

class UserIdSchemaNode(colander.SchemaNode):
    schema_type = colander.String
    title = 'User Id'

    def after_bind(self, node, kw):
        self.default = kw['request'].user.id

You can override the default values of a schemanode subclass in its constructor:

class RangedInt(colander.SchemaNode):
    schema_type = colander.Int
    default = 10
    title = 'Ranged Int'
    validator = colander.Range(0, 10)

ranged_int = RangedInt(validator=colander.Range(0, 20))

In the above example, the validation will be done on 0-20, not 0-10.

Normal inheritance rules apply to class attributes and methods defined in a schemanode subclass. If your schemanode subclass inherits from another schemanode class, your schemanode subclass' methods and class attributes will override the superclass' methods and class attributes.

### Schema Objects[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#schema-objects "Link to this heading")

In the examples above, if you've been paying attention, you'll have noticed that we're defining classes which subclass from [`colander.MappingSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.MappingSchema "colander.MappingSchema"), [`colander.TupleSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.TupleSchema "colander.TupleSchema") and [`colander.SequenceSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SequenceSchema "colander.SequenceSchema").

It's turtles all the way down: the result of creating an instance of any of [`colander.MappingSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.MappingSchema "colander.MappingSchema"), [`colander.TupleSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.TupleSchema "colander.TupleSchema") or [`colander.SequenceSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SequenceSchema "colander.SequenceSchema") object is _also_ a [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") object.

Instantiating a [`colander.MappingSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.MappingSchema "colander.MappingSchema") creates a schema node which has a _type_ value of [`colander.Mapping`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Mapping "colander.Mapping").

Instantiating a [`colander.TupleSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.TupleSchema "colander.TupleSchema") creates a schema node which has a _type_ value of [`colander.Tuple`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Tuple "colander.Tuple").

Instantiating a [`colander.SequenceSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SequenceSchema "colander.SequenceSchema") creates a schema node which has a _type_ value of [`colander.Sequence`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Sequence "colander.Sequence").

The name of a schema node that is introduced as a class-level attribute of a [`colander.MappingSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.MappingSchema "colander.MappingSchema"), [`colander.TupleSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.TupleSchema "colander.TupleSchema") or a [`colander.SequenceSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SequenceSchema "colander.SequenceSchema") is its class attribute name. For example:

1import colander
2
3class Phone(colander.MappingSchema):
4    location = colander.SchemaNode(
5        colander.String(),
6        validator=colander.OneOf(['home', 'work']))
7    number = colander.SchemaNode(colander.String())

The name of the schema node defined via 
```
location =
colander.SchemaNode(..)
```
 within the schema above is `location`. The title of the same schema node is `Location`.

Deserialization[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#deserialization "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

Earlier we defined a schema:

 1import colander
 2
 3class Friend(colander.TupleSchema):
 4    rank = colander.SchemaNode(colander.Int(),
 5                               validator=colander.Range(0, 9999))
 6    name = colander.SchemaNode(colander.String())
 7
 8class Phone(colander.MappingSchema):
 9    location = colander.SchemaNode(
10        colander.String(),
11        validator=colander.OneOf(['home', 'work']))
12    number = colander.SchemaNode(colander.String())
13
14class Friends(colander.SequenceSchema):
15    friend = Friend()
16
17class Phones(colander.SequenceSchema):
18    phone = Phone()
19
20class Person(colander.MappingSchema):
21    name = colander.SchemaNode(colander.String())
22    age = colander.SchemaNode(colander.Int(),
23                              validator=colander.Range(0, 200))
24    friends = Friends()
25    phones = Phones()

Let's now use this schema to try to deserialize some concrete data structures.

Each of these concrete data structures is called a [cstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-cstruct). "cstruct" is an abbreviation of "colander structure": you can think of a cstruct as a serialized representation of some application data. A "cstruct" is usually generated by the [`colander.SchemaNode.serialize()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.serialize "colander.SchemaNode.serialize") method, and is converted back into an application structure (aka [appstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-appstruct)) via [`colander.SchemaNode.deserialize()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.deserialize "colander.SchemaNode.deserialize").

### Deserializing A Valid Serialization[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#deserializing-a-valid-serialization "Link to this heading")

1cstruct = {
2    'name': 'keith',
3    'age': '20',
4    'friends': [('1', 'jim'), ('2', 'bob'), ('3', 'joe'), ('4', 'fred')],
5    'phones': [{'location': 'home', 'number': '555-1212'},
6               {'location': 'work', 'number': '555-8989'}],
7}
8schema = Person()
9deserialized = schema.deserialize(cstruct)

When `schema.deserialize(cstruct)` is called, because all the data in the schema is valid, and the structure represented by `cstruct` conforms to the schema, `deserialized` will be the following:

1{
2    'name': 'keith',
3    'age': 20,
4    'friends': [(1, 'jim'), (2, 'bob'), (3, 'joe'), (4, 'fred')],
5    'phones': [{'location': 'home', 'number': '555-1212'},
6               {'location': 'work', 'number': '555-8989'}],
7}

Note that all the friend rankings have been converted to integers, likewise for the age.

### Deserializing An Invalid Serialization[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#deserializing-an-invalid-serialization "Link to this heading")

Below, the `cstruct` structure has some problems. The `age` is a negative number. The rank for `bob` is `t` which is not a valid integer. The `location` of the first phone is `bar`, which is not a valid location (it is not one of "work" or "home"). What happens when a cstruct cannot be deserialized due to a data type error or a validation error?

 1import colander
 2
 3cstruct = {
 4    'name': 'keith',
 5    'age': '-1',
 6    'friends': [('1', 'jim'), ('t', 'bob'), ('3', 'joe'), ('4', 'fred')],
 7    'phones': [{'location': 'bar', 'number': '555-1212'},
 8               {'location': 'work', 'number': '555-8989'}],
 9}
10schema = Person()
11schema.deserialize(cstruct)

The `deserialize` method will raise an exception, and the `except` clause above will be invoked, causing an error message to be printed. It will print something like:

1Invalid: {'age': '-1 is less than minimum value 0',
2          'friends.1.0': '"t" is not a number',
3          'phones.0.location': '"bar" is not one of "home", "work"'}

The above error is telling us that:

*   The top-level age variable failed validation.

*   Bob's rank (the Friend tuple name `bob`'s zeroth element) is not a valid number.

*   The zeroth phone number has a bad location: it should be one of "home" or "work".

We can optionally catch the exception raised and obtain the raw error dictionary:

 1import colander
 2
 3cstruct = {
 4    'name': 'keith',
 5    'age': '-1',
 6    'friends': [('1', 'jim'), ('t', 'bob'), ('3', 'joe'), ('4', 'fred')],
 7    'phones': [{'location': 'bar', 'number': '555-1212'},
 8               {'location': 'work', 'number': '555-8989'}],
 9}
10schema = Person()
11try:
12    schema.deserialize(cstruct)
13except colander.Invalid, e:
14    errors = e.asdict()
15    print errors

This will print something like:

1{'age': '-1 is less than minimum value 0',
2 'friends.1.0': '"t" is not a number',
3 'phones.0.location': '"bar" is not one of "home", "work"'}

### [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") Exceptions[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#colander-invalid-exceptions "Link to this heading")

The exceptions raised by Colander during deserialization are instances of the [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exception class. We saw previously that instances of this exception class have a [`colander.Invalid.asdict()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid.asdict "colander.Invalid.asdict") method which returns a dictionary of error messages. This dictionary is composed by Colander by walking the _exception tree_. The exception tree is composed entirely of [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exceptions.

While the [`colander.Invalid.asdict()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid.asdict "colander.Invalid.asdict") method is useful for simple error reporting, a more complex application, such as a form library that uses Colander as an underlying schema system, may need to do error reporting in a different way. In particular, such a system may need to present the errors next to a field in a form. It may need to translate error messages to another language. To do these things effectively, it will almost certainly need to walk and introspect the exception graph manually.

The [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exceptions raised by Colander validation are very rich. They contain detailed information about the circumstances of an error. If you write a system based on Colander that needs to display and format Colander exceptions specially, you will need to get comfy with the Invalid exception API.

When a validation-related error occurs during deserialization, each node in the schema that had an error (and any of its parents) will be represented by a corresponding [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exception. To support this behavior, each [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exception has a `children` attribute which is a list. Each element in this list (if any) will also be an [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exception, recursively, representing the error circumstances for a particular schema deserialization.

Each exception in the graph has a `msg` attribute, which will either be the value `None`, a `str` or `unicode` object, or a _translation string_ instance representing a freeform error value set by a particular type during an unsuccessful deserialization. Exceptions that exist purely for structure will have a `msg` attribute with the value `None`. Each exception instance will also have an attribute named `node`, representing the schema node to which the exception is related.

Note

Translation strings are objects which behave like Unicode objects but have extra metadata associated with them for use in translation systems. See [https://docs.pylonsproject.org/projects/translationstring/en/latest/](https://docs.pylonsproject.org/projects/translationstring/en/latest/) for documentation about translation strings. All error messages used by Colander internally are translation strings, which means they can be translated to other languages. In particular, they are suitable for use as gettext _message ids_.

See the [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") API documentation for more information.

### Preparing deserialized data for validation[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#preparing-deserialized-data-for-validation "Link to this heading")

In certain circumstances, it is necessary to modify the deserialized value before validating it.

For example, a [`String`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.String "colander.String") node may be required to contain content, but that content may come from a rich text editor. Such an editor may return `<b></b>` which may appear to be valid but doesn't contain content, or `<a href="javascript:alert('evil'')">good</a>` which is valid, but only after some processing.

The following schema uses [htmllaundry](https://pypi.org/project/htmllaundry/) and a [`Preparer`](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html#colander.interfaces.Preparer "colander.interfaces.Preparer") to do the correct thing in both cases:

1import colander
2import htmllaundry
3
4class Page(colander.MappingSchema):
5    title = colander.SchemaNode(colander.String())
6    content = colander.SchemaNode(colander.String(),
7                                  preparer=htmllaundry.sanitize,
8                                  validator=colander.Length(1))

You can even specify multiple preparers to be run in order, by passing a list of functions to the preparer kwarg, like so:

 1import colander
 2# removes whitespace, newlines, and tabs from the beginning/end of a string
 3strip_whitespace = lambda v: v.strip(' \t\n\r') if v is not None else v
 4# replaces multiple spaces with a single space
 5remove_multiple_spaces = lambda v: re.sub(' +', ' ', v)
 6
 7class Page(colander.MappingSchema):
 8    title = colander.SchemaNode(colander.String())
 9    content = colander.SchemaNode(
10        colander.String(),
11        preparer=[strip_whitespace, remove_multiple_spaces],
12        validator=colander.Length(1))

Serialization[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#serialization "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

Serializing a data structure is obviously the inverse operation from deserializing a data structure. The [`colander.SchemaNode.serialize()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.serialize "colander.SchemaNode.serialize") method of a schema performs serialization of application data (aka an [appstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-appstruct)). If you pass the [`colander.SchemaNode.serialize()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.serialize "colander.SchemaNode.serialize") method data that can be understood by the schema types in the schema you're calling it against, you will be returned a data structure of serialized values.

For example, given the following schema:

1import colander
2
3class Person(colander.MappingSchema):
4    name = colander.SchemaNode(colander.String())
5    age = colander.SchemaNode(colander.Int(),
6                              validator=colander.Range(0, 200))

We can serialize a matching data structure:

1  appstruct = {'age': 20, 'name': 'Bob'}
2  schema = Person()
3  serialized = schema.serialize(appstruct)

The value for `serialized` above will be 
```
{'age': '20',
'name': 'Bob'}
```
. Note that the `age` integer has become a string.

Serialization and deserialization are not completely symmetric, however. Although schema-driven data conversion happens during serialization, and default values are injected as necessary, [`colander`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#module-colander "colander") types are defined in such a way that structural validation and validation of values does _not_ happen as it does during deserialization. For example, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is substituted into the cstruct for every missing subvalue in an appstruct, and none of the validators associated with the schema or any of is nodes is invoked.

This usually means you may "partially" serialize an appstruct where some of the values are missing. If we try to serialize partial data using the `serialize` method of the schema:

1  appstruct = {'age': 20}
2  schema = Person()
3  serialized = schema.serialize(appstruct)

The value for `serialized` above will be 
```
{'age': '20',
'name': colander.null}
```
. Note the `age` integer has become a string, and the missing `name` attribute has been replaced with [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null"). Above, even though we did not include the `name` attribute in the appstruct we fed to `serialize`, an error is _not_ raised. For more information about [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") substitution during serialization, see [Serializing The Null Value](https://docs.pylonsproject.org/projects/colander/en/latest/null_and_drop.html#serializing-null).

The corollary: it is the responsibility of the developer to ensure they serialize "the right" data; [`colander`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#module-colander "colander") will not raise an error when asked to serialize something that is partially nonsense.

Inheriting Schemas[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#inheriting-schemas "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

Note

This feature is new as of Colander 0.9.9.

One class-based schema can be inherited from another. For example:

import colander
import pprint

class Friend(colander.MappingSchema):
    rank = colander.SchemaNode(
        colander.Int(),
        )
    name = colander.SchemaNode(
        colander.String(),
        )

class SpecialFriend(Friend):
    iwannacomefirst = colander.SchemaNode(
        colander.String(),
        insert_before='rank',
        )
    another = colander.SchemaNode(
        colander.String(),
        )

class SuperSpecialFriend(SpecialFriend):
    iwannacomefirst = colander.SchemaNode(
        colander.Int(),
        )

friend = SuperSpecialFriend()
pprint.pprint([(x, x.typ) for x in friend.children])

Here's what's printed when the above is run:

[(<colander.SchemaNode object at 38407568 (named iwannacomefirst)>,
  <colander.Integer object at 0x24a0d10>),
 (<colander.SchemaNode object at 37016144 (named rank)>,
  <colander.Integer object at 0x7f17c5606710>),
 (<colander.SchemaNode object at 37017424 (named name)>,
  <colander.String object at 0x234d610>),
 (<colander.SchemaNode object at 38407184 (named another)>,
  <colander.String object at 0x2359250>)]

Multiple inheritance also works:

import colander
import pprint

class One(colander.MappingSchema):
    a = colander.SchemaNode(colander.Int())
    b = colander.SchemaNode(colander.Int())

class Two(colander.MappingSchema):
    a = colander.SchemaNode(colander.String())
    c = colander.SchemaNode(colander.String())

class Three(One, Two):
    b = colander.SchemaNode(colander.Bool())
    d = colander.SchemaNode(colander.Bool())

s = Three()
pprint.pprint([(x, x.typ) for x in s.children])

Here's what's printed when the above is run:

[(<colander.SchemaNode object at 14868560 (named a)>,
  <colander.Integer object at 0xe25f90>),
 (<colander.SchemaNode object at 14868816 (named c)>,
  <colander.String object at 0xe2e110>),
 (<colander.SchemaNode object at 14868688 (named b)>,
  <colander.Boolean object at 0xe2e090>),
 (<colander.SchemaNode object at 14868944 (named d)>,
  <colander.Boolean object at 0xe2e190>)]

Note

The order of the children in the output above might seem suprising: it is governed by how Python's multiple-inheritance works (the `__mro__` order).

This feature only works with mapping schemas. A "mapping schema" is schema defined as a class which inherits from [`colander.Schema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Schema "colander.Schema") or [`colander.MappingSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.MappingSchema "colander.MappingSchema").

Ordering of child schema nodes when inheritance is used works like this: the "deepest" SchemaNode class in the MRO of the inheritance chain is consulted first for nodes, then the next deepest, then the next, and so on. So the deepest class' nodes come first in the relative ordering of schema nodes, then the next deepest, and so on. For example:

class One(colander.MappingSchema):
    a = colander.SchemaNode(colander.String(), id='a1')
    b = colander.SchemaNode(colander.String(), id='b1')
    d = colander.SchemaNode(colander.String(), id='d1')

class Two(One):
    a = colander.SchemaNode(colander.String(), id='a2')
    c = colander.SchemaNode(colander.String(), id='c2')
    e = colander.SchemaNode(colander.String(), id='e2')

class Three(Two):
    b = colander.SchemaNode(colander.String(), id='b3')
    d = colander.SchemaNode(colander.String(), id='d3')
    f = colander.SchemaNode(colander.String(), id='f3')

three = Three()

The ordering of child nodes computed in the schema node `three` will be `['a2', 'b3', 'd3', 'c2', 'e2', 'f3']`. The ordering starts `a1`, `b1`, `d1` because that's the ordering of nodes in `One`, and `One` is the deepest SchemaNode in the inheritance hierarchy. Then it processes the nodes attached to `Two`, the next deepest, which causes `a1` to be replaced by `a2`, and `c2` and `e2` to be appended to the node list. Then finally it processes the nodes attached to `Three`, which causes `b1` to be replaced by `b3`, and `d1` to be replaced by `d3`, then finally `f` is appended.

Multiple inheritance works the same way:

class One(colander.MappingSchema):
    a = colander.SchemaNode(colander.String(), id='a1')
    b = colander.SchemaNode(colander.String(), id='b1')
    d = colander.SchemaNode(colander.String(), id='d1')

class Two(colander.MappingSchema):
    a = colander.SchemaNode(colander.String(), id='a2')
    c = colander.SchemaNode(colander.String(), id='c2')
    e = colander.SchemaNode(colander.String(), id='e2')

class Three(Two, One):
    b = colander.SchemaNode(colander.String(), id='b3')
    d = colander.SchemaNode(colander.String(), id='d3')
    f = colander.SchemaNode(colander.String(), id='f3')

three = Three()

The resulting node ordering of `three` is the same as the single inheritance example: `['a2', 'b3', 'd3', 'c2', 'e2', 'f3']` due to the MRO deepest-first ordering (`One`, then `Two`, then `Three`).

The behavior of subclassing one mapping schema using another is as follows:

*   A node declared in a subclass of a mapping schema overrides any node with the same name inherited from any superclass. The node remains at the child order of the superclass node unless the subclass node defines an `insert_before` value.

*   A node declared in a subclass of a mapping schema with a name that doesn't override any node in a superclass will be placed _after_ all nodes defined in all superclasses unless the subclass node defines an `insert_before` value. You can think of it like this: nodes added in subclasses will _follow_ nodes added in superclasses unless the node is already defined in any of those superclasses.

An `insert_before` keyword argument may be passed to the SchemaNode constructor of mapping schema child nodes. This is a string which influences the node's position in its mapping schema. The node will be inserted into the mapping schema before the node named by `insert_before`. An `insert_before` value must match the name of a schema node in a superclass or it must match the name of a schema node already defined in the class; it cannot name a schema node in a subclass, and it cannot name a schema node in the same class that hasn't already been defined. If an `insert_before` is provided that doesn't match any existing node name, a `KeyError` is raised.

If a schema node name conflicts with a schema value attribute name on the same class in a [`colander.MappingSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.MappingSchema "colander.MappingSchema"), [`colander.TupleSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.TupleSchema "colander.TupleSchema") or [`colander.SequenceSchema`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SequenceSchema "colander.SequenceSchema") definition, you can work around this by giving the schema node a bogus name in the class definition but providing a correct `name` argument to the schema node constructor:

from colander import SchemaNode, MappingSchema

class SomeSchema(MappingSchema):
    title = 'Some Schema'
    thisnamewillbeignored = colander.SchemaNode(
        colander.String(),
        name='title')

Note that such a workaround is only required if the conflicting names are attached to the _exact same_ class definition. Colander scrapes off schema node definitions at each class' construction time, so it's not an issue for inherited values. For example:

from colander import SchemaNode, MappingSchema

class SomeSchema(MappingSchema):
    title = colander.SchemaNode(colander.String())

class AnotherSchema(SomeSchema):
    title = 'Some Schema'

schema = AnotherSchema()

In the above example, even though the `title = 'Some Schema'` appears to override the superclass' `title` SchemaNode, a `title` SchemaNode will indeed be present in the child list of the `schema` instance (`schema['title']` will return the `title` SchemaNode) and the schema's `title` attribute will be `Some Schema` (`schema.title` will return `Some Schema`).

Defining A Schema Declaratively[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#defining-a-schema-declaratively "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Previously, we defined the schema in such a way that the individual sequences and mappings within the schema could be re-used in different schemas. If all nodes within a schema are only likely to be used in that schema, then the schema definition can be made more succinct using the [`instantiate`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.instantiate "colander.instantiate") class decorator as shown below:

 1import colander
 2
 3class Person(colander.MappingSchema):
 4    name = colander.SchemaNode(colander.String())
 5    age = colander.SchemaNode(colander.Int(),
 6                              validator=colander.Range(0, 200))
 7
 8    @colander.instantiate()
 9    class friends(colander.SequenceSchema):
10
11        @colander.instantiate()
12        class friend(colander.TupleSchema):
13            rank = colander.SchemaNode(colander.Int(),
14                                       validator=colander.Range(0, 9999))
15            name = colander.SchemaNode(colander.String())
16
17    @colander.instantiate()
18    class phones(colander.SequenceSchema):
19
20        @colander.instantiate()
21        class phone(colander.MappingSchema):
22            location = colander.SchemaNode(
23                colander.String(),
24                validator=colander.OneOf(['home', 'work']))
25            number = colander.SchemaNode(colander.String())

If you need to pass parameters when using this style of schema definition, such as a `missing` value to a `SchemaNode` during instantiation, you can pass these as parameters to [`instantiate`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.instantiate "colander.instantiate"). For example, if we wanted to limit the number of friends a person can have, and cater for people who have no friends, we could adjust the schema as shown below:

1class Person(colander.MappingSchema):
2
3    @colander.instantiate(missing=(),
4                          validator=colander.Length(max=5))
5    class friends(colander.SequenceSchema):
6
7        @colander.instantiate()
8        class friend(colander.TupleSchema):
9            name = colander.SchemaNode(colander.String())

Defining A Schema Imperatively[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#defining-a-schema-imperatively "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

The above schema we defined was defined declaratively via a set of `class` statements. It's often useful to create schemas more dynamically. For this reason, Colander offers an "imperative" mode of schema configuration. Here's our previous declarative schema:

 1import colander
 2
 3class Friend(colander.TupleSchema):
 4    rank = colander.SchemaNode(colander.Int(),
 5                               validator=colander.Range(0, 9999))
 6    name = colander.SchemaNode(colander.String())
 7
 8class Phone(colander.MappingSchema):
 9    location = colander.SchemaNode(colander.String(),
10                                   validator=colander.OneOf(['home', 'work']))
11    number = colander.SchemaNode(colander.String())
12
13class Friends(colander.SequenceSchema):
14    friend = Friend()
15
16class Phones(colander.SequenceSchema):
17    phone = Phone()
18
19class Person(colander.MappingSchema):
20    name = colander.SchemaNode(colander.String())
21    age = colander.SchemaNode(colander.Int(),
22                              validator=colander.Range(0, 200))
23    friends = Friends()
24    phones = Phones()

We can imperatively construct a completely equivalent schema like so:

 1import colander
 2
 3friend = colander.SchemaNode(colander.Tuple())
 4friend.add(colander.SchemaNode(colander.Int(),
 5                               validator=colander.Range(0, 9999),
 6           name='rank'))
 7friend.add(colander.SchemaNode(colander.String(), name='name'))
 8
 9phone = colander.SchemaNode(
10    colander.Mapping(),
11    colander.SchemaNode(
12        colander.String(),
13        validator=colander.OneOf(['home', 'work']),
14        name='location'))
15phone.add(colander.SchemaNode(colander.String(), name='number'))
16
17schema = colander.SchemaNode(colander.Mapping())
18schema.add(colander.SchemaNode(colander.String(), name='name'))
19schema.add(colander.SchemaNode(colander.Int(), name='age',
20                               validator=colander.Range(0, 200)))
21schema.add(colander.SequenceSchema(friend, name='friends'))
22schema.add(colander.SequenceSchema(phone, name='phones'))

Defining a schema imperatively is a lot uglier than defining a schema declaratively, but it's often more useful when you need to define a schema dynamically. Perhaps in the body of a function or method you may need to disinclude a particular schema field based on a business condition; when you define a schema imperatively, you have more opportunity to control the schema composition.

Serializing and deserializing using a schema created imperatively is done exactly the same way as you would serialize or deserialize using a schema created declaratively:

1data = {
2    'name': 'keith',
3    'age': '20',
4    'friends': [('1', 'jim'), ('2', 'bob'), ('3', 'joe'), ('4', 'fred')],
5    'phones': [{'location': 'home', 'number': '555-1212'},
6               {'location': 'work', 'number': '555-8989'}],
7}
8deserialized = schema.deserialize(data)

Gotchas[¶](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#gotchas "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

You may be using a module scope schema definition with the expectation that calling a [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") constructor will clone all of its subnodes. This is not the case.

For example, in a Python module, you might have code that looks like this:

from colander import SchemaNode, MappingSchema
from colander import Int

class MySchema1(MappingSchema):
    a = SchemaNode(Int())
class MySchema2(MappingSchema):
    b = MySchema1()

def afunction():
    s = MySchema2()
    s['a'].add(SchemaNode(Int(), name='c'))

Because you're mutating `a` (by appending a child node to it via the [`colander.SchemaNode.add()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.add "colander.SchemaNode.add") method) you are probably expecting that you are working with a _copy_ of `a`. This is incorrect: you're mutating the module-scope copy of the `a` instance defined within the `MySchema1` class. This is almost certainly not what you mean to do. The symptom of making such a mistake might be that multiple `c` nodes are added as children of `a` over the course of the Python process lifetime.

To get around this, use the [`colander.SchemaNode.clone()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.clone "colander.SchemaNode.clone") method to create a deep copy of an instance of a schema otherwise defined at module scope before mutating any of its subnodes:

def afunction():
    s = MySchema2().clone()
    s['a'].add(SchemaNode(Int(), name='c'))

[`colander.SchemaNode.clone()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.clone "colander.SchemaNode.clone") clones all the nodes in the schema, so you can work with a "deep copy" of the schema without disturbing the "template" schema nodes defined at a higher scope.
