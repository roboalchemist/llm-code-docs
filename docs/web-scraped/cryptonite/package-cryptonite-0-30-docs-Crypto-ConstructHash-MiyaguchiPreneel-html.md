# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html

Title: Crypto.ConstructHash.MiyaguchiPreneel

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html

Markdown Content:
Crypto.ConstructHash.MiyaguchiPreneel
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Instances](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#)
*   [Quick Jump](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#)
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ConstructHash.MiyaguchiPreneel.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Kei Hibino <ex8k.hibino@gmail.com> |
| Stability | experimental |
| Portability | unknown |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.ConstructHash.MiyaguchiPreneel

Description

Provide the hash function construction method from block cipher [https://en.wikipedia.org/wiki/One-way_compression_function](https://en.wikipedia.org/wiki/One-way_compression_function)

Synopsis
*   [compute](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:compute) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bin, [BlockCipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher "Crypto.Cipher.Types") cipher) => bin ->[MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") cipher
*   [compute'](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:compute-39-) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bin, [BlockCipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher "Crypto.Cipher.Types") cipher) => ([Bytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:Bytes "Data.ByteArray") -> cipher) -> bin ->[MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") cipher
*   data[MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel) a

Documentation
=============

[compute](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ConstructHash.MiyaguchiPreneel.html#compute)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:compute)

Arguments

:: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bin, [BlockCipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher "Crypto.Cipher.Types") cipher)
=> bin input message
->[MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") cipher output tag

Compute Miyaguchi-Preneel one way compress using the inferred block cipher. Only safe when KEY-SIZE equals to BLOCK-SIZE.

Simple usage _mp' msg :: MiyaguchiPreneel AES128_

[compute'](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ConstructHash.MiyaguchiPreneel.html#compute%27)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:compute-39-)

Arguments

:: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bin, [BlockCipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher "Crypto.Cipher.Types") cipher)
=> ([Bytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:Bytes "Data.ByteArray") -> cipher)key build function to compute Miyaguchi-Preneel. care about block-size and key-size
-> bin input message
->[MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") cipher output tag

Compute Miyaguchi-Preneel one way compress using the supplied block cipher.

data[MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html) a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ConstructHash.MiyaguchiPreneel.html#MiyaguchiPreneel)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel)

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq") ([MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ConstructHash.MiyaguchiPreneel.html#line-29)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel)
Instance details
Defined in [Crypto.ConstructHash.MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:-61--61-) :: [MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") a ->[MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:-47--61-) :: [MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") a ->[MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:-47--61-)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ([MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.ConstructHash.MiyaguchiPreneel.html#line-27)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel)
Instance details
Defined in [Crypto.ConstructHash.MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:length) :: [MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") a ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:withByteArray) :: [MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") a -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a0) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a0 [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:copyByteArrayToPtr) :: [MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#t:MiyaguchiPreneel "Crypto.ConstructHash.MiyaguchiPreneel") a ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html#v:copyByteArrayToPtr)

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
