wundergraph::query_builder::selection
# Module filter 
Source 
## Modules§
collectorThis module contains helper types to combine multiple filter expressions
into a final expression
## Structs§
FilterMain filter structFilterOptionThis struct summarize all possible filter operations for a given graphql
field
## Traits§
AsColumnFilterMarker trait indicating that some value has a filter that is
applied to a specific  database columnAsNonColumnFilterMarker trait indicating that some value has a filter
that is not attached to a columnBuildFilterA trait that indicates that some type could be converted into a sql filter
operation.BuildFilterHelperA helper trait describing a single node of a filter argumentCreateFilterHelper trait to build a compound filter from filter nodes
that exist for each fieldFilterValueA fundamental trait marking that a filter could be constructed for a given typeInnerFilterA trait marking that some type is part of a filter
## Derive Macros§
BuildFilterHelperA custom derive to implement the `BuildFilterHelper` trait