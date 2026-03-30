# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html

Title: Crypto.KDF.Argon2

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html

Markdown Content:
Description

Synopsis
*   data[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options) = [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:Options) {
    *   [iterations](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:iterations) :: ![TimeCost](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:TimeCost "Crypto.KDF.Argon2")
    *   [memory](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:memory) :: ![MemoryCost](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:MemoryCost "Crypto.KDF.Argon2")
    *   [parallelism](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:parallelism) :: ![Parallelism](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Parallelism "Crypto.KDF.Argon2")
    *   [variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:variant) :: ![Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")
    *   [version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:version) :: ![Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")

}
*   type[TimeCost](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:TimeCost) = [Word32](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word32 "Data.Word")
*   type[MemoryCost](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:MemoryCost) = [Word32](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word32 "Data.Word")
*   type[Parallelism](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Parallelism) = [Word32](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word32 "Data.Word")
*   data[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant)
    *   = [Argon2d](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:Argon2d)
    *   | [Argon2i](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:Argon2i)
    *   | [Argon2id](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:Argon2id)

*   data[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version)
    *   = [Version10](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:Version10)
    *   | [Version13](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:Version13)

*   [defaultOptions](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:defaultOptions) :: [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")
*   [hash](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:hash) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") password, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") salt, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out) =>[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") -> password -> salt ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") out

Documentation
-------------

data[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#Options)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options)

Parameters that can be adjusted to change the runtime performance of the hashing.

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-80)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-61--61-) :: [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-47--61-) :: [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-47--61-)
[Ord](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ord "Data.Ord")[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-80)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[compare](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:compare) :: [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Ordering](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ordering "Data.Ord")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:compare)

[(<)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60-) :: [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60-)

[(<=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60--61-) :: [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60--61-)

[(>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62-) :: [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62-)

[(>=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62--61-) :: [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62--61-)

[max](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:max) :: [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:max)

[min](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:min) :: [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:min)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-80)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-80)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:show) :: [Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showList) :: [[Options](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Options "Crypto.KDF.Argon2")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showList)

data[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#Variant)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant)

Which variant of Argon2 to use. You should choose the variant that is most applicable to your intention to hash inputs.

Constructors

[Argon2d](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)Argon2d is faster than Argon2i and uses data-depending memory access, which makes it suitable for cryptocurrencies and applications with no threats from side-channel timing attacks.
[Argon2i](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)Argon2i uses data-independent memory access, which is preferred for password hashing and password-based key derivation. Argon2i is slower as it makes more passes over the memory to protect from tradeoff attacks.
[Argon2id](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)Argon2id is a hybrid of Argon2i and Argon2d, using a combination of data-depending and data-independent memory accesses, which gives some of Argon2i's resistance to side-channel cache timing attacks and much of Argon2d's resistance to GPU cracking attacks

#### Instances

Instances details
[Bounded](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Bounded "Prelude")[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[minBound](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:minBound) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:minBound)

[maxBound](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:maxBound) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:maxBound)
[Enum](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Enum "Prelude")[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[succ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:succ) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:succ)

[pred](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:pred) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:pred)

[toEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:toEnum) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:toEnum)

[fromEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:fromEnum) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:fromEnum)

[enumFrom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFrom) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") -> [[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFrom)

[enumFromThen](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromThen) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") -> [[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromThen)

[enumFromTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromTo) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") -> [[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromTo)

[enumFromThenTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromThenTo) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") -> [[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromThenTo)
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-61--61-) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-47--61-) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-47--61-)
[Ord](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ord "Data.Ord")[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[compare](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:compare) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Ordering](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ordering "Data.Ord")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:compare)

[(<)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60-) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60-)

[(<=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60--61-) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60--61-)

[(>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62-) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62-)

[(>=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62--61-) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62--61-)

[max](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:max) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:max)

[min](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:min) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:min)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:show) :: [Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showList) :: [[Variant](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Variant "Crypto.KDF.Argon2")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showList)

data[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#Version)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version)

Which version of Argon2 to use

Constructors

#### Instances

Instances details
[Bounded](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Bounded "Prelude")[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[minBound](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:minBound) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:minBound)

[maxBound](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:maxBound) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:maxBound)
[Enum](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Enum "Prelude")[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[succ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:succ) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:succ)

[pred](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:pred) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:pred)

[toEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:toEnum) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:toEnum)

[fromEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:fromEnum) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:fromEnum)

[enumFrom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFrom) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") -> [[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFrom)

[enumFromThen](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromThen) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") -> [[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromThen)

[enumFromTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromTo) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") -> [[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromTo)

[enumFromThenTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromThenTo) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") -> [[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:enumFromThenTo)
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-61--61-) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-47--61-) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-47--61-)
[Ord](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ord "Data.Ord")[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[compare](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:compare) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Ordering](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ordering "Data.Ord")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:compare)

[(<)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60-) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60-)

[(<=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60--61-) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-60--61-)

[(>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62-) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62-)

[(>=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62--61-) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:-62--61-)

[max](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:max) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:max)

[min](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:min) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:min)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.Argon2.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version)
Instance details
Defined in [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:show) :: [Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showList) :: [[Version](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#t:Version "Crypto.KDF.Argon2")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#v:showList)

[Hashing function ----------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html#g:1)
