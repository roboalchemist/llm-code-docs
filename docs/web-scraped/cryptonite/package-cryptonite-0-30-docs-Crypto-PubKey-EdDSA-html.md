# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html

Title: Crypto.PubKey.EdDSA

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html

Markdown Content:
Documentation
-------------

data[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html) curve [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#SecretKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey)

An EdDSA Secret key

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq") ([SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-77)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-61--61-) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-47--61-) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show") ([SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-77)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:show) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showList) :: [[SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq") ([SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-77)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:rnf) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ([SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-77)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:length) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:withByteArray) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:copyByteArrayToPtr) :: [SecretKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:SecretKey "Crypto.PubKey.EdDSA") curve ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:copyByteArrayToPtr)

data[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html) curve hash [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#PublicKey)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey)

An EdDSA public key

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq") ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-81)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-61--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-47--61-) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show") ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-81)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:show) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showList) :: [[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq") ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-81)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:rnf) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-81)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:length) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:withByteArray) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:copyByteArrayToPtr) :: [PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:PublicKey "Crypto.PubKey.EdDSA") curve hash ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:copyByteArrayToPtr)

data[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html) curve hash [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#Signature)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature)

An EdDSA signature

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq") ([Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-85)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-61--61-) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-47--61-) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show") ([Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-85)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:show) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showList) :: [[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq") ([Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-85)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:rnf) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ([Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.EdDSA.html#line-85)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:length) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:withByteArray) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:copyByteArrayToPtr) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#t:Signature "Crypto.PubKey.EdDSA") curve hash ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#v:copyByteArrayToPtr)

[Curves with EdDSA implementation --------------------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#g:1)[Smart constructors ------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#g:2)[Methods -------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html#g:3)
