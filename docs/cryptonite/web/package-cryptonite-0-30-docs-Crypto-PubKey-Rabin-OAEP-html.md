# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html

Title: Crypto.PubKey.Rabin.OAEP

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html

Markdown Content:
Description

Synopsis
*   data[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams) hash seed output = [OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#v:OAEPParams) {
    *   [oaepHash](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#v:oaepHash) :: hash
    *   [oaepMaskGenAlg](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#v:oaepMaskGenAlg) :: [MaskGenAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-MaskGenFunction.html#t:MaskGenAlgorithm "Crypto.PubKey.MaskGenFunction") seed output
    *   [oaepLabel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#v:oaepLabel) :: [Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")

}
*   [defaultOAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#v:defaultOAEPParams) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") seed, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") output, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash) => hash ->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash seed output
*   [pad](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#v:pad) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")
*   [unpad](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#v:unpad) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")

Documentation
-------------

[pad](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.Rabin.OAEP.html#pad)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#v:pad)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=>[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")Seed
->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html#t:OAEPParams "Crypto.PubKey.Rabin.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")OAEP params to use
->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")size of public key in bytes
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")Message pad
->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html#t:Error "Crypto.PubKey.Rabin.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")

Pad a message using OAEP.
