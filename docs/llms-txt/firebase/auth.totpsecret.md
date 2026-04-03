# Source: https://firebase.google.com/docs/reference/js/auth.totpsecret.md.txt

# TotpSecret class

Provider for generating a [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/js/auth.totpmultifactorassertion.md#totpmultifactorassertion_interface).

Stores the shared secret key and other parameters to generate time-based OTPs. Implements methods to retrieve the shared secret key and generate a QR code URL.

**Signature:**  

    export declare class TotpSecret 

## Properties

|                                                                Property                                                                 | Modifiers |  Type  |                                Description                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------|--------|----------------------------------------------------------------------------|
| [codeIntervalSeconds](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecretcodeintervalseconds)                   |           | number | The interval (in seconds) when the OTP codes should change.                |
| [codeLength](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecretcodelength)                                     |           | number | Length of the one-time passwords to be generated.                          |
| [enrollmentCompletionDeadline](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecretenrollmentcompletiondeadline) |           | string | The timestamp (UTC string) by which TOTP enrollment should be completed.   |
| [hashingAlgorithm](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecrethashingalgorithm)                         |           | string | Hashing algorithm used.                                                    |
| [secretKey](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecretsecretkey)                                       |           | string | Shared secret key/seed used for enrolling in TOTP MFA and generating OTPs. |

## Methods

|                                                                 Method                                                                 | Modifiers |                                                                                                                                              Description                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [generateQrCodeUrl(accountName, issuer)](https://firebase.google.com/docs/reference/js/auth.totpsecret.md#totpsecretgenerateqrcodeurl) |           | Returns a QR code URL as described in https://github.com/google/google-authenticator/wiki/Key-Uri-Format This can be displayed to the user as a QR code to be scanned into a TOTP app like Google Authenticator. If the optional parameters are unspecified, an accountName of and issuer of are used. |

## TotpSecret.codeIntervalSeconds

The interval (in seconds) when the OTP codes should change.

**Signature:**  

    readonly codeIntervalSeconds: number;

## TotpSecret.codeLength

Length of the one-time passwords to be generated.

**Signature:**  

    readonly codeLength: number;

## TotpSecret.enrollmentCompletionDeadline

The timestamp (UTC string) by which TOTP enrollment should be completed.

**Signature:**  

    readonly enrollmentCompletionDeadline: string;

## TotpSecret.hashingAlgorithm

Hashing algorithm used.

**Signature:**  

    readonly hashingAlgorithm: string;

## TotpSecret.secretKey

Shared secret key/seed used for enrolling in TOTP MFA and generating OTPs.

**Signature:**  

    readonly secretKey: string;

## TotpSecret.generateQrCodeUrl()

Returns a QR code URL as described in https://github.com/google/google-authenticator/wiki/Key-Uri-Format This can be displayed to the user as a QR code to be scanned into a TOTP app like Google Authenticator. If the optional parameters are unspecified, an accountName of and issuer of are used.

**Signature:**  

    generateQrCodeUrl(accountName?: string, issuer?: string): string;

#### Parameters

|  Parameter  |  Type  |                        Description                        |
|-------------|--------|-----------------------------------------------------------|
| accountName | string | the name of the account/app along with a user identifier. |
| issuer      | string | issuer of the TOTP (likely the app name).                 |

**Returns:**

string

A QR code URL string.