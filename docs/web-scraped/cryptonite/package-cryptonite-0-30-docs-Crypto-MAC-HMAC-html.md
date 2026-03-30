# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html

Title: Crypto.MAC.HMAC

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html

Markdown Content:
Description

Synopsis
*   [hmac](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:hmac) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") message, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a) => key -> message ->[HMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:HMAC "Crypto.MAC.HMAC") a
*   [hmacLazy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:hmacLazy) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a) => key ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString-Lazy.html#t:ByteString "Data.ByteString.Lazy") ->[HMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:HMAC "Crypto.MAC.HMAC") a
*   newtype[HMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:HMAC) a = [HMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:HMAC) {
    *   [hmacGetDigest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:hmacGetDigest) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a

}
*   data[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:Context) hashalg = [Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:Context) !([Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Context "Crypto.Hash") hashalg) !([Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Context "Crypto.Hash") hashalg)
*   [initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:initialize) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a) => key ->[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:Context "Crypto.MAC.HMAC") a
*   [update](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:update) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") message, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a) =>[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:Context "Crypto.MAC.HMAC") a -> message ->[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:Context "Crypto.MAC.HMAC") a
*   [updates](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:updates) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") message, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a) =>[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:Context "Crypto.MAC.HMAC") a -> [message] ->[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:Context "Crypto.MAC.HMAC") a
*   [finalize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:finalize) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a =>[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:Context "Crypto.MAC.HMAC") a ->[HMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:HMAC "Crypto.MAC.HMAC") a

Documentation
-------------

[hmac](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.HMAC.html#hmac)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:hmac)

Arguments

Compute a MAC using the supplied hashing function

[hmacLazy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.HMAC.html#hmacLazy)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:hmacLazy)

Arguments

Compute a MAC using the supplied hashing function, for a lazy input

newtype[HMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html) a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.HMAC.html#HMAC)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:HMAC)

Represent an HMAC that is a phantom type with the hash used to produce the mac.

The Eq instance is constant time. No Show instance is provided, to avoid printing by mistake.

Constructors

[Incremental -----------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#g:1)

data[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html) hashalg [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.HMAC.html#Context)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#t:Context)

Represent an ongoing HMAC state, that can be appended with `update` and finalize to an HMAC with `hmacFinalize`

Constructors

[updates](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.HMAC.html#updates)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html#v:updates)

Arguments

Increamentally update a HMAC context with multiple inputs
