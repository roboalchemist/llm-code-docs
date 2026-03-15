# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Generate.html

Title: Crypto.PubKey.ECC.Generate

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Generate.html

Markdown Content:
| Safe Haskell | None |
| --- |
| Language | Haskell2010 |

Crypto.PubKey.ECC.Generate

Description

Signature generation.

Synopsis
*   [generateQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Generate.html#v:generateQ) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")
*   [generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Generate.html#v:generate) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") -> m ([PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-ECDSA.html#t:PublicKey "Crypto.PubKey.ECC.ECDSA"), [PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-ECDSA.html#t:PrivateKey "Crypto.PubKey.ECC.ECDSA"))

Documentation
-------------

[generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Generate.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Generate.html#generate)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Generate.html#v:generate)

Arguments

Generate a pair of (private, public) key.

_WARNING:_ Vulnerable to timing attacks.
