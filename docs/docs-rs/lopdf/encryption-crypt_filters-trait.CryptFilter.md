lopdf::encryption::crypt_filters
# Trait CryptFilter 
Source 

```
pub trait CryptFilter:
    Debug
    + Send
    + Sync {
    // Required methods
    fn method(&self) -> &[u8] ⓘ;
    fn compute_key(
        &self,
        key: &[u8],
        obj_id: ObjectId,
    ) -> Result<Vec<u8>, DecryptionError>;
    fn encrypt(
        &self,
        key: &[u8],
        plaintext: &[u8],
    ) -> Result<Vec<u8>, DecryptionError>;
    fn decrypt(
        &self,
        key: &[u8],
        ciphertext: &[u8],
    ) -> Result<Vec<u8>, DecryptionError>;
}
```

## Required Methods§
Source
#### fn method(&self) -> &[u8] ⓘ