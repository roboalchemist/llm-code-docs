# Source: https://hackage.haskell.org/package/async

Title: async

URL Source: https://hackage.haskell.org/package/async

Markdown Content:
This package provides a higher-level interface over threads, in which an `Async a` is a concurrent thread that will eventually deliver a value of type `a`. The package provides ways to create `Async` computations, wait for their results, and cancel them.

Using `Async` is safer than using threads in two ways:

*   When waiting for a thread to return a result, if the thread dies with an exception then the caller must either re-throw the exception (`wait`) or handle it (`waitCatch`); the exception cannot be ignored.

*   The API makes it possible to build a tree of threads that are automatically killed when their parent dies (see `withAsync`).

[![Image 1](https://img.shields.io/static/v1?label=Build&message=InstallOk&color=success)](https://hackage.haskell.org/package/async-2.2.6/reports/1)![Image 2](https://img.shields.io/static/v1?label=Tests&message=Passed&color=success)![Image 3](https://img.shields.io/static/v1?label=Coverage&message=74%&color=brightgreen)![Image 4](https://img.shields.io/static/v1?label=Documentation&message=Available&color=success)

Modules
-------

[[Index](https://hackage.haskell.org/package/async-2.2.6/docs/doc-index.html)] [[Quick Jump](https://hackage.haskell.org/package/async-2.2.6/#)]

*   _Control_
    *   _Concurrent_
        *   [Control.Concurrent.Async](https://hackage.haskell.org/package/async-2.2.6/docs/Control-Concurrent-Async.html)
            *   [Control.Concurrent.Async.Internal](https://hackage.haskell.org/package/async-2.2.6/docs/Control-Concurrent-Async-Internal.html)
            *   [Control.Concurrent.Async.Warden](https://hackage.haskell.org/package/async-2.2.6/docs/Control-Concurrent-Async-Warden.html)

        *   [Control.Concurrent.Stream](https://hackage.haskell.org/package/async-2.2.6/docs/Control-Concurrent-Stream.html)

Flags
-----

### Manual Flags

| Name | Description | Default |
| --- | --- | --- |
| debug-auto-label | Strictly for debugging as it might have a non-negligible overhead. Enabling this flag will auto-label the threads spawned by `async`. Use it to find where are unlabelled threads spawned in your program (be it your code or dependency code). | Disabled |

Automatic Flags
| Name | Description | Default |
| --- | --- | --- |
| bench |  | Disabled |

Use -f <flag> to enable a flag, or -f -<flag> to disable that flag. [More info](https://cabal.readthedocs.io/en/latest/setup-commands.html#controlling-flag-assignments)

Downloads
---------

*   [async-2.2.6.tar.gz](https://hackage.haskell.org/package/async-2.2.6/async-2.2.6.tar.gz) [[browse](https://hackage.haskell.org/package/async-2.2.6/src/)] (Cabal source package)
*   [Package description](https://hackage.haskell.org/package/async-2.2.6/async.cabal) (as included in the package)

| Versions [[RSS](https://hackage.haskell.org/package/async.rss)] | [1.0](https://hackage.haskell.org/package/async-1.0), [1.1](https://hackage.haskell.org/package/async-1.1), [1.2](https://hackage.haskell.org/package/async-1.2), [1.3](https://hackage.haskell.org/package/async-1.3), [1.4](https://hackage.haskell.org/package/async-1.4), [2.0.0.0](https://hackage.haskell.org/package/async-2.0.0.0), [2.0.1.0](https://hackage.haskell.org/package/async-2.0.1.0), [2.0.1.1](https://hackage.haskell.org/package/async-2.0.1.1), [2.0.1.2](https://hackage.haskell.org/package/async-2.0.1.2), [2.0.1.3](https://hackage.haskell.org/package/async-2.0.1.3), [2.0.1.4](https://hackage.haskell.org/package/async-2.0.1.4), [2.0.1.5](https://hackage.haskell.org/package/async-2.0.1.5), [2.0.1.6](https://hackage.haskell.org/package/async-2.0.1.6), [2.0.2](https://hackage.haskell.org/package/async-2.0.2), [2.1.0](https://hackage.haskell.org/package/async-2.1.0), [2.1.1](https://hackage.haskell.org/package/async-2.1.1), [2.1.1.1](https://hackage.haskell.org/package/async-2.1.1.1), [2.2.1](https://hackage.haskell.org/package/async-2.2.1), [2.2.2](https://hackage.haskell.org/package/async-2.2.2), [2.2.3](https://hackage.haskell.org/package/async-2.2.3), [2.2.4](https://hackage.haskell.org/package/async-2.2.4), [2.2.5](https://hackage.haskell.org/package/async-2.2.5), **2.2.6** |
| --- |
| Change log | [changelog.md](https://hackage.haskell.org/package/async-2.2.6/changelog) |
| Dependencies | [async](https://hackage.haskell.org/package/async), [base](https://hackage.haskell.org/package/base) (>=4.3 &&<4.23), [hashable](https://hackage.haskell.org/package/hashable) (>=1.1.2.0 &&<1.6), [stm](https://hackage.haskell.org/package/stm) (>=2.2 &&<2.6), [unordered-containers](https://hackage.haskell.org/package/unordered-containers) (>=0.2 &&<0.3) [[details](https://hackage.haskell.org/package/async-2.2.6/dependencies)] |
| Tested with | ghc ==9.14.1, ghc ==9.12.2, ghc ==9.10.3, ghc ==9.8.4, ghc ==9.6.7, ghc ==9.4.8, ghc ==9.2.8, ghc ==9.0.2, ghc ==8.10.7, ghc ==8.8.4, ghc ==8.6.5, ghc ==8.4.4, ghc ==8.2.2, ghc ==8.0.2 |
| License | [BSD-3-Clause](https://hackage.haskell.org/package/async-2.2.6/src/LICENSE) |
| Copyright | (c) Simon Marlow 2012 |
| Author | Simon Marlow |
| Maintainer | Simon Marlow <marlowsd@gmail.com> |
| Uploaded | by [SimonMarlow](https://hackage.haskell.org/user/SimonMarlow) at 2026-01-07T11:26:16Z |
| Category | [Concurrency](https://hackage.haskell.org/packages/#cat:Concurrency) |
| Home page | [https://github.com/simonmar/async](https://github.com/simonmar/async) |
| Bug tracker | [https://github.com/simonmar/async/issues](https://github.com/simonmar/async/issues) |
| Source repo | head: git clone [https://github.com/simonmar/async.git](https://github.com/simonmar/async.git) |
| Distributions | Arch:[2.2.5](https://archlinux.org/packages/extra/x86_64/haskell-async), Debian:[2.2.2](http://packages.debian.org/source/bullseye/haskell-async), Fedora:[2.2.6](https://src.fedoraproject.org/rpms/ghc-async), FreeBSD:[2.0.2](http://www.freshports.org/devel/hs-async), LTSHaskell:[2.2.6](https://www.stackage.org/package/async), NixOS:[2.2.6](http://hydra.nixos.org/job/nixpkgs/trunk/haskellPackages.async.x86_64-linux), Stackage:[2.2.6](https://www.stackage.org/package/async), openSUSE:[2.2.5](https://build.opensuse.org/package/show/devel:languages:haskell/ghc-async) |
| Reverse Dependencies | 605 direct, 5187 indirect [[details](https://hackage.haskell.org/package/async-2.2.6/)] |
| Executables | race, conccancel, concasync |
| Downloads | 296356 total (99 in the last 30 days) |
| Rating | 2.75 (votes: 7) [estimated by [Bayesian average](https://en.wikipedia.org/wiki/Bayesian_average)] |
| Your Rating | * λ * λ * λ |
| Status | Docs available [[build log](https://hackage.haskell.org/package/async-2.2.6/reports/1)] Last success reported on 2026-01-07 [[all 1 reports](https://hackage.haskell.org/package/async-2.2.6/reports/)] |
