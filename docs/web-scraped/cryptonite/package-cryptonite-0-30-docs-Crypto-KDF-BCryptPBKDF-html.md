# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html

Title: Crypto.KDF.BCryptPBKDF

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html

Markdown Content:
Description

Synopsis
*   data[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters) = [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:Parameters) {
    *   [iterCounts](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:iterCounts) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
    *   [outputLength](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:outputLength) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")

}
*   [generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:generate) :: ([ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") pass, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") salt, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") output) =>[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") -> pass -> salt -> output
*   [hashInternal](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:hashInternal) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") pass, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") salt, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") output) => pass -> salt -> output

Documentation
-------------

data[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.BCryptPBKDF.html#Parameters)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters)

Constructors

[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html)
Fields

*   [iterCounts](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
The number of user-defined iterations for the algorithm (must be > 0)

*   [outputLength](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
The number of bytes to generate out of BCryptPBKDF (must be in 1..1024)

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.BCryptPBKDF.html#line-46)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters)
Instance details
Defined in [Crypto.KDF.BCryptPBKDF](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-61--61-) :: [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-47--61-) :: [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-47--61-)
[Ord](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ord "Data.Ord")[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.BCryptPBKDF.html#line-46)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters)
Instance details
Defined in [Crypto.KDF.BCryptPBKDF](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html)

Methods

[compare](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:compare) :: [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Ordering](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ordering "Data.Ord")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:compare)

[(<)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-60-) :: [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-60-)

[(<=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-60--61-) :: [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-60--61-)

[(>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-62-) :: [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-62-)

[(>=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-62--61-) :: [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:-62--61-)

[max](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:max) :: [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:max)

[min](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:min) :: [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:min)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.BCryptPBKDF.html#line-46)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters)
Instance details
Defined in [Crypto.KDF.BCryptPBKDF](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:show) :: [Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:showList) :: [[Parameters](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#t:Parameters "Crypto.KDF.BCryptPBKDF")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html#v:showList)
