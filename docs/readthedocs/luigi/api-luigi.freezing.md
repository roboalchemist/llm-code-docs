# luigi.freezing

Internal-only module with immutable data structures.

Please, do not use it outside of Luigi codebase itself.

Functions

`recursively_freeze`(value)

Recursively walks `Mapping``s and ``list``s and converts them to ``FrozenOrderedDict` and `tuples`, respectively.

`recursively_unfreeze`(value)

Recursively walks `FrozenOrderedDict``s and ``tuple``s and converts them to ``dict` and `list`, respectively.

Classes

`FrozenOrderedDict`(*args, **kwargs)

It is an immutable wrapper around ordered dictionaries that implements the complete `collections.Mapping` interface.

class luigi.freezing.FrozenOrderedDict(**args*, ***kwargs*)

It is an immutable wrapper around ordered dictionaries that implements the complete `collections.Mapping`
interface. It can be used as a drop-in replacement for dictionaries where immutability and ordering are desired.

get_wrapped()

luigi.freezing.recursively_freeze(*value*)

Recursively walks `Mapping``s and ``list``s and converts them to ``FrozenOrderedDict` and `tuples`, respectively.

luigi.freezing.recursively_unfreeze(*value*)

Recursively walks `FrozenOrderedDict``s and ``tuple``s and converts them to ``dict` and `list`, respectively.