# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html

Title: Crypto.PubKey.Curve448

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html

Markdown Content:
Contents

*   [Smart constructors](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#g:1)
*   [Methods](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#g:2)

Description

Curve448 support

Internally uses Decaf point compression to omit the cofactor and implementation by Mike Hamburg. Externally API and data types are compatible with the encoding specified in RFC 7748.

Synopsis
*   data[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey)
*   data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey)
*   data[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret)
*   [dhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:dhSecret) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") b => b ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448")
*   [publicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:publicKey) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bs => bs ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448")
*   [secretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:secretKey) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bs => bs ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448")
*   [dh](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:dh) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") ->[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448")
*   [toPublic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:toPublic) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448")
*   [generateSecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:generateSecretKey) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m => m [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448")

Documentation
-------------

data[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#SecretKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey)

A Curve448 Secret key

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-41)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-61--61-) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-47--61-) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-41)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:show) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showList) :: [[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-41)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:rnf) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-41)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:length) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:withByteArray) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:copyByteArrayToPtr) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:copyByteArrayToPtr)

data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#PublicKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey)

A Curve448 public key

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-61--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-47--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:show) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showList) :: [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:rnf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:length) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:withByteArray) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:copyByteArrayToPtr) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:copyByteArrayToPtr)

data[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#DhSecret)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret)

A Curve448 Diffie Hellman secret related to a public key and a secret key.

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-61--61-) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448") ->[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-47--61-) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448") ->[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:show) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showList) :: [[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:rnf) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret)
Instance details
Defined in [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:length) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:withByteArray) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:copyByteArrayToPtr) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:copyByteArrayToPtr)

[Smart constructors ------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#g:1)[Methods -------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#g:2)

[dh](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:PublicKey "Crypto.PubKey.Curve448") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:SecretKey "Crypto.PubKey.Curve448") ->[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#t:DhSecret "Crypto.PubKey.Curve448")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve448.html#dh)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html#v:dh)

Compute the Diffie Hellman secret from a public key and a secret key.

This implementation may return an all-zero value as it does not check for the condition.
