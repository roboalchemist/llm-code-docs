# Source: https://hackage.haskell.org/package/cryptonite-0.1

Title: cryptonite

URL Source: https://hackage.haskell.org/package/cryptonite-0.1

Markdown Content:
[cryptonite](https://hackage.haskell.org/package/cryptonite): Cryptography Primitives sink
------------------------------------------------------------------------------------------

A repository of cryptographic primitives.

*   Symmetric ciphers: AES, DES, 3DES, Blowfish, Camellia, RC4, Salsa, ChaCha.

*   Hash: SHA1, SHA2, SHA3, MD2, MD4, MD5, Kekkak, Skein, Ripemd, Tiger, Whirlpool

*   MAC: HMAC, Poly1305

*   Assymmetric crypto: DSA, RSA, DH, ECDH, ECDSA, ECC, Curve25519, Ed25519

*   Key Derivation Function: PBKDF2, Scrypt

*   Cryptographic Random generation: System Entropy, Deterministic Random Generator

*   Data related: Anti-Forensic Information Splitter (AFIS)

If anything cryptographic related is missing from here, submit a pull request to have it added. This package strive to be a cryptographic kitchen sink that provides cryptography for everyone.

Evaluate the security related to your requirements before using.

* * *

[[Skip to Readme](https://hackage.haskell.org/package/cryptonite-0.1/#readme)]

![Image 1](https://img.shields.io/static/v1?label=Documentation&message=Available&color=success)

Modules
-------

[[Index](https://hackage.haskell.org/package/cryptonite-0.1/docs/doc-index.html)]

*   _Crypto_
    *   _Cipher_
        *   [Crypto.Cipher.AES](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Cipher-AES.html)
        *   [Crypto.Cipher.Blowfish](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Cipher-Blowfish.html)
        *   [Crypto.Cipher.Camellia](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Cipher-Camellia.html)
        *   [Crypto.Cipher.ChaCha](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Cipher-ChaCha.html)
        *   [Crypto.Cipher.DES](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Cipher-DES.html)
        *   [Crypto.Cipher.RC4](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Cipher-RC4.html)
        *   [Crypto.Cipher.Salsa](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Cipher-Salsa.html)
        *   [Crypto.Cipher.TripleDES](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Cipher-TripleDES.html)
        *   [Crypto.Cipher.Types](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Cipher-Types.html)

    *   _Data_
        *   [Crypto.Data.AFIS](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Data-AFIS.html)

    *   [Crypto.Error](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Error.html)
    *   [Crypto.Hash](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Hash.html)
        *   [Crypto.Hash.Algorithms](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Hash-Algorithms.html)
        *   [Crypto.Hash.IO](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Hash-IO.html)

    *   _KDF_
        *   [Crypto.KDF.PBKDF2](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-KDF-PBKDF2.html)
        *   [Crypto.KDF.Scrypt](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-KDF-Scrypt.html)

    *   _MAC_
        *   [Crypto.MAC.HMAC](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-MAC-HMAC.html)
        *   [Crypto.MAC.Poly1305](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-MAC-Poly1305.html)

    *   _Number_
        *   [Crypto.Number.Basic](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Number-Basic.html)
        *   [Crypto.Number.F2m](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Number-F2m.html)
        *   [Crypto.Number.Generate](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Number-Generate.html)
        *   [Crypto.Number.ModArithmetic](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Number-ModArithmetic.html)
        *   [Crypto.Number.Prime](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Number-Prime.html)
        *   [Crypto.Number.Serialize](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Number-Serialize.html)

    *   _PubKey_
        *   [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-Curve25519.html)
        *   [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-DH.html)
        *   [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-DSA.html)
        *   _ECC_
            *   [Crypto.PubKey.ECC.DH](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-ECC-DH.html)
            *   [Crypto.PubKey.ECC.ECDSA](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-ECC-ECDSA.html)
            *   [Crypto.PubKey.ECC.Generate](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-ECC-Generate.html)
            *   [Crypto.PubKey.ECC.P256](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-ECC-P256.html)
            *   [Crypto.PubKey.ECC.Prim](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-ECC-Prim.html)
            *   [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-ECC-Types.html)

        *   [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-Ed25519.html)
        *   [Crypto.PubKey.HashDescr](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-HashDescr.html)
        *   [Crypto.PubKey.MaskGenFunction](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-MaskGenFunction.html)
        *   [Crypto.PubKey.RSA](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-RSA.html)
            *   [Crypto.PubKey.RSA.OAEP](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-RSA-OAEP.html)
            *   [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-RSA-PKCS15.html)
            *   [Crypto.PubKey.RSA.PSS](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-RSA-PSS.html)
            *   [Crypto.PubKey.RSA.Prim](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-RSA-Prim.html)
            *   [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-PubKey-RSA-Types.html)

    *   [Crypto.Random](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Random.html)
        *   [Crypto.Random.Entropy](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Random-Entropy.html)
            *   [Crypto.Random.Entropy.Unsafe](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Random-Entropy-Unsafe.html)

        *   [Crypto.Random.EntropyPool](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Random-EntropyPool.html)
        *   [Crypto.Random.Types](https://hackage.haskell.org/package/cryptonite-0.1/docs/Crypto-Random-Types.html)

Flags
-----

### Manual Flags

| Name | Description | Default |
| --- | --- | --- |
| support_aesni | allow compilation with AESNI on system and architecture that supports it | Enabled |
| support_pclmuldq | Allow compilation with pclmuldq on architecture that supports it | Disabled |
| integer-gmp | Whether or not to use GMP for some functions | Enabled |
| support_deepseq | add deepseq instances for cryptographic types | Enabled |

Use -f <flag> to enable a flag, or -f -<flag> to disable that flag. [More info](https://cabal.readthedocs.io/en/latest/setup-commands.html#controlling-flag-assignments)

#### Maintainer's Corner

[Package maintainers](https://hackage.haskell.org/package/cryptonite/maintainers)

*   [LukeTaylor](https://hackage.haskell.org/user/LukeTaylor), [VincentHanquez](https://hackage.haskell.org/user/VincentHanquez)

For package maintainers and hackage trustees

*   [edit package information](https://hackage.haskell.org/package/cryptonite/maintain)

Candidates

*    No Candidates 

| Versions [[RSS](https://hackage.haskell.org/package/cryptonite.rss)] | **0.1**, [0.2](https://hackage.haskell.org/package/cryptonite-0.2), [0.3](https://hackage.haskell.org/package/cryptonite-0.3), [0.4](https://hackage.haskell.org/package/cryptonite-0.4), [0.5](https://hackage.haskell.org/package/cryptonite-0.5), [0.6](https://hackage.haskell.org/package/cryptonite-0.6), [0.7](https://hackage.haskell.org/package/cryptonite-0.7), [0.8](https://hackage.haskell.org/package/cryptonite-0.8), [0.9](https://hackage.haskell.org/package/cryptonite-0.9), [0.10](https://hackage.haskell.org/package/cryptonite-0.10), [0.11](https://hackage.haskell.org/package/cryptonite-0.11), [0.12](https://hackage.haskell.org/package/cryptonite-0.12), [0.13](https://hackage.haskell.org/package/cryptonite-0.13), [0.14](https://hackage.haskell.org/package/cryptonite-0.14), [0.15](https://hackage.haskell.org/package/cryptonite-0.15), [0.15.1](https://hackage.haskell.org/package/cryptonite-0.15.1), [0.16](https://hackage.haskell.org/package/cryptonite-0.16), [0.17](https://hackage.haskell.org/package/cryptonite-0.17), [0.18](https://hackage.haskell.org/package/cryptonite-0.18), [0.19](https://hackage.haskell.org/package/cryptonite-0.19), [0.20](https://hackage.haskell.org/package/cryptonite-0.20), [0.21](https://hackage.haskell.org/package/cryptonite-0.21), [0.22](https://hackage.haskell.org/package/cryptonite-0.22), [0.23](https://hackage.haskell.org/package/cryptonite-0.23), [0.24](https://hackage.haskell.org/package/cryptonite-0.24), [0.25](https://hackage.haskell.org/package/cryptonite-0.25), [0.26](https://hackage.haskell.org/package/cryptonite-0.26), [0.27](https://hackage.haskell.org/package/cryptonite-0.27), [0.28](https://hackage.haskell.org/package/cryptonite-0.28), [0.29](https://hackage.haskell.org/package/cryptonite-0.29), [0.30](https://hackage.haskell.org/package/cryptonite-0.30) |
| --- |
| Change log | [CHANGELOG.md](https://hackage.haskell.org/package/cryptonite-0.1/changelog) |
| Dependencies | [base](https://hackage.haskell.org/package/base) (>=4.3 &&<5), [bytestring](https://hackage.haskell.org/package/bytestring), [deepseq](https://hackage.haskell.org/package/deepseq), [ghc-prim](https://hackage.haskell.org/package/ghc-prim), [integer-gmp](https://hackage.haskell.org/package/integer-gmp) (<1.1), [memory](https://hackage.haskell.org/package/memory) (>=0.2), [Win32](https://hackage.haskell.org/package/Win32) [[details](https://hackage.haskell.org/package/cryptonite-0.1/dependencies)] |
| License | [BSD-3-Clause](https://hackage.haskell.org/package/cryptonite-0.1/src/LICENSE) |
| Copyright | Vincent Hanquez <vincent@snarc.org> |
| Author | Vincent Hanquez <vincent@snarc.org> |
| Maintainer | vincent@snarc.org |
| Uploaded | by [VincentHanquez](https://hackage.haskell.org/user/VincentHanquez) at 2015-05-23T17:04:48Z |
| Revised | [Revision 1](https://hackage.haskell.org/package/cryptonite-0.1/revisions/) made by [sjakobi](https://hackage.haskell.org/user/sjakobi) at 2021-05-08T22:25:15Z |
| Category | [Cryptography](https://hackage.haskell.org/packages/#cat:Cryptography) |
| Home page | [https://github.com/vincenthz/cryptonite](https://github.com/vincenthz/cryptonite) |
| Bug tracker | [https://github.com/vincenthz/cryptonite/issues](https://github.com/vincenthz/cryptonite/issues) |
| Source repo | head: git clone [https://github.com/vincenthz/cryptonite](https://github.com/vincenthz/cryptonite) |
| Distributions | Debian:[0.26](http://packages.debian.org/source/bullseye/haskell-cryptonite), Fedora:[0.30](https://src.fedoraproject.org/rpms/ghc-cryptonite), LTSHaskell:[0.30](https://www.stackage.org/package/cryptonite), openSUSE:[0.30](https://build.opensuse.org/package/show/devel:languages:haskell/ghc-cryptonite) |
| Reverse Dependencies | 257 direct, 3650 indirect [[details](https://hackage.haskell.org/package/cryptonite-0.1/)] |
| Downloads | 167796 total (112 in the last 30 days) |
| Rating | 2.75 (votes: 13) [estimated by [Bayesian average](https://en.wikipedia.org/wiki/Bayesian_average)] |
| Your Rating | * λ * λ * λ |
| Status | Docs uploaded by user Build status unknown [[no reports yet](https://hackage.haskell.org/package/cryptonite-0.1/reports/)] |

* * *

Readme for cryptonite-0.1
-------------------------

[[back to package description](https://hackage.haskell.org/package/cryptonite-0.1/#description)]

[![Image 2: Build Status](https://travis-ci.org/vincenthz/cryptonite.png?branch=master)](https://travis-ci.org/vincenthz/cryptonite)[![Image 3: BSD](http://b.repl.ca/v1/license-BSD-blue.png)](http://en.wikipedia.org/wiki/BSD_licenses)[![Image 4: Haskell](http://b.repl.ca/v1/language-haskell-lightgrey.png)](http://haskell.org/)

Cryptonite is a haskell repository of cryptographic primitives. Each crypto algorithm have specificities, that are hard to wrap in common APIs and types, so instead of trying to provide a common ground for algorithms that wouldn't allow to provide all different usage or a really complicated system, this just provide a non-consistant low-level API.

If you have no idea what're you doing, please do not use this directly, rely on higher level protocols or higher level implementation.

Documentation: [cryptonite on hackage](http://hackage.haskell.org/package/cryptonite)

Versioning
----------

Development versions are an incremental number prefixed by 0. No specific meaning is associated with the versions, specially no API stability.

Production versions : TBD

Coding Style
------------

The coding style of this project mostly follows: [haskell-style](https://github.com/tibbe/haskell-style-guide/blob/master/haskell-style.md)

Support
-------

cryptonite supports the following platform:

*   Windows >= 8 
*   OSX >= 10.8 
*   Linux 

On the following architectures:

*   x86-64 
*   i386 

On the following haskell versions:

*   GHC 7.0.x 
*   GHC 7.4.x 
*   GHC 7.6.x 
*   GHC 7.8.x 
*   GHC 7.10.x 

Further platforms and architectures probably works too, but until maintainer(s) don't have regular access to them, we can't commit for further support

Links
-----

*   [ChaCha](http://cr.yp.to/chacha.html)
*   [ChaCha-test-vectors](https://github.com/secworks/chacha_testvectors.git)
*   [Poly1305](http://cr.yp.to/mac.html)
*   [Poly1305-test-vectors](http://tools.ietf.org/html/draft-nir-cfrg-chacha20-poly1305-06#page-12)
*   [Salsa](http://cr.yp.to/snuffle.html)
*   [Salsa128-test-vectors](https://github.com/alexwebr/salsa20/blob/master/test_vectors.128)
*   [Salsa256-test-vectors](https://github.com/alexwebr/salsa20/blob/master/test_vectors.256)
*   [PBKDF2](http://tools.ietf.org/html/rfc2898)
*   [PBKDF2-test-vectors](http://www.ietf.org/rfc/rfc6070.txt)
*   [Scrypt](http://www.tarsnap.com/scrypt.html)
*   [Curve25519](http://cr.yp.to/ecdh.html)
*   [Ed25519](http://ed25519.cr.yp.to/papers.html)
*   [AFIS](http://clemens.endorphin.org/cryptography)

TODO
----

*   finish google P256 binding 
*   add support for XSalsa
