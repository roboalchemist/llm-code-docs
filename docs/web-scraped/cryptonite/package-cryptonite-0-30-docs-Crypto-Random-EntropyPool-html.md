# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html

Title: Crypto.Random.EntropyPool

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html

Markdown Content:
Description

Synopsis
*   data[EntropyPool](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html#t:EntropyPool)
*   [createEntropyPool](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html#v:createEntropyPool) :: [IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO")[EntropyPool](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html#t:EntropyPool "Crypto.Random.EntropyPool")
*   [createEntropyPoolWith](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html#v:createEntropyPoolWith) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> [[EntropyBackend](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html#t:EntropyBackend "Crypto.Random.Entropy.Unsafe")] ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO")[EntropyPool](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html#t:EntropyPool "Crypto.Random.EntropyPool")
*   [getEntropyFrom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html#v:getEntropyFrom) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") byteArray =>[EntropyPool](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html#t:EntropyPool "Crypto.Random.EntropyPool") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") byteArray

Documentation
-------------

data[EntropyPool](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.EntropyPool.html#EntropyPool)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html#t:EntropyPool)

Pool of Entropy. Contains a self-mutating pool of entropy, that is always guaranteed to contain data.

[createEntropyPool](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html) :: [IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO")[EntropyPool](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html#t:EntropyPool "Crypto.Random.EntropyPool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.EntropyPool.html#createEntropyPool)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html#v:createEntropyPool)

Create a new entropy pool with a default size.

While you can create as many entropy pools as you want, the pool can be shared between multiples RNGs.
