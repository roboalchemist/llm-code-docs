# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html

Title: Crypto.PubKey.Rabin.Basic

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html

Markdown Content:
Crypto.PubKey.Rabin.Basic
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Carlos Rodriguez-Vega <crodveg@yahoo.es> |
| Stability | experimental |
| Portability | unknown |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.PubKey.Rabin.Basic

Description

Rabin cryptosystem for public-key cryptography and digital signature.

Synopsis
*   data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey) = [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:PublicKey) {
    *   [public_size](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:public_size) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
    *   [public_n](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:public_n) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

}
*   data[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey) = [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:PrivateKey) {
    *   [private_pub](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:private_pub) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")
    *   [private_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:private_p) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_q](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:private_q) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_a](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:private_a) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_b](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:private_b) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

}
*   data[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature) = [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:Signature) ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"))
*   [generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:generate) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> m ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic"), [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic"))
*   [encrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:encrypt) :: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m) =>[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") -> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString"))
*   [encryptWithSeed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:encryptWithSeed) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")
*   [decrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:decrypt) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")
*   [sign](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:sign) :: ([MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash) =>[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") -> hash ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") -> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic"))
*   [signWith](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:signWith) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") -> hash ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")
*   [verify](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:verify) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") -> hash ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")

Documentation
=============

data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#PublicKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey)

Represent a Rabin public key.

Constructors

[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)
Fields

*   [public_size](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")size of key in bytes 
*   [public_n](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")public p*q

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-41)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-61--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-47--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-41)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") -> c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:toConstr) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataTypeOf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-41)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-41)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:show) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showList) :: [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showList)

data[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#PrivateKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey)

Represent a Rabin private key.

Constructors

[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)
Fields

*   [private_pub](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic") 
*   [private_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")p prime number 
*   [private_q](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")q prime number 
*   [private_a](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") 
*   [private_b](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-61--61-) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-47--61-) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") -> c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:toConstr) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataTypeOf) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:show) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showList) :: [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showList)

data[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#Signature)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature)

Rabin Signature.

Constructors

[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html) ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"))

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-53)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-61--61-) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-47--61-) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-53)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") -> c [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:toConstr) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataTypeOf) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") -> m [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") -> m [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") -> m [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-53)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#line-53)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:show) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showList) :: [[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:showList)

[generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> m ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic"), [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#generate)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:generate)

Generate a pair of (private, public) key of size in bytes. Primes p and q are both congruent 3 mod 4.

See algorithm 8.11 in "Handbook of Applied Cryptography" by Alfred J. Menezes et al.

[encrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#encrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:encrypt)

Arguments

:: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m)
=>[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")OAEP padding parameters
->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")public key
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")plaintext
-> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString"))

Encrypt plaintext using public key.

[encryptWithSeed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#encryptWithSeed)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:encryptWithSeed)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=>[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")Seed
->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")OAEP padding
->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")public key
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")plaintext
->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")

Encrypt plaintext using public key an a predefined OAEP seed.

See algorithm 8.11 in "Handbook of Applied Cryptography" by Alfred J. Menezes et al.

[decrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#decrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:decrypt)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=>[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")OAEP padding parameters
->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")private key
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")ciphertext
->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")

Decrypt ciphertext using private key.

See algorithm 8.12 in "Handbook of Applied Cryptography" by Alfred J. Menezes et al.

[sign](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#sign)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:sign)

Arguments

:: ([MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash)
=>[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")private key
-> hash hash function
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")message to sign
-> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic"))

Sign message using hash algorithm and private key.

See [https://en.wikipedia.org/wiki/Rabin_signature_algorithm](https://en.wikipedia.org/wiki/Rabin_signature_algorithm).

[signWith](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#signWith)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:signWith)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=>[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")padding
->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PrivateKey "Crypto.PubKey.Rabin.Basic")private key
-> hash hash function
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")message to sign
->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")

Sign message using padding, hash algorithm and private key.

See [https://en.wikipedia.org/wiki/Rabin_signature_algorithm](https://en.wikipedia.org/wiki/Rabin_signature_algorithm).

[verify](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Basic.html#verify)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#v:verify)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=>[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:PublicKey "Crypto.PubKey.Rabin.Basic")private key
-> hash hash function
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")message
->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html#t:Signature "Crypto.PubKey.Rabin.Basic")signature
->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")

Verify signature using hash algorithm and public key.

See [https://en.wikipedia.org/wiki/Rabin_signature_algorithm](https://en.wikipedia.org/wiki/Rabin_signature_algorithm).

Produced by [Haddock](http://www.haskell.org/haddock/) version 2.24.0
