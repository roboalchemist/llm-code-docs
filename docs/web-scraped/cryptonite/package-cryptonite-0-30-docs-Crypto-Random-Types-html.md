# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html

Title: Crypto.Random.Types

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html

Markdown Content:
Description

Synopsis
*   class[Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m =>[MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom) m where
    *   [getRandomBytes](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:getRandomBytes) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") byteArray =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> m byteArray

*   data[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom) gen a
*   class[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:DRG) gen where
    *   [randomBytesGenerate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:randomBytesGenerate) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") byteArray =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> gen -> (byteArray, gen)

*   [withDRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:withDRG) :: [DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:DRG "Crypto.Random.Types") gen => gen ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a -> (a, gen)

Documentation
-------------

data[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html) gen a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#MonadPseudoRandom)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom)

A simple Monad class very similar to a State Monad with the state being a DRG.

#### Instances

Instances details
[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:DRG "Crypto.Random.Types") gen =>[Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") ([MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#line-48)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom)
Instance details
Defined in [Crypto.Random.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html)

Methods

[(>>=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-62--62--61-) :: [MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a -> (a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen b) ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-62--62--61-)

[(>>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-62--62-) :: [MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen b ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-62--62-)

[return](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:return) :: a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:return)
[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:DRG "Crypto.Random.Types") gen =>[Functor](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Functor.html#t:Functor "Data.Functor") ([MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#line-37)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom)
Instance details
Defined in [Crypto.Random.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html)

Methods

[fmap](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:fmap) :: (a -> b) ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:fmap)

[(<$)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-60--36-) :: a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen b ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-60--36-)
[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:DRG "Crypto.Random.Types") gen =>[Applicative](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Applicative.html#t:Applicative "Control.Applicative") ([MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#line-41)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom)
Instance details
Defined in [Crypto.Random.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html)

Methods

[pure](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:pure) :: a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:pure)

[(<*>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-60--42--62-) :: [MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen (a -> b) ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-60--42--62-)

[liftA2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:liftA2) :: (a -> b -> c) ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen b ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen c [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:liftA2)

[(*>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-42--62-) :: [MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen b ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen b [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-42--62-)

[(<*)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-60--42-) :: [MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen b ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:-60--42-)
[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:DRG "Crypto.Random.Types") gen =>[MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") ([MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom)
Instance details
Defined in [Crypto.Random.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html)

Methods

[getRandomBytes](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:getRandomBytes) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") byteArray =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[MonadPseudoRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadPseudoRandom "Crypto.Random.Types") gen byteArray [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#getRandomBytes)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#v:getRandomBytes)

class[DRG](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html) gen where[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Random.Types.html#DRG)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:DRG)

A Deterministic Random Generator (DRG) class
