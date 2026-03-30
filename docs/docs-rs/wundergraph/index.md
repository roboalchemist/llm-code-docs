# Crate wundergraph 
Source 
## Modules§
diesel_extA module containing extension traits for various diesel typeserrorThis module contains all error handling related functionality in wundergraphhelperA module containing various helper traits and types mostly useful
to work with tuples at compile timejuniper_extA module containing juniper specific extension traitspreludeRe-exports important traits and types. Meant to be glob imported
when using wundergraph.query_builderThis module contains functionality used by wundergraph
to convert a GraphQL request as sql query.scalarA module containing a wundergraph specific juniper scalar value implementation
## Macros§
mutation_objectMacro to register the main mutation objectquery_objectMacro to register the main query object
## Derive Macros§
WundergraphEntityA custom derive to implement all wundergraph related traits for a entity
Using this trait implies internally `#[derive(WundergraphBelongsTo)]`
and `#[derive(BuildFilterHelper)]`