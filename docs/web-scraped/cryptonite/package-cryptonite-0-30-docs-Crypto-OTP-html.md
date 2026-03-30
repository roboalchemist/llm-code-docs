# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html

Title: Crypto.OTP

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html

Markdown Content:
Description

One-time password implementation as defined by the [HOTP](http://tools.ietf.org/html/rfc4226) and [TOTP](http://tools.ietf.org/html/rfc6238) specifications.

Both implementations use a shared key between the client and the server. HOTP passwords are based on a synchronized counter. TOTP passwords use the same approach but calculate the counter as a number of time steps from the Unix epoch to the current time, thus requiring that both client and server have synchronized clocks.

Probably the best-known use of TOTP is in Google's 2-factor authentication.

The TOTP API doesn't depend on any particular time package, so the user needs to supply the current `OTPTime` value, based on the system time. For example, using the `hourglass` package, you could create a `getOTPTime` function:

`>>>`**```
import Time.System
```**`>>>`**```
import Time.Types
```**`>>>`**```

```**`>>>`**```
let getOTPTime = timeCurrent >>= \(Elapsed t) -> return (fromIntegral t :: OTPTime)
```**
Or if you prefer, the `time` package could be used:

`>>>`**```
import Data.Time.Clock.POSIX
```**`>>>`**```

```**`>>>`**```
let getOTPTime = getPOSIXTime >>= \t -> return (floor t :: OTPTime)
```**

Synopsis
*   type[OTP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTP) = [Word32](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word32 "Data.Word")
*   data[OTPDigits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPDigits)
    *   = [OTP4](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:OTP4)
    *   | [OTP5](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:OTP5)
    *   | [OTP6](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:OTP6)
    *   | [OTP7](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:OTP7)
    *   | [OTP8](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:OTP8)
    *   | [OTP9](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:OTP9)

*   type[OTPTime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPTime) = [Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word")
*   [hotp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:hotp) :: forall hash key. ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key) => hash ->[OTPDigits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPDigits "Crypto.OTP") -> key ->[Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word") ->[OTP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTP "Crypto.OTP")
*   [resynchronize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:resynchronize) :: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key) => hash ->[OTPDigits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPDigits "Crypto.OTP") ->[Word16](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word16 "Data.Word") -> key ->[Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word") -> ([OTP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTP "Crypto.OTP"), [[OTP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTP "Crypto.OTP")]) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word")
*   [totp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:totp) :: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key) =>[TOTPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:TOTPParams "Crypto.OTP") hash -> key ->[OTPTime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPTime "Crypto.OTP") ->[OTP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTP "Crypto.OTP")
*   [totpVerify](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:totpVerify) :: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key) =>[TOTPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:TOTPParams "Crypto.OTP") hash -> key ->[OTPTime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPTime "Crypto.OTP") ->[OTP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTP "Crypto.OTP") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   data[TOTPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:TOTPParams) h
*   data[ClockSkew](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:ClockSkew)
    *   = [NoSkew](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:NoSkew)
    *   | [OneStep](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:OneStep)
    *   | [TwoSteps](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:TwoSteps)
    *   | [ThreeSteps](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:ThreeSteps)
    *   | [FourSteps](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:FourSteps)

*   [defaultTOTPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:defaultTOTPParams) :: [TOTPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:TOTPParams "Crypto.OTP")[SHA1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA1 "Crypto.Hash.Algorithms")
*   [mkTOTPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:mkTOTPParams) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash => hash ->[OTPTime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPTime "Crypto.OTP") ->[Word16](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word16 "Data.Word") ->[OTPDigits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPDigits "Crypto.OTP") ->[ClockSkew](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:ClockSkew "Crypto.OTP") ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String") ([TOTPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:TOTPParams "Crypto.OTP") hash)

Documentation
-------------

type[OTP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html) = [Word32](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word32 "Data.Word")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.OTP.html#OTP)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTP)

A one-time password which is a sequence of 4 to 9 digits.

data[OTPDigits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.OTP.html#OTPDigits)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPDigits)

The strength of the calculated HOTP value, namely the number of digits (between 4 and 9) in the extracted value.

Constructors

[OTP4](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)
[OTP5](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)
[OTP6](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)
[OTP7](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)
[OTP8](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)
[OTP9](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)

[hotp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.OTP.html#hotp)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:hotp)

Arguments

:: forall hash key. ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key)
=> hash
->[OTPDigits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPDigits "Crypto.OTP")Number of digits in the HOTP value extracted from the calculated HMAC
-> key Shared secret between the client and server
->[Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word")Counter value synchronized between the client and server
->[OTP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTP "Crypto.OTP")The HOTP value

[resynchronize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.OTP.html#resynchronize)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:resynchronize)

Arguments

:: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key)
=> hash
->[OTPDigits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPDigits "Crypto.OTP")
->[Word16](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word16 "Data.Word")The look-ahead window parameter. Up to this many values will be calculated and checked against the value(s) submitted by the client
-> key The shared secret
->[Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word")The current server counter value
-> ([OTP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTP "Crypto.OTP"), [[OTP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTP "Crypto.OTP")])The first OTP submitted by the client and a list of additional sequential OTPs (which may be empty)
->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word")The new counter value, synchronized with the client's current counter or Nothing if the submitted OTP values didn't match anywhere within the window

Attempt to resynchronize the server's counter value with the client, given a sequence of HOTP values.

[totp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.OTP.html#totp)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:totp)

Arguments

Calculate a totp value for the given time.

[mkTOTPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.OTP.html#mkTOTPParams)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#v:mkTOTPParams)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=> hash
->[OTPTime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPTime "Crypto.OTP")The T0 parameter in seconds. This is the Unix time from which to start counting steps (default 0). Must be before the current time.
->[Word16](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word16 "Data.Word")The time step parameter X in seconds (default 30, maximum allowed 300)
->[OTPDigits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:OTPDigits "Crypto.OTP")Number of required digits in the OTP (default 6)
->[ClockSkew](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:ClockSkew "Crypto.OTP")The number of time steps to check either side of the current value to allow for clock skew between client and server and or delay in submitting the value. The default is two time steps.
->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String") ([TOTPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html#t:TOTPParams "Crypto.OTP") hash)

Create a TOTP configuration with customized parameters.
