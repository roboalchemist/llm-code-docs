# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html

Title: Crypto.Hash

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html

Markdown Content:
[Types -----](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#g:1)

data[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html) a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Hash.Types.html#Context)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Context)

Represent a context for a given hash algorithm.

This type is an instance of `ByteArrayAccess` for debugging purpose. Internal layout is architecture dependent, may contain uninitialized data fragments, and change in future versions. The bytearray should not be used as input to cryptographic algorithms.

data[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html) a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Hash.Types.html#Digest)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest)

Represent a digest for a given hash algorithm.

This type is an instance of `ByteArrayAccess` from package [memory](https://hackage.haskell.org/package/memory). Module [Data.ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html) provides many primitives to work with those values including conversion to other types.

Creating a digest from a bytearray is also possible with function `digestFromByteString`.

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq") ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Hash.Types.html#line-98)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest)
Instance details
Defined in [Crypto.Hash.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-61--61-) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-47--61-) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") a =>[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Hash.Types.html#line-98)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest)
Instance details
Defined in [Crypto.Hash.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a -> c ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:toConstr) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:dataTypeOf) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a)) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a)) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a -> m ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a -> m ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a -> m ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:gmapMo)
[Ord](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ord "Data.Ord") ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Hash.Types.html#line-98)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest)
Instance details
Defined in [Crypto.Hash.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Types.html)

Methods

[compare](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:compare) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Ordering](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ordering "Data.Ord")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:compare)

[(<)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-60-) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-60-)

[(<=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-60--61-) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-60--61-)

[(>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-62-) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-62-)

[(>=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-62--61-) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:-62--61-)

[max](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:max) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:max)

[min](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:min) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:min)
[HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a =>[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read") ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Hash.Types.html#line-107)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest)
Instance details
Defined in [Crypto.Hash.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show") ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Hash.Types.html#line-103)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest)
Instance details
Defined in [Crypto.Hash.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:show) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:showList) :: [[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq") ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Hash.Types.html#line-100)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest)
Instance details
Defined in [Crypto.Hash.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Types.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:rnf) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ([Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Hash.Types.html#line-98)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest)
Instance details
Defined in [Crypto.Hash.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Types.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:length) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:withByteArray) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a0) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a0 [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:copyByteArrayToPtr) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:copyByteArrayToPtr)

[Functions ---------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#g:2)[Hash methods parametrized by algorithm --------------------------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#g:3)[Hash methods ------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#g:4)

[hashFinalizePrefix](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html) :: forall a ba. ([HashAlgorithmPrefix](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:HashAlgorithmPrefix "Crypto.Hash.Algorithms") a, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba) =>[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Context "Crypto.Hash") a -> ba ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Hash.html#hashFinalizePrefix)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#v:hashFinalizePrefix)

Update the context with the first N bytes of a bytestring and return the digest. The code path is independent from N but much slower than a normal `hashUpdate`. The function can be called for the last bytes of a message, in order to exclude a variable padding, without leaking the padding length. The begining of the message, never impacted by the padding, should preferably go through `hashUpdate` for better performance.

[Hash algorithms ---------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#g:5)
