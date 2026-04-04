# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html

Title: Crypto.Random.Entropy.Unsafe

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html

Markdown Content:
| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | experimental |
| Portability | Good |
| Safe Haskell | Safe-Inferred |
| Language | Haskell2010 |

Crypto.Random.Entropy.Unsafe

Description

Synopsis
*   [replenish](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html#v:replenish) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> [[EntropyBackend](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html#t:EntropyBackend "Crypto.Random.Entropy.Unsafe")] ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr")[Word8](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word8 "Data.Word") ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") ()
*   data[EntropyBackend](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html#t:EntropyBackend)
*   [supportedBackends](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html#v:supportedBackends) :: [[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") ([Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[EntropyBackend](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html#t:EntropyBackend "Crypto.Random.Entropy.Unsafe"))]
*   [gatherBackend](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html#v:gatherBackend) :: [EntropyBackend](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html#t:EntropyBackend "Crypto.Random.Entropy.Unsafe") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr")[Word8](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word8 "Data.Word") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO")[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")

Documentation
-------------

[replenish](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> [[EntropyBackend](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html#t:EntropyBackend "Crypto.Random.Entropy.Unsafe")] ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr")[Word8](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word8 "Data.Word") ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Entropy.Unsafe.html#replenish)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html#v:replenish)

Refill the entropy in a buffer

Call each entropy backend in turn until the buffer has been replenished.

If the buffer cannot be refill after 3 loopings, this will raise an User Error exception
