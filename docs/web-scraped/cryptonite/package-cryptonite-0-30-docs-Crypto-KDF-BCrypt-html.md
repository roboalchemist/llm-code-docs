# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html

Title: Crypto.KDF.BCrypt

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html

Markdown Content:
Description

Password encoding and validation using bcrypt.

Example usage:

`>>>`**```
import Crypto.KDF.BCrypt (hashPassword, validatePassword)
```**`>>>`**```
import qualified Data.ByteString.Char8 as B
```**`>>>`**```

```**`>>>`**```
let bcryptHash = B.pack "$2a$10$MJJifxfaqQmbx1Mhsq3oq.YmMmfNhkyW4s/MS3K5rIMVfB7w0Q/OW"
```**`>>>`**```
let password = B.pack "password"
```**`>>>`**```
validatePassword password bcryptHash
```**`>>>`**```
True
```**`>>>`**```
let otherPassword = B.pack "otherpassword"
```**`>>>`**```
otherHash <- hashPassword 12 otherPassword :: IO B.ByteString
```**`>>>`**```
validatePassword otherPassword otherHash
```**`>>>`**```
True
```**
See [https://www.usenix.org/conference/1999-usenix-annual-technical-conference/future-adaptable-password-scheme](https://www.usenix.org/conference/1999-usenix-annual-technical-conference/future-adaptable-password-scheme) for details of the original algorithm.

The functions `hashPassword` and `validatePassword` should be all that most users need.

Hashes are strings of the form `$2a$10$MJJifxfaqQmbx1Mhsq3oq.YmMmfNhkyW4sMS3K5rIMVfB7w0QOW` which encode a version number, an integer cost parameter and the concatenated salt and hash bytes (each separately Base64 encoded. Incrementing the cost parameter approximately doubles the time taken to calculate the hash.

The different version numbers evolved to account for bugs in the standard C implementations. They don't represent different versions of the algorithm itself and in most cases should produce identical results. The most up to date version is `2b` and this implementation uses the `2b` version prefix, but will also attempt to validate against hashes with versions `2a` and `2y`. Version `2` or `2x` will be rejected. No attempt is made to differentiate between the different versions when validating a password, but in practice this shouldn't cause any problems if passwords are UTF-8 encoded (which they should be) and less than 256 characters long.

The cost parameter can be between 4 and 31 inclusive, but anything less than 10 is probably not strong enough. High values may be prohibitively slow depending on your hardware. Choose the highest value you can without having an unacceptable impact on your users. The cost parameter can also be varied depending on the account, since it is unique to an individual hash.

Synopsis
*   [hashPassword](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html#v:hashPassword) :: ([MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") password, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") hash) =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> password -> m hash
*   [validatePassword](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html#v:validatePassword) :: ([ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") password, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") hash) => password -> hash ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [validatePasswordEither](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html#v:validatePasswordEither) :: ([ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") password, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") hash) => password -> hash ->[Either](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Either.html#t:Either "Data.Either")[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")
*   [bcrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html#v:bcrypt) :: ([ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") salt, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") password, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") output) =>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> salt -> password -> output

Documentation
-------------

[hashPassword](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.BCrypt.html#hashPassword)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html#v:hashPassword)

Arguments

:: ([MonadRandom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html#t:MonadRandom "Crypto.Random.Types") m, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") password, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") hash)
=>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")The cost parameter. Should be between 4 and 31 (inclusive). Values which lie outside this range will be adjusted accordingly.
-> password The password. Should be the UTF-8 encoded bytes of the password text.
-> m hash The bcrypt hash in standard format.

Create a bcrypt hash for a password with a provided cost value. Typically used to create a hash when a new user account is registered or when a user changes their password.

Each increment of the cost approximately doubles the time taken. The 16 bytes of random salt will be generated internally.

[validatePassword](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html) :: ([ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") password, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") hash) => password -> hash ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.BCrypt.html#validatePassword)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html#v:validatePassword)

Check a password against a stored bcrypt hash when authenticating a user.

Returns `False` if the password doesn't match the hash, or if the hash is invalid or an unsupported version.

[bcrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.KDF.BCrypt.html#bcrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html#v:bcrypt)

Arguments

:: ([ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") salt, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") password, [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") output)
=>[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")The cost parameter. Should be between 4 and 31 (inclusive). Values which lie outside this range will be adjusted accordingly.
-> salt The salt. Must be 16 bytes in length or an error will be raised.
-> password The password. Should be the UTF-8 encoded bytes of the password text.
-> output The bcrypt hash in standard format.

Create a bcrypt hash for a password with a provided cost value and salt.

Cost value under 4 will be automatically adjusted back to 10 for safety reason.
