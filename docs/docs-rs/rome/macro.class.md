rome
# Macro class 
Source 

```
macro_rules! class {
    (
    $(#[$meta:meta])*
    :$iri:expr,
    $name:ident,
    $pos:expr) => { ... };
}
```