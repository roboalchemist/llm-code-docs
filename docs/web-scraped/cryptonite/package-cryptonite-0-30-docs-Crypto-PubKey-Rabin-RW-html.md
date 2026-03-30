# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html

Title: Crypto.PubKey.Rabin.RW

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html

Markdown Content:
Crypto.PubKey.Rabin.RW
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Instances](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#)
*   [Quick Jump](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#)
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Carlos Rodriguez-Vega <crodveg@yahoo.es> |
| Stability | experimental |
| Portability | unknown |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.PubKey.Rabin.RW

Description

Rabin-Williams cryptosystem for public-key encryption and digital signature. See pages 323 - 324 in "Computational Number Theory and Modern Cryptography" by Song Y. Yan. Also inspired by [https://github.com/vanilala/vncrypt/blob/master/vncrypt/vnrw_gmp.c](https://github.com/vanilala/vncrypt/blob/master/vncrypt/vnrw_gmp.c).

Synopsis
*   data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey) = [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:PublicKey) {
    *   [public_size](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:public_size) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
    *   [public_n](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:public_n) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

}
*   data[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey) = [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:PrivateKey) {
    *   [private_pub](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:private_pub) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")
    *   [private_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:private_p) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_q](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:private_q) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_d](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:private_d) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

}
*   [generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:generate) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> m ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW"), [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW"))
*   [encrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:encrypt) :: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m) =>[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") -> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString"))
*   [encryptWithSeed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:encryptWithSeed) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")
*   [decrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:decrypt) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")
*   [sign](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:sign) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") -> hash ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [verify](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:verify) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") -> hash ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")

Documentation
=============

data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#PublicKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey)

Represent a Rabin-Williams public key.

Constructors

[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)
Fields

*   [public_size](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")size of key in bytes 
*   [public_n](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")public p*q

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#line-39)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Rabin.RW](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:-61--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:-47--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#line-39)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Rabin.RW](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") -> c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:toConstr) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataTypeOf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#line-39)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Rabin.RW](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#line-39)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Rabin.RW](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:show) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:showList) :: [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:showList)

data[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#PrivateKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey)

Represent a Rabin-Williams private key.

Constructors

[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)
Fields

*   [private_pub](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW") 
*   [private_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")p prime number 
*   [private_q](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")q prime number 
*   [private_d](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.Rabin.RW](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:-61--61-) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:-47--61-) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.Rabin.RW](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") -> c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:toConstr) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataTypeOf) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.Rabin.RW](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.Rabin.RW](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:show) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:showList) :: [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:showList)

[generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> m ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW"), [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#generate)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:generate)

Generate a pair of (private, public) key of size in bytes. Prime p is congruent 3 mod 8 and prime q is congruent 7 mod 8.

[encrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#encrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:encrypt)

Arguments

:: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m)
=>[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")OAEP padding parameters
->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")public key
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")plaintext
-> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString"))

Encrypt plaintext using public key.

[encryptWithSeed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#encryptWithSeed)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:encryptWithSeed)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=>[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")Seed
->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")OAEP padding
->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")public key
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")plaintext
->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")

Encrypt plaintext using public key an a predefined OAEP seed.

See algorithm 8.11 in "Handbook of Applied Cryptography" by Alfred J. Menezes et al.

[decrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#decrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:decrypt)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=>[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")OAEP padding parameters
->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")private key
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")ciphertext
->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")

Decrypt ciphertext using private key.

[sign](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#sign)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:sign)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=>[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PrivateKey "Crypto.PubKey.Rabin.RW")private key
-> hash hash function
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")message to sign
->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

Sign message using hash algorithm and private key.

[verify](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.RW.html#verify)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#v:verify)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=>[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html#t:PublicKey "Crypto.PubKey.Rabin.RW")public key
-> hash hash function
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")message
->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")signature
->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")

Verify signature using hash algorithm and public key.

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
