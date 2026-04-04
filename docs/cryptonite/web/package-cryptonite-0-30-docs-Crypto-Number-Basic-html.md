# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html

Title: Crypto.Number.Basic

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html

Markdown Content:
Description

Synopsis
*   [sqrti](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html#v:sqrti) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"))
*   [gcde](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html#v:gcde) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"))
*   [areEven](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html#v:areEven) :: [[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")] ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [log2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html#v:log2) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
*   [numBits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html#v:numBits) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
*   [numBytes](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html#v:numBytes) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
*   [asPowerOf2AndOdd](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html#v:asPowerOf2AndOdd) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> ([Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"))

Documentation
-------------

[sqrti](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Basic.html#sqrti)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html#v:sqrti)

`sqrti` returns two integers `(l,b)` so that `l <= sqrt i <= b`. The implementation is quite naive, use an approximation for the first number and use a dichotomy algorithm to compute the bound relatively efficiently.
