# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html

Title: Crypto.PubKey.ECC.P256

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html

Markdown Content:
Crypto.PubKey.ECC.P256
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Instances](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#)
*   [Quick Jump](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#)
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | experimental |
| Portability | unknown |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.PubKey.ECC.P256

Contents

*   [Point arithmetic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#g:1)
*   [Scalar arithmetic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#g:2)

Description

P256 support

Synopsis
*   data[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar)
*   data[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point)
*   [pointBase](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointBase) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")
*   [pointAdd](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointAdd) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")
*   [pointNegate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointNegate) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")
*   [pointMul](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointMul) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")
*   [pointDh](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointDh) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") binary =>[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") -> binary
*   [pointsMulVarTime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointsMulVarTime) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")
*   [pointIsValid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointIsValid) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [pointIsAtInfinity](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointIsAtInfinity) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [toPoint](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:toPoint) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")
*   [pointX](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointX) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")
*   [pointToIntegers](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointToIntegers) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") -> ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"))
*   [pointFromIntegers](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointFromIntegers) :: ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")) ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")
*   [pointToBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointToBinary) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") -> ba
*   [pointFromBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointFromBinary) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")
*   [unsafePointFromBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:unsafePointFromBinary) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")
*   [scalarGenerate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarGenerate) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") randomly => randomly [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")
*   [scalarZero](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarZero) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")
*   [scalarN](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarN) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")
*   [scalarIsZero](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarIsZero) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [scalarAdd](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarAdd) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")
*   [scalarSub](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarSub) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")
*   [scalarMul](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarMul) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")
*   [scalarInv](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarInv) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")
*   [scalarInvSafe](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarInvSafe) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")
*   [scalarCmp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarCmp) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Ordering](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ordering "Data.Ord")
*   [scalarFromBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarFromBinary) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")
*   [scalarToBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarToBinary) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") -> ba
*   [scalarFromInteger](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarFromInteger) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")
*   [scalarToInteger](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarToInteger) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

Documentation
=============

data[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#Scalar)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar)

A P256 scalar

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#line-65)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar)
Instance details
Defined in [Crypto.PubKey.ECC.P256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:-61--61-) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:-47--61-) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#line-65)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar)
Instance details
Defined in [Crypto.PubKey.ECC.P256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:show) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:showList) :: [[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#line-65)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar)
Instance details
Defined in [Crypto.PubKey.ECC.P256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:rnf) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#line-65)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar)
Instance details
Defined in [Crypto.PubKey.ECC.P256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:length) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:withByteArray) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:copyByteArrayToPtr) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:copyByteArrayToPtr)

data[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#Point)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point)

A P256 point

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#line-69)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point)
Instance details
Defined in [Crypto.PubKey.ECC.P256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:-61--61-) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:-47--61-) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#line-69)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point)
Instance details
Defined in [Crypto.PubKey.ECC.P256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:show) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:showList) :: [[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#line-69)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point)
Instance details
Defined in [Crypto.PubKey.ECC.P256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:rnf) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:rnf)

[Point arithmetic ================](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#g:1)

[pointBase](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointBase)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointBase)

Get the base point for the P256 Curve

[pointAdd](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointAdd)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointAdd)

Add a point to another point

[pointNegate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointNegate)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointNegate)

Negate a point

[pointMul](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointMul)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointMul)

Multiply a point by a scalar

warning: variable time

[pointDh](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") binary =>[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") -> binary [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointDh)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointDh)

Similar to `pointMul`, serializing the x coordinate as binary. When scalar is multiple of point order the result is all zero.

[pointsMulVarTime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointsMulVarTime)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointsMulVarTime)

multiply the point `p with`n2 and add a lifted to curve value @n1

n1 * G + n2 * p
warning: variable time

[pointIsValid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointIsValid)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointIsValid)

Check if a `Point` is valid

[pointIsAtInfinity](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointIsAtInfinity)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointIsAtInfinity)

Check if a `Point` is the point at infinity

[toPoint](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#toPoint)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:toPoint)

Lift to curve a scalar

Using the curve generator as base point compute:

scalar * G

[pointX](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointX)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointX)

Return the x coordinate as a `Scalar` if the point is not at infinity

[pointToIntegers](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") -> ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointToIntegers)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointToIntegers)

Convert a point to (x,y) Integers

[pointFromIntegers](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")) ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointFromIntegers)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointFromIntegers)

Convert from (x,y) Integers to a point

[pointToBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256") -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointToBinary)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointToBinary)

Convert a point to a binary representation

[pointFromBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#pointFromBinary)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:pointFromBinary)

Convert from binary to a valid point

[unsafePointFromBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Point "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#unsafePointFromBinary)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:unsafePointFromBinary)

Convert from binary to a point, possibly invalid

[Scalar arithmetic =================](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#g:2)

[scalarGenerate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") randomly => randomly [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarGenerate)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarGenerate)

Generate a randomly generated new scalar

[scalarZero](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarZero)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarZero)

The scalar representing 0

[scalarN](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarN)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarN)

The scalar representing the curve order

[scalarIsZero](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarIsZero)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarIsZero)

Check if the scalar is 0

[scalarAdd](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarAdd)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarAdd)

Perform addition between two scalars

a + b

[scalarSub](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarSub)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarSub)

Perform subtraction between two scalars

a - b

[scalarMul](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarMul)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarMul)

Perform multiplication between two scalars

a * b

[scalarInv](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarInv)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarInv)

Give the inverse of the scalar

1 / a
warning: variable time

[scalarInvSafe](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarInvSafe)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarInvSafe)

Give the inverse of the scalar using safe exponentiation

1 / a

[scalarCmp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Ordering](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ordering "Data.Ord")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarCmp)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarCmp)

Compare 2 Scalar

[scalarFromBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarFromBinary)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarFromBinary)

convert a scalar from binary

[scalarToBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarToBinary)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarToBinary)

convert a scalar to binary

[scalarFromInteger](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarFromInteger)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarFromInteger)

Convert from an Integer to a P256 Scalar

[scalarToInteger](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html) :: [Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#t:Scalar "Crypto.PubKey.ECC.P256") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.P256.html#scalarToInteger)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html#v:scalarToInteger)

Convert from a P256 Scalar to an Integer

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
