# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult.md.txt

# VerifiedPhoneNumberTokenResult

# VerifiedPhoneNumberTokenResult


```
class VerifiedPhoneNumberTokenResult : Parcelable
```

<br />

*** ** * ** ***

Result object that contains a Firebase Phone Number Verification (FPNV) Token.

## Summary

| ### Public companion properties |
|---|---|
| `https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#CREATOR()` `https://developer.android.com/reference/android/os/Parcelable.Creator.html` for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#VerifiedPhoneNumberTokenResult(kotlin.String)(token: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

| ### Public functions |
|---|---|
| `final https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#describeContents()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getClaims()()` Returns the entire payload claims of the token. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getExpirationTimestamp()()` Returns the expiration timestamp of the token in seconds since the epoch. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getIssuedAtTimestamp()()` Returns the issued-at timestamp of the token in seconds since the epoch. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getNonce()()` Returns the nonce of the token. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getPhoneNumber()()` Returns the phone number associated with the token. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getToken()()` Returns the Firebase Phone Number Verification (FPNV) token. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#writeToParcel(android.os.Parcel,kotlin.Int)(dest: https://developer.android.com/reference/android/os/Parcel.html, flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Writes the object's data to a `https://developer.android.com/reference/android/os/Parcel.html`. |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#getStability()()` | |

## Public companion properties

### CREATOR

```
val CREATOR: Parcelable.Creator<VerifiedPhoneNumberTokenResult>
```

`https://developer.android.com/reference/android/os/Parcelable.Creator.html` for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult`.

## Public constructors

### VerifiedPhoneNumberTokenResult

```
VerifiedPhoneNumberTokenResult(token: String)
```

## Public functions

### describeContents

```
final fun describeContents(): Int
```

### getClaims

```
fun getClaims(): Map<String, Any>
```

Returns the entire payload claims of the token. Returns an empty map if no claims are present.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The claims as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html` of `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` to `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html`. |

### getExpirationTimestamp

```
fun getExpirationTimestamp(): Long
```

Returns the expiration timestamp of the token in seconds since the epoch.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The expiration timestamp as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html`. |

### getIssuedAtTimestamp

```
fun getIssuedAtTimestamp(): Long
```

Returns the issued-at timestamp of the token in seconds since the epoch.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The issued-at timestamp as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html`. |

### getNonce

```
fun getNonce(): String
```

Returns the nonce of the token.

If a nonce was provided during the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getDigitalCredentialPayload(kotlin.String)` invocation, then that nonce will be returned. Otherwise, the nonce will be a random UUID.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The nonce as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`. |

### getPhoneNumber

```
fun getPhoneNumber(): String
```

Returns the phone number associated with the token.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The phone number as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`. |

### getToken

```
fun getToken(): String
```

Returns the Firebase Phone Number Verification (FPNV) token.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The FPNV token as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`. |

### writeToParcel

```
open fun writeToParcel(dest: Parcel, flags: Int): Unit
```

Writes the object's data to a `https://developer.android.com/reference/android/os/Parcel.html`.

| Parameters |
|---|---|
| `dest: https://developer.android.com/reference/android/os/Parcel.html` | The `https://developer.android.com/reference/android/os/Parcel.html` in which the object should be written. |
| `flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | Additional flags about how the object should be written. |