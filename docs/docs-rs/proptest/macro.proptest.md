proptest
# Macro proptest 
Source 

```
macro_rules! proptest {
    (#![proptest_config($config:expr)]
     $(
        $(#[$meta:meta])*
       fn $test_name:ident($($parm:pat in $strategy:expr),+ $(,)?) $body:block
    )*) => { ... };
    (#![proptest_config($config:expr)]
     $(
        $(#[$meta:meta])*
        fn $test_name:ident($($arg:tt)+) $body:block
    )*) => { ... };
    ($(
        $(#[$meta:meta])*
        fn $test_name:ident($($parm:pat in $strategy:expr),+ $(,)?) $body:block
    )*) => { ... };
    ($(
        $(#[$meta:meta])*
        fn $test_name:ident($($arg:tt)+) $body:block
    )*) => { ... };
    (|($($parm:pat in $strategy:expr),+ $(,)?)| $body:expr) => { ... };
    (move |($($parm:pat in $strategy:expr),+ $(,)?)| $body:expr) => { ... };
    (|($($arg:tt)+)| $body:expr) => { ... };
    (move |($($arg:tt)+)| $body:expr) => { ... };
    ($config:expr, |($($parm:pat in $strategy:expr),+ $(,)?)| $body:expr) => { ... };
    ($config:expr, move |($($parm:pat in $strategy:expr),+ $(,)?)| $body:expr) => { ... };
    ($config:expr, |($($arg:tt)+)| $body:expr) => { ... };
    ($config:expr, move |($($arg:tt)+)| $body:expr) => { ... };
}
```