lopdf
# Macro dictionary 
Source 

```
macro_rules! dictionary {
    () => { ... };
    ($( $key: expr => $value: expr ),+ ,) => { ... };
    ($( $key: expr => $value: expr ),*) => { ... };
}
```