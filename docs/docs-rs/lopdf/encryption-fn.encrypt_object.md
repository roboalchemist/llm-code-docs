lopdf::encryption
# Function encrypt_object 
Source 

```
pub fn encrypt_object(
    state: &EncryptionState,
    obj_id: ObjectId,
    obj: &mut Object,
) -> Result<(), DecryptionError>
```