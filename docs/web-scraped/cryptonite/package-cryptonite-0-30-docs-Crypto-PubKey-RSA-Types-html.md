# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html

Title: Crypto.PubKey.RSA.Types

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html

Markdown Content:
Description

Synopsis
*   data[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error)
    *   = [MessageSizeIncorrect](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:MessageSizeIncorrect)
    *   | [MessageTooLong](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:MessageTooLong)
    *   | [MessageNotRecognized](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:MessageNotRecognized)
    *   | [SignatureTooLong](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:SignatureTooLong)
    *   | [InvalidParameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:InvalidParameters)

*   data[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Blinder) = [Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:Blinder) ![Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ![Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey) = [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:PublicKey) {
    *   [public_size](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:public_size) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
    *   [public_n](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:public_n) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [public_e](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:public_e) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

}
*   data[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey) = [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:PrivateKey) {
    *   [private_pub](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:private_pub) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")
    *   [private_d](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:private_d) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:private_p) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_q](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:private_q) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_dP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:private_dP) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_dQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:private_dQ) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_qinv](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:private_qinv) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

}
*   newtype[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair) = [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:KeyPair)[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")
*   [toPublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:toPublicKey) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")
*   [toPrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:toPrivateKey) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")
*   [private_size](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:private_size) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
*   [private_n](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:private_n) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [private_e](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:private_e) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

Documentation
-------------

data[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#Error)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error)

error possible during encryption, decryption or signing.

Constructors

data[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#Blinder)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Blinder)

Blinder which is used to obfuscate the timing of the decryption primitive (used by decryption and signing).

Constructors

data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#PublicKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey)

Represent a RSA public key

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-61--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-47--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") -> c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:toConstr) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataTypeOf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:show) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showList) :: [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:rnf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:rnf)

data[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#PrivateKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey)

Represent a RSA private key.

Only the pub, d fields are mandatory to fill.

p, q, dP, dQ, qinv are by-product during RSA generation, but are useful to record here to speed up massively the decrypt and sign operation.

implementations can leave optional fields to 0.

Constructors

[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)
Fields

*   [private_pub](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")
public part of a private key (size, n and e)

*   [private_d](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
private exponent d

*   [private_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
p prime number

*   [private_q](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
q prime number

*   [private_dP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
d mod (p-1)

*   [private_dQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
d mod (q-1)

*   [private_qinv](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
q^(-1) mod p

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-68)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-61--61-) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-47--61-) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-68)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") -> c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:toConstr) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataTypeOf) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-68)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-68)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:show) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showList) :: [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-70)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:rnf) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:rnf)

newtype[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#KeyPair)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair)

Represent RSA KeyPair

note the RSA private key contains already an instance of public key for efficiency

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-90)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-61--61-) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-47--61-) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-90)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") -> c [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:toConstr) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataTypeOf) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") -> m [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") -> m [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") -> m [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-90)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-90)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:show) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showList) :: [[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-90)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:rnf) :: [KeyPair](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:KeyPair "Crypto.PubKey.RSA.Types") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#v:rnf)
