# Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html

Title: Hadolint.Config.Commandline

URL Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html

Markdown Content:
Hadolint.Config.Commandline
===============

hadolint
*   [Quick Jump](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#)
*   [Instances](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#)
*   [Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Commandline.html)
*   [Contents](https://hackage.haskell.org/package/hadolint-2.14.0)
*   [Index](https://hackage.haskell.org/package/hadolint-2.14.0/docs/doc-index.html)

| Safe Haskell | None |
| --- |
| Language | GHC2021 |

Hadolint.Config.Commandline

Documentation
=============

data[CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html)[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Commandline.html#CommandlineConfig)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig)

Constructors

[CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html)
Fields

*   [showVersion](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html) :: [Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude") 
*   [configFile](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html) :: [Maybe](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Maybe "Distribution.Compat.Prelude")[FilePath](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:FilePath "Distribution.Compat.Prelude") 
*   [dockerfiles](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html) :: [[String](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")] 
*   [filePathInReportOption](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html) :: [Maybe](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Maybe "Distribution.Compat.Prelude")[FilePath](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:FilePath "Distribution.Compat.Prelude") 
*   [configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html) :: [PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")

#### Instances

Instances details
[Show](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Show "Distribution.Compat.Prelude")[CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig "Hadolint.Config.Commandline")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Commandline.html#line-49)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig)
Instance details
Defined in [Hadolint.Config.Commandline](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html)

Methods

[showsPrec](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude") ->[CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig "Hadolint.Config.Commandline") ->[ShowS](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#v:showsPrec)

[show](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#v:show) :: [CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig "Hadolint.Config.Commandline") ->[String](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#v:show)

[showList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#v:showList) :: [[CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig "Hadolint.Config.Commandline")] ->[ShowS](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#v:showList)
[Eq](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Eq "Distribution.Compat.Prelude")[CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig "Hadolint.Config.Commandline")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Commandline.html#line-49)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig)
Instance details
Defined in [Hadolint.Config.Commandline](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html)

Methods

[(==)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#v:-61--61-) :: [CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig "Hadolint.Config.Commandline") ->[CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig "Hadolint.Config.Commandline") ->[Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#v:-47--61-) :: [CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig "Hadolint.Config.Commandline") ->[CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig "Hadolint.Config.Commandline") ->[Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#v:-47--61-)

[parseCommandline](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html) :: [Parser](https://hackage.haskell.org/package/optparse-applicative-0.19.0.0/docs/Options-Applicative-Types.html#t:Parser "Options.Applicative.Types")[CommandlineConfig](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#t:CommandlineConfig "Hadolint.Config.Commandline")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Commandline.html#parseCommandline)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Commandline.html#v:parseCommandline)

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
