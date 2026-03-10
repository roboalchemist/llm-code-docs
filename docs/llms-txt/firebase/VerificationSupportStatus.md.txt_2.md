# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus.md.txt

# VerificationSupportStatus

# VerificationSupportStatus


```
@Target(allowedTargets = [AnnotationTarget.TYPE])
@IntDef(value = [0, 1, 2, 3, 4])
@Retention(value = AnnotationRetention.SOURCE)
annotation VerificationSupportStatus
```

<br />

*** ** * ** ***

Defines the possible values for the capability status.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus#CAPABILITY_STATUS_UNSPECIFIED()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus#CAPABLE()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus#INCAPABLE_DUE_TO_CARRIER_UNSUPPORTED()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus#INCAPABLE_DUE_TO_ANDROID_VERSION()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus#INCAPABLE_DUE_TO_SIM_STATE()` |   |

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus#CAPABILITY_STATUS_UNSPECIFIED() = 0` The capability status is unspecified. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus#CAPABLE() = 1` The capability is supported. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus#INCAPABLE_DUE_TO_ANDROID_VERSION() = 3` The capability is not supported because the Android version does not support it. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus#INCAPABLE_DUE_TO_CARRIER_UNSUPPORTED() = 2` The capability is not supported because the carrier does not support it. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus#INCAPABLE_DUE_TO_SIM_STATE() = 4` The capability is not supported because the SIM card is not ready. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportStatus#VerificationSupportStatus()()` |

## Constants

### CAPABILITY_STATUS_UNSPECIFIED

```
const val CAPABILITY_STATUS_UNSPECIFIED = 0: Int
```

The capability status is unspecified.

### CAPABLE

```
const val CAPABLE = 1: Int
```

The capability is supported.

### INCAPABLE_DUE_TO_ANDROID_VERSION

```
const val INCAPABLE_DUE_TO_ANDROID_VERSION = 3: Int
```

The capability is not supported because the Android version does not support it.

### INCAPABLE_DUE_TO_CARRIER_UNSUPPORTED

```
const val INCAPABLE_DUE_TO_CARRIER_UNSUPPORTED = 2: Int
```

The capability is not supported because the carrier does not support it.

### INCAPABLE_DUE_TO_SIM_STATE

```
const val INCAPABLE_DUE_TO_SIM_STATE = 4: Int
```

The capability is not supported because the SIM card is not ready.

## Public constructors

### VerificationSupportStatus

```
VerificationSupportStatus()
```