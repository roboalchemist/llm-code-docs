# Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Json.html

Title: Hadolint.Formatter.Json

URL Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Json.html

Markdown Content:
Hadolint.Formatter.Json
===============

hadolint
*   [Quick Jump](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Json.html#)
*   [Instances](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Json.html#)
*   [Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Json.html)
*   [Contents](https://hackage.haskell.org/package/hadolint-2.14.0)
*   [Index](https://hackage.haskell.org/package/hadolint-2.14.0/docs/doc-index.html)

| Safe Haskell | None |
| --- |
| Language | GHC2021 |

Hadolint.Formatter.Json

Documentation
=============

[printResults](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Json.html) :: ([VisualStream](https://hackage.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Stream.html#t:VisualStream "Text.Megaparsec.Stream") s, [TraversableStream](https://hackage.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Stream.html#t:TraversableStream "Text.Megaparsec.Stream") s, [ShowErrorComponent](https://hackage.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Error.html#t:ShowErrorComponent "Text.Megaparsec.Error") e, [Foldable](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Foldable "Distribution.Compat.Prelude") f) => f ([Result](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:Result "Hadolint.Formatter.Format") s e) ->[IO](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:IO "Distribution.Compat.Prelude") () [Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Json.html#printResults)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Json.html#v:printResults)

[formatResult](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Json.html) :: [Result](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:Result "Hadolint.Formatter.Format") s e ->[Seq](https://hackage.haskell.org/package/containers-0.7/docs/Data-Sequence.html#t:Seq "Data.Sequence") (JsonFormat s e) [Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Json.html#formatResult)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Json.html#v:formatResult)

Produced by [Haddock](http://www.haskell.org/haddock/) version 2.31.1

Linuwial

Expand All Instances Collapse All Instances

- [x] Collapse All Instances By Default

- [x] Remember Manually Collapsed/Expanded Instances 

You can find any exported type, constructor, class, function or pattern defined in this package by (approximate) name.

| Key | Shortcut |
| --- | --- |
| s | Open this search box |
| esc | Close this search box |
| ↓,ctrl + j | Move down in search results |
| ↑,ctrl + k | Move up in search results |
| ↵ | Go to active search result |
