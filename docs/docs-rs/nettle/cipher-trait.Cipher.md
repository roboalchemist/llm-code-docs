nettle::cipher
# Trait Cipher 
Source 

```
pub trait Cipher: Sized {
    const BLOCK_SIZE: usize;
    const KEY_SIZE: usize;

    // Required methods
    fn with_decrypt_key(key: &[u8]) -> Result<Self>;
    fn with_encrypt_key(key: &[u8]) -> Result<Self>;
    fn decrypt(&mut self, dst: &mut [u8], src: &[u8]);
    fn encrypt(&mut self, dst: &mut [u8], src: &[u8]);
    fn context(&mut self) -> *mut c_void;
    fn raw_decrypt_function() -> RawCipherFunctionPointer;
    fn raw_encrypt_function() -> RawCipherFunctionPointer;
}
```

## Required Associated Constants§