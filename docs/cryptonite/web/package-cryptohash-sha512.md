# Source: https://hackage.haskell.org/package/cryptohash-sha512

Title: cryptohash-sha512

URL Source: https://hackage.haskell.org/package/cryptohash-sha512

Markdown Content:
[cryptohash-sha512](https://hackage.haskell.org/package/cryptohash-sha512): Fast, pure and practical SHA-512 implementation
---------------------------------------------------------------------------------------------------------------------------

A practical incremental and one-pass, pure API to the [SHA-512, SHA512/t and SHA-384 cryptographic hash algorithms](https://en.wikipedia.org/wiki/SHA-2) according to [FIPS 180-4](http://dx.doi.org/10.6028/NIST.FIPS.180-4) with performance close to the fastest implementations available in other languages.

The core SHA-512 algorithm is implemented in C and is thus expected to be as fast as the standard [sha512sum(1) tool](https://linux.die.net/man/1/sha512sum). (If, instead, you require a pure Haskell implementation and performance is secondary, please refer to the [SHA package](https://hackage.haskell.org/package/SHA).)

Additionally, this package provides support for

*   HMAC-SHA-384: SHA-384-based [Hashed Message Authentication Codes](https://en.wikipedia.org/wiki/HMAC) (HMAC)

*   HMAC-SHA-512: SHA-512-based [Hashed Message Authentication Codes](https://en.wikipedia.org/wiki/HMAC) (HMAC)

*   HMAC-SHA-512/t: SHA-512/t-based [Hashed Message Authentication Codes](https://en.wikipedia.org/wiki/HMAC) (HMAC)

*   HKDF-SHA-384: [HMAC-SHA-384-based Key Derivation Function](https://en.wikipedia.org/wiki/HKDF) (HKDF)

*   HKDF-SHA-512: [HMAC-SHA-512-based Key Derivation Function](https://en.wikipedia.org/wiki/HKDF) (HKDF)

conforming to [RFC6234](https://tools.ietf.org/html/rfc6234), [RFC4231](https://tools.ietf.org/html/rfc4231), [RFC5869](https://tools.ietf.org/html/rfc5869), et al..

#### Packages in the `cryptohash-*` family

*   [cryptohash-md5](https://hackage.haskell.org/package/cryptohash-md5)

*   [cryptohash-sha1](https://hackage.haskell.org/package/cryptohash-sha1)

*   [cryptohash-sha256](https://hackage.haskell.org/package/cryptohash-sha256)

*   [cryptohash-sha512](https://hackage.haskell.org/package/cryptohash-sha512)

#### Relationship to the `cryptohash` package and its API

This package has been originally a fork of `cryptohash-0.11.7` because the `cryptohash` package had been deprecated and so this package continues to satisfy the need for a lightweight package providing the SHA-512 hash algorithms without any dependencies on packages other than `base` and `bytestring`. The API exposed by `cryptohash-sha512-0.11.*`'s [Crypto.Hash.SHA512](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/docs/Crypto-Hash-SHA512.html), [Crypto.Hash.SHA512t](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/docs/Crypto-Hash-SHA512t.html), and [Crypto.Hash.SHA384](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/docs/Crypto-Hash-SHA384.html) module is guaranteed to remain a compatible superset of the API provided by the `cryptohash-0.11.7`'s module of the same name.

Consequently, this package is designed to be used as a drop-in replacement for the `cryptohash-0.11.7` modules mentioned above, though with a [clearly smaller footprint by almost 3 orders of magnitude](https://www.reddit.com/r/haskell/comments/5lxv75/psa_please_use_unique_module_names_when_uploading/dbzegx3/).

[![Image 1](https://img.shields.io/static/v1?label=Build&message=InstallOk&color=success)](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/reports/1)![Image 2](https://img.shields.io/static/v1?label=Documentation&message=Available&color=success)

Modules
-------

[[Index](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/docs/doc-index.html)] [[Quick Jump](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/#)]

*   _Crypto_
    *   _Hash_
        *   [Crypto.Hash.SHA384](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/docs/Crypto-Hash-SHA384.html)
        *   [Crypto.Hash.SHA512](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/docs/Crypto-Hash-SHA512.html)
        *   [Crypto.Hash.SHA512t](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/docs/Crypto-Hash-SHA512t.html)

Downloads
---------

*   [cryptohash-sha512-0.11.103.0.tar.gz](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/cryptohash-sha512-0.11.103.0.tar.gz) [[browse](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/src/)] (Cabal source package)
*   [Package description](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/cryptohash-sha512.cabal) (as included in the package)

#### Maintainer's Corner

[Package maintainers](https://hackage.haskell.org/package/cryptohash-sha512/maintainers)

*   [HerbertValerioRiedel](https://hackage.haskell.org/user/HerbertValerioRiedel), [phadej](https://hackage.haskell.org/user/phadej)

For package maintainers and hackage trustees

*   [edit package information](https://hackage.haskell.org/package/cryptohash-sha512/maintain)

Candidates

*   [0.11.100.1](https://hackage.haskell.org/package/cryptohash-sha512-0.11.100.1/candidate)

| Versions [[RSS](https://hackage.haskell.org/package/cryptohash-sha512.rss)] | [0.11.100.1](https://hackage.haskell.org/package/cryptohash-sha512-0.11.100.1), [0.11.101.0](https://hackage.haskell.org/package/cryptohash-sha512-0.11.101.0), [0.11.102.0](https://hackage.haskell.org/package/cryptohash-sha512-0.11.102.0), **0.11.103.0** |
| --- |
| Change log | [changelog.md](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/changelog) |
| Dependencies | [base](https://hackage.haskell.org/package/base) (>=4.5 &&<5), [bytestring](https://hackage.haskell.org/package/bytestring) (>=0.9.2 &&<0.13) [[details](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/dependencies)] |
| Tested with | ghc ==9.12.2, ghc ==9.10.2, ghc ==9.8.4, ghc ==9.6.7, ghc ==9.4.8, ghc ==9.2.8, ghc ==9.0.2, ghc ==8.10.7, ghc ==8.8.4, ghc ==8.6.5, ghc ==8.4.4, ghc ==8.2.2 |
| License | [BSD-3-Clause](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/src/LICENSE) |
| Copyright | Vincent Hanquez, Herbert Valerio Riedel |
| Author |  |
| Maintainer | Herbert Valerio Riedel <hvr@gnu.org> |
| Uploaded | by [HerbertValerioRiedel](https://hackage.haskell.org/user/HerbertValerioRiedel) at 2025-10-18T10:12:49Z |
| Category | [Data](https://hackage.haskell.org/packages/#cat:Data), [Cryptography](https://hackage.haskell.org/packages/#cat:Cryptography) |
| Home page | [https://github.com/haskell-hvr/cryptohash-sha512](https://github.com/haskell-hvr/cryptohash-sha512) |
| Bug tracker | [https://github.com/haskell-hvr/cryptohash-sha512/issues](https://github.com/haskell-hvr/cryptohash-sha512/issues) |
| Source repo | head: git clone [https://github.com/haskell-hvr/cryptohash-sha512.git](https://github.com/haskell-hvr/cryptohash-sha512.git) |
| Distributions | LTSHaskell:[0.11.103.0](https://www.stackage.org/package/cryptohash-sha512), Stackage:[0.11.103.0](https://www.stackage.org/package/cryptohash-sha512) |
| Reverse Dependencies | 9 direct, 41 indirect [[details](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/)] |
| Downloads | 3752 total (7 in the last 30 days) |
| Rating | (no votes yet) [estimated by [Bayesian average](https://en.wikipedia.org/wiki/Bayesian_average)] |
| Your Rating | * λ * λ * λ |
| Status | Docs available [[build log](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/reports/1)] Last success reported on 2025-10-18 [[all 1 reports](https://hackage.haskell.org/package/cryptohash-sha512-0.11.103.0/reports/)] |
