# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html

Title: Crypto.KDF.HKDF

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html

Markdown Content:
Description

Key Derivation Function based on HMAC

See RFC5869

Synopsis
*   data[PRK](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html#t:PRK) a
*   [extract](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html#v:extract) :: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") salt, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ikm) => salt -> ikm ->[PRK](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html#t:PRK "Crypto.KDF.HKDF") a
*   [extractSkip](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html#v:extractSkip) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ikm => ikm ->[PRK](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html#t:PRK "Crypto.KDF.HKDF") a
*   [expand](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html#v:expand) :: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") info, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out) =>[PRK](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html#t:PRK "Crypto.KDF.HKDF") a -> info ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> out

Documentation
-------------

[extract](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.HKDF.html#extract)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html#v:extract)

Arguments

Extract a Pseudo Random Key using the parameter and the underlaying hash mechanism

[extractSkip](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ikm => ikm ->[PRK](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html#t:PRK "Crypto.KDF.HKDF") a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.HKDF.html#extractSkip)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html#v:extractSkip)

Create a PRK directly from the input key material.

Only use when guaranteed to have a good quality and random data to use directly as key. This effectively skip a HMAC with key=salt and data=key.

[expand](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.HKDF.html#expand)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html#v:expand)

Arguments

Expand key material of specific length out of the parameters
