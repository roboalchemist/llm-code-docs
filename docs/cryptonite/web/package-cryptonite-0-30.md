# Source: https://hackage.haskell.org/package/cryptonite-0.30/

Title: cryptonite

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/

Markdown Content:
cryptonite: Cryptography Primitives sink
===============

[Hackage :: [Package]](https://hackage.haskell.org/)
*   Search
*   [Browse](https://hackage.haskell.org/packages/browse)
*   [What's new](https://hackage.haskell.org/packages/recent)
*   [Upload](https://hackage.haskell.org/upload)
*   [User accounts](https://hackage.haskell.org/accounts)

[cryptonite](https://hackage.haskell.org/package/cryptonite): Cryptography Primitives sink
==========================================================================================

 [ [bsd3](https://hackage.haskell.org/packages/tag/bsd3), [cryptography](https://hackage.haskell.org/packages/tag/cryptography), [deprecated](https://hackage.haskell.org/packages/tag/deprecated) ] [ [Propose Tags](https://hackage.haskell.org/package/cryptonite/tags/edit) ] [ [Report a vulnerability](https://github.com/haskell/security-advisories/blob/main/CONTRIBUTING.md) ] 

Deprecated in favor of [crypton](https://hackage.haskell.org/package/crypton), [cryptohash-md5](https://hackage.haskell.org/package/cryptohash-md5), [cryptohash-sha1](https://hackage.haskell.org/package/cryptohash-sha1), [cryptohash-sha256](https://hackage.haskell.org/package/cryptohash-sha256), [cryptohash-sha512](https://hackage.haskell.org/package/cryptohash-sha512)

A repository of cryptographic primitives.

*   Symmetric ciphers: AES, DES, 3DES, CAST5, Blowfish, Twofish, Camellia, RC4, Salsa, XSalsa, ChaCha.

*   Hash: SHA1, SHA2, SHA3, SHAKE, MD2, MD4, MD5, Keccak, Skein, Ripemd, Tiger, Whirlpool, Blake2

*   MAC: HMAC, KMAC, Poly1305

*   Asymmetric crypto: DSA, RSA, DH, ECDH, ECDSA, ECC, Curve25519, Curve448, Ed25519, Ed448

*   Key Derivation Function: PBKDF2, Scrypt, HKDF, Argon2, BCrypt, BCryptPBKDF

*   Cryptographic Random generation: System Entropy, Deterministic Random Generator

*   Data related: Anti-Forensic Information Splitter (AFIS)

If anything cryptographic related is missing from here, submit a pull request to have it added. This package strives to be a cryptographic kitchen sink that provides cryptography for everyone.

Evaluate the security related to your requirements before using.

Read [Crypto.Tutorial](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Tutorial.html) for a quick start guide.

* * *

 [[Skip to Readme](https://hackage.haskell.org/package/cryptonite-0.30/#readme)] 

[![Image 5](https://img.shields.io/static/v1?label=Build&message=InstallOk&color=success)](https://hackage.haskell.org/package/cryptonite-0.30/reports/1)![Image 6](https://img.shields.io/static/v1?label=Tests&message=Passed&color=success)![Image 7](https://img.shields.io/static/v1?label=Coverage&message=72%&color=brightgreen)![Image 8](https://img.shields.io/static/v1?label=Documentation&message=Available&color=success)

Modules
-------

[[Index](https://hackage.haskell.org/package/cryptonite-0.30/docs/doc-index.html)] [[Quick Jump](https://hackage.haskell.org/package/cryptonite-0.30/#)]

*   _Crypto_
    *   _Cipher_
        *   [Crypto.Cipher.AES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AES.html)
        *   [Crypto.Cipher.AESGCMSIV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-AESGCMSIV.html)
        *   [Crypto.Cipher.Blowfish](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Blowfish.html)
        *   [Crypto.Cipher.CAST5](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-CAST5.html)
        *   [Crypto.Cipher.Camellia](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Camellia.html)
        *   [Crypto.Cipher.ChaCha](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaCha.html)
        *   [Crypto.Cipher.ChaChaPoly1305](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-ChaChaPoly1305.html)
        *   [Crypto.Cipher.DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html)
        *   [Crypto.Cipher.RC4](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-RC4.html)
        *   [Crypto.Cipher.Salsa](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Salsa.html)
        *   [Crypto.Cipher.TripleDES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-TripleDES.html)
        *   [Crypto.Cipher.Twofish](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Twofish.html)
        *   [Crypto.Cipher.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html)
        *   [Crypto.Cipher.Utils](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Utils.html)
        *   [Crypto.Cipher.XSalsa](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-XSalsa.html)

    *   _ConstructHash_
        *   [Crypto.ConstructHash.MiyaguchiPreneel](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ConstructHash-MiyaguchiPreneel.html)

    *   _Data_
        *   [Crypto.Data.AFIS](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-AFIS.html)
        *   [Crypto.Data.Padding](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Data-Padding.html)

    *   [Crypto.ECC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html)
        *   [Crypto.ECC.Edwards25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC-Edwards25519.html)

    *   [Crypto.Error](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html)
    *   [Crypto.Hash](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html)
        *   [Crypto.Hash.Algorithms](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-Algorithms.html)
        *   [Crypto.Hash.IO](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html)

    *   _KDF_
        *   [Crypto.KDF.Argon2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Argon2.html)
        *   [Crypto.KDF.BCrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCrypt.html)
        *   [Crypto.KDF.BCryptPBKDF](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-BCryptPBKDF.html)
        *   [Crypto.KDF.HKDF](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-HKDF.html)
        *   [Crypto.KDF.PBKDF2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-PBKDF2.html)
        *   [Crypto.KDF.Scrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-KDF-Scrypt.html)

    *   _MAC_
        *   [Crypto.MAC.CMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-CMAC.html)
        *   [Crypto.MAC.HMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-HMAC.html)
        *   [Crypto.MAC.KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html)
        *   [Crypto.MAC.Poly1305](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html)

    *   _Number_
        *   [Crypto.Number.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Basic.html)
        *   [Crypto.Number.F2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-F2m.html)
        *   [Crypto.Number.Generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Generate.html)
        *   [Crypto.Number.ModArithmetic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-ModArithmetic.html)
        *   [Crypto.Number.Nat](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Nat.html)
        *   [Crypto.Number.Prime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Prime.html)
        *   [Crypto.Number.Serialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize.html)
            *   [Crypto.Number.Serialize.Internal](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize-Internal.html)
                *   [Crypto.Number.Serialize.Internal.LE](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize-Internal-LE.html)

            *   [Crypto.Number.Serialize.LE](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Serialize-LE.html)

    *   [Crypto.OTP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-OTP.html)
    *   _PubKey_
        *   [Crypto.PubKey.Curve25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve25519.html)
        *   [Crypto.PubKey.Curve448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Curve448.html)
        *   [Crypto.PubKey.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DH.html)
        *   [Crypto.PubKey.DSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-DSA.html)
        *   _ECC_
            *   [Crypto.PubKey.ECC.DH](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-DH.html)
            *   [Crypto.PubKey.ECC.ECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-ECDSA.html)
            *   [Crypto.PubKey.ECC.Generate](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Generate.html)
            *   [Crypto.PubKey.ECC.P256](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-P256.html)
            *   [Crypto.PubKey.ECC.Prim](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Prim.html)
            *   [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

        *   [Crypto.PubKey.ECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html)
        *   [Crypto.PubKey.ECIES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECIES.html)
        *   [Crypto.PubKey.Ed25519](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed25519.html)
        *   [Crypto.PubKey.Ed448](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Ed448.html)
        *   [Crypto.PubKey.EdDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-EdDSA.html)
        *   [Crypto.PubKey.MaskGenFunction](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-MaskGenFunction.html)
        *   [Crypto.PubKey.RSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA.html)
            *   [Crypto.PubKey.RSA.OAEP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-OAEP.html)
            *   [Crypto.PubKey.RSA.PKCS15](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PKCS15.html)
            *   [Crypto.PubKey.RSA.PSS](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-PSS.html)
            *   [Crypto.PubKey.RSA.Prim](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Prim.html)
            *   [Crypto.PubKey.RSA.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-RSA-Types.html)

        *   _Rabin_
            *   [Crypto.PubKey.Rabin.Basic](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Basic.html)
            *   [Crypto.PubKey.Rabin.Modified](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Modified.html)
            *   [Crypto.PubKey.Rabin.OAEP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-OAEP.html)
            *   [Crypto.PubKey.Rabin.RW](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-RW.html)
            *   [Crypto.PubKey.Rabin.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-Rabin-Types.html)

    *   [Crypto.Random](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random.html)
        *   [Crypto.Random.Entropy](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy.html)
            *   [Crypto.Random.Entropy.Unsafe](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Entropy-Unsafe.html)

        *   [Crypto.Random.EntropyPool](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-EntropyPool.html)
        *   [Crypto.Random.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Random-Types.html)

    *   _System_
        *   [Crypto.System.CPU](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-System-CPU.html)

    *   [Crypto.Tutorial](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Tutorial.html)

Flags
-----

### Manual Flags

| Name | Description | Default |
| --- | --- | --- |
| support_aesni | allow compilation with AESNI on system and architecture that supports it | Enabled |
| support_rdrand | allow compilation with RDRAND on system and architecture that supports it | Enabled |
| support_pclmuldq | Allow compilation with pclmuldq on architecture that supports it | Disabled |
| support_sse | Use SSE optimized version of (BLAKE2, ARGON2) | Disabled |
| integer-gmp | Whether or not to use GMP for some functions | Enabled |
| support_deepseq | add deepseq instances for cryptographic types | Enabled |
| old_toolchain_inliner | use -fgnu89-inline to workaround an old compiler _linker_ glibc issue. | Disabled |
| check_alignment | extra check on alignment in C layers, which cause lowlevel assert errors. for debugging only. | Disabled |
| use_target_attributes | use GCC / clang function attributes instead of global target options. | Enabled |

Use -f <flag> to enable a flag, or -f -<flag> to disable that flag. [More info](https://cabal.readthedocs.io/en/latest/setup-commands.html#controlling-flag-assignments)

Downloads
---------

*   [cryptonite-0.30.tar.gz](https://hackage.haskell.org/package/cryptonite-0.30/cryptonite-0.30.tar.gz) [[browse](https://hackage.haskell.org/package/cryptonite-0.30/src/)] (Cabal source package)
*   [Package description](https://hackage.haskell.org/package/cryptonite-0.30/cryptonite.cabal) (as included in the package)

#### Maintainer's Corner

[Package maintainers](https://hackage.haskell.org/package/cryptonite/maintainers)

*   [LukeTaylor](https://hackage.haskell.org/user/LukeTaylor), [VincentHanquez](https://hackage.haskell.org/user/VincentHanquez)

For package maintainers and hackage trustees

*   [edit package information](https://hackage.haskell.org/package/cryptonite/maintain)

Candidates

*    No Candidates 

| Versions [[RSS](https://hackage.haskell.org/package/cryptonite.rss)] | [0.1](https://hackage.haskell.org/package/cryptonite-0.1), [0.2](https://hackage.haskell.org/package/cryptonite-0.2), [0.3](https://hackage.haskell.org/package/cryptonite-0.3), [0.4](https://hackage.haskell.org/package/cryptonite-0.4), [0.5](https://hackage.haskell.org/package/cryptonite-0.5), [0.6](https://hackage.haskell.org/package/cryptonite-0.6), [0.7](https://hackage.haskell.org/package/cryptonite-0.7), [0.8](https://hackage.haskell.org/package/cryptonite-0.8), [0.9](https://hackage.haskell.org/package/cryptonite-0.9), [0.10](https://hackage.haskell.org/package/cryptonite-0.10), [0.11](https://hackage.haskell.org/package/cryptonite-0.11), [0.12](https://hackage.haskell.org/package/cryptonite-0.12), [0.13](https://hackage.haskell.org/package/cryptonite-0.13), [0.14](https://hackage.haskell.org/package/cryptonite-0.14), [0.15](https://hackage.haskell.org/package/cryptonite-0.15), [0.15.1](https://hackage.haskell.org/package/cryptonite-0.15.1), [0.16](https://hackage.haskell.org/package/cryptonite-0.16), [0.17](https://hackage.haskell.org/package/cryptonite-0.17), [0.18](https://hackage.haskell.org/package/cryptonite-0.18), [0.19](https://hackage.haskell.org/package/cryptonite-0.19), [0.20](https://hackage.haskell.org/package/cryptonite-0.20), [0.21](https://hackage.haskell.org/package/cryptonite-0.21), [0.22](https://hackage.haskell.org/package/cryptonite-0.22), [0.23](https://hackage.haskell.org/package/cryptonite-0.23), [0.24](https://hackage.haskell.org/package/cryptonite-0.24), [0.25](https://hackage.haskell.org/package/cryptonite-0.25), [0.26](https://hackage.haskell.org/package/cryptonite-0.26), [0.27](https://hackage.haskell.org/package/cryptonite-0.27), [0.28](https://hackage.haskell.org/package/cryptonite-0.28), [0.29](https://hackage.haskell.org/package/cryptonite-0.29), **0.30** |
| --- |
| Change log | [CHANGELOG.md](https://hackage.haskell.org/package/cryptonite-0.30/changelog) |
| Dependencies | [base](https://hackage.haskell.org/package/base), [basement](https://hackage.haskell.org/package/basement) (>=0.0.6), [bytestring](https://hackage.haskell.org/package/bytestring), [deepseq](https://hackage.haskell.org/package/deepseq), [ghc-prim](https://hackage.haskell.org/package/ghc-prim), [integer-gmp](https://hackage.haskell.org/package/integer-gmp), [memory](https://hackage.haskell.org/package/memory) (>=0.14.18), [Win32](https://hackage.haskell.org/package/Win32) [[details](https://hackage.haskell.org/package/cryptonite-0.30/dependencies)] |
| Tested with | ghc ==9.2.2, ghc ==9.0.2, ghc ==8.10.7, ghc ==8.8.4 |
| License | [BSD-3-Clause](https://hackage.haskell.org/package/cryptonite-0.30/src/LICENSE) |
| Copyright | Vincent Hanquez <vincent@snarc.org> |
| Author | Vincent Hanquez <vincent@snarc.org> |
| Maintainer | vincent@snarc.org |
| Uploaded | by [VincentHanquez](https://hackage.haskell.org/user/VincentHanquez) at 2022-03-13T12:56:59Z |
| Category | [Cryptography](https://hackage.haskell.org/packages/#cat:Cryptography) |
| Home page | [https://github.com/haskell-crypto/cryptonite](https://github.com/haskell-crypto/cryptonite) |
| Bug tracker | [https://github.com/haskell-crypto/cryptonite/issues](https://github.com/haskell-crypto/cryptonite/issues) |
| Source repo | head: git clone [https://github.com/haskell-crypto/cryptonite](https://github.com/haskell-crypto/cryptonite) |
| Distributions | Debian:[0.26](http://packages.debian.org/source/bullseye/haskell-cryptonite), Fedora:[0.30](https://src.fedoraproject.org/rpms/ghc-cryptonite), LTSHaskell:[0.30](https://www.stackage.org/package/cryptonite), openSUSE:[0.30](https://build.opensuse.org/package/show/devel:languages:haskell/ghc-cryptonite) |
| Reverse Dependencies | 257 direct, 3650 indirect [[details](https://hackage.haskell.org/package/cryptonite-0.30/)] |
| Downloads | 167796 total (112 in the last 30 days) |
| Rating | 2.75 (votes: 13) [estimated by [Bayesian average](https://en.wikipedia.org/wiki/Bayesian_average)] |
| Your Rating | * λ * λ * λ |
| Status | Docs available [[build log](https://hackage.haskell.org/package/cryptonite-0.30/reports/1)] Last success reported on 2022-03-13 [[all 1 reports](https://hackage.haskell.org/package/cryptonite-0.30/reports/)] |

* * *

Readme for cryptonite-0.30
--------------------------

 [[back to package description](https://hackage.haskell.org/package/cryptonite-0.30/#description)] 

cryptonite
==========

[![Image 9: Join the chat at https://gitter.im/vincenthz/cryptonite](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/vincenthz/cryptonite?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)[![Image 10: Build Status](https://travis-ci.org/haskell-crypto/cryptonite.png?branch=master)](https://travis-ci.org/haskell-crypto/cryptonite)[![Image 11: BSD](http://b.repl.ca/v1/license-BSD-blue.png)](http://en.wikipedia.org/wiki/BSD_licenses)[![Image 12: Haskell](http://b.repl.ca/v1/language-haskell-lightgrey.png)](http://haskell.org/)

Cryptonite is a haskell repository of cryptographic primitives. Each crypto algorithm has specificities that are hard to wrap in common APIs and types, so instead of trying to provide a common ground for algorithms, this package provides a non-consistent low-level API.

If you have no idea what you're doing, please do not use this directly. Instead, rely on higher level protocols or implementations.

Documentation: [cryptonite on hackage](http://hackage.haskell.org/package/cryptonite)

Stability
---------

Cryptonite APIs are stable, and we only strive to add, not change or remove. Note that because the API exposed is wide and also expose internals things (for power users and flexibility), certains APIs can be revised in extreme cases where we can't just add.

Versioning
----------

Next version of `0.x` is `0.(x+1)`. There's no exceptions, or API related meaning behind the numbers.

Each versions of stackage (going back 3 stable LTS) has a cryptonite version that we maintain with security fixes when necessary and are versioned with the following `0.x.y` scheme.

Coding Style
------------

The coding style of this project mostly follows: [haskell-style](https://github.com/tibbe/haskell-style-guide/blob/master/haskell-style.md)

Support
-------

See [Haskell packages guidelines](https://github.com/vincenthz/haskell-pkg-guidelines/blob/master/README.md#support)

Known Building Issues
---------------------

On OSX <= 10.7, the system compiler doesn't understand the '-maes' option, and with the lack of autodetection feature builtin in .cabal file, it is left on the user to disable the aesni. See the [Disabling AESNI] section

On CentOS 7 the default C compiler includes intrinsic header files incompatible with per-function target options. Solutions are to use GCC >= 4.9 or disable flag _use\_target\_attributes_ (see flag configuration examples below).

Disabling AESNI
---------------

It may be useful to disable AESNI for building, testing or runtime purposes. This is achieved with the _support\_aesni_ flag.

As part of configure of cryptonite:

```
cabal configure --flag='-support_aesni'
```

or as part of an installation:

```
cabal install --constraint="cryptonite -support_aesni"
```

For help with cabal flags, see: [stackoverflow : is there a way to define flags for cabal](http://stackoverflow.com/questions/23523869/is-there-any-way-to-define-flags-for-cabal-dependencies)

Enabling PCLMULDQ
-----------------

When the C toolchain supports it, enabling flag _support\_pclmuldq_ can bring additional security and performance for AES GCM. A CPU with the necessary instruction set will use an alternate implementation selected at runtime.

Links
-----

*   [ChaCha](http://cr.yp.to/chacha.html)
*   [ChaCha-test-vectors](https://github.com/secworks/chacha_testvectors.git)
*   [Poly1305](http://cr.yp.to/mac.html)
*   [Poly1305-test-vectors](http://tools.ietf.org/html/draft-nir-cfrg-chacha20-poly1305-06#page-12)
*   [Salsa](http://cr.yp.to/snuffle.html)
*   [Salsa128-test-vectors](https://github.com/alexwebr/salsa20/blob/master/test_vectors.128)
*   [Salsa256-test-vectors](https://github.com/alexwebr/salsa20/blob/master/test_vectors.256)
*   [XSalsa](https://cr.yp.to/snuffle/xsalsa-20081128.pdf)
*   [PBKDF2](http://tools.ietf.org/html/rfc2898)
*   [PBKDF2-test-vectors](http://www.ietf.org/rfc/rfc6070.txt)
*   [Scrypt](http://www.tarsnap.com/scrypt.html)
*   [Curve25519](http://cr.yp.to/ecdh.html)
*   [Ed25519](http://ed25519.cr.yp.to/papers.html)
*   [Ed448-Goldilocks](http://ed448goldilocks.sourceforge.net/)
*   [EdDSA-test-vectors](http://www.ietf.org/rfc/rfc8032.txt)
*   [AFIS](http://clemens.endorphin.org/cryptography)

Produced by [hackage](https://hackage.haskell.org/) and [Cabal](http://haskell.org/cabal/) 3.16.1.0.

You can find any exported type, constructor, class, function or pattern defined in this package by (approximate) name.

| Key | Shortcut |
| --- | --- |
| s | Open this search box |
| esc | Close this search box |
| ↓,ctrl + j | Move down in search results |
| ↑,ctrl + k | Move up in search results |
| ↵ | Go to active search result |
