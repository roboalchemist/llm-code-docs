# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html

Title: Crypto.Number.F2m

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html

Markdown Content:
Description

This module provides basic arithmetic operations over F₂m. Performance is not optimal and it doesn't provide protection against timing attacks. The `m` parameter is implicitly derived from the irreducible polynomial where applicable.

Synopsis
*   type[BinaryPolynomial](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#t:BinaryPolynomial) = [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [addF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:addF2m) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [mulF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:mulF2m) :: [BinaryPolynomial](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#t:BinaryPolynomial "Crypto.Number.F2m") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [squareF2m'](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:squareF2m-39-) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [squareF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:squareF2m) :: [BinaryPolynomial](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#t:BinaryPolynomial "Crypto.Number.F2m") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [powF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:powF2m) :: [BinaryPolynomial](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#t:BinaryPolynomial "Crypto.Number.F2m") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [modF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:modF2m) :: [BinaryPolynomial](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#t:BinaryPolynomial "Crypto.Number.F2m") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [sqrtF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:sqrtF2m) :: [BinaryPolynomial](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#t:BinaryPolynomial "Crypto.Number.F2m") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [invF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:invF2m) :: [BinaryPolynomial](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#t:BinaryPolynomial "Crypto.Number.F2m") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [divF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:divF2m) :: [BinaryPolynomial](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#t:BinaryPolynomial "Crypto.Number.F2m") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

Documentation
-------------

[mulF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.F2m.html#mulF2m)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:mulF2m)

Arguments

Multiplication over F₂m.

This function is undefined for negative arguments, because their bit representation is platform-dependent. Zero modulus is also prohibited.

[squareF2m'](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.F2m.html#squareF2m%27)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:squareF2m-39-)

Squaring over F₂m without reduction by modulo.

The implementation utilizes the fact that for binary polynomial S(x) we have S(x)^2 = S(x^2). In other words, insert a zero bit between every bits of argument: 1101 -> 1010001.

This function is undefined for negative arguments, because their bit representation is platform-dependent.

[squareF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.F2m.html#squareF2m)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:squareF2m)

Arguments

Squaring over F₂m.

This function is undefined for negative arguments, because their bit representation is platform-dependent. Zero modulus is also prohibited.

[powF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.F2m.html#powF2m)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:powF2m)

Arguments

Exponentiation in F₂m by computing `a^b mod fx`.

This implements an exponentiation by squaring based solution. It inherits the same restrictions as `squareF2m`. Negative exponents are disallowed.

[modF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.F2m.html#modF2m)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:modF2m)

Arguments

Reduction by modulo over F₂m.

This function is undefined for negative arguments, because their bit representation is platform-dependent. Zero modulus is also prohibited.

[sqrtF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.F2m.html#sqrtF2m)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:sqrtF2m)

Arguments

Square rooot in F₂m.

We exploit the fact that `a^(2^m) = a`, or in particular, `a^(2^m - 1) = 1` from a classical result by Lagrange. Thus the square root is simply 
```
a^(2^(m
 - 1))
```
.

[invF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.F2m.html#invF2m)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:invF2m)

Arguments

Modular inversion over F₂m. If `n` doesn't have an inverse, `Nothing` is returned.

This function is undefined for negative arguments, because their bit representation is platform-dependent. Zero modulus is also prohibited.

[divF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.F2m.html#divF2m)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html#v:divF2m)

Arguments

Division over F₂m. If the dividend doesn't have an inverse it returns `Nothing`.

This function is undefined for negative arguments, because their bit representation is platform-dependent. Zero modulus is also prohibited.
