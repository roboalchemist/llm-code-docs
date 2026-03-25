# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html

Title: Crypto.Random

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html

Markdown Content:
Contents

*   [Deterministic instances](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#g:1)
*   [Seed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#g:2)
*   [Deterministic Random class](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#g:3)
*   [Random abstraction](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#g:4)

Description

Synopsis
*   data[ChaChaDRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:ChaChaDRG)
*   data[SystemDRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:SystemDRG)
*   data[Seed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:Seed)
*   [seedNew](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:seedNew) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadRandom "Crypto.Random") randomly => randomly [Seed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:Seed "Crypto.Random")
*   [seedFromInteger](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:seedFromInteger) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude") ->[Seed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:Seed "Crypto.Random")
*   [seedToInteger](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:seedToInteger) :: [Seed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:Seed "Crypto.Random") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [seedFromBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:seedFromBinary) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") b => b ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Seed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:Seed "Crypto.Random")
*   [getSystemDRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:getSystemDRG) :: [IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO")[SystemDRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:SystemDRG "Crypto.Random")
*   [drgNew](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:drgNew) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadRandom "Crypto.Random") randomly => randomly [ChaChaDRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:ChaChaDRG "Crypto.Random")
*   [drgNewSeed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:drgNewSeed) :: [Seed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:Seed "Crypto.Random") ->[ChaChaDRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:ChaChaDRG "Crypto.Random")
*   [drgNewTest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:drgNewTest) :: ([Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word"), [Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word"), [Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word"), [Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word"), [Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word")) ->[ChaChaDRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:ChaChaDRG "Crypto.Random")
*   [withDRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:withDRG) :: [DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:DRG "Crypto.Random") gen => gen ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a -> (a, gen)
*   [withRandomBytes](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:withRandomBytes) :: ([ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba, [DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:DRG "Crypto.Random") g) => g ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (ba -> a) -> (a, g)
*   class[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:DRG) gen where
    *   [randomBytesGenerate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:randomBytesGenerate) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") byteArray =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> gen -> (byteArray, gen)

*   class[Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m =>[MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadRandom) m where
    *   [getRandomBytes](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:getRandomBytes) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") byteArray =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> m byteArray

*   data[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom) gen a

[Deterministic instances -----------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#g:1)

data[SystemDRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.SystemDRG.html#SystemDRG)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:SystemDRG)

A referentially transparent System representation of the random evaluated out of the system.

Holding onto a specific DRG means that all the already evaluated bytes will be consistently replayed.

There's no need to reseed this DRG, as only pure entropy is represented here.

[Seed ----](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#g:2)[Deterministic Random class --------------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#g:3)

[drgNewTest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html) :: ([Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word"), [Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word"), [Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word"), [Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word"), [Word64](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Word.html#t:Word64 "Data.Word")) ->[ChaChaDRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:ChaChaDRG "Crypto.Random")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.html#drgNewTest)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:drgNewTest)

Create a new DRG from 5 Word64.

This is a convenient interface to create deterministic interface for quickcheck style testing.

It can also be used in other contexts provided the input has been properly randomly generated.

Note that the `Arbitrary` instance provided by QuickCheck for `Word64` does not have a uniform distribution. It is often better to use instead `arbitraryBoundedRandom`.

System endianness impacts how the tuple is interpreted and therefore changes the resulting DRG.

class[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html) gen where[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#DRG)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:DRG)

A Deterministic Random Generator (DRG) class

[Random abstraction ------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#g:4)

data[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html) gen a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#MonadPseudoRandom)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom)

A simple Monad class very similar to a State Monad with the state being a DRG.

#### Instances

Instances details
[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:DRG "Crypto.Random") gen =>[Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") ([MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#line-48)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom)
Instance details
Defined in [Crypto.Random.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html)

Methods

[(>>=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-62--62--61-) :: [MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a -> (a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen b) ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-62--62--61-)

[(>>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-62--62-) :: [MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen b ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-62--62-)

[return](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:return) :: a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:return)
[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:DRG "Crypto.Random") gen =>[Functor](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Functor.html#t:Functor "Data.Functor") ([MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#line-37)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom)
Instance details
Defined in [Crypto.Random.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html)

Methods

[fmap](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:fmap) :: (a -> b) ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:fmap)

[(<$)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-60--36-) :: a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen b ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-60--36-)
[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:DRG "Crypto.Random") gen =>[Applicative](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Applicative.html#t:Applicative "Control.Applicative") ([MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#line-41)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom)
Instance details
Defined in [Crypto.Random.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html)

Methods

[pure](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:pure) :: a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:pure)

[(<*>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-60--42--62-) :: [MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen (a -> b) ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-60--42--62-)

[liftA2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:liftA2) :: (a -> b -> c) ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen b ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen c [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:liftA2)

[(*>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-42--62-) :: [MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen b ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-42--62-)

[(<*)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-60--42-) :: [MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen b ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:-60--42-)
[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:DRG "Crypto.Random") gen =>[MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadRandom "Crypto.Random") ([MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom)
Instance details
Defined in [Crypto.Random.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html)

Methods

[getRandomBytes](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:getRandomBytes) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") byteArray =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#t:MonadPseudoRandom "Crypto.Random") gen byteArray [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#getRandomBytes)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html#v:getRandomBytes)
