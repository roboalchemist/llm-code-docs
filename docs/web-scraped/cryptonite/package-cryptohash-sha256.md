# Source: https://hackage.haskell.org/package/cryptohash-sha256

Title: cryptohash-sha256

URL Source: https://hackage.haskell.org/package/cryptohash-sha256

Markdown Content:
[cryptohash-sha256](https://hackage.haskell.org/package/cryptohash-sha256): Fast, pure and practical SHA-256 implementation
---------------------------------------------------------------------------------------------------------------------------

A practical incremental and one-pass, pure API to the [SHA-256 cryptographic hash algorithm](https://en.wikipedia.org/wiki/SHA-2) according to [FIPS 180-4](http://dx.doi.org/10.6028/NIST.FIPS.180-4) with performance close to the fastest implementations available in other languages.

The core SHA-256 algorithm is implemented in C and is thus expected to be as fast as the standard [sha256sum(1) tool](https://linux.die.net/man/1/sha256sum); for instance, on an _Intel Core i7-3770_ at 3.40GHz this implementation can compute a SHA-256 hash over 230 MiB of data in under one second. (If, instead, you require a pure Haskell implementation and performance is secondary, please refer to the [SHA package](https://hackage.haskell.org/package/SHA).)

Additionally, this package provides support for

*   HMAC-SHA-256: SHA-256-based [Hashed Message Authentication Codes](https://en.wikipedia.org/wiki/HMAC) (HMAC)

*   HKDF-SHA-256: [HMAC-SHA-256-based Key Derivation Function](https://en.wikipedia.org/wiki/HKDF) (HKDF)

conforming to [RFC6234](https://tools.ietf.org/html/rfc6234), [RFC4231](https://tools.ietf.org/html/rfc4231), [RFC5869](https://tools.ietf.org/html/rfc5869), et al..

#### Relationship to the `cryptohash` package and its API

This package has been originally a fork of `cryptohash-0.11.7` because the `cryptohash` package had been deprecated and so this package continues to satisfy the need for a lightweight package providing the SHA-256 hash algorithm without any dependencies on packages other than `base` and `bytestring`. The API exposed by `cryptohash-sha256-0.11.*`'s [Crypto.Hash.SHA256](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/docs/Crypto-Hash-SHA256.html) module is guaranteed to remain a compatible superset of the API provided by the `cryptohash-0.11.7`'s module of the same name.

Consequently, this package is designed to be used as a drop-in replacement for `cryptohash-0.11.7`'s [Crypto.Hash.SHA256](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/docs/Crypto-Hash-SHA256.html) module, though with a [clearly smaller footprint by almost 3 orders of magnitude](https://www.reddit.com/r/haskell/comments/5lxv75/psa_please_use_unique_module_names_when_uploading/dbzegx3/).

[![Image 1](https://img.shields.io/static/v1?label=Build&message=InstallOk&color=success)](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/reports/1)![Image 2](https://img.shields.io/static/v1?label=Tests&message=Passed&color=success)![Image 3](https://img.shields.io/static/v1?label=Coverage&message=88%&color=brightgreen)![Image 4](https://img.shields.io/static/v1?label=Documentation&message=Available&color=success)

Modules
-------

[[Index](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/docs/doc-index.html)] [[Quick Jump](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/#)]

*   _Crypto_
    *   _Hash_
        *   [Crypto.Hash.SHA256](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/docs/Crypto-Hash-SHA256.html)

Flags
-----

### Manual Flags

| Name | Description | Default |
| --- | --- | --- |
| exe | Enable building `sha256sum` executable | Disabled |
| use-cbits | Use fast optimized C routines via FFI; if flag is disabled falls back to non-FFI Haskell optimized implementation. | Enabled |

Use -f <flag> to enable a flag, or -f -<flag> to disable that flag. [More info](https://cabal.readthedocs.io/en/latest/setup-commands.html#controlling-flag-assignments)

| Versions [[RSS](https://hackage.haskell.org/package/cryptohash-sha256.rss)] | [0.11.7.1](https://hackage.haskell.org/package/cryptohash-sha256-0.11.7.1), [0.11.7.2](https://hackage.haskell.org/package/cryptohash-sha256-0.11.7.2), [0.11.100.0](https://hackage.haskell.org/package/cryptohash-sha256-0.11.100.0), [0.11.100.1](https://hackage.haskell.org/package/cryptohash-sha256-0.11.100.1), [0.11.101.0](https://hackage.haskell.org/package/cryptohash-sha256-0.11.101.0), [0.11.102.0](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.0), **0.11.102.1** |
| --- |
| Change log | [changelog.md](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/changelog) |
| Dependencies | [base](https://hackage.haskell.org/package/base) (>=4.5 &&<5), [bytestring](https://hackage.haskell.org/package/bytestring) (>=0.9.2.0 &&<0.10 || >=0.10.0.0 &&<0.11 || >=0.11.0.0 &&<0.12 || >=0.12.0.2 &&<0.13) [[details](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/dependencies)] |
| Tested with | ghc ==9.12.1, ghc ==9.10.1, ghc ==9.8.4, ghc ==9.6.6, ghc ==9.4.8, ghc ==9.2.8, ghc ==9.0.2, ghc ==8.10.7, ghc ==8.8.4, ghc ==8.6.5, ghc ==8.4.4, ghc ==8.2.2 |
| License | [BSD-3-Clause](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/src/LICENSE) |
| Copyright | Vincent Hanquez, Herbert Valerio Riedel |
| Author |  |
| Maintainer | Herbert Valerio Riedel <hvr@gnu.org> |
| Uploaded | by [phadej](https://hackage.haskell.org/user/phadej) at 2021-10-10T16:53:05Z |
| Revised | [Revision 6](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/revisions/) made by [AndreasAbel](https://hackage.haskell.org/user/AndreasAbel) at 2025-01-01T19:53:11Z |
| Category | [Data](https://hackage.haskell.org/packages/#cat:Data), [Cryptography](https://hackage.haskell.org/packages/#cat:Cryptography) |
| Home page | [https://github.com/haskell-hvr/cryptohash-sha256](https://github.com/haskell-hvr/cryptohash-sha256) |
| Bug tracker | [https://github.com/haskell-hvr/cryptohash-sha256/issues](https://github.com/haskell-hvr/cryptohash-sha256/issues) |
| Source repo | head: git clone [https://github.com/haskell-hvr/cryptohash-sha256.git](https://github.com/haskell-hvr/cryptohash-sha256.git) |
| Distributions | Debian:[0.11.101.0](http://packages.debian.org/source/bullseye/haskell-cryptohash-sha256), Fedora:[0.11.102.1](https://src.fedoraproject.org/rpms/ghc-cryptohash-sha256), LTSHaskell:[0.11.102.1](https://www.stackage.org/package/cryptohash-sha256), Stackage:[0.11.102.1](https://www.stackage.org/package/cryptohash-sha256), openSUSE:[0.11.102.1](https://build.opensuse.org/package/show/devel:languages:haskell/ghc-cryptohash-sha256) |
| Reverse Dependencies | 52 direct, 147 indirect [[details](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/)] |
| Executables | sha256sum |
| Downloads | 53289 total (11 in the last 30 days) |
| Rating | 2.25 (votes: 2) [estimated by [Bayesian average](https://en.wikipedia.org/wiki/Bayesian_average)] |
| Your Rating | * λ * λ * λ |
| Status | Docs available [[build log](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/reports/1)] Last success reported on 2021-10-10 [[all 1 reports](https://hackage.haskell.org/package/cryptohash-sha256-0.11.102.1/reports/)] |
