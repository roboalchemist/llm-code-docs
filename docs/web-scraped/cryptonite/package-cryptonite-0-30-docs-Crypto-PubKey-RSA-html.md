# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html

Title: Crypto.PubKey.RSA

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html

Markdown Content:
Crypto.PubKey.RSA
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Instances](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#)
*   [Quick Jump](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#)
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | experimental |
| Portability | Good |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.PubKey.RSA

Contents

*   [Generation function](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#g:1)

Description

Synopsis
*   data[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error)
    *   = [MessageSizeIncorrect](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:MessageSizeIncorrect)
    *   | [MessageTooLong](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:MessageTooLong)
    *   | [MessageNotRecognized](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:MessageNotRecognized)
    *   | [SignatureTooLong](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:SignatureTooLong)
    *   | [InvalidParameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:InvalidParameters)

*   data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey) = [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:PublicKey) {
    *   [public_size](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:public_size) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
    *   [public_n](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:public_n) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [public_e](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:public_e) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

}
*   data[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey) = [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:PrivateKey) {
    *   [private_pub](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:private_pub) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")
    *   [private_d](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:private_d) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:private_p) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_q](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:private_q) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_dP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:private_dP) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_dQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:private_dQ) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [private_qinv](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:private_qinv) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

}
*   data[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder) = [Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:Blinder) ![Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ![Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [generateWith](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:generateWith) :: ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")) ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA"), [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA"))
*   [generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:generate) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> m ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA"), [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA"))
*   [generateBlinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:generateBlinder) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> m [Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder "Crypto.PubKey.RSA")

Documentation
=============

data[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#Error)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error)

error possible during encryption, decryption or signing.

Constructors

[MessageSizeIncorrect](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)the message to decrypt is not of the correct size (need to be == private_size)
[MessageTooLong](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)the message to encrypt is too long
[MessageNotRecognized](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)the message decrypted doesn't have a PKCS15 structure (0 2 .. 0 msg)
[SignatureTooLong](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)the message's digest is too long
[InvalidParameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)some parameters lead to breaking assumptions.

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-38)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-61--61-) :: [Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error "Crypto.PubKey.RSA") ->[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error "Crypto.PubKey.RSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-47--61-) :: [Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error "Crypto.PubKey.RSA") ->[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error "Crypto.PubKey.RSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-38)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error "Crypto.PubKey.RSA") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:show) :: [Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error "Crypto.PubKey.RSA") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showList) :: [[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Error "Crypto.PubKey.RSA")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showList)

data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#PublicKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey)

Represent a RSA public key

Constructors

[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)
Fields

*   [public_size](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")size of key in bytes 
*   [public_n](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")public p*q 
*   [public_e](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")public exponent e

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-61--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-47--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") -> c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:toConstr) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataTypeOf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") -> m [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:show) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showList) :: [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:rnf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:rnf)

data[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#PrivateKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey)

Represent a RSA private key.

Only the pub, d fields are mandatory to fill.

p, q, dP, dQ, qinv are by-product during RSA generation, but are useful to record here to speed up massively the decrypt and sign operation.

implementations can leave optional fields to 0.

Constructors

[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)
Fields

*   [private_pub](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA")public part of a private key (size, n and e) 
*   [private_d](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")private exponent d 
*   [private_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")p prime number 
*   [private_q](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")q prime number 
*   [private_dP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")d mod (p-1) 
*   [private_dQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")d mod (q-1) 
*   [private_qinv](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")q^(-1) mod p

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-68)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-61--61-) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-47--61-) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-68)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") -> c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:toConstr) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataTypeOf) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") -> m [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-68)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-68)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:show) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showList) :: [[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-70)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:rnf) :: [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:rnf)

data[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#Blinder)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder)

Blinder which is used to obfuscate the timing of the decryption primitive (used by decryption and signing).

Constructors

[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html) ![Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ![Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-29)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-61--61-) :: [Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder "Crypto.PubKey.RSA") ->[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder "Crypto.PubKey.RSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-47--61-) :: [Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder "Crypto.PubKey.RSA") ->[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder "Crypto.PubKey.RSA") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder "Crypto.PubKey.RSA")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.Types.html#line-29)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder)
Instance details
Defined in [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder "Crypto.PubKey.RSA") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:show) :: [Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder "Crypto.PubKey.RSA") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showList) :: [[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder "Crypto.PubKey.RSA")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:showList)

[Generation function ===================](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#g:1)

[generateWith](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.html#generateWith)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:generateWith)

Arguments

:: ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"))chosen distinct primes p and q
->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")size in bytes
->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")RSA public exponent `e`
->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA"), [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA"))

Generate a key pair given p and q.

p and q need to be distinct prime numbers.

e need to be coprime to phi=(p-1)*(q-1). If that's not the case, the function will not return a key pair. A small hamming weight results in better performance.

*   e=0x10001 is a popular choice
*   e=3 is popular as well, but proven to not be as secure for some cases.

[generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.html#generate)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:generate)

Arguments

:: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m
=>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")size in bytes
->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")RSA public exponent `e`
-> m ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PublicKey "Crypto.PubKey.RSA"), [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:PrivateKey "Crypto.PubKey.RSA"))

generate a pair of (private, public) key of size in bytes.

[generateBlinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.html#generateBlinder)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#v:generateBlinder)

Arguments

:: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m
=>[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")RSA public N parameter.
-> m [Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html#t:Blinder "Crypto.PubKey.RSA")

Generate a blinder to use with decryption and signing operation

the unique parameter apart from the random number generator is the public key value N.

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
