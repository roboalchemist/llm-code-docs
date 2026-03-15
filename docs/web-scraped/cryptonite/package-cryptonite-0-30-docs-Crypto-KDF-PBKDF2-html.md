# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html

Title: Crypto.KDF.PBKDF2

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html

Markdown Content:
Description

Password Based Key Derivation Function 2

Synopsis
*   type[PRF](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#t:PRF) password = password ->[Bytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:Bytes "Data.ByteArray") ->[Bytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:Bytes "Data.ByteArray")
*   [prfHMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#v:prfHMAC) :: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") password) => a ->[PRF](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#t:PRF "Crypto.KDF.PBKDF2") password
*   data[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#t:Parameters) = [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#v:Parameters) {
    *   [iterCounts](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#v:iterCounts) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
    *   [outputLength](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#v:outputLength) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")

}
*   [generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#v:generate) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") password, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") salt, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba) =>[PRF](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#t:PRF "Crypto.KDF.PBKDF2") password ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#t:Parameters "Crypto.KDF.PBKDF2") -> password -> salt -> ba
*   [fastPBKDF2_SHA1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#v:fastPBKDF2_SHA1) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") password, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") salt, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out) =>[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#t:Parameters "Crypto.KDF.PBKDF2") -> password -> salt -> out
*   [fastPBKDF2_SHA256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#v:fastPBKDF2_SHA256) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") password, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") salt, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out) =>[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#t:Parameters "Crypto.KDF.PBKDF2") -> password -> salt -> out
*   [fastPBKDF2_SHA512](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#v:fastPBKDF2_SHA512) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") password, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") salt, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out) =>[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#t:Parameters "Crypto.KDF.PBKDF2") -> password -> salt -> out

Documentation
-------------

type[PRF](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html) password [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.PBKDF2.html#PRF)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html#t:PRF)

Arguments

= password the password parameters
->[Bytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:Bytes "Data.ByteArray")the content
->[Bytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:Bytes "Data.ByteArray")prf(password,content)

The PRF used for PBKDF2
