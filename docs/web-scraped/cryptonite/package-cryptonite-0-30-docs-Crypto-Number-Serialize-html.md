# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize.html

Title: Crypto.Number.Serialize

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize.html

Markdown Content:
Description

Fast serialization primitives for integer

Synopsis
*   [i2osp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize.html#v:i2osp) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> ba
*   [os2ip](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize.html#v:os2ip) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [i2ospOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize.html#v:i2ospOf) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ba
*   [i2ospOf_](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize.html#v:i2ospOf_) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> ba

Documentation
-------------

[i2osp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize.html) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Serialize.html#i2osp)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize.html#v:i2osp)

`i2osp` converts a positive integer into a byte string.

The first byte is MSB (most significant byte); the last byte is the LSB (least significant byte)

[i2ospOf_](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize.html) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Serialize.html#i2ospOf_)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize.html#v:i2ospOf_)

Just like `i2ospOf` except that it doesn't expect a failure: i.e. an integer larger than the number of output bytes requested.

For example if you just took a modulo of the number that represent the size (example the RSA modulo n).
