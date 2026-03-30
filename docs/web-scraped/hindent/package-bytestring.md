# Source: https://hackage.haskell.org/package/bytestring

Title: bytestring

URL Source: https://hackage.haskell.org/package/bytestring

Markdown Content:
bytestring: Fast, compact, strict and lazy byte strings with a list interface
===============

[Hackage :: [Package]](https://hackage.haskell.org/)
*   Search
*   [Browse](https://hackage.haskell.org/packages/browse)
*   [What's new](https://hackage.haskell.org/packages/recent)
*   [Upload](https://hackage.haskell.org/upload)
*   [User accounts](https://hackage.haskell.org/accounts)

[bytestring](https://hackage.haskell.org/package/bytestring): Fast, compact, strict and lazy byte strings with a list interface
===============================================================================================================================

 [ [bsd3](https://hackage.haskell.org/packages/tag/bsd3), [data](https://hackage.haskell.org/packages/tag/data), [library](https://hackage.haskell.org/packages/tag/library) ] [ [Propose Tags](https://hackage.haskell.org/package/bytestring/tags/edit) ] [ [Report a vulnerability](https://github.com/haskell/security-advisories/blob/main/CONTRIBUTING.md) ] 

An efficient compact, immutable byte string type (both strict and lazy) suitable for binary or 8-bit character data.

The `ByteString` type represents sequences of bytes or 8-bit characters. It is suitable for high performance use, both in terms of large data quantities, or high speed requirements. The `ByteString` functions follow the same style as Haskell's ordinary lists, so it is easy to convert code from using `String` to `ByteString`.

Two `ByteString` variants are provided:

*   Strict `ByteString`s keep the string as a single large array. This makes them convenient for passing data between C and Haskell.

*   Lazy `ByteString`s use a lazy list of strict chunks which makes it suitable for I/O streaming tasks.

The `Char8` modules provide a character-based view of the same underlying `ByteString` types. This makes it convenient to handle mixed binary and 8-bit character content (which is common in many file formats and network protocols).

The `Builder` module provides an efficient way to build up `ByteString`s in an ad-hoc way by repeated concatenation. This is ideal for fast serialisation or pretty printing.

There is also a `ShortByteString` type which has a lower memory overhead and can be converted to or from a `ByteString`. It is suitable for keeping many short strings in memory, especially long-term, without incurring any possible heap fragmentation costs.

`ByteString`s are not designed for Unicode. For Unicode strings you should use the `Text` type from the `text` package.

These modules are intended to be imported qualified, to avoid name clashes with [Prelude](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Prelude.html) functions, e.g.

import qualified Data.ByteString as BS

* * *

 [[Skip to Readme](https://hackage.haskell.org/package/bytestring#readme)] 

[![Image 1](https://img.shields.io/static/v1?label=Build&message=InstallOk&color=success)](https://hackage.haskell.org/package/reports/4)![Image 2](https://img.shields.io/static/v1?label=Documentation&message=Available&color=success)

Modules
-------

[[Index](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/doc-index.html)] [[Quick Jump](https://hackage.haskell.org/package/bytestring#)]

*   _Data_
    *   [Data.ByteString](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString.html)
        *   [Data.ByteString.Builder](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Builder.html)
            *   [Data.ByteString.Builder.Extra](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Builder-Extra.html)
            *   [Data.ByteString.Builder.Internal](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Builder-Internal.html)
            *   [Data.ByteString.Builder.Prim](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Builder-Prim.html)
                *   [Data.ByteString.Builder.Prim.Internal](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Builder-Prim-Internal.html)

            *   [Data.ByteString.Builder.RealFloat](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Builder-RealFloat.html)

        *   [Data.ByteString.Char8](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Char8.html)
        *   [Data.ByteString.Internal](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Internal.html)
        *   [Data.ByteString.Lazy](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Lazy.html)
            *   [Data.ByteString.Lazy.Char8](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Lazy-Char8.html)
            *   [Data.ByteString.Lazy.Internal](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Lazy-Internal.html)

        *   [Data.ByteString.Short](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Short.html)
            *   [Data.ByteString.Short.Internal](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Short-Internal.html)

        *   [Data.ByteString.Unsafe](https://hackage.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString-Unsafe.html)

Flags
-----

### Manual Flags

Name Description Default pure-haskell Don't use bytestring's standard C routines When this flag is true, bytestring will use pure Haskell variants (no C FFI) of the internal functions. This is not recommended except in use cases that cannot (or do not) depend on C, such as with GHC's JavaScript backend.Disabled

Use -f <flag> to enable a flag, or -f -<flag> to disable that flag. [More info](https://cabal.readthedocs.io/en/latest/setup-commands.html#controlling-flag-assignments)

Downloads
---------

*   [bytestring-0.12.2.0.tar.gz](https://hackage.haskell.org/package/bytestring-0.12.2.0/bytestring-0.12.2.0.tar.gz) [[browse](https://hackage.haskell.org/package/bytestring-0.12.2.0/src/)] (Cabal source package)
*   [Package description](https://hackage.haskell.org/package/bytestring-0.12.2.0/bytestring.cabal) ([revised](https://hackage.haskell.org/package/bytestring-0.12.2.0/revisions/) from the package)

Note: This package has [metadata revisions](https://hackage.haskell.org/package/bytestring-0.12.2.0/revisions/) in the cabal description newer than included in the tarball. To unpack the package including the revisions, use 'cabal get'.

#### Maintainer's Corner

[Package maintainers](https://hackage.haskell.org/package/bytestring/maintainers)

*   [BenGamari](https://hackage.haskell.org/user/BenGamari), [DuncanCoutts](https://hackage.haskell.org/user/DuncanCoutts), [SylvainHenry](https://hackage.haskell.org/user/SylvainHenry), [Bodigrim](https://hackage.haskell.org/user/Bodigrim), [chessai](https://hackage.haskell.org/user/chessai), [clyring](https://hackage.haskell.org/user/clyring)

For package maintainers and hackage trustees

*   [edit package information](https://hackage.haskell.org/package/bytestring/maintain)

Candidates

*    No Candidates 

| Versions [[RSS](https://hackage.haskell.org/package/bytestring.rss)] | [0.9](https://hackage.haskell.org/package/bytestring-0.9), [0.9.0.1](https://hackage.haskell.org/package/bytestring-0.9.0.1), [0.9.0.2](https://hackage.haskell.org/package/bytestring-0.9.0.2), [0.9.0.3](https://hackage.haskell.org/package/bytestring-0.9.0.3), [0.9.0.4](https://hackage.haskell.org/package/bytestring-0.9.0.4), [0.9.1.0](https://hackage.haskell.org/package/bytestring-0.9.1.0), [0.9.1.1](https://hackage.haskell.org/package/bytestring-0.9.1.1), [0.9.1.2](https://hackage.haskell.org/package/bytestring-0.9.1.2), [0.9.1.3](https://hackage.haskell.org/package/bytestring-0.9.1.3), [0.9.1.4](https://hackage.haskell.org/package/bytestring-0.9.1.4), [0.9.1.5](https://hackage.haskell.org/package/bytestring-0.9.1.5), [0.9.1.6](https://hackage.haskell.org/package/bytestring-0.9.1.6), [0.9.1.7](https://hackage.haskell.org/package/bytestring-0.9.1.7), [0.9.1.8](https://hackage.haskell.org/package/bytestring-0.9.1.8), [0.9.1.9](https://hackage.haskell.org/package/bytestring-0.9.1.9), [0.9.1.10](https://hackage.haskell.org/package/bytestring-0.9.1.10), [0.9.2.0](https://hackage.haskell.org/package/bytestring-0.9.2.0), [0.9.2.1](https://hackage.haskell.org/package/bytestring-0.9.2.1), [0.10.0.0](https://hackage.haskell.org/package/bytestring-0.10.0.0), [0.10.0.1](https://hackage.haskell.org/package/bytestring-0.10.0.1), [0.10.0.2](https://hackage.haskell.org/package/bytestring-0.10.0.2), [0.10.2.0](https://hackage.haskell.org/package/bytestring-0.10.2.0), [0.10.4.0](https://hackage.haskell.org/package/bytestring-0.10.4.0), [0.10.4.1](https://hackage.haskell.org/package/bytestring-0.10.4.1), [0.10.6.0](https://hackage.haskell.org/package/bytestring-0.10.6.0), [0.10.8.0](https://hackage.haskell.org/package/bytestring-0.10.8.0), [0.10.8.1](https://hackage.haskell.org/package/bytestring-0.10.8.1), [0.10.8.2](https://hackage.haskell.org/package/bytestring-0.10.8.2), [0.10.9.0](https://hackage.haskell.org/package/bytestring-0.10.9.0), [0.10.10.0](https://hackage.haskell.org/package/bytestring-0.10.10.0), [0.10.10.1](https://hackage.haskell.org/package/bytestring-0.10.10.1), [0.10.12.0](https://hackage.haskell.org/package/bytestring-0.10.12.0), [0.10.12.1](https://hackage.haskell.org/package/bytestring-0.10.12.1), [0.11.0.0](https://hackage.haskell.org/package/bytestring-0.11.0.0), [0.11.1.0](https://hackage.haskell.org/package/bytestring-0.11.1.0), [0.11.2.0](https://hackage.haskell.org/package/bytestring-0.11.2.0), [0.11.3.0](https://hackage.haskell.org/package/bytestring-0.11.3.0), [0.11.3.1](https://hackage.haskell.org/package/bytestring-0.11.3.1), [0.11.4.0](https://hackage.haskell.org/package/bytestring-0.11.4.0), [0.11.5.0](https://hackage.haskell.org/package/bytestring-0.11.5.0), [0.11.5.1](https://hackage.haskell.org/package/bytestring-0.11.5.1), [0.11.5.2](https://hackage.haskell.org/package/bytestring-0.11.5.2), [0.11.5.3](https://hackage.haskell.org/package/bytestring-0.11.5.3), [0.11.5.4](https://hackage.haskell.org/package/bytestring-0.11.5.4), [0.12.0.0](https://hackage.haskell.org/package/bytestring-0.12.0.0), [0.12.0.1](https://hackage.haskell.org/package/bytestring-0.12.0.1), [0.12.0.2](https://hackage.haskell.org/package/bytestring-0.12.0.2), [0.12.1.0](https://hackage.haskell.org/package/bytestring-0.12.1.0), **0.12.2.0** |
| --- |
| Change log | [Changelog.md](https://hackage.haskell.org/package/bytestring-0.12.2.0/changelog) |
| Dependencies | [base](https://hackage.haskell.org/package/base) (>=4.11 &&<5), [data-array-byte](https://hackage.haskell.org/package/data-array-byte) (>=0.1 &&<0.2), [deepseq](https://hackage.haskell.org/package/deepseq), [ghc-prim](https://hackage.haskell.org/package/ghc-prim), [template-haskell](https://hackage.haskell.org/package/template-haskell) [[details](https://hackage.haskell.org/package/bytestring-0.12.2.0/dependencies)] |
| Tested with | ghc ==9.10.1, ghc ==9.8.2, ghc ==9.6.5, ghc ==9.4.8, ghc ==9.2.8, ghc ==9.0.2, ghc ==8.10.7, ghc ==8.8.4, ghc ==8.6.5, ghc ==8.4.4 |
| License | [BSD-3-Clause](https://hackage.haskell.org/package/bytestring-0.12.2.0/src/LICENSE) |
| Copyright | Copyright (c) Don Stewart 2005-2009, (c) Duncan Coutts 2006-2015, (c) David Roundy 2003-2005, (c) Jasper Van der Jeugt 2010, (c) Simon Meier 2010-2013. |
| Author | Don Stewart, Duncan Coutts |
| Maintainer | Haskell Bytestring Team <andrew.lelechenko@gmail.com>, Core Libraries Committee |
| Uploaded | by [Bodigrim](https://hackage.haskell.org/user/Bodigrim) at 2024-12-06T21:41:31Z |
| Revised | [Revision 1](https://hackage.haskell.org/package/bytestring-0.12.2.0/revisions/) made by [clyring](https://hackage.haskell.org/user/clyring) at 2025-10-12T23:57:03Z |
| Category | [Data](https://hackage.haskell.org/packages/#cat:Data) |
| Home page | [https://github.com/haskell/bytestring](https://github.com/haskell/bytestring) |
| Bug tracker | [https://github.com/haskell/bytestring/issues](https://github.com/haskell/bytestring/issues) |
| Source repo | head: git clone [https://github.com/haskell/bytestring](https://github.com/haskell/bytestring) |
| Distributions | Arch:[0.11.5.3](https://archlinux.org/packages/extra/x86_64/ghc), Fedora:[0.12.2.0](https://src.fedoraproject.org/rpms/ghc) |
| Reverse Dependencies | 6404 direct, 9389 indirect [[details](https://hackage.haskell.org/package/bytestring)] |
| Downloads | 121752 total (109 in the last 30 days) |
| Rating | 2.75 (votes: 20) [estimated by [Bayesian average](https://en.wikipedia.org/wiki/Bayesian_average)] |
| Your Rating | * λ * λ * λ |
| Status | Docs available [[build log](https://hackage.haskell.org/package/bytestring-0.12.2.0/reports/3)] Last success reported on 2026-03-14 [[all 4 reports](https://hackage.haskell.org/package/bytestring-0.12.2.0/reports/)] |

* * *

Readme for bytestring-0.12.2.0
------------------------------

 [[back to package description](https://hackage.haskell.org/package/bytestring#description)] 

ByteString: Fast, Packed Strings of Bytes
=========================================

[![Image 3: Build Status](https://github.com/haskell/bytestring/workflows/ci/badge.svg)](https://github.com/haskell/bytestring/actions?query=workflow%3Aci)[![Image 4: Hackage](http://img.shields.io/hackage/v/bytestring.svg)](https://hackage.haskell.org/package/bytestring)[![Image 5: Stackage LTS](http://stackage.org/package/bytestring/badge/lts)](http://stackage.org/lts/package/bytestring)[![Image 6: Stackage Nightly](http://stackage.org/package/bytestring/badge/nightly)](http://stackage.org/nightly/package/bytestring)

This library provides the `Data.ByteString` module -- strict and lazy byte arrays manipulable as strings -- providing very time/space-efficient string and IO operations.

For very large data requirements, or constraints on heap size, `Data.ByteString.Lazy` is provided, a lazy list of bytestring chunks. Efficient processing of multi-gigabyte data can be achieved this way.

The library also provides `Data.ByteString.Builder` for efficient construction of `ByteString` values from smaller pieces during binary serialization.

Requirements:

*   Cabal 2.2 or greater 
*   GHC 8.4 or greater 

### Authors

`ByteString` was derived from the GHC `PackedString` library, originally written by Bryan O'Sullivan, and then by Simon Marlow. It was adapted and greatly extended for darcs by David Roundy and others. Don Stewart and Duncan Coutts cleaned up and further extended the implementation and added the `.Lazy` code. Simon Meier contributed the `Builder` feature.

Produced by [hackage](https://hackage.haskell.org/) and [Cabal](http://haskell.org/cabal/) 3.16.1.0.
