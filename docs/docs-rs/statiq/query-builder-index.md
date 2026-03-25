statiq::query
# Module builder 
Source 
## Structs§
QueryBuilderRuntime query builder — wraps static SQL templates with dynamic extensions.
## Functions§
batch_insert_sqlsBuild batch INSERT SQL strings (one per row, to be executed in a transaction).filtered_sqlBuild a WHERE-filtered SELECT.paged_sqlBuild a paged SELECT from a static base SELECT SQL.