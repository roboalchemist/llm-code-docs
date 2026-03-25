mbedtls::rng
# Trait EntropyCallback 
Source 

```
pub trait EntropyCallback: Send + Sync {
    // Required methods
    unsafe extern "C" fn call(
        user_data: *mut c_void,
        data: *mut c_uchar,
        len: size_t,
    ) -> c_int
       where Self: Sized;
    fn data_ptr(&self) -> *mut c_void;
}
```

## Required Methods§
Source
#### unsafe extern "C" fn call(
    user_data: *mut c_void,
    data: *mut c_uchar,
    len: size_t,
) -> c_intwhere
    Self: Sized,