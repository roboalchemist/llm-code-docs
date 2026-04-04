# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase.md.txt

# firebase Namespace

# firebase

Namespace that encompasses all Firebase APIs.

## Summary

| ### Enumerations ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1aa31afaaff6e6fe7cf1f2a13961273fba{ https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1aa31afaaff6e6fe7cf1f2a13961273fbaa33e40478e42949d7dc59951089f56921, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1aa31afaaff6e6fe7cf1f2a13961273fbaa987aeae3af8bc84856772d0be82acacd, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1aa31afaaff6e6fe7cf1f2a13961273fbaa9b4a72ef84a53ec51395b07715599389 }` | enumAsynchronous call status. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478{ https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478a11c8441be81525f6c644baf36f8aed3b = 0, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478a1c28184b82cd2bece405e416ebc24b5d }` | enumReports whether a Firebase module initialized successfully. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698{ https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698a25702e7044c1182ae173fde767d4db13 = 0, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698a5def00ce8e590ab1090f88a43d1d661b, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698a86f4df11d354cb9899e1809b7cd0c728, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698a2f803e8663792a5d32998070fa5ce51b, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698a750d4eba90e182f8ef1c80e57b61d205, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698a65b931c5c492f41e070d2a1a5e8f770e }` | enumLevels used when logging messages. |

| ### Typedefs ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a51a10eff4d5c3f029db299b3857515e1` | typedef `uintptr_t` Handle that the API uses to identify an asynchronous call. |

| ### Functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1ad7d5ccf5f01cebe6be28a107b746c1b5()` | `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698` Gets the logging verbosity. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1ab7c51a4808e6c60e1dbd61407d6a2276(https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698 level)` | `void` Sets the logging verbosity. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1add6df98f65d75bdcd068d0062a67b449(const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & lhs, const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & rhs)` | `bool` Checks `lhs` and `rhs` for inequality. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a186f0d745dd4da9cee3ac733581b6229(const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & lhs, const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & rhs)` | `bool` Checks whether `lhs` and `rhs` are in ascending order. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a31fe9c3a7e1dbee68a65b7bfcb557e5b(const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & lhs, const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & rhs)` | `bool` Checks whether `lhs` and `rhs` are in non-descending order. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1ae591837f86a1f54877af84150b3cbed6(const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & lhs, const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & rhs)` | `bool` Checks `lhs` and `rhs` for equality. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a651a889d77fa3942a9840a34305fb32b(const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & lhs, const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & rhs)` | `bool` Checks whether `lhs` and `rhs` are in descending order. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1af171375cda16911c33f659e3efa50856(const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & lhs, const https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp & rhs)` | `bool` Checks whether `lhs` and `rhs` are in non-ascending order. |

