# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html

Title: Crypto.Cipher.AESGCMSIV

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html

Markdown Content:
Description

Implementation of AES-GCM-SIV, an AEAD scheme with nonce misuse resistance defined in [RFC 8452](https://tools.ietf.org/html/rfc8452).

To achieve the nonce misuse-resistance property, encryption requires two passes on the plaintext, hence no streaming API is provided. This AEAD operates on complete inputs held in memory. For simplicity, the implementation of decryption uses a similar pattern, with performance penalty compared to an implementation which is able to merge both passes.

The specification allows inputs up to 2^36 bytes but this implementation requires AAD and plaintext/ciphertext to be both smaller than 2^32 bytes.

Synopsis
*   data[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce)
*   [nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:nonce) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") iv => iv ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV")
*   [generateNonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:generateNonce) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m => m [Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV")
*   [encrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:encrypt) :: ([BlockCipher128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher128 "Crypto.Cipher.Types") aes, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") aad, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba) => aes ->[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV") -> aad -> ba -> ([AuthTag](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:AuthTag "Crypto.Cipher.Types"), ba)
*   [decrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:decrypt) :: ([BlockCipher128](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher128 "Crypto.Cipher.Types") aes, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") aad, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba) => aes ->[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV") -> aad -> ba ->[AuthTag](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:AuthTag "Crypto.Cipher.Types") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ba

Documentation
-------------

data[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.AESGCMSIV.html#Nonce)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce)

Nonce value for AES-GCM-SIV, always 12 bytes.

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.AESGCMSIV.html#line-52)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce)
Instance details
Defined in [Crypto.Cipher.AESGCMSIV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:-61--61-) :: [Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV") ->[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:-47--61-) :: [Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV") ->[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.AESGCMSIV.html#line-52)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce)
Instance details
Defined in [Crypto.Cipher.AESGCMSIV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:show) :: [Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:showList) :: [[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:showList)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.AESGCMSIV.html#line-52)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce)
Instance details
Defined in [Crypto.Cipher.AESGCMSIV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:length) :: [Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:withByteArray) :: [Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:copyByteArrayToPtr) :: [Nonce](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#t:Nonce "Crypto.Cipher.AESGCMSIV") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html#v:copyByteArrayToPtr)
