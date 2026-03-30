# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html

Title: Crypto.PubKey.Rabin.Types

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html

Markdown Content:
Crypto.PubKey.Rabin.Types
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Instances](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#)
*   [Quick Jump](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#)
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Types.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Carlos Rodriguez-Vega <crodveg@yahoo.es> |
| Stability | experimental |
| Portability | unknown |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.PubKey.Rabin.Types

Description

Synopsis
*   data[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error)
    *   = [MessageTooLong](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:MessageTooLong)
    *   | [MessageNotRecognized](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:MessageNotRecognized)
    *   | [InvalidParameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:InvalidParameters)

*   [generatePrimes](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:generatePrimes) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> PrimeCondition -> PrimeCondition -> m ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"))

Documentation
=============

data[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Types.html#Error)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error)

Error possible during encryption, decryption or signing.

Constructors

[MessageTooLong](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html)the message to encrypt is too long
[MessageNotRecognized](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html)the message decrypted doesn't have a OAEP structure
[InvalidParameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html)some parameters lead to breaking assumptions

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Types.html#line-23)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error)
Instance details
Defined in [Crypto.PubKey.Rabin.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:-61--61-) :: [Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types") ->[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:-47--61-) :: [Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types") ->[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Types.html#line-23)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error)
Instance details
Defined in [Crypto.PubKey.Rabin.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:show) :: [Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:showList) :: [[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:showList)

[generatePrimes](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.Types.html#generatePrimes)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#v:generatePrimes)

Arguments

:: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m
=>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")size in bytes
-> PrimeCondition condition prime p must satisfy
-> PrimeCondition condition prime q must satisfy
-> m ([Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"), [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude"))chosen distinct primes p and q

Generate primes p & q

Produced by [Haddock](http://www.haskell.org/haddock/) version 2.24.0

Linuwial

You can find any exported type, constructor, class, function or pattern defined in this package by (approximate) name.

| Key | Shortcut |
| --- | --- |
| s | Open this search box |
| esc | Close this search box |
| ↓,ctrl + j | Move down in search results |
| ↑,ctrl + k | Move up in search results |
| ↵ | Go to active search result |

Expand All Instances Collapse All Instances

- [x] Collapse All Instances By Default

- [x] Remember Manually Collapsed/Expanded Instances
