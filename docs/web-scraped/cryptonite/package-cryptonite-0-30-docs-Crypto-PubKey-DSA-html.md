# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html

Title: Crypto.PubKey.DSA

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html

Markdown Content:
Contents

*   [Generation](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#g:1)
*   [Signature primitive](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#g:2)
*   [Verification primitive](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#g:3)
*   [Key pair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#g:4)

Description

An implementation of the Digital Signature Algorithm (DSA)

Synopsis
*   data[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params) = [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:Params) {
    *   [params_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:params_p) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [params_g](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:params_g) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [params_q](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:params_q) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

}
*   data[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature) = [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:Signature) {
    *   [sign_r](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:sign_r) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [sign_s](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:sign_s) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

}
*   data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey) = [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:PublicKey) {
    *   [public_params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:public_params) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")
    *   [public_y](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:public_y) :: [PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicNumber "Crypto.PubKey.DSA")

}
*   data[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey) = [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:PrivateKey) {
    *   [private_params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:private_params) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")
    *   [private_x](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:private_x) :: [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateNumber "Crypto.PubKey.DSA")

}
*   type[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicNumber) = [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   type[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateNumber) = [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [generatePrivate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:generatePrivate) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") -> m [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateNumber "Crypto.PubKey.DSA")
*   [calculatePublic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:calculatePublic) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") ->[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateNumber "Crypto.PubKey.DSA") ->[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicNumber "Crypto.PubKey.DSA")
*   [sign](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:sign) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") msg, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m) =>[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") -> hash -> msg -> m [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")
*   [signWith](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:signWith) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") msg, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash) =>[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") -> hash -> msg ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")
*   [verify](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:verify) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") msg, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash) => hash ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") -> msg ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   data[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair) = [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:KeyPair)[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[PublicNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicNumber "Crypto.PubKey.DSA")[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateNumber "Crypto.PubKey.DSA")
*   [toPublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toPublicKey) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")
*   [toPrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toPrivateKey) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")

Documentation
-------------

data[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#Params)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params)

Represent DSA parameters namely P, G, and Q.

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-61--61-) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-47--61-) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") -> c [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toConstr) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataTypeOf) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") -> m [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") -> m [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") -> m [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:show) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showList) :: [[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-56)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:rnf) :: [Params](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Params "Crypto.PubKey.DSA") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:rnf)

data[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#Signature)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature)

Represent a DSA signature namely R and S.

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-63)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-61--61-) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-47--61-) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-63)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") -> c [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toConstr) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataTypeOf) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") -> m [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") -> m [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") -> m [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-63)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-63)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:show) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showList) :: [[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-65)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:rnf) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:rnf)

data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#PublicKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey)

Represent a DSA public key.

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-72)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-61--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-47--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-72)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") -> c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toConstr) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataTypeOf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-72)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-72)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:show) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showList) :: [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-74)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:rnf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PublicKey "Crypto.PubKey.DSA") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:rnf)

data[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#PrivateKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey)

Represent a DSA private key.

Only x need to be secret. the DSA parameters are publicly shared with the other side.

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-84)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-61--61-) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-47--61-) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-84)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") -> c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toConstr) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataTypeOf) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-84)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-84)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:show) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showList) :: [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-86)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:rnf) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:rnf)

[Generation ----------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#g:1)[Signature primitive -------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#g:2)

[signWith](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#signWith)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:signWith)

Arguments

:: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") msg, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash)
=>[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")k random number
->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:PrivateKey "Crypto.PubKey.DSA")private key
-> hash hash function
-> msg message to sign
->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:Signature "Crypto.PubKey.DSA")

sign message using the private key and an explicit k number.

[Verification primitive ----------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#g:3)[Key pair --------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#g:4)

data[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#KeyPair)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair)

Represent a DSA key pair

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-91)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-61--61-) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-47--61-) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-91)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") -> c [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toConstr) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataTypeOf) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") -> m [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") -> m [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") -> m [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-91)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-91)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:show) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showList) :: [[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.DSA.html#line-93)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair)
Instance details
Defined in [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:rnf) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#t:KeyPair "Crypto.PubKey.DSA") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html#v:rnf)
