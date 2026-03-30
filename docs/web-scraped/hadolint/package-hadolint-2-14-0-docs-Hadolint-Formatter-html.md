# Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html

Title: Hadolint.Formatter

URL Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html

Markdown Content:
Documentation
-------------

data[OutputFormat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html)[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#OutputFormat)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat)

Constructors

[Json](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html)
[SonarQube](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html)
[TTY](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html)
[CodeclimateJson](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html)
[GitLabCodeclimateJson](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html)
[Gnu](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html)
[Checkstyle](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html)
[Codacy](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html)
[Sarif](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html)

#### Instances

Instances details
[FromYAML](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:FromYAML "Data.YAML")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-59)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[parseYAML](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:parseYAML) :: [Node](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:Node "Data.YAML")[Pos](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML-Event.html#t:Pos "Data.YAML.Event") ->[Parser](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:Parser "Data.YAML")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:parseYAML)
[Default](https://hackage-content.haskell.org/package/data-default-0.8.0.1/docs/Data-Default-Internal.html#t:Default "Data.Default.Internal")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-72)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[def](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:def) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:def)
[Monoid](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Semigroup.html#t:Monoid "Distribution.Compat.Semigroup")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-56)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[mempty](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:mempty) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:mempty)

[mappend](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:mappend) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:mappend)

[mconcat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:mconcat) :: [[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")] ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:mconcat)
[Semigroup](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Semigroup.html#t:Semigroup "Distribution.Compat.Semigroup")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-53)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[(<>)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:-60--62-) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:-60--62-)

[sconcat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:sconcat) :: [NonEmpty](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:NonEmpty "Distribution.Compat.Prelude")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:sconcat)

[stimes](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:stimes) :: [Integral](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Integral "Distribution.Compat.Prelude") b => b ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:stimes)
[Show](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Show "Distribution.Compat.Prelude")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-40)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[showsPrec](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:showsPrec) :: [Int](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:showsPrec)

[show](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:show) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:show)

[showList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:showList) :: [[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")] ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:showList)
[Eq](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Eq "Distribution.Compat.Prelude")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-40)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[(==)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:-61--61-) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:-47--61-) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:-47--61-)
[Pretty](https://hackage-content.haskell.org/package/optparse-applicative-0.19.0.0/docs/Options-Applicative-Help-Pretty.html#t:Pretty "Options.Applicative.Help.Pretty")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-42)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[pretty](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:pretty) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter") ->[Doc](https://hackage-content.haskell.org/package/prettyprinter-1.7.1/docs/Prettyprinter.html#t:Doc "Prettyprinter") ann [#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:pretty)

[prettyList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:prettyList) :: [[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#t:OutputFormat "Hadolint.Formatter")] ->[Doc](https://hackage-content.haskell.org/package/prettyprinter-1.7.1/docs/Prettyprinter.html#t:Doc "Prettyprinter") ann [#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter.html#v:prettyList)
