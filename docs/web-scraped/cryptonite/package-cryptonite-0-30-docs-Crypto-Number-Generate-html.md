# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html

Title: Crypto.Number.Generate

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html

Markdown Content:
Crypto.Number.Generate
===============

cryptonite-0.30: Cryptography Primitives sink
*   [Instances](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#)
*   [Quick Jump](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#)
*   [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Generate.html)
*   [Contents](https://hackage.haskell.org/package/cryptonite-0.30)
*   [Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)

| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | experimental |
| Portability | Good |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.Number.Generate

Description

Synopsis
*   data[GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy)
    *   = [SetHighest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:SetHighest)
    *   | [SetTwoHighest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:SetTwoHighest)

*   [generateParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:generateParams) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy "Crypto.Number.Generate") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool") -> m [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [generateMax](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:generateMax) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> m [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [generateBetween](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:generateBetween) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> m [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

Documentation
=============

data[GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Generate.html#GenTopPolicy)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy)

Top bits policy when generating a number

Constructors

[SetHighest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html)set the highest bit
[SetTwoHighest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html)set the two highest bit

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy "Crypto.Number.Generate")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Generate.html#line-31)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy)
Instance details
Defined in [Crypto.Number.Generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:-61--61-) :: [GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy "Crypto.Number.Generate") ->[GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy "Crypto.Number.Generate") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:-47--61-) :: [GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy "Crypto.Number.Generate") ->[GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy "Crypto.Number.Generate") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy "Crypto.Number.Generate")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Generate.html#line-31)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy)
Instance details
Defined in [Crypto.Number.Generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy "Crypto.Number.Generate") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:show) :: [GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy "Crypto.Number.Generate") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:showList) :: [[GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy "Crypto.Number.Generate")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:showList)

[generateParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Generate.html#generateParams)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:generateParams)

Arguments

:: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m
=>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")number of bits
->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[GenTopPolicy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#t:GenTopPolicy "Crypto.Number.Generate")top bit policy
->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")force the number to be odd
-> m [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

Generate a number for a specific size of bits, and optionaly set bottom and top bits

If the top bit policy is `Nothing`, then nothing is done on the highest bit (it's whatever the random generator set).

If @generateOdd is set to `True`, then the number generated is guaranteed to be odd. Otherwise it will be whatever is generated

[generateMax](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Generate.html#generateMax)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:generateMax)

Arguments

:: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m
=>[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")range
-> m [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

Generate a positive integer x, s.t. 0 <= x < range

[generateBetween](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") -> m [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Number.Generate.html#generateBetween)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html#v:generateBetween)

generate a number between the inclusive bound [low,high].

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
