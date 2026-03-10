# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePnvStatusCodes.md.txt

# FirebasePnvStatusCodes

# FirebasePnvStatusCodes


```
object FirebasePnvStatusCodes : CommonStatusCodes
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.android.gms.common.api.CommonStatusCodes](https://developers.google.com/android/reference/com/google/android/gms/common/api/CommonStatusCodes.html) ||
|   | ↳ | [com.google.firebase.pnv.FirebasePnvStatusCodes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePnvStatusCodes) |

*** ** * ** ***

Status codes for Firebase PNV.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePnvStatusCodes#CARRIER_NOT_SUPPORTED() = 55501` *** ** * ** *** Firebase PNV status codes. <br /> |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePnvStatusCodes#CREDENTIAL_MANAGER_ERROR() = 55506` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePnvStatusCodes#INTEGRITY_CHECK_FAILED() = 55503` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePnvStatusCodes#INVALID_DIGITAL_CREDENTIAL_RESPONSE() = 55502` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePnvStatusCodes#PREFLIGHT_CHECK_FAILED() = 55504` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePnvStatusCodes#UNSUPPORTED_OPERATION() = 55505` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePnvStatusCodes#getMessage(kotlin.Int)(errorCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Returns the message for the given error code. |

## Constants

### CARRIER_NOT_SUPPORTED

```
const val CARRIER_NOT_SUPPORTED = 55501: Int
```

*** ** * ** ***


Firebase PNV status codes. Range: 55500 to 55999
---

<br />

### CREDENTIAL_MANAGER_ERROR

```
const val CREDENTIAL_MANAGER_ERROR = 55506: Int
```

### INTEGRITY_CHECK_FAILED

```
const val INTEGRITY_CHECK_FAILED = 55503: Int
```

### INVALID_DIGITAL_CREDENTIAL_RESPONSE

```
const val INVALID_DIGITAL_CREDENTIAL_RESPONSE = 55502: Int
```

### PREFLIGHT_CHECK_FAILED

```
const val PREFLIGHT_CHECK_FAILED = 55504: Int
```

### UNSUPPORTED_OPERATION

```
const val UNSUPPORTED_OPERATION = 55505: Int
```

## Public functions

### getMessage

```
fun getMessage(errorCode: Int): String
```

Returns the message for the given error code.

| Parameters |
|---|---|
| `errorCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The error code to get the message for. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The message for the given error code. |