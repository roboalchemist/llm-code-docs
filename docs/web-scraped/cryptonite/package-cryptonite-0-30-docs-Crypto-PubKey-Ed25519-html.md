# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html

Title: Crypto.PubKey.Ed25519

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html

Markdown Content:
Contents

*   [Size constants](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#g:1)
*   [Smart constructors](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#g:2)
*   [Methods](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#g:3)

Description

Ed25519 support

Synopsis
*   data[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey)
*   data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey)
*   data[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature)
*   [publicKeySize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:publicKeySize) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
*   [secretKeySize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:secretKeySize) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
*   [signatureSize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:signatureSize) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
*   [signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:signature) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519")
*   [publicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:publicKey) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519")
*   [secretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:secretKey) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519")
*   [toPublic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:toPublic) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519")
*   [sign](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:sign) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba =>[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") -> ba ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519")
*   [verify](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:verify) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba =>[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") -> ba ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [generateSecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:generateSecretKey) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m => m [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519")

Documentation
-------------

data[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#SecretKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey)

An Ed25519 Secret key

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-61--61-) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-47--61-) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:show) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showList) :: [[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:rnf) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-45)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:length) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:withByteArray) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:copyByteArrayToPtr) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:SecretKey "Crypto.PubKey.Ed25519") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:copyByteArrayToPtr)

data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#PublicKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey)

An Ed25519 public key

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-49)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-61--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-47--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-49)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:show) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showList) :: [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-49)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:rnf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-49)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:length) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:withByteArray) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:copyByteArrayToPtr) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:PublicKey "Crypto.PubKey.Ed25519") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:copyByteArrayToPtr)

data[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#Signature)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature)

An Ed25519 signature

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-53)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-61--61-) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-47--61-) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-53)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:show) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showList) :: [[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-53)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:rnf) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Ed25519.html#line-53)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:length) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:withByteArray) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:copyByteArrayToPtr) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#t:Signature "Crypto.PubKey.Ed25519") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#v:copyByteArrayToPtr)

[Size constants --------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#g:1)[Smart constructors ------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#g:2)[Methods -------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html#g:3)
