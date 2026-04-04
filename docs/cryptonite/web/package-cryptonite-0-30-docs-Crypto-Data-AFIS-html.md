# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-AFIS.html

Title: Crypto.Data.AFIS

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-AFIS.html

Markdown Content:
Description

Haskell implementation of the Anti-forensic information splitter available in LUKS. [http://clemens.endorphin.org/AFsplitter](http://clemens.endorphin.org/AFsplitter)

The algorithm bloats an arbitrary secret with many bits that are necessary for the recovery of the key (merge), and allow greater way to permanently destroy a key stored on disk.

Synopsis
*   [split](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-AFIS.html#v:split) :: ([ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:DRG "Crypto.Random.Types") rng) => hash -> rng ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> ba -> (ba, rng)
*   [merge](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-AFIS.html#v:merge) :: ([ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash) => hash ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> ba -> ba

Documentation
-------------

[split](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-AFIS.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Data.AFIS.html#split)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-AFIS.html#v:split)

Arguments

:: ([ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:DRG "Crypto.Random.Types") rng)
=> hash Hash algorithm to use as diffuser
-> rng Random generator to use
->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")Number of times to diffuse the data.
-> ba original data to diffuse.
-> (ba, rng)The diffused data

Split data to diffused data, using a random generator and an hash algorithm.

the diffused data will consist of random data for (expandTimes-1) then the last block will be xor of the accumulated random data diffused by the hash algorithm.

*   ---------
*   orig -
*   ---------
*   --------- ---------- --------------
*   rand1 - - rand2 - - orig ^ acc -
*   --------- ---------- --------------

where acc is : acc(n+1) = hash (n ++ rand(n)) ^ acc(n)

[merge](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-AFIS.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Data.AFIS.html#merge)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-AFIS.html#v:merge)

Arguments

:: ([ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash)
=> hash Hash algorithm used as diffuser
->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")Number of times to un-diffuse the data
-> ba Diffused data
-> ba Original data

Merge previously diffused data back to the original data.
