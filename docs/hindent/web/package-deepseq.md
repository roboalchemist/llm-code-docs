# Source: https://hackage.haskell.org/package/deepseq

Title: deepseq

URL Source: https://hackage.haskell.org/package/deepseq

Markdown Content:
[deepseq](https://hackage.haskell.org/package/deepseq): Deep evaluation of data structures
------------------------------------------------------------------------------------------

This package provides methods for fully evaluating data structures ("deep evaluation"). Deep evaluation is often used for adding strictness to a program, e.g. in order to force pending exceptions, remove space leaks, or force lazy I/O to happen. It is also useful in parallel programs, to ensure pending work does not migrate to the wrong thread.

The primary use of this package is via the `deepseq` function, a "deep" version of `seq`. It is implemented on top of an `NFData` typeclass ("Normal Form Data", data structures with no unevaluated components) which defines strategies for fully evaluating different data types. See module documentation in [Control.DeepSeq](https://hackage.haskell.org/package/deepseq-1.5.2.0/docs/Control-DeepSeq.html) for more details.

[![Image 1](https://img.shields.io/static/v1?label=Build&message=InstallOk&color=success)](https://hackage.haskell.org/package/deepseq-1.5.2.0/reports/1)![Image 2](https://img.shields.io/static/v1?label=Tests&message=Passed&color=success)![Image 3](https://img.shields.io/static/v1?label=Coverage&message=7%&color=red)![Image 4](https://img.shields.io/static/v1?label=Documentation&message=Available&color=success)

Downloads
---------

*   [deepseq-1.5.2.0.tar.gz](https://hackage.haskell.org/package/deepseq-1.5.2.0/deepseq-1.5.2.0.tar.gz) [[browse](https://hackage.haskell.org/package/deepseq-1.5.2.0/src/)] (Cabal source package)
*   [Package description](https://hackage.haskell.org/package/deepseq-1.5.2.0/deepseq.cabal) (as included in the package)

| Versions [[RSS](https://hackage.haskell.org/package/deepseq.rss)] | [1.0.0.0](https://hackage.haskell.org/package/deepseq-1.0.0.0), [1.1.0.0](https://hackage.haskell.org/package/deepseq-1.1.0.0), [1.1.0.1](https://hackage.haskell.org/package/deepseq-1.1.0.1), [1.1.0.2](https://hackage.haskell.org/package/deepseq-1.1.0.2), [1.2.0.0](https://hackage.haskell.org/package/deepseq-1.2.0.0), [1.2.0.1](https://hackage.haskell.org/package/deepseq-1.2.0.1), [1.3.0.0](https://hackage.haskell.org/package/deepseq-1.3.0.0), [1.3.0.1](https://hackage.haskell.org/package/deepseq-1.3.0.1), [1.3.0.2](https://hackage.haskell.org/package/deepseq-1.3.0.2), [1.4.0.0](https://hackage.haskell.org/package/deepseq-1.4.0.0), [1.4.1.0](https://hackage.haskell.org/package/deepseq-1.4.1.0), [1.4.1.1](https://hackage.haskell.org/package/deepseq-1.4.1.1), [1.4.1.2](https://hackage.haskell.org/package/deepseq-1.4.1.2), [1.4.2.0](https://hackage.haskell.org/package/deepseq-1.4.2.0), [1.4.3.0](https://hackage.haskell.org/package/deepseq-1.4.3.0), [1.4.4.0](https://hackage.haskell.org/package/deepseq-1.4.4.0), [1.4.5.0](https://hackage.haskell.org/package/deepseq-1.4.5.0), [1.4.6.0](https://hackage.haskell.org/package/deepseq-1.4.6.0), [1.4.6.1](https://hackage.haskell.org/package/deepseq-1.4.6.1), [1.4.7.0](https://hackage.haskell.org/package/deepseq-1.4.7.0), [1.4.8.0](https://hackage.haskell.org/package/deepseq-1.4.8.0), [1.4.8.1](https://hackage.haskell.org/package/deepseq-1.4.8.1), [1.5.0.0](https://hackage.haskell.org/package/deepseq-1.5.0.0), [1.5.1.0](https://hackage.haskell.org/package/deepseq-1.5.1.0), **1.5.2.0**, [1.6.0.0](https://hackage.haskell.org/package/deepseq-1.6.0.0) ([info](https://hackage.haskell.org/package/deepseq/preferred)) |
| --- |
| Change log | [changelog.md](https://hackage.haskell.org/package/deepseq-1.5.2.0/changelog) |
| Dependencies | [base](https://hackage.haskell.org/package/base) (>=4.12 &&<4.23), [ghc-prim](https://hackage.haskell.org/package/ghc-prim) [[details](https://hackage.haskell.org/package/deepseq-1.5.2.0/dependencies)] |
| Tested with | ghc ==9.12.2, ghc ==9.10.2, ghc ==9.8.4, ghc ==9.6.6, ghc ==9.4.8, ghc ==9.2.8, ghc ==9.0.2, ghc ==8.10.7, ghc ==8.8.4, ghc ==8.6.5 |
| License | [BSD-3-Clause](https://hackage.haskell.org/package/deepseq-1.5.2.0/src/LICENSE) |
| Author |  |
| Maintainer | libraries@haskell.org |
| Uploaded | by [melaniebrown](https://hackage.haskell.org/user/melaniebrown) at 2025-06-14T22:25:04Z |
| Category | [Control](https://hackage.haskell.org/packages/#cat:Control) |
| Bug tracker | [https://github.com/haskell/deepseq/issues](https://github.com/haskell/deepseq/issues) |
| Source repo | head: git clone [https://github.com/haskell/deepseq.git](https://github.com/haskell/deepseq.git) |
| Distributions | Arch:[1.4.8.1](https://archlinux.org/packages/extra/x86_64/ghc), Fedora:[1.5.0.0](https://src.fedoraproject.org/rpms/ghc) |
| Reverse Dependencies | 1509 direct, 14284 indirect [[details](https://hackage.haskell.org/package/deepseq-1.5.2.0/)] |
| Downloads | 66613 total (119 in the last 30 days) |
| Rating | 2.5 (votes: 3) [estimated by [Bayesian average](https://en.wikipedia.org/wiki/Bayesian_average)] |
| Your Rating | * λ * λ * λ |
| Status | Docs available [[build log](https://hackage.haskell.org/package/deepseq-1.5.2.0/reports/1)] Last success reported on 2025-06-14 [[all 1 reports](https://hackage.haskell.org/package/deepseq-1.5.2.0/reports/)] |
