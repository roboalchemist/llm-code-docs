# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user-metadata.md.txt

# firebase::auth::UserMetadata Struct Reference

# firebase::auth::UserMetadata


`#include <user.h>`

Metadata corresponding to a Firebase user.

## Summary

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user-metadata#structfirebase_1_1auth_1_1_user_metadata_1abf4043dec3b4eaa0a3dd7a2c52f8450b()` ||

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user-metadata#structfirebase_1_1auth_1_1_user_metadata_1a6544df83c8968cfc198a97e7f81460ad` | `uint64_t` The Firebase user creation UTC timestamp in milliseconds. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user-metadata#structfirebase_1_1auth_1_1_user_metadata_1a8521038f82702936eb4a3bb1853e112b` | `uint64_t` The last sign in UTC timestamp in milliseconds. |

## Public attributes

### creation_timestamp

```c++
uint64_t firebase::auth::UserMetadata::creation_timestamp
```
The Firebase user creation UTC timestamp in milliseconds.

### last_sign_in_timestamp

```c++
uint64_t firebase::auth::UserMetadata::last_sign_in_timestamp
```
The last sign in UTC timestamp in milliseconds.

See <https://en.wikipedia.org/wiki/Unix_time> for details of UTC.

## Public functions

### UserMetadata

```c++
 firebase::auth::UserMetadata::UserMetadata()
```