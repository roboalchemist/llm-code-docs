# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html

Title: Crypto.Cipher.ChaCha

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html

Markdown Content:
Contents

*   [Simple interface for DRG purpose](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#g:1)

Description

Synopsis
*   [initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#v:initialize) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") nonce) =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> key -> nonce ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:State "Crypto.Cipher.ChaCha")
*   [combine](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#v:combine) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:State "Crypto.Cipher.ChaCha") -> ba -> (ba, [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:State "Crypto.Cipher.ChaCha"))
*   [generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#v:generate) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:State "Crypto.Cipher.ChaCha") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (ba, [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:State "Crypto.Cipher.ChaCha"))
*   data[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:State)
*   [initializeSimple](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#v:initializeSimple) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") seed => seed ->[StateSimple](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:StateSimple "Crypto.Cipher.ChaCha")
*   [generateSimple](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#v:generateSimple) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[StateSimple](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:StateSimple "Crypto.Cipher.ChaCha") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (ba, [StateSimple](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:StateSimple "Crypto.Cipher.ChaCha"))
*   data[StateSimple](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:StateSimple)

Documentation
-------------

[initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.ChaCha.html#initialize)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#v:initialize)

Arguments

Initialize a new ChaCha context with the number of rounds, the key and the nonce associated.

[combine](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.ChaCha.html#combine)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#v:combine)

Arguments

:: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba
=>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:State "Crypto.Cipher.ChaCha")the current ChaCha state
-> ba the source to xor with the generator
-> (ba, [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#t:State "Crypto.Cipher.ChaCha"))

Combine the chacha output and an arbitrary message with a xor, and return the combined output and the new state.

[generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.ChaCha.html#generate)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#v:generate)

Arguments

Generate a number of bytes from the ChaCha output directly

[Simple interface for DRG purpose --------------------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html#g:1)
