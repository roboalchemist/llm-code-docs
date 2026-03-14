cursive
# Macro manual_blueprint 
Source 

```
macro_rules! manual_blueprint {
    ($name:ident from $config_builder:expr) => { ... };
    (with $name:ident, $builder:expr) => { ... };
    ($name:ident, $builder:expr) => { ... };
}
```
Available on **crate feature `builder`** only.