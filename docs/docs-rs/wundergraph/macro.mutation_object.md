wundergraph
# Macro mutation_object 
Source 

```
macro_rules! mutation_object {
    (
        $(#[doc = $glob_doc: expr])*
        $mutation_name: ident {
            $($entity_name: ident (
                $(insert = $insert: ident)?
                $($(,)? update = $update: ident)?
                $($(,)? delete = $delete: ident)?
                $(,)?
            )$(,)?)*
        }
    ) => { ... };
}
```