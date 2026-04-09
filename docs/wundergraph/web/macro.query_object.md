wundergraph
# Macro query_object 
Source 

```
macro_rules! query_object {
    (
        $(#[doc = $glob_doc: expr])*
        $query_name: ident {
            $(
                $(#[$($meta: tt)*])*
                $graphql_struct: ident$((
                        $($(#[wundergraph(default = $arg_default: expr)])? $arg: ident : $arg_ty: ty $(,)?)*
                ))?$(,)?)*
        }
    ) => { ... };
}
```