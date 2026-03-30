# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult.md.txt

# VerifiedPhoneNumberTokenResult

# VerifiedPhoneNumberTokenResult


```
public final class VerifiedPhoneNumberTokenResult implements Parcelable
```

<br />

*** ** * ** ***

Result object that contains a Firebase Phone Number Verification (FPNV) Token.

## Summary

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/os/Parcelable.Creator.html<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#CREATOR()` `https://developer.android.com/reference/android/os/Parcelable.Creator.html` for `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#VerifiedPhoneNumberTokenResult(kotlin.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html token)` |

| ### Public methods |
|---|---|
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#describeContents()()` |
| `final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/Map.html<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/Object.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getClaims()()` Returns the entire payload claims of the token. |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getExpirationTimestamp()()` Returns the expiration timestamp of the token in seconds since the epoch. |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getIssuedAtTimestamp()()` Returns the issued-at timestamp of the token in seconds since the epoch. |
| `final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getNonce()()` Returns the nonce of the token. |
| `final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getPhoneNumber()()` Returns the phone number associated with the token. |
| `final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#getToken()()` Returns the Firebase Phone Number Verification (FPNV) token. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult#writeToParcel(android.os.Parcel,kotlin.Int)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/os/Parcel.html dest, int flags)` Writes the object's data to a `https://developer.android.com/reference/android/os/Parcel.html`. |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `int` | `https://developer.android.com/reference/android/os/Parcelable.html#getStability()()` | |

## Public fields

### CREATOR

```
public static final @NonNull Parcelable.Creator<@NonNull VerifiedPhoneNumberTokenResult> CREATOR
```

`https://developer.android.com/reference/android/os/Parcelable.Creator.html` for `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult`.

## Public constructors

### VerifiedPhoneNumberTokenResult

```
public VerifiedPhoneNumberTokenResult(@NonNull String token)
```

## Public methods

### describeContents

```
public final int describeContents()
```

### getClaims

```
public final @NonNull Map<@NonNull String, @NonNull Object> getClaims()
```

Returns the entire payload claims of the token. Returns an empty map if no claims are present.

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/Map.html<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/Object.html>` | The claims as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html` of `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` to `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html`. |

### getExpirationTimestamp

```
public final long getExpirationTimestamp()
```

Returns the expiration timestamp of the token in seconds since the epoch.

| Returns |
|---|---|
| `long` | The expiration timestamp as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html`. |

### getIssuedAtTimestamp

```
public final long getIssuedAtTimestamp()
```

Returns the issued-at timestamp of the token in seconds since the epoch.

| Returns |
|---|---|
| `long` | The issued-at timestamp as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html`. |

### getNonce

```
public final @NonNull String getNonce()
```

Returns the nonce of the token.

If a nonce was provided during the `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getDigitalCredentialPayload(kotlin.String)` invocation, then that nonce will be returned. Otherwise, the nonce will be a random UUID.

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | The nonce as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`. |

### getPhoneNumber

```
public final @NonNull String getPhoneNumber()
```

Returns the phone number associated with the token.

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | The phone number as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`. |

### getToken

```
public final @NonNull String getToken()
```

Returns the Firebase Phone Number Verification (FPNV) token.

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | The FPNV token as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`. |

### writeToParcel

```
public void writeToParcel(@NonNull Parcel dest, int flags)
```

Writes the object's data to a `https://developer.android.com/reference/android/os/Parcel.html`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/os/Parcel.html dest` | The `https://developer.android.com/reference/android/os/Parcel.html` in which the object should be written. |
| `int flags` | Additional flags about how the object should be written. |