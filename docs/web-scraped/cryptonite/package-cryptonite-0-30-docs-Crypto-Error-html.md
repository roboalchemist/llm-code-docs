# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html

Title: Crypto.Error

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html

Markdown Content:
Crypto.Error
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Instances](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#)
*   [Quick Jump](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#)
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | Stable |
| Portability | Excellent |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.Error

Description

Synopsis
*   data[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError)
    *   = [CryptoError_KeySizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_KeySizeInvalid)
    *   | [CryptoError_IvSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_IvSizeInvalid)
    *   | [CryptoError_SeedSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_SeedSizeInvalid)
    *   | [CryptoError_AEADModeNotSupported](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_AEADModeNotSupported)
    *   | [CryptoError_SecretKeySizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_SecretKeySizeInvalid)
    *   | [CryptoError_SecretKeyStructureInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_SecretKeyStructureInvalid)
    *   | [CryptoError_PublicKeySizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_PublicKeySizeInvalid)
    *   | [CryptoError_SharedSecretSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_SharedSecretSizeInvalid)
    *   | [CryptoError_EcScalarOutOfBounds](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_EcScalarOutOfBounds)
    *   | [CryptoError_PointSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_PointSizeInvalid)
    *   | [CryptoError_PointFormatInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_PointFormatInvalid)
    *   | [CryptoError_PointFormatUnsupported](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_PointFormatUnsupported)
    *   | [CryptoError_PointCoordinatesInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_PointCoordinatesInvalid)
    *   | [CryptoError_ScalarMultiplicationInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_ScalarMultiplicationInvalid)
    *   | [CryptoError_MacKeyInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_MacKeyInvalid)
    *   | [CryptoError_AuthenticationTagSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_AuthenticationTagSizeInvalid)
    *   | [CryptoError_PrimeSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_PrimeSizeInvalid)
    *   | [CryptoError_SaltTooSmall](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_SaltTooSmall)
    *   | [CryptoError_OutputLengthTooSmall](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_OutputLengthTooSmall)
    *   | [CryptoError_OutputLengthTooBig](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoError_OutputLengthTooBig)

*   data[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable) a
    *   = [CryptoPassed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoPassed) a
    *   | [CryptoFailed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:CryptoFailed)[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")

*   [throwCryptoErrorIO](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:throwCryptoErrorIO) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a
*   [throwCryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:throwCryptoError) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a -> a
*   [onCryptoFailure](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:onCryptoFailure) :: ([CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> r) -> (a -> r) ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a -> r
*   [eitherCryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:eitherCryptoError) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") a
*   [maybeCryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:maybeCryptoError) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") a

Documentation
=============

data[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#CryptoError)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError)

Enumeration of all possible errors that can be found in this library

Constructors

[CryptoError_KeySizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_IvSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_SeedSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_AEADModeNotSupported](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_SecretKeySizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_SecretKeyStructureInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_PublicKeySizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_SharedSecretSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_EcScalarOutOfBounds](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_PointSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_PointFormatInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_PointFormatUnsupported](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_PointCoordinatesInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_ScalarMultiplicationInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_MacKeyInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_AuthenticationTagSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_PrimeSizeInvalid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_SaltTooSmall](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_OutputLengthTooSmall](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
[CryptoError_OutputLengthTooBig](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)

#### Instances

Instances details
[Enum](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Enum "Prelude")[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-55)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

Methods

[succ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:succ) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:succ)

[pred](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:pred) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:pred)

[toEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:toEnum) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:toEnum)

[fromEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:fromEnum) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:fromEnum)

[enumFrom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:enumFrom) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> [[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:enumFrom)

[enumFromThen](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:enumFromThen) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> [[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:enumFromThen)

[enumFromTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:enumFromTo) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> [[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:enumFromTo)

[enumFromThenTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:enumFromThenTo) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> [[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:enumFromThenTo)
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-55)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-61--61-) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-47--61-) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-55)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> c [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:toConstr) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:dataTypeOf) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> m [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> m [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> m [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:gmapMo)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-55)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:show) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:showList) :: [[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:showList)
[Exception](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Exception-Base.html#t:Exception "Control.Exception.Base")[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-57)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

Methods

[toException](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:toException) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[SomeException](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Exception-Base.html#t:SomeException "Control.Exception.Base")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:toException)

[fromException](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:fromException) :: [SomeException](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Exception-Base.html#t:SomeException "Control.Exception.Base") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:fromException)

[displayException](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:displayException) :: [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:displayException)

data[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html) a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#CryptoFailable)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable)

A simple Either like type to represent a computation that can fail

2 possibles values are:

*   `CryptoPassed` : The computation succeeded, and contains the result of the computation
*   `CryptoFailed` : The computation failed, and contains the cryptographic error associated

Constructors

[CryptoPassed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html) a
[CryptoFailed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")

#### Instances

Instances details
[Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad")[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-84)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

Methods

[(>>=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-62--62--61-) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a -> (a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") b) ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-62--62--61-)

[(>>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-62--62-) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") b ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-62--62-)

[return](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:return) :: a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:return)
[Functor](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Functor.html#t:Functor "Data.Functor")[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-77)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

Methods

[fmap](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:fmap) :: (a -> b) ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:fmap)

[(<$)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-60--36-) :: a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") b ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-60--36-)
[Applicative](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Applicative.html#t:Applicative "Control.Applicative")[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-81)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

Methods

[pure](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:pure) :: a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:pure)

[(<*>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-60--42--62-) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") (a -> b) ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-60--42--62-)

[liftA2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:liftA2) :: (a -> b -> c) ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") b ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") c [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:liftA2)

[(*>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-42--62-) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") b ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-42--62-)

[(<*)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-60--42-) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") b ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-60--42-)
[MonadFailure](https://hackage.haskell.org/package/basement-0.0.14/docs/Basement-Monad.html#t:MonadFailure "Basement.Monad")[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-91)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

Associated Types

type[Failure](https://hackage.haskell.org/package/basement-0.0.14/docs/Basement-Monad.html#t:Failure "Basement.Monad")[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:Failure)

Methods

[mFail](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:mFail) :: [Failure](https://hackage.haskell.org/package/basement-0.0.14/docs/Basement-Monad.html#t:Failure "Basement.Monad")[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:mFail)
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq") a =>[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq") ([CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-72)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-61--61-) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-47--61-) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show") a =>[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show") ([CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-70)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:show) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:showList) :: [[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:showList)
type[Failure](https://hackage.haskell.org/package/basement-0.0.14/docs/Basement-Monad.html#t:Failure "Basement.Monad")[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#line-92)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable)
Instance details
Defined in [Crypto.Error.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error-Types.html)

type[Failure](https://hackage.haskell.org/package/basement-0.0.14/docs/Basement-Monad.html#t:Failure "Basement.Monad")[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") = [CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error")

[throwCryptoErrorIO](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#throwCryptoErrorIO)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:throwCryptoErrorIO)

Throw an CryptoError as exception on CryptoFailed result, otherwise return the computed value

[throwCryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a -> a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#throwCryptoError)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:throwCryptoError)

Same as `throwCryptoErrorIO` but throw the error asynchronously.

[onCryptoFailure](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html) :: ([CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") -> r) -> (a -> r) ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a -> r [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#onCryptoFailure)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:onCryptoFailure)

Simple `either` like combinator for CryptoFailable type

[eitherCryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[CryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoError "Crypto.Error") a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#eitherCryptoError)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:eitherCryptoError)

Transform a CryptoFailable to an Either

[maybeCryptoError](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html) :: [CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") a ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Error.Types.html#maybeCryptoError)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#v:maybeCryptoError)

Transform a CryptoFailable to a Maybe

Produced by [Haddock](http://www.haskell.org/haddock/) version 2.24.0

Linuwial

You can find any exported type, constructor, class, function or pattern defined in this package by (approximate) name.

| Key | Shortcut |
| --- | --- |
| s | Open this search box |
| esc | Close this search box |
| ↓,ctrl + j | Move down in search results |
| ↑,ctrl + k | Move up in search results |
| ↵ | Go to active search result |

Expand All Instances Collapse All Instances

- [x] Collapse All Instances By Default

- [x] Remember Manually Collapsed/Expanded Instances
