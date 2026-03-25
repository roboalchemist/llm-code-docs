pgp::composed
# Enum Edata 
Source 

```
pub enum Edata<'a> {
    SymEncryptedData {
        reader: SymEncryptedDataReader<MessageReader<'a>>,
    },
    SymEncryptedProtectedData {
        reader: SymEncryptedProtectedDataReader<MessageReader<'a>>,
    },
    GnupgAeadData {
        reader: SymEncryptedProtectedDataReader<MessageReader<'a>>,
    },
}
```

## Variants§
§
### SymEncryptedData