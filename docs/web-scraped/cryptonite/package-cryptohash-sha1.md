# Source: https://hackage.haskell.org/package/cryptohash-sha1

Title: cryptohash-sha1

URL Source: https://hackage.haskell.org/package/cryptohash-sha1

Markdown Content:
[cryptohash-sha1](https://hackage.haskell.org/package/cryptohash-sha1): Fast, pure and practical SHA-1 implementation
---------------------------------------------------------------------------------------------------------------------

A practical incremental and one-pass, pure API to the [SHA-1 hash algorithm](https://en.wikipedia.org/wiki/SHA-1) (including [HMAC](https://en.wikipedia.org/wiki/HMAC) support) with performance close to the fastest implementations available in other languages.

The implementation is made in C with a haskell FFI wrapper that hides the C implementation.

NOTE: This package has been forked off `cryptohash-0.11.7` because the `cryptohash` package has been deprecated and so this package continues to satisfy the need for a lightweight package providing the SHA1 hash algorithm without any dependencies on packages other than `base` and `bytestring`.

Consequently, this package can be used as a drop-in replacement for `cryptohash`'s [Crypto.Hash.SHA1](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/docs/Crypto-Hash-SHA1.html) module, though with a clearly smaller footprint.

[![Image 1](https://img.shields.io/static/v1?label=Build&message=InstallOk&color=success)](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/reports/1)![Image 2](https://img.shields.io/static/v1?label=Tests&message=Passed&color=success)![Image 3](https://img.shields.io/static/v1?label=Coverage&message=88%&color=brightgreen)![Image 4](https://img.shields.io/static/v1?label=Documentation&message=Available&color=success)

Modules
-------

[[Index](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/docs/doc-index.html)] [[Quick Jump](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/#)]

*   _Crypto_
    *   _Hash_
        *   [Crypto.Hash.SHA1](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/docs/Crypto-Hash-SHA1.html)

| Versions [[RSS](https://hackage.haskell.org/package/cryptohash-sha1.rss)] | [0.11.7.1](https://hackage.haskell.org/package/cryptohash-sha1-0.11.7.1), [0.11.7.2](https://hackage.haskell.org/package/cryptohash-sha1-0.11.7.2), [0.11.100.0](https://hackage.haskell.org/package/cryptohash-sha1-0.11.100.0), [0.11.100.1](https://hackage.haskell.org/package/cryptohash-sha1-0.11.100.1), **0.11.101.0** |
| --- |
| Change log | [changelog.md](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/changelog) |
| Dependencies | [base](https://hackage.haskell.org/package/base) (>=4.5 &&<5), [bytestring](https://hackage.haskell.org/package/bytestring) (>=0.9.2 &&<0.13) [[details](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/dependencies)] |
| Tested with | ghc ==9.12.1, ghc ==9.10.1, ghc ==9.8.4, ghc ==9.6.6, ghc ==9.4.8, ghc ==9.2.8, ghc ==9.0.2, ghc ==8.10.7, ghc ==8.8.4, ghc ==8.6.5, ghc ==8.4.4, ghc ==8.2.2, ghc ==8.0.2 |
| License | [BSD-3-Clause](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/src/LICENSE) |
| Copyright | Vincent Hanquez, Herbert Valerio Riedel |
| Author |  |
| Maintainer | https://github.com/haskell-hvr/cryptohash-sha1 |
| Uploaded | by [phadej](https://hackage.haskell.org/user/phadej) at 2021-11-13T17:15:39Z |
| Revised | [Revision 6](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/revisions/) made by [AndreasAbel](https://hackage.haskell.org/user/AndreasAbel) at 2025-01-01T18:59:14Z |
| Category | [Data](https://hackage.haskell.org/packages/#cat:Data), [Cryptography](https://hackage.haskell.org/packages/#cat:Cryptography) |
| Home page | [https://github.com/haskell-hvr/cryptohash-sha1](https://github.com/haskell-hvr/cryptohash-sha1) |
| Bug tracker | [https://github.com/haskell-hvr/cryptohash-sha1/issues](https://github.com/haskell-hvr/cryptohash-sha1/issues) |
| Source repo | head: git clone [https://github.com/haskell-hvr/cryptohash-sha1.git](https://github.com/haskell-hvr/cryptohash-sha1.git) |
| Distributions | Debian:[0.11.100.1](http://packages.debian.org/source/bullseye/haskell-cryptohash-sha1), Fedora:[0.11.101.0](https://src.fedoraproject.org/rpms/ghc-cryptohash-sha1), LTSHaskell:[0.11.101.0](https://www.stackage.org/package/cryptohash-sha1), Stackage:[0.11.101.0](https://www.stackage.org/package/cryptohash-sha1), openSUSE:[0.11.101.0](https://build.opensuse.org/package/show/devel:languages:haskell/ghc-cryptohash-sha1) |
| Reverse Dependencies | 27 direct, 3767 indirect [[details](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/)] |
| Downloads | 42946 total (17 in the last 30 days) |
| Rating | (no votes yet) [estimated by [Bayesian average](https://en.wikipedia.org/wiki/Bayesian_average)] |
| Your Rating | * λ * λ * λ |
| Status | Docs available [[build log](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/reports/1)] Last success reported on 2021-11-13 [[all 1 reports](https://hackage.haskell.org/package/cryptohash-sha1-0.11.101.0/reports/)] |
