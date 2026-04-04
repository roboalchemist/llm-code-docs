# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html

Title: Crypto.KDF.Scrypt

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html

Markdown Content:
Synopsis
*   data[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html#t:Parameters) = [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html#v:Parameters) {
    *   [n](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html#v:n) :: [Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word")
    *   [r](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html#v:r) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
    *   [p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html#v:p) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
    *   [outputLength](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html#v:outputLength) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")

}
*   [generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html#v:generate) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") password, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") salt, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") output) =>[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html#t:Parameters "Crypto.KDF.Scrypt") -> password -> salt -> output

Documentation
-------------

data[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Scrypt.html#Parameters)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html#t:Parameters)

Parameters for Scrypt

Constructors

[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html)
Fields

*   [n](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html) :: [Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word")
Cpu/Memory cost ratio. must be a power of 2 greater than 1. also known as N.

*   [r](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
Must satisfy r * p < 2^30

*   [p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
Must satisfy r * p < 2^30

*   [outputLength](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
the number of bytes to generate out of Scrypt
