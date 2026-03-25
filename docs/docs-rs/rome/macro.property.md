rome
# Macro property 
Source 

```
macro_rules! property {
    (
    $(#[$meta:meta])*
    :$iri:expr,
    $trait_name:ident,
    $function:ident,
    $range:path,
    $pos:expr) => { ... };
}
```