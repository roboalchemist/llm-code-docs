# Source: https://firebase.google.com/docs/reference/cpp/struct/std/hash-firebase/firestore/field-path-.md.txt

# std::hash Struct Reference

# std::hash\< firebase::firestore::FieldPath \>


`#include <field_path.h>`

A convenient specialization of std::hash for FieldPath.

## Summary

|                                                                                                                                                                                                                    ### Public functions                                                                                                                                                                                                                     ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| [operator()](https://firebase.google.com/docs/reference/cpp/struct/std/hash-firebase/firestore/field-path-#structstd_1_1hash_3_01firebase_1_1firestore_1_1_field_path_01_4_1ad7b7993822a41cd641611c7f02231986)`(const `[firebase::firestore::FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path)` & field_path) const ` | `size_t` Calculates the hash of the argument. |

## Public functions

### operator()

```c++
size_t std::hash< firebase::firestore::FieldPath >::operator()(
  const firebase::firestore::FieldPath & field_path
) const 
```  
Calculates the hash of the argument.

Note: specialization of `std::hash` is provided for convenience only. The implementation is subject to change.