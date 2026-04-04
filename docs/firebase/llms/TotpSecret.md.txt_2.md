# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret.md.txt

# TotpSecret

# TotpSecret


```
interface TotpSecret
```

<br />

*** ** * ** ***

Represents a TOTP secret that is used for enrolling a TOTP second factor. Contains the shared secret key and other parameters to generate time-based one-time passwords. Implements methods to retrieve the shared secret key, generate a QR code URL, and open the QR code URL in an OTP authenticator app.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#generateQrCodeUrl()()` Returns a QR code URL. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#generateQrCodeUrl(java.lang.String,java.lang.String)(accountName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, issuer: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns a QR code URL. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getCodeIntervalSeconds()()` Returns the interval (in seconds) when the OTP codes should change. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getCodeLength()()` Returns the length of the OTP codes to be generated. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getEnrollmentCompletionDeadline()()` Returns the timestamp (in seconds since epoch) by which enrollment should complete. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getHashAlgorithm()()` Returns the hashing algorithm used to generate time-based one-time passwords. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getSessionInfo()()` Returns the enrollment session. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getSharedSecretKey()()` Returns the shared secret key/seed used to generate time-based one-time passwords. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#openInOtpApp(java.lang.String)(qrCodeUrl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Opens the specified QR Code URL in an OTP authenticator app on the device as a new Activity. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#openInOtpApp(java.lang.String,java.lang.String,android.app.Activity)(qrCodeUrl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, fallbackUrl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, activity: https://developer.android.com/reference/android/app/Activity.html)` Opens the specified QR Code URL in an OTP app on the device. |

## Public functions

### generateQrCodeUrl

```
fun generateQrCodeUrl(): String
```

Returns a QR code URL. For more details, see [Key-Uri-Format](https://github.com/google/google-authenticator/wiki/Key-Uri-Format). You can display this URL to the end-user as a QR code to be scanned into an OTP authenticator app, like Google Authenticator. Alternatively, you can automatically load this URL into a TOTP authenticator app using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#openInOtpApp(java.lang.String)`.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A QR code URL String. |

### generateQrCodeUrl

```
fun generateQrCodeUrl(accountName: String, issuer: String): String
```

Returns a QR code URL. For more details, see [Key-Uri-Format](https://github.com/google/google-authenticator/wiki/Key-Uri-Format). You can display this URL to the end-user as a QR code to be scanned into an OTP authenticator app, like Google Authenticator. Alternatively, you can automatically load this URL into a TOTP authenticator app using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#openInOtpApp(java.lang.String)`.

| Parameters |
|---|---|
| `accountName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the name of the account/app along with a user identifier.. |
| `issuer: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | issuer of the TOTP (the app name). |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A QR code URL String. |

### getCodeIntervalSeconds

```
fun getCodeIntervalSeconds(): Int
```

Returns the interval (in seconds) when the OTP codes should change.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The interval (in seconds) when the OTP codes should change. |

### getCodeLength

```
fun getCodeLength(): Int
```

Returns the length of the OTP codes to be generated.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | Length of the one-time passwords to be generated. |

### getEnrollmentCompletionDeadline

```
fun getEnrollmentCompletionDeadline(): Long
```

Returns the timestamp (in seconds since epoch) by which enrollment should complete.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The timestamp (in seconds since epoch) by which enrollment should complete. |

### getHashAlgorithm

```
fun getHashAlgorithm(): String
```

Returns the hashing algorithm used to generate time-based one-time passwords.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Hashing algorithm used. |

### getSessionInfo

```
fun getSessionInfo(): String
```

Returns the enrollment session.

### getSharedSecretKey

```
fun getSharedSecretKey(): String
```

Returns the shared secret key/seed used to generate time-based one-time passwords.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Shared secret key for enrolling in TOTP MFA. |

### openInOtpApp

```
fun openInOtpApp(qrCodeUrl: String): Unit
```

Opens the specified QR Code URL in an OTP authenticator app on the device as a new Activity. The shared secret key and account name will be populated in the OTP authenticator app. The URL uses the `otpauth://` scheme and will be opened on an app that handles this scheme, if it exists on the device.

If a suitable OTP authenticator app was not found, this opens the Google Play Store instead, using the following URL: `https://play.google.com/store/search?q=otpauth&amp;c=apps`.

| Parameters |
|---|---|
| `qrCodeUrl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the QR Code URL to open. |

### openInOtpApp

```
fun openInOtpApp(qrCodeUrl: String, fallbackUrl: String, activity: Activity): Unit
```

Opens the specified QR Code URL in an OTP app on the device. The shared secret key and account name will be populated in the OTP app. The URL uses the `otpauth://` scheme and will be opened on an app that handles this scheme, if it exists on the device.

| Parameters |
|---|---|
| `qrCodeUrl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the QR Code URL to open. |
| `fallbackUrl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the URL to open if a suitable OTP authenticator app was not found. |
| `activity: https://developer.android.com/reference/android/app/Activity.html` | a reference to the current activity, to open the OTP authenticator app on. |