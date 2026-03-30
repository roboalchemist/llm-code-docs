# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html

Title: Crypto.ECC.Edwards25519

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html

Markdown Content:
Contents

*   [Scalars](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#g:1)
*   [Points](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#g:2)
*   [Arithmetic functions](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#g:3)

Description

Arithmetic primitives over curve edwards25519.

Twisted Edwards curves are a familly of elliptic curves allowing complete addition formulas without any special case and no point at infinity. Curve edwards25519 is based on prime 2^255 - 19 for efficient implementation. Equation and parameters are given in [RFC 7748](https://tools.ietf.org/html/rfc7748).

This module provides types and primitive operations that are useful to implement cryptographic schemes based on curve edwards25519:

*   arithmetic functions for point addition, doubling, negation, scalar multiplication with an arbitrary point, with the base point, etc.
*   arithmetic functions dealing with scalars modulo the prime order L of the base point

All functions run in constant time unless noted otherwise.

Warnings:

1.   Curve edwards25519 has a cofactor h = 8 so the base point does not generate the entire curve and points with order 2, 4, 8 exist. When implementing cryptographic algorithms, special care must be taken using one of the following methods:

    *   points must be checked for membership in the prime-order subgroup
    *   or cofactor must be cleared by multiplying points by 8

Utility functions are provided to implement this. Testing subgroup membership with `pointHasPrimeOrder` is 50-time slower than call `pointMulByCofactor`.

2.   Scalar arithmetic is always reduced modulo L, allowing fixed length and constant execution time, but this reduction is valid only when points are in the prime-order subgroup.
3.   Because of modular reduction in this implementation it is not possible to multiply points directly by scalars like 8.s or L. This has to be decomposed into several steps.

Synopsis
*   data[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar)
*   data[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point)
*   [scalarGenerate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:scalarGenerate) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") randomly => randomly [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519")
*   [scalarDecodeLong](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:scalarDecodeLong) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bs => bs ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519")
*   [scalarEncode](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:scalarEncode) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") bs =>[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") -> bs
*   [pointDecode](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:pointDecode) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bs => bs ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")
*   [pointEncode](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:pointEncode) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") bs =>[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") -> bs
*   [pointHasPrimeOrder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:pointHasPrimeOrder) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [toPoint](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:toPoint) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")
*   [scalarAdd](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:scalarAdd) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519")
*   [scalarMul](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:scalarMul) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519")
*   [pointNegate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:pointNegate) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")
*   [pointAdd](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:pointAdd) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")
*   [pointDouble](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:pointDouble) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")
*   [pointMul](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:pointMul) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")
*   [pointMulByCofactor](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:pointMulByCofactor) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")
*   [pointsMulVarTime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:pointsMulVarTime) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")

Documentation
-------------

data[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ECC.Edwards25519.html#Scalar)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar)

A scalar modulo prime order of curve edwards25519.

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ECC.Edwards25519.html#line-95)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar)
Instance details
Defined in [Crypto.ECC.Edwards25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:-61--61-) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:-47--61-) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ECC.Edwards25519.html#line-93)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar)
Instance details
Defined in [Crypto.ECC.Edwards25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:show) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:showList) :: [[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ECC.Edwards25519.html#line-93)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar)
Instance details
Defined in [Crypto.ECC.Edwards25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:rnf) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:rnf)

data[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ECC.Edwards25519.html#Point)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point)

A point on curve edwards25519.

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ECC.Edwards25519.html#line-115)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point)
Instance details
Defined in [Crypto.ECC.Edwards25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:-61--61-) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:-47--61-) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ECC.Edwards25519.html#line-109)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point)
Instance details
Defined in [Crypto.ECC.Edwards25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:show) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:showList) :: [[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ECC.Edwards25519.html#line-107)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point)
Instance details
Defined in [Crypto.ECC.Edwards25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:rnf) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:rnf)

[Scalars -------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#g:1)

[scalarDecodeLong](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bs => bs ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ECC.Edwards25519.html#scalarDecodeLong)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:scalarDecodeLong)

Deserialize a little-endian number as a scalar. Input array can have any length from 0 to 64 bytes.

Note: it is not advised to put secret information in the 3 lowest bits of a scalar if this scalar may be multiplied to untrusted points outside the prime-order subgroup.

[Points ------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#g:2)[Arithmetic functions --------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#g:3)

[pointMul](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Scalar "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#t:Point "Crypto.ECC.Edwards25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ECC.Edwards25519.html#pointMul)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html#v:pointMul)

Scalar multiplication over curve edwards25519.

Note: when the scalar had reduction modulo L and the input point has a torsion component, the output point may not be in the expected subgroup.
