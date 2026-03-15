# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html

Title: Crypto.Cipher.Salsa

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html

Markdown Content:
Description

Synopsis
*   [initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#v:initialize) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") nonce) =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> key -> nonce ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#t:State "Crypto.Cipher.Salsa")
*   [combine](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#v:combine) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#t:State "Crypto.Cipher.Salsa") -> ba -> (ba, [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#t:State "Crypto.Cipher.Salsa"))
*   [generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#v:generate) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#t:State "Crypto.Cipher.Salsa") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (ba, [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#t:State "Crypto.Cipher.Salsa"))
*   newtype[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#t:State) = [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#v:State)[ScrubbedBytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ScrubbedBytes "Data.ByteArray")

Documentation
-------------

[initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Salsa.html#initialize)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#v:initialize)

Arguments

Initialize a new Salsa context with the number of rounds, the key and the nonce associated.

[combine](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Salsa.html#combine)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#v:combine)

Arguments

:: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba
=>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#t:State "Crypto.Cipher.Salsa")the current Salsa state
-> ba the source to xor with the generator
-> (ba, [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#t:State "Crypto.Cipher.Salsa"))

Combine the salsa output and an arbitrary message with a xor, and return the combined output and the new state.

[generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Salsa.html#generate)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html#v:generate)

Arguments

Generate a number of bytes from the Salsa output directly
