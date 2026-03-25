# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECIES.html

Title: Crypto.PubKey.ECIES

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECIES.html

Markdown Content:
Description

IES with Elliptic curve [https://en.wikipedia.org/wiki/Integrated_Encryption_Scheme](https://en.wikipedia.org/wiki/Integrated_Encryption_Scheme)

This is a simple cryptographic system between 2 parties using Elliptic Curve.

The sending party create a shared secret using the receiver public key, and use the shared secret to generate cryptographic material for an symmetric encryption scheme (preferably authenticated encryption).

The receiving party receive the temporary ephemeral public key which is combined to its secret key to create the shared secret which just like on the sending is used to generate cryptographic material.

This module doesn't provide any symmetric data encryption capability or any mean to derive cryptographic key material for a symmetric key from the shared secret. this is left to the user for now.

Synopsis
*   [deriveEncrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECIES.html#v:deriveEncrypt) :: ([MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") randomly, [EllipticCurveDH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:EllipticCurveDH "Crypto.ECC") curve) => proxy curve ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Point "Crypto.ECC") curve -> randomly ([CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") ([Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Point "Crypto.ECC") curve, [SharedSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:SharedSecret "Crypto.ECC")))
*   [deriveDecrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECIES.html#v:deriveDecrypt) :: [EllipticCurveDH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:EllipticCurveDH "Crypto.ECC") curve => proxy curve ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Point "Crypto.ECC") curve ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC") curve ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[SharedSecret](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:SharedSecret "Crypto.ECC")

Documentation
-------------

[deriveEncrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECIES.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECIES.html#deriveEncrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECIES.html#v:deriveEncrypt)

Arguments

Generate random a new Shared secret and the associated point to do a ECIES style encryption

[deriveDecrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECIES.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECIES.html#deriveDecrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECIES.html#v:deriveDecrypt)

Arguments

Derive the shared secret with the receiver key and the R point of the scheme.
