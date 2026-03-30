# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize-Internal.html

Title: Crypto.Number.Serialize.Internal

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize-Internal.html

Markdown Content:
Description

Fast serialization primitives for integer using raw pointers

Synopsis
*   [i2osp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize-Internal.html#v:i2osp) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr")[Word8](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word8 "Data.Word") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO")[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
*   [i2ospOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize-Internal.html#v:i2ospOf) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr")[Word8](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word8 "Data.Word") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO")[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
*   [os2ip](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize-Internal.html#v:os2ip) :: [Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr")[Word8](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word8 "Data.Word") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO")[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

Documentation
-------------

[i2osp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize-Internal.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr")[Word8](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word8 "Data.Word") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO")[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Serialize.Internal.html#i2osp)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize-Internal.html#v:i2osp)

Fill a pointer with the big endian binary representation of an integer

If the room available `ptrSz` is less than the number of bytes needed, 0 is returned. Likewise if a parameter is invalid, 0 is returned.

Returns the number of bytes written
