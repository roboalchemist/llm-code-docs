# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html

Title: Crypto.Number.ModArithmetic

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html

Markdown Content:
Contents

*   [Exponentiation](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#g:1)
*   [Inverse computing](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#g:2)
*   [Squares](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#g:3)

Description

Synopsis
*   [expSafe](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:expSafe) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [expFast](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:expFast) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [inverse](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:inverse) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [inverseCoprimes](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:inverseCoprimes) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [inverseFermat](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:inverseFermat) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [jacobi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:jacobi) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [squareRoot](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:squareRoot) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

[Exponentiation --------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#g:1)

[expSafe](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.ModArithmetic.html#expSafe)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:expSafe)

Arguments

Compute the modular exponentiation of base^exponent using algorithms design to avoid side channels and timing measurement

Modulo need to be odd otherwise the normal fast modular exponentiation is used.

When used with integer-simple, this function is not different from expFast, and thus provide the same unstudied and dubious timing and side channels claims.

Before GHC 8.4.2, powModSecInteger is missing from integer-gmp, so expSafe has the same security as expFast.

[expFast](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.ModArithmetic.html#expFast)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:expFast)

Arguments

Compute the modular exponentiation of base^exponent using the fastest algorithm without any consideration for hiding parameters.

Use this function when all the parameters are public, otherwise `expSafe` should be preferred.

[Inverse computing -----------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#g:2)

[inverseCoprimes](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.ModArithmetic.html#inverseCoprimes)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:inverseCoprimes)

Compute the modular inverse of two coprime numbers. This is equivalent to inverse except that the result is known to exists.

If the numbers are not defined as coprime, this function will raise a `CoprimesAssertionError`.

[Squares -------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#g:3)

[jacobi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.ModArithmetic.html#jacobi)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:jacobi)

Computes the Jacobi symbol (a/n). 0 ≤ a < n; n ≥ 3 and odd.

The Legendre and Jacobi symbols are indistinguishable exactly when the lower argument is an odd prime, in which case they have the same value.

See algorithm 2.149 in "Handbook of Applied Cryptography" by Alfred J. Menezes et al.

[squareRoot](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.ModArithmetic.html#squareRoot)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html#v:squareRoot)

Modular square root of `g` modulo a prime `p`.

If the modulus is found not to be prime, the function will raise a `ModulusAssertionError`.

This implementation is variable time and should be used with public parameters only.
