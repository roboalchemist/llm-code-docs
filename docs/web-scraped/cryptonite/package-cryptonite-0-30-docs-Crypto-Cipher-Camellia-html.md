# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html

Title: Crypto.Cipher.Camellia

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html

Markdown Content:
Crypto.Cipher.Camellia
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Instances](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#)
*   [Quick Jump](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#)
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Camellia.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | experimental |
| Portability | Good |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.Cipher.Camellia

Description

Camellia support. only 128 bit variant available for now.

Synopsis
*   data[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128)

Documentation
=============

data[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Camellia.html#Camellia128)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128)

Camellia block cipher with 128 bit key

#### Instances

Instances details
[Cipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:Cipher "Crypto.Cipher.Types")[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Camellia.html#line-20)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128)
Instance details
Defined in [Crypto.Cipher.Camellia](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html)

Methods

[cipherInit](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cipherInit) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") key => key ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Base.html#cipherInit)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cipherInit)

[cipherName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cipherName) :: [Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Base.html#cipherName)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cipherName)

[cipherKeySize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cipherKeySize) :: [Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") ->[KeySizeSpecifier](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:KeySizeSpecifier "Crypto.Cipher.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Base.html#cipherKeySize)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cipherKeySize)
[BlockCipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher "Crypto.Cipher.Types")[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Camellia.html#line-25)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128)
Instance details
Defined in [Crypto.Cipher.Camellia](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html)

Methods

[blockSize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:blockSize) :: [Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#blockSize)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:blockSize)

[ecbEncrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:ecbEncrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#ecbEncrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:ecbEncrypt)

[ecbDecrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:ecbDecrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#ecbDecrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:ecbDecrypt)

[cbcEncrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cbcEncrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") ->[IV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:IV "Crypto.Cipher.Types")[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#cbcEncrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cbcEncrypt)

[cbcDecrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cbcDecrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") ->[IV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:IV "Crypto.Cipher.Types")[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#cbcDecrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cbcDecrypt)

[cfbEncrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cfbEncrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") ->[IV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:IV "Crypto.Cipher.Types")[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#cfbEncrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cfbEncrypt)

[cfbDecrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cfbDecrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") ->[IV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:IV "Crypto.Cipher.Types")[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#cfbDecrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:cfbDecrypt)

[ctrCombine](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:ctrCombine) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") ->[IV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:IV "Crypto.Cipher.Types")[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#ctrCombine)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:ctrCombine)

[aeadInit](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:aeadInit) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") iv =>[AEADMode](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:AEADMode "Crypto.Cipher.Types") ->[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia") -> iv ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") ([AEAD](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:AEAD "Crypto.Cipher.Types")[Camellia128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#t:Camellia128 "Crypto.Cipher.Camellia")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#aeadInit)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html#v:aeadInit)

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
