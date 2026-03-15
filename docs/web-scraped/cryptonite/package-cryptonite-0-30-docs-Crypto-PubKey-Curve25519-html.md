# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html

Title: Crypto.PubKey.Curve25519

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html

Markdown Content:
Contents

*   [Smart constructors](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#g:1)
*   [Methods](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#g:2)

Description

Curve25519 support

Synopsis
*   data[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey)
*   data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey)
*   data[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret)
*   [dhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:dhSecret) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") b => b ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519")
*   [publicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:publicKey) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bs => bs ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519")
*   [secretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:secretKey) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bs => bs ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519")
*   [dh](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:dh) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") ->[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519")
*   [toPublic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:toPublic) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519")
*   [generateSecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:generateSecretKey) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m => m [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519")

Documentation
-------------

data[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#SecretKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey)

A Curve25519 Secret key

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-42)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-61--61-) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-47--61-) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-42)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:show) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showList) :: [[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-42)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:rnf) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-42)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:length) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:withByteArray) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:copyByteArrayToPtr) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:copyByteArrayToPtr)

data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#PublicKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey)

A Curve25519 public key

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-46)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-61--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-47--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-46)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:show) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showList) :: [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-46)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:rnf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-46)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:length) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:withByteArray) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:copyByteArrayToPtr) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:copyByteArrayToPtr)

data[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#DhSecret)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret)

A Curve25519 Diffie Hellman secret related to a public key and a secret key.

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-61--61-) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519") ->[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-47--61-) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519") ->[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:show) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showList) :: [[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:rnf) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#line-51)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret)
Instance details
Defined in [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:length) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:withByteArray) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:copyByteArrayToPtr) :: [DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:copyByteArrayToPtr)

[Smart constructors ------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#g:1)[Methods -------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#g:2)

[dh](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:PublicKey "Crypto.PubKey.Curve25519") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:SecretKey "Crypto.PubKey.Curve25519") ->[DhSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#t:DhSecret "Crypto.PubKey.Curve25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Curve25519.html#dh)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html#v:dh)

Compute the Diffie Hellman secret from a public key and a secret key.

This implementation may return an all-zero value as it does not check for the condition.