| ### Classes ||
|---|---|
| [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app) | Firebase application object. |
| [firebase::AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options) | Options that control the creation of a Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). |
| [firebase::Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future) | Type-specific version of [FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base). |
| [firebase::FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base) | Type-independent return type of asynchronous calls. |
| [firebase::FutureHandle](https://firebase.google.com/docs/reference/cpp/class/firebase/future-handle) | Class that provides more context to FutureHandleId, which allows the underlying API to track handles, perform reference counting, etc. |
| [firebase::ModuleInitializer](https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer) | Utility class to help with initializing Firebase modules. |
| [firebase::Timestamp](https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp) | A [Timestamp](https://firebase.google.com/docs/reference/cpp/class/firebase/timestamp#classfirebase_1_1_timestamp) represents a point in time independent of any time zone or calendar, represented as seconds and fractions of seconds at nanosecond resolution in UTC Epoch time. |
| [firebase::Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant) | [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) data type used by Firebase libraries. |

| ### Namespaces ||
|---|---|
| [firebase::analytics](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics) | Firebase Analytics API. |
| [firebase::app_check](https://firebase.google.com/docs/reference/cpp/namespace/firebase/app-check) |   |
| [firebase::auth](https://firebase.google.com/docs/reference/cpp/namespace/firebase/auth) | Firebase Authentication API. |
| [firebase::database](https://firebase.google.com/docs/reference/cpp/namespace/firebase/database) | Namespace for the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) C++ SDK. |
| [firebase::firestore](https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore) | Cloud [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) API. |
| [firebase::functions](https://firebase.google.com/docs/reference/cpp/namespace/firebase/functions) | Namespace for the Firebase C++ SDK for Cloud [Functions](https://firebase.google.com/docs/reference/cpp/class/firebase/functions/functions#classfirebase_1_1functions_1_1_functions). |
| [firebase::installations](https://firebase.google.com/docs/reference/cpp/namespace/firebase/installations) |   |
| [firebase::messaging](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging) | Firebase Cloud Messaging API. |
| [firebase::remote_config](https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config) | Firebase Remote Config API. |
| [firebase::storage](https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage) | Namespace for the Firebase C++ SDK for Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage). |
| [firebase::ump](https://firebase.google.com/docs/reference/cpp/namespace/firebase/ump) | API for User Messaging Platform. |

## Enumerations

### FutureStatus

```c++
 FutureStatus
```
Asynchronous call status.

| Properties ||
|---|---|
| `kFutureStatusComplete` | Results are ready. |
| `kFutureStatusInvalid` | No result is pending. [FutureBase::Release()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a195aacd8c035957b705cff98daa1920f) or move operator was called. |
| `kFutureStatusPending` | Result is still being processed. |

### InitResult

```c++
 InitResult
```
Reports whether a Firebase module initialized successfully.

| Properties ||
|---|---|
| `kInitResultFailedMissingDependency` | The given library failed to initialize due to a missing dependency. On Android, this typically means that Google Play services is not available and the library requires it. Use [google_play_services::CheckAvailability()](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1a03ea6a3db30e6ef80a816d7605423a3a) and [google_play_services::MakeAvailable()](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1a9b9a9a553ee7476d697260c685074520) to resolve this issue. Also, on Android, this value can be returned if the Java dependencies of a Firebase component are not included in the application, causing initialization to fail. This means that the application's build environment is not configured correctly. To resolve the problem, see the SDK setup documentation for the set of Java dependencies (AARs) required for the component that failed to initialize. |
| `kInitResultSuccess` | The given library was successfully initialized. |

### LogLevel

```c++
 LogLevel
```
Levels used when logging messages.

| Properties ||
|---|---|
| `kLogLevelAssert` | Assert Log Level. |
| `kLogLevelDebug` | Debug Log Level. |
| `kLogLevelError` | Error Log Level. |
| `kLogLevelInfo` | Info Log Level. |
| `kLogLevelVerbose` | Verbose Log Level. |
| `kLogLevelWarning` | Warning Log Level. |

## Typedefs

### FutureHandleId

```c++
uintptr_t FutureHandleId
```
Handle that the API uses to identify an asynchronous call.

The exact interpretation of the handle is up to the API.

## Functions

### GetLogLevel

```c++
LogLevel GetLogLevel()
```
Gets the logging verbosity.

<br />

| Details ||
|---|---|
| **Returns** | Get the currently configured logging verbosity. |

### SetLogLevel

```c++
void SetLogLevel(
  LogLevel level
)
```
Sets the logging verbosity.

All log messages at or above the specific log level.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `level` | Log level to display, by default this is set to kLogLevelInfo. | |

### operator!=

```c++
bool operator!=(
  const Timestamp & lhs,
  const Timestamp & rhs
)
```
Checks `lhs` and `rhs` for inequality.

### operator\<

```c++
bool operator<(
  const Timestamp & lhs,
  const Timestamp & rhs
)
```
Checks whether `lhs` and `rhs` are in ascending order.

### operator\<=

```c++
bool operator<=(
  const Timestamp & lhs,
  const Timestamp & rhs
)
```
Checks whether `lhs` and `rhs` are in non-descending order.

### operator==

```c++
bool operator==(
  const Timestamp & lhs,
  const Timestamp & rhs
)
```
Checks `lhs` and `rhs` for equality.

### operator\>

```c++
bool operator>(
  const Timestamp & lhs,
  const Timestamp & rhs
)
```
Checks whether `lhs` and `rhs` are in descending order.

### operator\>=

```c++
bool operator>=(
  const Timestamp & lhs,
  const Timestamp & rhs
)
```
Checks whether `lhs` and `rhs` are in non-ascending order.