# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html

Title: Crypto.Number.Prime

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html

Markdown Content:
Description

Synopsis
*   [generatePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:generatePrime) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> m [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [generateSafePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:generateSafePrime) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> m [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [isProbablyPrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:isProbablyPrime) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [findPrimeFrom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:findPrimeFrom) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [findPrimeFromWith](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:findPrimeFromWith) :: ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")) ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [primalityTestMillerRabin](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:primalityTestMillerRabin) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [primalityTestNaive](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:primalityTestNaive) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [primalityTestFermat](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:primalityTestFermat) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [isCoprime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:isCoprime) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")

Documentation
-------------

[generatePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> m [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Prime.html#generatePrime)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:generatePrime)

Generate a prime number of the required bitsize (i.e. in the range [2^(b-1)+2^(b-2), 2^b)).

May throw a `CryptoError_PrimeSizeInvalid` if the requested size is less than 5 bits, as the smallest prime meeting these conditions is 29. This function requires that the two highest bits are set, so that when multiplied with another prime to create a key, it is guaranteed to be of the proper size.

[generateSafePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> m [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Prime.html#generateSafePrime)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:generateSafePrime)

Generate a prime number of the form 2p+1 where p is also prime. it is also knowed as a Sophie Germaine prime or safe prime.

The number of safe prime is significantly smaller to the number of prime, as such it shouldn't be used if this number is supposed to be kept safe.

May throw a `CryptoError_PrimeSizeInvalid` if the requested size is less than 6 bits, as the smallest safe prime with the two highest bits set is 59.

[isProbablyPrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Prime.html#isProbablyPrime)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:isProbablyPrime)

Returns if the number is probably prime. First a list of small primes are implicitely tested for divisibility, then a fermat primality test is used with arbitrary numbers and then the Miller Rabin algorithm is used with an accuracy of 30 recursions.

[primalityTestMillerRabin](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Prime.html#primalityTestMillerRabin)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:primalityTestMillerRabin)

Miller Rabin algorithm return if the number is probably prime or composite. the tries parameter is the number of recursion, that determines the accuracy of the test.

[primalityTestFermat](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Prime.html#primalityTestFermat)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html#v:primalityTestFermat)

Arguments

:: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")number of iterations of the algorithm
->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")starting a
->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")number to test for primality
->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")

Probabilitic Test using Fermat primility test. Beware of Carmichael numbers that are Fermat liars, i.e. this test is useless for them. always combines with some other test.
