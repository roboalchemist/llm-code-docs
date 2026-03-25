# Types

Types are the smallest definition of structure in Schematics.  They represent
structure by offering functions to inspect or mutate the data in some way.

According to Schematics, a type is an instance of a way to do three things:

- 

Coerce the data type into an appropriate representation in Python

- 

Convert the Python representation into other formats suitable for
serialization

- 

Offer a precise method of validating data of many forms

These properties are implemented as `to_native`, `to_primitive`, and
`validate`.

## Coercion

A simple example is the `DateTimeType`.

```
>>> from schematics.types import DateTimeType
>>> dt_t = DateTimeType()

```