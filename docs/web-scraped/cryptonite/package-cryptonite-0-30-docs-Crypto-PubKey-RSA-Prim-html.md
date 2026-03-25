# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Prim.html

Title: Crypto.PubKey.RSA.Prim

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Prim.html

Markdown Content:
| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | experimental |
| Portability | Good |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.PubKey.RSA.Prim

Contents

*   [Decrypt primitive](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Prim.html#g:1)
*   [Encrypt primitive](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Prim.html#g:2)

Description

Synopsis
*   [dp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Prim.html#v:dp) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Blinder "Crypto.PubKey.RSA.Types") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") -> ba -> ba
*   [ep](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Prim.html#v:ep) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") -> ba -> ba
