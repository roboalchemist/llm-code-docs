# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html

Title: Crypto.PubKey.ECC.DH

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html

Markdown Content:
Crypto.PubKey.ECC.DH
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Instances](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#)
*   [Quick Jump](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#)
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.DH.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | experimental |
| Portability | unknown |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.PubKey.ECC.DH

Description

Elliptic curve Diffie Hellman

Synopsis
*   data[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve)
*   type[PublicPoint](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PublicPoint) = [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")
*   type[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PrivateNumber) = [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   newtype[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey) = [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:SharedKey)[ScrubbedBytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ScrubbedBytes "Data.ByteArray")
*   [generatePrivate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:generatePrivate) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") -> m [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PrivateNumber "Crypto.PubKey.ECC.DH")
*   [calculatePublic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:calculatePublic) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PrivateNumber "Crypto.PubKey.ECC.DH") ->[PublicPoint](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PublicPoint "Crypto.PubKey.ECC.DH")
*   [getShared](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:getShared) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PrivateNumber "Crypto.PubKey.ECC.DH") ->[PublicPoint](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PublicPoint "Crypto.PubKey.ECC.DH") ->[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH")

Documentation
=============

data[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#Curve)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve)

Define either a binary curve or a prime curve.

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:-61--61-) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:-47--61-) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") -> c [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:toConstr) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:dataTypeOf) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") -> m [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") -> m [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") -> m [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:show) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:showList) :: [[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:showList)

type[PublicPoint](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html) = [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#PublicPoint)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PublicPoint)

ECC Public Point

type[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html) = [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#PrivateNumber)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PrivateNumber)

ECC Private Number

newtype[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#SharedKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey)

Represent Diffie Hellman shared secret.

Constructors

[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html)[ScrubbedBytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ScrubbedBytes "Data.ByteArray")

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:-61--61-) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH") ->[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:-47--61-) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH") ->[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:show) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:showList) :: [[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:rnf) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:length) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:withByteArray) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:copyByteArrayToPtr) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:copyByteArrayToPtr)

[generatePrivate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") -> m [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PrivateNumber "Crypto.PubKey.ECC.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.DH.html#generatePrivate)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:generatePrivate)

Generating a private number d.

[calculatePublic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PrivateNumber "Crypto.PubKey.ECC.DH") ->[PublicPoint](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PublicPoint "Crypto.PubKey.ECC.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.DH.html#calculatePublic)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:calculatePublic)

Generating a public point Q.

[getShared](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:Curve "Crypto.PubKey.ECC.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PrivateNumber "Crypto.PubKey.ECC.DH") ->[PublicPoint](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:PublicPoint "Crypto.PubKey.ECC.DH") ->[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#t:SharedKey "Crypto.PubKey.ECC.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.DH.html#getShared)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html#v:getShared)

Generating a shared key using our private number and the other party public point.

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
