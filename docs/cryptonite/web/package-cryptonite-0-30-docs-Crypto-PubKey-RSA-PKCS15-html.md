# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html

Title: Crypto.PubKey.RSA.PKCS15

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html

Markdown Content:
Contents

*   [Padding and unpadding](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#g:1)
*   [Private key operations](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#g:2)
*   [Public key operations](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#g:3)
*   [Hash ASN1 description](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#g:4)

Description

Synopsis
*   [pad](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:pad) :: ([MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") message) =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> message -> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types") message)
*   [padSignature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:padSignature) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") signature =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> signature ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types") signature
*   [unpad](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:unpad) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") bytearray => bytearray ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types") bytearray
*   [decrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:decrypt) :: [Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Blinder "Crypto.PubKey.RSA.Types") ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")
*   [decryptSafer](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:decryptSafer) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") -> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString"))
*   [sign](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:sign) :: [HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15") hashAlg =>[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Blinder "Crypto.PubKey.RSA.Types") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") hashAlg ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")
*   [signSafer](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:signSafer) :: ([HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15") hashAlg, [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m) =>[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") hashAlg ->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") -> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString"))
*   [encrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:encrypt) :: [MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m =>[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") -> m ([Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString"))
*   [verify](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:verify) :: [HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15") hashAlg =>[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") hashAlg ->[PublicKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PublicKey "Crypto.PubKey.RSA.Types") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   class[HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hashAlg =>[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1) hashAlg

[Padding and unpadding ---------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#g:1)[Private key operations ----------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#g:2)

[decrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#decrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:decrypt)

Arguments

decrypt message using the private key.

When the decryption is not in a context where an attacker could gain information from the timing of the operation, the blinder can be set to None.

If unsure always set a blinder or use decryptSafer

The message is returned un-padded.

[decryptSafer](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#decryptSafer)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:decryptSafer)

Arguments

decrypt message using the private key and by automatically generating a blinder.

[sign](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#sign)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:sign)

Arguments

:: [HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15") hashAlg
=>[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe")[Blinder](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Blinder "Crypto.PubKey.RSA.Types")optional blinder
->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") hashAlg hash algorithm
->[PrivateKey](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:PrivateKey "Crypto.PubKey.RSA.Types")private key
->[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")message to sign
->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html#t:Error "Crypto.PubKey.RSA.Types")[ByteString](https://hackage.haskell.org/package/bytestring-0.10.10.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")

sign message using private key, a hash and its ASN1 description

When the signature is not in a context where an attacker could gain information from the timing of the operation, the blinder can be set to None.

If unsure always set a blinder or use signSafer

[signSafer](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#signSafer)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:signSafer)

Arguments

sign message using the private key and by automatically generating a blinder.

[Public key operations ---------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#g:3)[Hash ASN1 description ---------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#g:4)

class[HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") hashAlg =>[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html) hashAlg [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#HashAlgorithmASN1)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1)

A specialized class for hash algorithm that can product a ASN1 wrapped description the algorithm plus the content of the digest.

Minimal complete definition

hashDigestASN1

#### Instances

Instances details
[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15")[SHA512t_256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA512t_256 "Crypto.Hash.Algorithms")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#line-64)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1)
Instance details
Defined in [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)

Methods

[hashDigestASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:hashDigestASN1) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out =>[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash")[SHA512t_256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA512t_256 "Crypto.Hash.Algorithms") -> out
[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15")[SHA512t_224](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA512t_224 "Crypto.Hash.Algorithms")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#line-62)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1)
Instance details
Defined in [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)

Methods

[hashDigestASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:hashDigestASN1) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out =>[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash")[SHA512t_224](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA512t_224 "Crypto.Hash.Algorithms") -> out
[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15")[SHA512](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA512 "Crypto.Hash.Algorithms")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#line-60)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1)
Instance details
Defined in [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)

Methods

[hashDigestASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:hashDigestASN1) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out =>[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash")[SHA512](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA512 "Crypto.Hash.Algorithms") -> out
[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15")[SHA384](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA384 "Crypto.Hash.Algorithms")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#line-58)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1)
Instance details
Defined in [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)

Methods

[hashDigestASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:hashDigestASN1) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out =>[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash")[SHA384](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA384 "Crypto.Hash.Algorithms") -> out
[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15")[SHA256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA256 "Crypto.Hash.Algorithms")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#line-56)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1)
Instance details
Defined in [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)

Methods

[hashDigestASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:hashDigestASN1) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out =>[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash")[SHA256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA256 "Crypto.Hash.Algorithms") -> out
[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15")[SHA224](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA224 "Crypto.Hash.Algorithms")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#line-54)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1)
Instance details
Defined in [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)

Methods

[hashDigestASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:hashDigestASN1) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out =>[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash")[SHA224](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA224 "Crypto.Hash.Algorithms") -> out
[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15")[SHA1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA1 "Crypto.Hash.Algorithms")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#line-52)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1)
Instance details
Defined in [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)

Methods

[hashDigestASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:hashDigestASN1) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out =>[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash")[SHA1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:SHA1 "Crypto.Hash.Algorithms") -> out
[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15")[RIPEMD160](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:RIPEMD160 "Crypto.Hash.Algorithms")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#line-66)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1)
Instance details
Defined in [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)

Methods

[hashDigestASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:hashDigestASN1) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out =>[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash")[RIPEMD160](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:RIPEMD160 "Crypto.Hash.Algorithms") -> out
[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15")[MD5](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:MD5 "Crypto.Hash.Algorithms")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1)
Instance details
Defined in [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)

Methods

[hashDigestASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:hashDigestASN1) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out =>[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash")[MD5](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:MD5 "Crypto.Hash.Algorithms") -> out
[HashAlgorithmASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1 "Crypto.PubKey.RSA.PKCS15")[MD2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:MD2 "Crypto.Hash.Algorithms")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.RSA.PKCS15.html#line-48)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#t:HashAlgorithmASN1)
Instance details
Defined in [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)

Methods

[hashDigestASN1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html#v:hashDigestASN1) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") out =>[Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash")[MD2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html#t:MD2 "Crypto.Hash.Algorithms") -> out
