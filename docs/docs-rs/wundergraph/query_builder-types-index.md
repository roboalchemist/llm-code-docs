wundergraph::query_builder
# Module types 
Source 
## Structs§
HasManyType used to indicate that a given field references multiple other entities
by a given idPlaceHolderA wrapper type used inside of wundergraph to load values of the type T
from the database
## Enums§
HasOneType used to indicate that a given field references a single
other entity by id
## Traits§
ResolveWundergraphFieldValueA internal helper trait indicating how to resolve a given type while query
executionWundergraphValueA marker trait indicating that a type could be used with wundergraph
## Derive Macros§
WundergraphValueA custom derive to add support for a custom enum type