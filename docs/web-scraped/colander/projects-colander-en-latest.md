# Source: https://docs.pylonsproject.org/projects/colander/en/latest/

Title: Colander — colander 2.0 documentation

URL Source: https://docs.pylonsproject.org/projects/colander/en/latest/

Markdown Content:
Colander is useful as a system for validating and deserializing data obtained via XML, JSON, an HTML form post or any other equally simple data serialization. It is tested on Python 2.7, 3.5, 3.6, 3.7, 3.8, 3.9, and 3.10, and PyPy 2.7 and PyPy 3.8. Colander can be used to:

*   Define a data schema.

*   Deserialize a data structure composed of strings, mappings, and lists into an arbitrary Python structure after validating the data structure against a data schema.

*   Serialize an arbitrary Python structure to a data structure composed of strings, mappings, and lists.

Colander is a good basis for form generation systems, data description systems, and configuration systems.

Out of the box, Colander can serialize and deserialize various types of objects, including:

*   A mapping object (e.g. dictionary).

*   A variable-length sequence of objects (each object is of the same type).

*   A fixed-length tuple of objects (each object is of a different type).

*   A string or Unicode object.

*   An integer.

*   A float.

*   A decimal float.

*   A boolean.

*   An importable Python object (to a dotted Python object path).

*   A Python `datetime.datetime` object.

*   A Python `datetime.date` object.

*   A Python `enum.Enum` object.

Colander allows additional data structures to be serialized and deserialized by allowing a developer to define new "types".

The error messages used by Colander's default types are internationalizable.

