lopdf::encryption
# Enum EncryptionVersion 
Source 

```
pub enum EncryptionVersion<'a> {
    V1 {
        document: &'a Document,
        owner_password: &'a str,
        user_password: &'a str,
        permissions: Permissions,
    },
    V2 {
        document: &'a Document,
        owner_password: &'a str,
        user_password: &'a str,
        key_length: usize,
        permissions: Permissions,
    },
    V4 {
        document: &'a Document,
        encrypt_metadata: bool,
        crypt_filters: BTreeMap<Vec<u8>, Arc<dyn CryptFilter>>,
        stream_filter: Vec<u8>,
        string_filter: Vec<u8>,
        owner_password: &'a str,
        user_password: &'a str,
        permissions: Permissions,
    },
    R5 {
        encrypt_metadata: bool,
        crypt_filters: BTreeMap<Vec<u8>, Arc<dyn CryptFilter>>,
        file_encryption_key: &'a [u8],
        stream_filter: Vec<u8>,
        string_filter: Vec<u8>,
        owner_password: &'a str,
        user_password: &'a str,
        permissions: Permissions,
    },
    V5 {
        encrypt_metadata: bool,
        crypt_filters: BTreeMap<Vec<u8>, Arc<dyn CryptFilter>>,
        file_encryption_key: &'a [u8],
        stream_filter: Vec<u8>,
        string_filter: Vec<u8>,
        owner_password: &'a str,
        user_password: &'a str,
        permissions: Permissions,
    },
}
```

## Variants§
§
### V1