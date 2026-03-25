lopdf::encryption
# Function decrypt_object 
Source 

```
pub fn decrypt_object(
    state: &EncryptionState,
    obj_id: ObjectId,
    obj: &mut Object,
) -> Result<(), DecryptionError>
```