*   [Colander Basics](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html)
    *   [Defining A Colander Schema](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#defining-a-colander-schema)
    *   [Deserialization](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#deserialization)
    *   [Serialization](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#serialization)
    *   [Inheriting Schemas](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#inheriting-schemas)
    *   [Defining A Schema Declaratively](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#defining-a-schema-declaratively)
    *   [Defining A Schema Imperatively](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#defining-a-schema-imperatively)
    *   [Gotchas](https://docs.pylonsproject.org/projects/colander/en/latest/basics.html#gotchas)

*   [The Null and Drop Values](https://docs.pylonsproject.org/projects/colander/en/latest/null_and_drop.html)
    *   [Serializing The Null Value](https://docs.pylonsproject.org/projects/colander/en/latest/null_and_drop.html#serializing-the-null-value)
    *   [Deserializing The Null Value](https://docs.pylonsproject.org/projects/colander/en/latest/null_and_drop.html#deserializing-the-null-value)

*   [Extending Colander](https://docs.pylonsproject.org/projects/colander/en/latest/extending.html)
    *   [Defining a New Type](https://docs.pylonsproject.org/projects/colander/en/latest/extending.html#defining-a-new-type)
    *   [Defining a New Validator](https://docs.pylonsproject.org/projects/colander/en/latest/extending.html#defining-a-new-validator)

*   [Schema Binding](https://docs.pylonsproject.org/projects/colander/en/latest/binding.html)
    *   [What Is Schema Binding?](https://docs.pylonsproject.org/projects/colander/en/latest/binding.html#what-is-schema-binding)
    *   [An Example](https://docs.pylonsproject.org/projects/colander/en/latest/binding.html#an-example)
    *   [`after_bind`](https://docs.pylonsproject.org/projects/colander/en/latest/binding.html#after-bind)
    *   [Unbound Schemas With Deferreds](https://docs.pylonsproject.org/projects/colander/en/latest/binding.html#unbound-schemas-with-deferreds)
    *   [See Also](https://docs.pylonsproject.org/projects/colander/en/latest/binding.html#see-also)

*   [Manipulating Data Structures](https://docs.pylonsproject.org/projects/colander/en/latest/manipulation.html)
    *   [Flattening a Data Structure](https://docs.pylonsproject.org/projects/colander/en/latest/manipulation.html#flattening-a-data-structure)
    *   [Accessing and Mutating Nodes in a Data Structure](https://docs.pylonsproject.org/projects/colander/en/latest/manipulation.html#accessing-and-mutating-nodes-in-a-data-structure)

*   [Interfaces](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html)
    *   [`Preparer()`](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html#colander.interfaces.Preparer)
    *   [`Validator()`](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html#colander.interfaces.Validator)
    *   [`Type`](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html#colander.interfaces.Type)

*   [Colander API](https://docs.pylonsproject.org/projects/colander/en/latest/api.html)
    *   [Exceptions](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#module-colander)
    *   [Validators](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#validators)
    *   [Types](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#types)
    *   [Schema-Related](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#schema-related)

*   [Glossary](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html)
*   [Change History](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html)
    *   [2.1 (unreleased)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#unreleased)
    *   [2.0 (2022-01-02)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id1)
    *   [1.8.3 (2020-11-28)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id2)
    *   [1.8.2 (2020-08-07)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id3)
    *   [1.8.1 (2020-08-06)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id4)
    *   [1.8.0 (2020-08-05)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id5)
    *   [1.7.0 (2019-02-01)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id6)
    *   [1.6.0 (2019-01-31)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id7)
    *   [1.5.1 (2018-09-10)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id8)
    *   [1.5.0 (2018-09-07)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id9)
    *   [1.4.0 (2017-07-31)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id10)
    *   [1.3.3 (2017-04-25)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id11)
    *   [1.3.2 (2017-01-31)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id12)
    *   [1.3.1 (2016-05-23)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id13)
    *   [1.3 (2016-05-23)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id14)
    *   [1.2 (2016-01-18)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id15)
    *   [1.1 (2016-01-15)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id16)
    *   [1.0 (2014-11-26)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id21)
    *   [1.0b1 (2013-09-01)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#b1-2013-09-01)
    *   [1.0a5 (2013-05-31)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#a5-2013-05-31)
    *   [1.0a4 (2013-05-21)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#a4-2013-05-21)
    *   [1.0a3 (2013-05-16)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#a3-2013-05-16)
    *   [1.0a2 (2013-01-30)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#a2-2013-01-30)
    *   [1.0a1 (2013-01-10)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#a1-2013-01-10)
    *   [0.9.9 (2012-09-24)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id32)
    *   [0.9.8 (2012-04-27)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id35)
    *   [0.9.7 (2012-03-20)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id36)
    *   [0.9.6 (2012-02-14)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id37)
    *   [0.9.5 (2012-01-13)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id38)
    *   [0.9.4 (2011-10-14)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id39)
    *   [0.9.3 (2011-06-23)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id40)
    *   [0.9.2 (2011-03-28)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id41)
    *   [0.9.1 (2010-12-02)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id42)
    *   [0.9 (2010-11-28)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id43)
    *   [0.8 (2010/09/08)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id44)
    *   [0.7.3 (2010/09/02)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id45)
    *   [0.7.2 (2010/08/30)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id46)
    *   [0.7.1 (2010/06/12)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id47)
    *   [0.7.0](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id48)
    *   [0.6.2 (2010-05-08)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id50)
    *   [0.6.1 (2010-05-04)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id51)
    *   [0.6.0 (2010-05-02)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id52)
    *   [0.5.2 (2010-04-09)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id53)
    *   [0.5.1 (2010-04-02)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id54)
    *   [0.5 (2010-03-31)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id55)
    *   [0.4 (2010-03-30)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id56)
    *   [0.3 (2010-03-29)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id57)
    *   [0.2 (2010-03-23)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id58)
    *   [0.1 (2010-03-14)](https://docs.pylonsproject.org/projects/colander/en/latest/changes.html#id59)

Indices and tables[¶](https://docs.pylonsproject.org/projects/colander/en/latest/#indices-and-tables "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------

*   [Index](https://docs.pylonsproject.org/projects/colander/en/latest/genindex.html)

*   [Module Index](https://docs.pylonsproject.org/projects/colander/en/latest/py-modindex.html)

*   [Search Page](https://docs.pylonsproject.org/projects/colander/en/latest/search.html)
