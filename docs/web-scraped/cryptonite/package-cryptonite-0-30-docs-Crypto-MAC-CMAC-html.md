# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html

Title: Crypto.MAC.CMAC

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html

Markdown Content:
Crypto.MAC.CMAC
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Instances](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#)
*   [Quick Jump](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#)
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.CMAC.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Kei Hibino <ex8k.hibino@gmail.com> |
| Stability | experimental |
| Portability | unknown |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.MAC.CMAC

Description

Provide the CMAC (Cipher based Message Authentification Code) base algorithm. [http://en.wikipedia.org/wiki/CMAC](http://en.wikipedia.org/wiki/CMAC)[http://csrc.nist.gov/publications/nistpubs/800-38B/SP_800-38B.pdf](http://csrc.nist.gov/publications/nistpubs/800-38B/SP_800-38B.pdf)

Synopsis
*   [cmac](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:cmac) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bin, [BlockCipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher "Crypto.Cipher.Types") cipher) => cipher -> bin ->[CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC "Crypto.MAC.CMAC") cipher
*   data[CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC) a
*   [subKeys](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:subKeys) :: ([BlockCipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher "Crypto.Cipher.Types") k, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba) => k -> (ba, ba)

Documentation
=============

[cmac](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.CMAC.html#cmac)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:cmac)

Arguments

:: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") bin, [BlockCipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher "Crypto.Cipher.Types") cipher)
=> cipher key to compute CMAC with
-> bin input message
->[CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC "Crypto.MAC.CMAC") cipher output tag

compute a MAC using the supplied cipher

data[CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html) a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.CMAC.html#CMAC)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC)

Authentication code

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq") ([CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC "Crypto.MAC.CMAC") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.CMAC.html#line-31)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC)
Instance details
Defined in [Crypto.MAC.CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:-61--61-) :: [CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC "Crypto.MAC.CMAC") a ->[CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC "Crypto.MAC.CMAC") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:-47--61-) :: [CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC "Crypto.MAC.CMAC") a ->[CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC "Crypto.MAC.CMAC") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:-47--61-)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ([CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC "Crypto.MAC.CMAC") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.CMAC.html#line-29)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC)
Instance details
Defined in [Crypto.MAC.CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:length) :: [CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC "Crypto.MAC.CMAC") a ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:withByteArray) :: [CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC "Crypto.MAC.CMAC") a -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a0) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a0 [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:copyByteArrayToPtr) :: [CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#t:CMAC "Crypto.MAC.CMAC") a ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:copyByteArrayToPtr)

[subKeys](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.CMAC.html#subKeys)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html#v:subKeys)

Arguments

:: ([BlockCipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher "Crypto.Cipher.Types") k, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba)
=> k key to compute CMAC with
-> (ba, ba)sub-keys to compute CMAC

make sub-keys used in CMAC

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
