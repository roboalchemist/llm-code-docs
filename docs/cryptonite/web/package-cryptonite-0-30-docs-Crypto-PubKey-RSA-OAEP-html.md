# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html

Title: Crypto.PubKey.RSA.OAEP

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html

Markdown Content:
Contents

*   [OAEP encryption](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#g:1)
*   [OAEP decryption](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#g:2)

Description

Synopsis
*   data[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#t:OAEPParams) hash seed output = [OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:OAEPParams) {
    *   [oaepHash](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:oaepHash) :: hash
    *   [oaepMaskGenAlg](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:oaepMaskGenAlg) :: [MaskGenAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-MaskGenFunction.html#t:MaskGenAlgorithm "Crypto.PubKey.MaskGenFunction") seed output
    *   [oaepLabel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:oaepLabel) :: [Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")

}
*   [defaultOAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:defaultOAEPParams) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") seed, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") output, [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash) => hash ->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#t:OAEPParams "Crypto.PubKey.RSA.OAEP") hash seed output
*   [encryptWithSeed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:encryptWithSeed) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#t:OAEPParams "Crypto.PubKey.RSA.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")
*   [encrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:encrypt) :: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m) =>[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#t:OAEPParams "Crypto.PubKey.RSA.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") -> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString"))
*   [decrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:decrypt) :: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash =>[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Blinder "Crypto.PubKey.RSA.Types") ->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#t:OAEPParams "Crypto.PubKey.RSA.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")
*   [decryptSafer](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:decryptSafer) :: ([HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash, [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m) =>[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#t:OAEPParams "Crypto.PubKey.RSA.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") -> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString"))

Documentation
-------------

data[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html) hash seed output [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.OAEP.html#OAEPParams)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#t:OAEPParams)

Parameters for OAEP encryption/decryption

[OAEP encryption ---------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#g:1)

[encryptWithSeed](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.OAEP.html#encryptWithSeed)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:encryptWithSeed)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=>[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")Seed
->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#t:OAEPParams "Crypto.PubKey.RSA.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")OAEP params to use for encryption
->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types")Public key.
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")Message to encrypt
->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")

Encrypt a message using OAEP with a predefined seed.

[OAEP decryption ---------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#g:2)

[decrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.OAEP.html#decrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:decrypt)

Arguments

:: [HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hash
=>[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Blinder "Crypto.PubKey.RSA.Types")Optional blinder
->[OAEPParams](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#t:OAEPParams "Crypto.PubKey.RSA.OAEP") hash [ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")OAEP params to use for decryption
->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")Private key
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")Cipher text
->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")

Decrypt a ciphertext using OAEP

When the signature is not in a context where an attacker could gain information from the timing of the operation, the blinder can be set to None.

If unsure always set a blinder or use decryptSafer

[decryptSafer](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.OAEP.html#decryptSafer)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html#v:decryptSafer)

Arguments

Decrypt a ciphertext using OAEP and by automatically generating a blinder.
