mbedtls::rng
# Trait RngCallbackMut 
Source 

```
pub trait RngCallbackMut: Send + Sync {
    // Required methods
    unsafe extern "C" fn call_mut(
        user_data: *mut c_void,
        data: *mut c_uchar,
        len: size_t,
    ) -> c_int
       where Self: Sized;
    fn data_ptr_mut(&mut self) -> *mut c_void;
}
```

## Required Methods§
Source
#### unsafe extern "C" fn call_mut(
    user_data: *mut c_void,
    data: *mut c_uchar,
    len: size_t,
) -> c_intwhere
    Self: Sized,