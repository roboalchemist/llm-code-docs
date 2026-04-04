# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.md.txt

# ActionCodeSettings

# ActionCodeSettings


```
class ActionCodeSettings : Parcelable
```

<br />

*** ** * ** ***

Structure that contains the required continue/state URL with optional Android and iOS bundle identifiers. The stateUrl used to initialize this class is the link/deep link/fallback url used while constructing the Firebase dynamic link.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder` A Builder class for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings`. |

| ### Constants |
|---|---|
| `const https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings#CREATOR()` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings#canHandleCodeInApp()()` Returns whether the out-of-band (OOB) code should be handled by the app. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings#getIOSBundle()()` Returns the bundle ID of the installed Apple platforms app. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings#newBuilder()()` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings#writeToParcel(android.os.Parcel,int)(out: https://developer.android.com/reference/android/os/Parcel.html, flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings#androidInstallApp()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings#androidMinimumVersion()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings#androidPackageName()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings#linkDomain()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings#url()` |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Constants

### CREATOR

```
const val CREATOR: Parcelable.Creator<ActionCodeSettings!>!
```

## Public functions

### canHandleCodeInApp

```
fun canHandleCodeInApp(): Boolean
```

Returns whether the out-of-band (OOB) code should be handled by the app. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#setHandleCodeInApp(boolean)`.

### getIOSBundle

```
fun getIOSBundle(): String?
```

Returns the bundle ID of the installed Apple platforms app. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder#setIOSBundleId(java.lang.String)`.

### newBuilder

```
java-static fun newBuilder(): ActionCodeSettings.Builder
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder`.

### writeToParcel

```
fun writeToParcel(out: Parcel, flags: Int): Unit
```

## Public properties

### androidInstallApp

```
val androidInstallApp: Boolean
```

### androidMinimumVersion

```
val androidMinimumVersion: String?
```

### androidPackageName

```
val androidPackageName: String!
```

### linkDomain

```
val linkDomain: String!
```

### url

```
val url: String!
```