# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html

Title: Crypto.Data.Padding

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html

Markdown Content:
| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | experimental |
| Portability | unknown |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.Data.Padding

Description

Various cryptographic padding commonly used for block ciphers or asymmetric systems.

Synopsis
*   data[Format](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html#t:Format)
    *   = [PKCS5](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html#v:PKCS5)
    *   | [PKCS7](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html#v:PKCS7)[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
    *   | [ZERO](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html#v:ZERO)[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")

*   [pad](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html#v:pad) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") byteArray =>[Format](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html#t:Format "Crypto.Data.Padding") -> byteArray -> byteArray
*   [unpad](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html#v:unpad) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") byteArray =>[Format](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html#t:Format "Crypto.Data.Padding") -> byteArray ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") byteArray

Documentation
-------------

data[Format](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Data.Padding.html#Format)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html#t:Format)

Format of padding

Constructors

[PKCS5](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html)PKCS5: PKCS7 with hardcoded size of 8
[PKCS7](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html)[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")PKCS7 with padding size between 1 and 255
[ZERO](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html)[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")zero padding with block size
