nettle
# Function version 
Source 

```
pub fn version() -> (u32, u32)
```

##### Examples found in repository?
examples/supported-algorithms.rs (line 5)

```
4fn main() {
5    let (major, minor) = nettle::version();
6    println!("Nettle {}.{}", major, minor);
7    println!("Cv448: {:?}", nettle::curve448::IS_SUPPORTED);
8    println!("OCB: {:?}", nettle::aead::OCB_IS_SUPPORTED);
9}
```