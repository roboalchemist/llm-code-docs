# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html

Title: Crypto.Cipher.RC4

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html

Markdown Content:
Description

Synopsis
*   [initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#v:initialize) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key => key ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#t:State "Crypto.Cipher.RC4")
*   [combine](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#v:combine) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#t:State "Crypto.Cipher.RC4") -> ba -> ([State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#t:State "Crypto.Cipher.RC4"), ba)
*   [generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#v:generate) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#t:State "Crypto.Cipher.RC4") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> ([State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#t:State "Crypto.Cipher.RC4"), ba)
*   data[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#t:State)

Documentation
-------------

[initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.RC4.html#initialize)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#v:initialize)

Arguments

RC4 context initialization.

seed the context with an initial key. the key size need to be adequate otherwise security takes a hit.

[combine](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.RC4.html#combine)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#v:combine)

Arguments

RC4 xor combination of the rc4 stream with an input

data[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.RC4.html#State)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html#t:State)

The encryption state for RC4

This type is an instance of `ByteArrayAccess` for debugging purpose. Internal layout is architecture dependent, may contain uninitialized data fragments, and change in future versions. The bytearray should not be used as input to cryptographic algorithms.
