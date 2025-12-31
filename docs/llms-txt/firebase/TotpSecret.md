# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpSecret.md.txt

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

|                               ### Public functions                               |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [generateQrCodeUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#generateQrCodeUrl())`()` Returns a QR code URL.                                                                                                                                                                                                                                                                                                                                                                            |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [generateQrCodeUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#generateQrCodeUrl(java.lang.String,java.lang.String))`(accountName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, issuer: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns a QR code URL.                                                                                                                                                |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)       | [getCodeIntervalSeconds](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getCodeIntervalSeconds())`()` Returns the interval (in seconds) when the OTP codes should change.                                                                                                                                                                                                                                                                                                                     |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)       | [getCodeLength](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getCodeLength())`()` Returns the length of the OTP codes to be generated.                                                                                                                                                                                                                                                                                                                                                      |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)     | [getEnrollmentCompletionDeadline](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getEnrollmentCompletionDeadline())`()` Returns the timestamp (in seconds since epoch) by which enrollment should complete.                                                                                                                                                                                                                                                                                   |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getHashAlgorithm](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getHashAlgorithm())`()` Returns the hashing algorithm used to generate time-based one-time passwords.                                                                                                                                                                                                                                                                                                                       |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getSessionInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getSessionInfo())`()` Returns the enrollment session.                                                                                                                                                                                                                                                                                                                                                                         |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getSharedSecretKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#getSharedSecretKey())`()` Returns the shared secret key/seed used to generate time-based one-time passwords.                                                                                                                                                                                                                                                                                                              |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)     | [openInOtpApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#openInOtpApp(java.lang.String))`(qrCodeUrl: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Opens the specified QR Code URL in an OTP authenticator app on the device as a new Activity.                                                                                                                                                                                                   |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)     | [openInOtpApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#openInOtpApp(java.lang.String,java.lang.String,android.app.Activity))`(qrCodeUrl: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, fallbackUrl: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, activity: `[Activity](https://developer.android.com/reference/android/app/Activity.html)`)` Opens the specified QR Code URL in an OTP app on the device. |

## Public functions

### generateQrCodeUrl

```
funÂ generateQrCodeUrl():Â String
```

Returns a QR code URL. For more details, see [Key-Uri-Format](https://github.com/google/google-authenticator/wiki/Key-Uri-Format). You can display this URL to the end-user as a QR code to be scanned into an OTP authenticator app, like Google Authenticator. Alternatively, you can automatically load this URL into a TOTP authenticator app using [openInOtpApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#openInOtpApp(java.lang.String)).  

|                                     Returns                                      |
|----------------------------------------------------------------------------------|-----------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | A QR code URL String. |

### generateQrCodeUrl

```
funÂ generateQrCodeUrl(accountName:Â String,Â issuer:Â String):Â String
```

Returns a QR code URL. For more details, see [Key-Uri-Format](https://github.com/google/google-authenticator/wiki/Key-Uri-Format). You can display this URL to the end-user as a QR code to be scanned into an OTP authenticator app, like Google Authenticator. Alternatively, you can automatically load this URL into a TOTP authenticator app using [openInOtpApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret#openInOtpApp(java.lang.String)).  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| `accountName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | the name of the account/app along with a user identifier.. |
| `issuer: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)      | issuer of the TOTP (the app name).                         |

|                                     Returns                                      |
|----------------------------------------------------------------------------------|-----------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | A QR code URL String. |

### getCodeIntervalSeconds

```
funÂ getCodeIntervalSeconds():Â Int
```

Returns the interval (in seconds) when the OTP codes should change.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|-------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | The interval (in seconds) when the OTP codes should change. |

### getCodeLength

```
funÂ getCodeLength():Â Int
```

Returns the length of the OTP codes to be generated.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|---------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | Length of the one-time passwords to be generated. |

### getEnrollmentCompletionDeadline

```
funÂ getEnrollmentCompletionDeadline():Â Long
```

Returns the timestamp (in seconds since epoch) by which enrollment should complete.  

|                                   Returns                                    |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | The timestamp (in seconds since epoch) by which enrollment should complete. |

### getHashAlgorithm

```
funÂ getHashAlgorithm():Â String
```

Returns the hashing algorithm used to generate time-based one-time passwords.  

|                                     Returns                                      |
|----------------------------------------------------------------------------------|-------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | Hashing algorithm used. |

### getSessionInfo

```
funÂ getSessionInfo():Â String
```

Returns the enrollment session.  

### getSharedSecretKey

```
funÂ getSharedSecretKey():Â String
```

Returns the shared secret key/seed used to generate time-based one-time passwords.  

|                                     Returns                                      |
|----------------------------------------------------------------------------------|----------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | Shared secret key for enrolling in TOTP MFA. |

### openInOtpApp

```
funÂ openInOtpApp(qrCodeUrl:Â String):Â Unit
```

Opens the specified QR Code URL in an OTP authenticator app on the device as a new Activity. The shared secret key and account name will be populated in the OTP authenticator app. The URL uses the `otpauth://` scheme and will be opened on an app that handles this scheme, if it exists on the device.

If a suitable OTP authenticator app was not found, this opens the Google Play Store instead, using the following URL: `https://play.google.com/store/search?q=otpauth&amp;c=apps`.  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|--------------------------|
| `qrCodeUrl: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | the QR Code URL to open. |

### openInOtpApp

```
funÂ openInOtpApp(qrCodeUrl:Â String,Â fallbackUrl:Â String,Â activity:Â Activity):Â Unit
```

Opens the specified QR Code URL in an OTP app on the device. The shared secret key and account name will be populated in the OTP app. The URL uses the `otpauth://` scheme and will be opened on an app that handles this scheme, if it exists on the device.  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `qrCodeUrl: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)   | the QR Code URL to open.                                                   |
| `fallbackUrl: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | the URL to open if a suitable OTP authenticator app was not found.         |
| `activity: `[Activity](https://developer.android.com/reference/android/app/Activity.html)       | a reference to the current activity, to open the OTP authenticator app on. |