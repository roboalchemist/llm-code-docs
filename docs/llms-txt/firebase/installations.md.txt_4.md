# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/installations.md.txt

# firebase::installations Namespace

# firebase::installations

## Summary

| ### Enumerations ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/installations#namespacefirebase_1_1installations_1a63045507e4d5479a50cc9455219f584f{ https://firebase.google.com/docs/reference/cpp/namespace/firebase/installations#namespacefirebase_1_1installations_1a63045507e4d5479a50cc9455219f584fa5ba79a07d99409fe9d48cefdd02c531e, https://firebase.google.com/docs/reference/cpp/namespace/firebase/installations#namespacefirebase_1_1installations_1a63045507e4d5479a50cc9455219f584fad57b3cb9651c3bc1f7ac67f2d6deb330, https://firebase.google.com/docs/reference/cpp/namespace/firebase/installations#namespacefirebase_1_1installations_1a63045507e4d5479a50cc9455219f584faea0546f226bedc3671829fec15d844ad }` | enum[Installations](https://firebase.google.com/docs/reference/cpp/class/firebase/installations/installations#classfirebase_1_1installations_1_1_installations) error codes. |

| ### Classes ||
|---|---|
| [firebase::installations::Installations](https://firebase.google.com/docs/reference/cpp/class/firebase/installations/installations) | [Installations](https://firebase.google.com/docs/reference/cpp/class/firebase/installations/installations#classfirebase_1_1installations_1_1_installations) provides a unique identifier for each app instance and a mechanism to authenticate and authorize actions (for example, sending an FCM message). |

## Enumerations

### Error

```c++
 Error
```
[Installations](https://firebase.google.com/docs/reference/cpp/class/firebase/installations/installations#classfirebase_1_1installations_1_1_installations) error codes.

| Properties ||
|---|---|
| `kErrorInvalidConfiguration` | Some of the parameters of the request were invalid. |
| `kErrorNoAccess` | [Installations](https://firebase.google.com/docs/reference/cpp/class/firebase/installations/installations#classfirebase_1_1installations_1_1_installations) service cannot be accessed. |
| `kErrorUnknown` | An unknown error occurred. |