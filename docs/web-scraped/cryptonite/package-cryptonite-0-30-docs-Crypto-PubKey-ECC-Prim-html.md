# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html

Title: Crypto.PubKey.ECC.Prim

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html

Markdown Content:
Description

Elliptic Curve Arithmetic.

_WARNING:_ These functions are vulnerable to timing attacks.

Synopsis
*   [scalarGenerate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html#v:scalarGenerate) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") randomly =>[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") -> randomly [PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:PrivateNumber "Crypto.PubKey.ECC.Types")
*   [pointAdd](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html#v:pointAdd) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")
*   [pointNegate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html#v:pointNegate) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")
*   [pointDouble](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html#v:pointDouble) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")
*   [pointBaseMul](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html#v:pointBaseMul) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")
*   [pointMul](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html#v:pointMul) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")
*   [pointAddTwoMuls](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html#v:pointAddTwoMuls) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")
*   [isPointAtInfinity](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html#v:isPointAtInfinity) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [isPointValid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html#v:isPointValid) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")

Documentation
-------------

[pointDouble](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Prim.html#pointDouble)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html#v:pointDouble)

Elliptic Curve point doubling.

_WARNING:_ Vulnerable to timing attacks.

This perform the following calculation: > lambda = (3 * xp ^ 2 + a) / 2 yp > xr = lambda ^ 2 - 2 xp > yr = lambda (xp - xr) - yp

With binary curve: > xp == 0 => P = O > otherwise =>> s = xp + (yp / xp) > xr = s ^ 2 + s + a > yr = xp ^ 2 + (s+1) * xr

[isPointValid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Prim.html#isPointValid)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html#v:isPointValid)

check if a point is on specific curve

This perform three checks:

*   x is not out of range
*   y is not out of range
*   the equation `y^2 = x^3 + a*x + b (mod p)` holds
