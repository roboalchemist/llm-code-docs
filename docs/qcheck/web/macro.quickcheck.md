qcheck
# Macro quickcheck 
Source 

```
macro_rules! quickcheck {
    (@as_items $($i:item)*) => { ... };
    {
        $(
            $(#[$m:meta])*
            fn $fn_name:ident($($arg_name:ident : $arg_ty:ty),*) -> $ret:ty {
                $($code:tt)*
            }
        )*
    } => { ... };
}
```