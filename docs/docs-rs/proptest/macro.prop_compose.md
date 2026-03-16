proptest
# Macro prop_compose 
Source 

```
macro_rules! prop_compose {
    ($(#[$meta:meta])*
     $vis:vis
     $([$($modi:tt)*])? fn $name:ident $params:tt
     ($($var:pat in $strategy:expr),+ $(,)?)
       -> $return_type:ty $body:block) => { ... };
    ($(#[$meta:meta])*
     $vis:vis
     $([$($modi:tt)*])? fn $name:ident $params:tt
     ($($var:pat in $strategy:expr),+ $(,)?)
     ($($var2:pat in $strategy2:expr),+ $(,)?)
       -> $return_type:ty $body:block) => { ... };
    ($(#[$meta:meta])*
     $vis:vis
     $([$($modi:tt)*])? fn $name:ident $params:tt
     ($($arg:tt)+)
       -> $return_type:ty $body:block) => { ... };
    ($(#[$meta:meta])*
     $vis:vis
     $([$($modi:tt)*])? fn $name:ident $params:tt
     ($($arg:tt)+ $(,)?)
     ($($arg2:tt)+ $(,)?)
       -> $return_type:ty $body:block) => { ... };
}
```