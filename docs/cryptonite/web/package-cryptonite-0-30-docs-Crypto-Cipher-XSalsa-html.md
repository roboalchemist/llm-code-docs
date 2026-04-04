# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html

Title: Crypto.Cipher.XSalsa

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html

Markdown Content:
Description

Synopsis
*   [initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#v:initialize) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") nonce) =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> key -> nonce ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#t:State "Crypto.Cipher.XSalsa")
*   [derive](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#v:derive) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") nonce =>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#t:State "Crypto.Cipher.XSalsa") -> nonce ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#t:State "Crypto.Cipher.XSalsa")
*   [combine](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#v:combine) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#t:State "Crypto.Cipher.XSalsa") -> ba -> (ba, [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#t:State "Crypto.Cipher.XSalsa"))
*   [generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#v:generate) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#t:State "Crypto.Cipher.XSalsa") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (ba, [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#t:State "Crypto.Cipher.XSalsa"))
*   data[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#t:State)

Documentation
-------------

[initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.XSalsa.html#initialize)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#v:initialize)

Arguments

Initialize a new XSalsa context with the number of rounds, the key and the nonce associated.

[derive](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.XSalsa.html#derive)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#v:derive)

Arguments

Use an already initialized context and new nonce material to derive another XSalsa context.

This allows a multi-level cascade where a first key `k1` and nonce `n1` is used to get `HState(k1,n1)`, and this value is then used as key `k2` to build `XSalsa(k2,n2)`. Function `initialize` is to be called with the first 192 bits of `n1|n2`, and the call to `derive` should add the remaining 128 bits.

The output context always uses the same number of rounds as the input context.

[combine](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Salsa.html#combine)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#v:combine)

Arguments

:: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba
=>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#t:State "Crypto.Cipher.XSalsa")the current Salsa state
-> ba the source to xor with the generator
-> (ba, [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#t:State "Crypto.Cipher.XSalsa"))

Combine the salsa output and an arbitrary message with a xor, and return the combined output and the new state.

[generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Salsa.html#generate)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html#v:generate)

Arguments

Generate a number of bytes from the Salsa output directly
