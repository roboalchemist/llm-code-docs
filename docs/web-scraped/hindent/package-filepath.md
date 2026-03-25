# Source: https://hackage.haskell.org/package/filepath

Title: filepath

URL Source: https://hackage.haskell.org/package/filepath

Markdown Content:
[filepath](https://hackage.haskell.org/package/filepath): Library for manipulating FilePaths in a cross platform way.
---------------------------------------------------------------------------------------------------------------------

This package provides functionality for manipulating `FilePath` values, and is shipped with [GHC](https://www.haskell.org/ghc/). It provides two variants for filepaths:

1.   legacy filepaths: `type FilePath = String`

2.   operating system abstracted filepaths (`OsPath`): internally unpinned `ShortByteString` (platform-dependent encoding)

It is recommended to use `OsPath` when possible, because it is more correct.

For each variant there are three main modules:

*   [System.FilePath.Posix](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-FilePath-Posix.html) / [System.OsPath.Posix](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-OsPath-Posix.html) manipulates POSIX/Linux style `FilePath` values (with `/` as the path separator).

*   [System.FilePath.Windows](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-FilePath-Windows.html) / [System.OsPath.Windows](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-OsPath-Windows.html) manipulates Windows style `FilePath` values (with either `\` or `/` as the path separator, and deals with drives).

*   [System.FilePath](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-FilePath.html) / [System.OsPath](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-OsPath.html) for dealing with current platform-specific filepaths

For more powerful string manipulation of `OsPath`, you can use the [os-string package](https://hackage.haskell.org/package/os-string) (`OsPath` is a type synonym for `OsString`).

An introduction into the new API can be found in this [blog post](https://hasufell.github.io/posts/2022-06-29-fixing-haskell-filepaths.html). Code examples for the new API can be found [here](https://github.com/hasufell/filepath-examples).

* * *

[[Skip to Readme](https://hackage.haskell.org/package/filepath-1.5.5.0/#readme)]

[![Image 1](https://img.shields.io/static/v1?label=Build&message=InstallOk&color=success)](https://hackage.haskell.org/package/filepath-1.5.5.0/reports/1)![Image 2](https://img.shields.io/static/v1?label=Tests&message=Passed&color=success)![Image 3](https://img.shields.io/static/v1?label=Coverage&message=4%&color=red)![Image 4](https://img.shields.io/static/v1?label=Documentation&message=Available&color=success)

Modules
-------

[[Index](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/doc-index.html)] [[Quick Jump](https://hackage.haskell.org/package/filepath-1.5.5.0/#)]

*   _System_
    *   [System.FilePath](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-FilePath.html)
        *   [System.FilePath.Posix](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-FilePath-Posix.html)
        *   [System.FilePath.Windows](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-FilePath-Windows.html)

    *   [System.OsPath](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-OsPath.html)
        *   [System.OsPath.Encoding](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-OsPath-Encoding.html)
        *   [System.OsPath.Internal](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-OsPath-Internal.html)
        *   [System.OsPath.Posix](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-OsPath-Posix.html)
            *   [System.OsPath.Posix.Internal](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-OsPath-Posix-Internal.html)

        *   [System.OsPath.Types](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-OsPath-Types.html)
        *   [System.OsPath.Windows](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-OsPath-Windows.html)
            *   [System.OsPath.Windows.Internal](https://hackage.haskell.org/package/filepath-1.5.5.0/docs/System-OsPath-Windows-Internal.html)

Flags
-----

### Manual Flags

| Name | Description | Default |
| --- | --- | --- |
| cpphs | Use cpphs (fixes haddock source links) | Disabled |

Use -f <flag> to enable a flag, or -f -<flag> to disable that flag. [More info](https://cabal.readthedocs.io/en/latest/setup-commands.html#controlling-flag-assignments)

Downloads
---------

*   [filepath-1.5.5.0.tar.gz](https://hackage.haskell.org/package/filepath-1.5.5.0/filepath-1.5.5.0.tar.gz) [[browse](https://hackage.haskell.org/package/filepath-1.5.5.0/src/)] (Cabal source package)
*   [Package description](https://hackage.haskell.org/package/filepath-1.5.5.0/filepath.cabal) (as included in the package)

#### Maintainer's Corner

[Package maintainers](https://hackage.haskell.org/package/filepath/maintainers)

*   [AustinSeipp](https://hackage.haskell.org/user/AustinSeipp), [DuncanCoutts](https://hackage.haskell.org/user/DuncanCoutts), [HerbertValerioRiedel](https://hackage.haskell.org/user/HerbertValerioRiedel), [IanLynagh](https://hackage.haskell.org/user/IanLynagh), [NeilMitchell](https://hackage.haskell.org/user/NeilMitchell), [maerwald](https://hackage.haskell.org/user/maerwald)

For package maintainers and hackage trustees

*   [edit package information](https://hackage.haskell.org/package/filepath/maintain)

Candidates

*   [1.4.0.0](https://hackage.haskell.org/package/filepath-1.4.0.0/candidate), [1.4.99.0](https://hackage.haskell.org/package/filepath-1.4.99.0/candidate), [1.4.99.1](https://hackage.haskell.org/package/filepath-1.4.99.1/candidate), [1.4.99.2](https://hackage.haskell.org/package/filepath-1.4.99.2/candidate), [1.4.99.3](https://hackage.haskell.org/package/filepath-1.4.99.3/candidate), [1.4.99.5](https://hackage.haskell.org/package/filepath-1.4.99.5/candidate), [2.0.0.0](https://hackage.haskell.org/package/filepath-2.0.0.0/candidate), [2.0.0.1](https://hackage.haskell.org/package/filepath-2.0.0.1/candidate), [2.0.0.2](https://hackage.haskell.org/package/filepath-2.0.0.2/candidate), [2.0.0.3](https://hackage.haskell.org/package/filepath-2.0.0.3/candidate)

| Versions [[RSS](https://hackage.haskell.org/package/filepath.rss)] | [1.0](https://hackage.haskell.org/package/filepath-1.0), [1.1.0.0](https://hackage.haskell.org/package/filepath-1.1.0.0), [1.1.0.1](https://hackage.haskell.org/package/filepath-1.1.0.1), [1.1.0.2](https://hackage.haskell.org/package/filepath-1.1.0.2), [1.1.0.3](https://hackage.haskell.org/package/filepath-1.1.0.3), [1.1.0.4](https://hackage.haskell.org/package/filepath-1.1.0.4), [1.2.0.0](https://hackage.haskell.org/package/filepath-1.2.0.0), [1.2.0.1](https://hackage.haskell.org/package/filepath-1.2.0.1), [1.3.0.0](https://hackage.haskell.org/package/filepath-1.3.0.0), [1.3.0.1](https://hackage.haskell.org/package/filepath-1.3.0.1), [1.3.0.2](https://hackage.haskell.org/package/filepath-1.3.0.2), [1.4.0.0](https://hackage.haskell.org/package/filepath-1.4.0.0), [1.4.1.0](https://hackage.haskell.org/package/filepath-1.4.1.0), [1.4.1.1](https://hackage.haskell.org/package/filepath-1.4.1.1), [1.4.1.2](https://hackage.haskell.org/package/filepath-1.4.1.2), [1.4.2](https://hackage.haskell.org/package/filepath-1.4.2), [1.4.2.1](https://hackage.haskell.org/package/filepath-1.4.2.1), [1.4.2.2](https://hackage.haskell.org/package/filepath-1.4.2.2), [1.4.100.0](https://hackage.haskell.org/package/filepath-1.4.100.0), [1.4.100.1](https://hackage.haskell.org/package/filepath-1.4.100.1), [1.4.100.2](https://hackage.haskell.org/package/filepath-1.4.100.2), [1.4.100.3](https://hackage.haskell.org/package/filepath-1.4.100.3), [1.4.100.4](https://hackage.haskell.org/package/filepath-1.4.100.4), [1.4.101.0](https://hackage.haskell.org/package/filepath-1.4.101.0), [1.4.102.0](https://hackage.haskell.org/package/filepath-1.4.102.0), [1.4.200.0](https://hackage.haskell.org/package/filepath-1.4.200.0), [1.4.200.1](https://hackage.haskell.org/package/filepath-1.4.200.1), [1.4.300.1](https://hackage.haskell.org/package/filepath-1.4.300.1), [1.4.300.2](https://hackage.haskell.org/package/filepath-1.4.300.2), [1.4.301.0](https://hackage.haskell.org/package/filepath-1.4.301.0), [1.5.0.0](https://hackage.haskell.org/package/filepath-1.5.0.0), [1.5.2.0](https://hackage.haskell.org/package/filepath-1.5.2.0), [1.5.3.0](https://hackage.haskell.org/package/filepath-1.5.3.0), [1.5.4.0](https://hackage.haskell.org/package/filepath-1.5.4.0), **1.5.5.0** ([info](https://hackage.haskell.org/package/filepath/preferred)) |
| --- |
| Change log | [changelog.md](https://hackage.haskell.org/package/filepath-1.5.5.0/changelog) |
| Dependencies | [base](https://hackage.haskell.org/package/base) (>=4.12.0.0 &&<4.23), [bytestring](https://hackage.haskell.org/package/bytestring) (>=0.11.3.0), [deepseq](https://hackage.haskell.org/package/deepseq), [exceptions](https://hackage.haskell.org/package/exceptions), [os-string](https://hackage.haskell.org/package/os-string) (>=2.0.1), [template-haskell](https://hackage.haskell.org/package/template-haskell), [template-haskell-lift](https://hackage.haskell.org/package/template-haskell-lift) (>=0.1 &&<0.2), [template-haskell-quasiquoter](https://hackage.haskell.org/package/template-haskell-quasiquoter) (>=0.1 &&<0.2) [[details](https://hackage.haskell.org/package/filepath-1.5.5.0/dependencies)] |
| Tested with | ghc ==8.6.5 || ==8.8.4 || ==8.10.7 || ==9.0.2 || ==9.2.8 || ==9.4.8 || ==9.6.3 || ==9.8.1 |
| License | [BSD-3-Clause](https://hackage.haskell.org/package/filepath-1.5.5.0/src/LICENSE) |
| Copyright | Neil Mitchell 2005-2020, Julian Ospald 2021-2022 |
| Author | Neil Mitchell <ndmitchell@gmail.com> |
| Maintainer | Julian Ospald <hasufell@posteo.de> |
| Uploaded | by [maerwald](https://hackage.haskell.org/user/maerwald) at 2026-01-20T08:14:45Z |
| Category | [System](https://hackage.haskell.org/packages/#cat:System) |
| Home page | [https://github.com/haskell/filepath/blob/master/README.md](https://github.com/haskell/filepath/blob/master/README.md) |
| Bug tracker | [https://github.com/haskell/filepath/issues](https://github.com/haskell/filepath/issues) |
| Source repo | head: git clone [https://github.com/haskell/filepath](https://github.com/haskell/filepath) |
| Distributions | Arch:[1.4.300.1](https://archlinux.org/packages/extra/x86_64/ghc), Fedora:[1.5.4.0](https://src.fedoraproject.org/rpms/ghc) |
| Reverse Dependencies | 1870 direct, 13923 indirect [[details](https://hackage.haskell.org/package/filepath-1.5.5.0/)] |
| Downloads | 70001 total (112 in the last 30 days) |
| Rating | 2.25 (votes: 2) [estimated by [Bayesian average](https://en.wikipedia.org/wiki/Bayesian_average)] |
| Your Rating | * λ * λ * λ |
| Status | Docs available [[build log](https://hackage.haskell.org/package/filepath-1.5.5.0/reports/1)] Last success reported on 2026-01-20 [[all 1 reports](https://hackage.haskell.org/package/filepath-1.5.5.0/reports/)] |

* * *

Readme for filepath-1.5.5.0
---------------------------

[[back to package description](https://hackage.haskell.org/package/filepath-1.5.5.0/#description)]

The `filepath` package provides functionality for manipulating `FilePath` values, and is shipped with [GHC](https://www.haskell.org/ghc/). It provides two variants for filepaths:

1.   legacy filepaths: `type FilePath = String`
2.   operating system abstracted filepaths (`OsPath`): internally unpinned `ShortByteString` (platform-dependent encoding) 

It is recommended to use `OsPath` when possible, because it is more correct.

For each variant there are three main modules:

*   `System.FilePath.Posix` / `System.OsPath.Posix` manipulates POSIX/Linux style `FilePath` values (with `/` as the path separator). 
*   `System.FilePath.Windows` / `System.OsPath.Windows` manipulates Windows style `FilePath` values (with either `\` or `/` as the path separator, and deals with drives). 
*   `System.FilePath` / `System.OsPath` for dealing with current platform-specific filepaths 

All three modules provide the same API, and the same documentation (calling out differences in the different variants).

`System.OsString` is like `System.OsPath`, but more general purpose. Refer to the documentation of those modules for more information.

### What is a `FilePath`?

In Haskell, the legacy definition (used in `base` and Prelude) is `type FilePath = String`, where a Haskell `String` is a list of Unicode code points.

The new definition is (simplified) `newtype OsPath = AFP ShortByteString`, where `ShortByteString` is an unpinned byte array and follows syscall conventions, preserving the encoding.

On unix, filenames don't have a predefined encoding as per the [POSIX specification](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_170) and are passed as `char[]` to syscalls.

On windows (at least the API used by `Win32`) filepaths are UTF-16LE strings.

You are encouraged to use `OsPath` whenever possible, because it is more correct.

Also note that this is a low-level library and it makes no attempt at providing a more type safe variant for filepaths (e.g. by distinguishing between absolute and relative paths) and ensures no invariants (such as filepath validity).

For such libraries, check out the following:

*   [hpath](https://hackage.haskell.org/package/hpath)
*   [path](https://hackage.haskell.org/package/path)
*   [paths](https://hackage.haskell.org/package/paths)
*   [strong-path](https://hackage.haskell.org/package/strong-path)
