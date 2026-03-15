# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-MaskGenFunction.html

Title: Crypto.PubKey.MaskGenFunction

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-MaskGenFunction.html

Markdown Content:
| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | experimental |
| Portability | Good |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.PubKey.MaskGenFunction

Description

Synopsis
*   type[MaskGenAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-MaskGenFunction.html#t:MaskGenAlgorithm) seed output = seed ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> output
*   [mgf1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-MaskGenFunction.html#v:mgf1) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") seed, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") output, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hashAlg) => hashAlg -> seed ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> output

Documentation
-------------

type[MaskGenAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-MaskGenFunction.html) seed output [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.MaskGenFunction.html#MaskGenAlgorithm)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-MaskGenFunction.html#t:MaskGenAlgorithm)

Arguments

= seed seed
->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")length to generate
-> output

Represent a mask generation algorithm
