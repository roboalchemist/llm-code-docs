# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html

Title: Crypto.PubKey.DH

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html

Markdown Content:
Crypto.PubKey.DH
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | experimental |
| Portability | Good |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.PubKey.DH

Description

Synopsis
*   data[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params) = [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:Params) {
    *   [params_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:params_p) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [params_g](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:params_g) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [params_bits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:params_bits) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")

}
*   newtype[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber) = [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:PublicNumber)[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   newtype[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber) = [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:PrivateNumber)[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   newtype[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey) = [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:SharedKey)[ScrubbedBytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ScrubbedBytes "Data.ByteArray")
*   [generateParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:generateParams) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> m [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")
*   [generatePrivate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:generatePrivate) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") -> m [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")
*   [calculatePublic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:calculatePublic) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")
*   [generatePublic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:generatePublic) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")
*   [getShared](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:getShared) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH")

Documentation
=============

data[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#Params)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params)

Represent Diffie Hellman parameters namely P (prime), and G (generator).

Constructors

[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)
Fields

*   [params_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") 
*   [params_g](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") 
*   [params_bits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-61--61-) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-47--61-) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") -> c [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:toConstr) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:dataTypeOf) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") -> m [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") -> m [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") -> m [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:show) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showList) :: [[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-38)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:rnf) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:rnf)

newtype[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#PublicNumber)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber)

Represent Diffie Hellman public number Y.

Constructors

[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

#### Instances

Instances details
[Enum](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Enum "Prelude")[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-43)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[succ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:succ) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:succ)

[pred](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:pred) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:pred)

[toEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:toEnum) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:toEnum)

[fromEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:fromEnum) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:fromEnum)

[enumFrom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFrom) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") -> [[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFrom)

[enumFromThen](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromThen) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") -> [[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromThen)

[enumFromTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromTo) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") -> [[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromTo)

[enumFromThenTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromThenTo) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") -> [[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromThenTo)
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-43)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-61--61-) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-47--61-) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-47--61-)
[Num](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Num "Prelude")[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-43)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[(+)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-43-) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-43-)

[(-)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-45-) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-45-)

[(*)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-42-) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-42-)

[negate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:negate) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:negate)

[abs](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:abs) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:abs)

[signum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:signum) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:signum)

[fromInteger](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:fromInteger) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:fromInteger)
[Ord](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ord "Data.Ord")[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-43)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[compare](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:compare) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[Ordering](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ordering "Data.Ord")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:compare)

[(<)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-60-) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-60-)

[(<=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-60--61-) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-60--61-)

[(>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-62-) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-62-)

[(>=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-62--61-) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-62--61-)

[max](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:max) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:max)

[min](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:min) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:min)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-43)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readListPrec)
[Real](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Real "Prelude")[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-43)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[toRational](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:toRational) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[Rational](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Rational "Prelude")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:toRational)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-43)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:show) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showList) :: [[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-43)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:rnf) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:rnf)

newtype[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#PrivateNumber)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber)

Represent Diffie Hellman private number X.

Constructors

[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

#### Instances

Instances details
[Enum](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Enum "Prelude")[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[succ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:succ) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:succ)

[pred](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:pred) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:pred)

[toEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:toEnum) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:toEnum)

[fromEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:fromEnum) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:fromEnum)

[enumFrom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFrom) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") -> [[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFrom)

[enumFromThen](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromThen) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") -> [[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromThen)

[enumFromTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromTo) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") -> [[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromTo)

[enumFromThenTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromThenTo) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") -> [[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:enumFromThenTo)
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-61--61-) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-47--61-) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-47--61-)
[Num](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Num "Prelude")[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[(+)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-43-) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-43-)

[(-)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-45-) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-45-)

[(*)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-42-) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-42-)

[negate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:negate) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:negate)

[abs](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:abs) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:abs)

[signum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:signum) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:signum)

[fromInteger](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:fromInteger) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:fromInteger)
[Ord](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ord "Data.Ord")[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[compare](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:compare) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[Ordering](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ordering "Data.Ord")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:compare)

[(<)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-60-) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-60-)

[(<=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-60--61-) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-60--61-)

[(>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-62-) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-62-)

[(>=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-62--61-) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-62--61-)

[max](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:max) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:max)

[min](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:min) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:min)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:readListPrec)
[Real](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Real "Prelude")[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[toRational](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:toRational) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[Rational](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Rational "Prelude")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:toRational)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:show) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showList) :: [[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:rnf) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:rnf)

newtype[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#SharedKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey)

Represent Diffie Hellman shared secret.

Constructors

[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)[ScrubbedBytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ScrubbedBytes "Data.ByteArray")

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-61--61-) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH") ->[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-47--61-) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH") ->[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:show) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showList) :: [[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:rnf) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey)
Instance details
Defined in [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:length) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:withByteArray) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:copyByteArrayToPtr) :: [SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:copyByteArrayToPtr)

[generateParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#generateParams)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:generateParams)

Arguments

:: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m
=>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")number of bits
->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")generator
-> m [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH")

generate params from a specific generator (2 or 5 are common values) we generate a safe prime (a prime number of the form 2p+1 where p is also prime)

[generatePrivate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") -> m [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#generatePrivate)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:generatePrivate)

generate a private number with no specific property this number is usually called X in DH text.

[calculatePublic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#calculatePublic)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:calculatePublic)

calculate the public number from the parameters and the private key this number is usually called Y in DH text.

[generatePublic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#generatePublic)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:generatePublic)

calculate the public number from the parameters and the private key this number is usually called Y in DH text.

DEPRECATED use calculatePublic

[getShared](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:Params "Crypto.PubKey.DH") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PrivateNumber "Crypto.PubKey.DH") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:PublicNumber "Crypto.PubKey.DH") ->[SharedKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#t:SharedKey "Crypto.PubKey.DH")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DH.html#getShared)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html#v:getShared)

generate a shared key using our private number and the other party public number

Produced by [Haddock](http://www.haskell.org/haddock/) version 2.24.0
