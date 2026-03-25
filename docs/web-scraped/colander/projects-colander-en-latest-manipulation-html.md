# Source: https://docs.pylonsproject.org/projects/colander/en/latest/manipulation.html

Title: Manipulating Data Structures — colander 2.0 documentation

URL Source: https://docs.pylonsproject.org/projects/colander/en/latest/manipulation.html

Markdown Content:
Colander schemas have some utility functions which can be used to manipulate an [appstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-appstruct) or a [cstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-cstruct). Nested data structures can be flattened into a single dictionary or a single flattened dictionary can be used to produce a nested data structure. Values of particular nodes can also be set or retrieved based on a flattened path spec.

Flattening a Data Structure[¶](https://docs.pylonsproject.org/projects/colander/en/latest/manipulation.html#flattening-a-data-structure "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

[`colander.SchemaNode.flatten()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.flatten "colander.SchemaNode.flatten") can be used to convert a datastructure with nested dictionaries and/or lists into a single flattened dictionary where each key in the dictionary is a dotted name path to the node in the nested structure.

Consider the following schema:

 1import colander
 2
 3class Friend(colander.TupleSchema):
 4    rank = colander.SchemaNode(colander.Int(),
 5                               validator=colander.Range(0, 9999))
 6    name = colander.SchemaNode(colander.String())
 7
 8class Phone(colander.MappingSchema):
 9    location = colander.SchemaNode(colander.String(),
10                                  validator=colander.OneOf(['home', 'work']))
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
22                             validator=colander.Range(0, 200))
23    friends = Friends()
24    phones = Phones()

Consider also a particular serialization of data using that schema:

1  appstruct = {
2  'name':'keith',
3  'age':20,
4  'friends':[(1, 'jim'),(2, 'bob'), (3, 'joe'), (4, 'fred')],
5  'phones':[{'location':'home', 'number':'555-1212'},
6            {'location':'work', 'number':'555-8989'},],
7  }

This data can be flattened:

1  schema = Person()
2  fstruct = schema.flatten(appstruct)

The resulting flattened structure would look like this:

 1  {
 2  'name': 'keith',
 3  'age': 20,
 4  'friends.0.rank': 1,
 5  'friends.0.name': 'jim',
 6  'friends.1.rank': 2,
 7  'friends.1.name': 'bob',
 8  'friends.2.rank': 3,
 9  'friends.2.name': 'joe',
10  'friends.3.rank': 4,
11  'friends.3.name': 'fred',
12  'phones.0.location': 'home',
13  'phones.0.number': '555-1212',
14  'phones.1.location': 'work',
15  'phones.1.number': '555-8989',
16  }

The process can be reversed using [`colander.SchemaNode.unflatten()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.unflatten "colander.SchemaNode.unflatten"):

1  appstruct = schema.unflatten(fstruct)

Either an [appstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-appstruct) or a [cstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-cstruct) can be flattened or unflattened in this way.

Accessing and Mutating Nodes in a Data Structure[¶](https://docs.pylonsproject.org/projects/colander/en/latest/manipulation.html#accessing-and-mutating-nodes-in-a-data-structure "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`colander.SchemaNode.get_value`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.get_value "colander.SchemaNode.get_value") and [`colander.SchemaNode.set_value`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.set_value "colander.SchemaNode.set_value") can be used to access and mutate nodes in an [appstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-appstruct) or [cstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-cstruct). Using the example from above:

1  # How much do I like Joe?
2  rank = schema.get_value(appstruct, 'friends.2.rank')
3
4  # Joe bought me beer. Let's promote Joe.
5  schema.set_value(appstruct, 'friends.2.rank', rank + 5000)
