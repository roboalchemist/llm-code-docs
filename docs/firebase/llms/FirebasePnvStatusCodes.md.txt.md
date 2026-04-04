# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePnvStatusCodes.md.txt

# FirebasePnvStatusCodes

# FirebasePnvStatusCodes


```
public static class FirebasePnvStatusCodes extends CommonStatusCodes
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||
| ↳ | [com.google.android.gms.common.api.CommonStatusCodes](https://developers.google.com/android/reference/com/google/android/gms/common/api/CommonStatusCodes.html) ||
|   | ↳ | [com.google.firebase.pnv.FirebasePnvStatusCodes](https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePnvStatusCodes) |

*** ** * ** ***

Status codes for Firebase PNV.

## Summary

| ### Constants |
|---|---|
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePnvStatusCodes#CARRIER_NOT_SUPPORTED() = 55501` *** ** * ** *** Firebase PNV status codes. <br /> |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePnvStatusCodes#CREDENTIAL_MANAGER_ERROR() = 55506` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePnvStatusCodes#INTEGRITY_CHECK_FAILED() = 55503` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePnvStatusCodes#INVALID_DIGITAL_CREDENTIAL_RESPONSE() = 55502` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePnvStatusCodes#PREFLIGHT_CHECK_FAILED() = 55504` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePnvStatusCodes#UNSUPPORTED_OPERATION() = 55505` |

| ### Public fields |
|---|---|
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePnvStatusCodes` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePnvStatusCodes#INSTANCE()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePnvStatusCodes#getMessage(kotlin.Int)(int errorCode)` Returns the message for the given error code. |

## Constants

### CARRIER_NOT_SUPPORTED

```
public static final int CARRIER_NOT_SUPPORTED = 55501
```

*** ** * ** ***


Firebase PNV status codes. Range: 55500 to 55999
---

<br />

### CREDENTIAL_MANAGER_ERROR

```
public static final int CREDENTIAL_MANAGER_ERROR = 55506
```

### INTEGRITY_CHECK_FAILED

```
public static final int INTEGRITY_CHECK_FAILED = 55503
```

### INVALID_DIGITAL_CREDENTIAL_RESPONSE

```
public static final int INVALID_DIGITAL_CREDENTIAL_RESPONSE = 55502
```

### PREFLIGHT_CHECK_FAILED

```
public static final int PREFLIGHT_CHECK_FAILED = 55504
```

### UNSUPPORTED_OPERATION

```
public static final int UNSUPPORTED_OPERATION = 55505
```

## Public fields

### INSTANCE

```
public static @NonNull FirebasePnvStatusCodes INSTANCE
```

## Public methods

### getMessage

```
public final @NonNull String getMessage(int errorCode)
```

Returns the message for the given error code.

| Parameters |
|---|---|
| `int errorCode` | The error code to get the message for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | The message for the given error code. |