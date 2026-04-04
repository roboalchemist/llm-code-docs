# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html

Title: Crypto.Cipher.ChaChaPoly1305

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html

Markdown Content:
Description

A simple AEAD scheme using ChaCha20 and Poly1305. See [RFC 7539](https://tools.ietf.org/html/rfc7539).

The State is not modified in place, so each function changing the State, returns a new State.

Authenticated Data need to be added before any call to `encrypt` or `decrypt`, and once all the data has been added, then `finalizeAAD` need to be called.

Once `finalizeAAD` has been called, no further `appendAAD` call should be make.

import Data.ByteString.Char8 as B
import Data.ByteArray
import Crypto.Error
import Crypto.Cipher.ChaChaPoly1305 as C

encrypt
    :: ByteString -- nonce (12 random bytes)
    -> ByteString -- symmetric key
    -> ByteString -- optional associated data (won't be encrypted)
    -> ByteString -- input plaintext to be encrypted
    -> CryptoFailable ByteString -- ciphertext with a 128-bit tag attached
encrypt nonce key header plaintext = do
    st1 <- C.nonce12 nonce >>= C.initialize key
    let
        st2 = C.finalizeAAD $ C.appendAAD header st1
        (out, st3) = C.encrypt plaintext st2
        auth = C.finalize st3
    return $ out `B.append` Data.ByteArray.convert auth

Synopsis
*   data[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State)
*   data[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:Nonce)
*   [nonce12](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#v:nonce12) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") iv => iv ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:Nonce "Crypto.Cipher.ChaChaPoly1305")
*   [nonce8](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#v:nonce8) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba -> ba ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:Nonce "Crypto.Cipher.ChaChaPoly1305")
*   [incrementNonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#v:incrementNonce) :: [Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:Nonce "Crypto.Cipher.ChaChaPoly1305") ->[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:Nonce "Crypto.Cipher.ChaChaPoly1305")
*   [initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#v:initialize) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key => key ->[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:Nonce "Crypto.Cipher.ChaChaPoly1305") ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State "Crypto.Cipher.ChaChaPoly1305")
*   [appendAAD](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#v:appendAAD) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba => ba ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State "Crypto.Cipher.ChaChaPoly1305") ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State "Crypto.Cipher.ChaChaPoly1305")
*   [finalizeAAD](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#v:finalizeAAD) :: [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State "Crypto.Cipher.ChaChaPoly1305") ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State "Crypto.Cipher.ChaChaPoly1305")
*   [encrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#v:encrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba => ba ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State "Crypto.Cipher.ChaChaPoly1305") -> (ba, [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State "Crypto.Cipher.ChaChaPoly1305"))
*   [decrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#v:decrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba => ba ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State "Crypto.Cipher.ChaChaPoly1305") -> (ba, [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State "Crypto.Cipher.ChaChaPoly1305"))
*   [finalize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#v:finalize) :: [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State "Crypto.Cipher.ChaChaPoly1305") ->[Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305")

Documentation
-------------

data[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.ChaChaPoly1305.html#State)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html#t:State)

A ChaChaPoly1305 State.

The state is immutable, and only new state can be created
