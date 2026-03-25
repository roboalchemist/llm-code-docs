# Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html

Title: Hadolint.Config.Configuration

URL Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html

Markdown Content:
Hadolint.Config.Configuration
===============

hadolint
*   [Quick Jump](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#)
*   [Instances](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#)
*   [Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html)
*   [Contents](https://hackage.haskell.org/package/hadolint-2.14.0)
*   [Index](https://hackage.haskell.org/package/hadolint-2.14.0/docs/doc-index.html)

| Safe Haskell | None |
| --- |
| Language | GHC2021 |

Hadolint.Config.Configuration

Documentation
=============

data[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#Configuration)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration)

Constructors

[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)
Fields

*   [noFail](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude") 
*   [noColor](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude") 
*   [verbose](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude") 
*   [format](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [OutputFormat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") 
*   [errorRules](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [[RuleCode](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] 
*   [warningRules](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [[RuleCode](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] 
*   [infoRules](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [[RuleCode](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] 
*   [styleRules](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [[RuleCode](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] 
*   [ignoreRules](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [[RuleCode](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] 
*   [allowedRegistries](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Set](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Set "Distribution.Compat.Prelude")[Registry](https://hackage.haskell.org/package/language-docker-15.0.0/docs/Language-Docker-Syntax.html#t:Registry "Language.Docker.Syntax") 
*   [labelSchema](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [LabelSchema](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelSchema "Hadolint.Rule") 
*   [strictLabels](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude") 
*   [disableIgnorePragma](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude") 
*   [failureThreshold](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [DLSeverity](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:DLSeverity "Hadolint.Rule")

#### Instances

Instances details
[Default](https://hackage.haskell.org/package/data-default-0.8.0.1/docs/Data-Default-Internal.html#t:Default "Data.Default.Internal")[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#line-44)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration)
Instance details
Defined in [Hadolint.Config.Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)

Methods

[def](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:def) :: [Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:def)
[Show](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Show "Distribution.Compat.Prelude")[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#line-42)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration)
Instance details
Defined in [Hadolint.Config.Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)

Methods

[showsPrec](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude") ->[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration") ->[ShowS](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:showsPrec)

[show](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:show) :: [Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration") ->[String](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:show)

[showList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:showList) :: [[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration")] ->[ShowS](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:showList)
[Eq](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Eq "Distribution.Compat.Prelude")[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#line-42)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration)
Instance details
Defined in [Hadolint.Config.Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)

Methods

[(==)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:-61--61-) :: [Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration") ->[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration") ->[Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:-47--61-) :: [Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration") ->[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration") ->[Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:-47--61-)
[Pretty](https://hackage.haskell.org/package/optparse-applicative-0.19.0.0/docs/Options-Applicative-Help-Pretty.html#t:Pretty "Options.Applicative.Help.Pretty")[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#line-81)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration)
Instance details
Defined in [Hadolint.Config.Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)

Methods

[pretty](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:pretty) :: [Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration") ->[Doc](https://hackage.haskell.org/package/prettyprinter-1.7.1/docs/Prettyprinter.html#t:Doc "Prettyprinter") ann [#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:pretty)

[prettyList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:prettyList) :: [[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration")] ->[Doc](https://hackage.haskell.org/package/prettyprinter-1.7.1/docs/Prettyprinter.html#t:Doc "Prettyprinter") ann [#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:prettyList)

data[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#PartialConfiguration)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration)

Constructors

[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)
Fields

*   [partialNoFail](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Maybe](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Maybe "Distribution.Compat.Prelude")[Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude") 
*   [partialNoColor](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Maybe](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Maybe "Distribution.Compat.Prelude")[Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude") 
*   [partialVerbose](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Maybe](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Maybe "Distribution.Compat.Prelude")[Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude") 
*   [partialFormat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Maybe](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Maybe "Distribution.Compat.Prelude")[OutputFormat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") 
*   [partialErrorRules](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [[RuleCode](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] 
*   [partialWarningRules](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [[RuleCode](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] 
*   [partialInfoRules](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [[RuleCode](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] 
*   [partialStyleRules](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [[RuleCode](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] 
*   [partialIgnoreRules](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [[RuleCode](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] 
*   [partialAllowedRegistries](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Set](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Set "Distribution.Compat.Prelude")[Registry](https://hackage.haskell.org/package/language-docker-15.0.0/docs/Language-Docker-Syntax.html#t:Registry "Language.Docker.Syntax") 
*   [partialLabelSchema](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [LabelSchema](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelSchema "Hadolint.Rule") 
*   [partialStrictLabels](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Maybe](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Maybe "Distribution.Compat.Prelude")[Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude") 
*   [partialDisableIgnorePragma](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Maybe](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Maybe "Distribution.Compat.Prelude")[Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude") 
*   [partialFailureThreshold](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Maybe](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Maybe "Distribution.Compat.Prelude")[DLSeverity](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:DLSeverity "Hadolint.Rule")

#### Instances

Instances details
[FromYAML](https://hackage.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:FromYAML "Data.YAML")[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#line-190)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration)
Instance details
Defined in [Hadolint.Config.Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)

Methods

[parseYAML](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:parseYAML) :: [Node](https://hackage.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:Node "Data.YAML")[Pos](https://hackage.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML-Event.html#t:Pos "Data.YAML.Event") ->[Parser](https://hackage.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:Parser "Data.YAML")[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:parseYAML)
[Default](https://hackage.haskell.org/package/data-default-0.8.0.1/docs/Data-Default-Internal.html#t:Default "Data.Default.Internal")[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#line-187)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration)
Instance details
Defined in [Hadolint.Config.Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)

Methods

[def](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:def) :: [PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:def)
[Monoid](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Semigroup.html#t:Monoid "Distribution.Compat.Semigroup")[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#line-169)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration)
Instance details
Defined in [Hadolint.Config.Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)

Methods

[mempty](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:mempty) :: [PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:mempty)

[mappend](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:mappend) :: [PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:mappend)

[mconcat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:mconcat) :: [[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")] ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:mconcat)
[Semigroup](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Semigroup.html#t:Semigroup "Distribution.Compat.Semigroup")[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#line-150)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration)
Instance details
Defined in [Hadolint.Config.Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)

Methods

[(<>)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:-60--62-) :: [PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:-60--62-)

[sconcat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:sconcat) :: [NonEmpty](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:NonEmpty "Distribution.Compat.Prelude")[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:sconcat)

[stimes](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:stimes) :: [Integral](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Integral "Distribution.Compat.Prelude") b => b ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:stimes)
[Show](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Show "Distribution.Compat.Prelude")[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#line-147)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration)
Instance details
Defined in [Hadolint.Config.Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)

Methods

[showsPrec](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude") ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[ShowS](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:showsPrec)

[show](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:show) :: [PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[String](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:show)

[showList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:showList) :: [[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")] ->[ShowS](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:showList)
[Eq](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Eq "Distribution.Compat.Prelude")[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#line-147)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration)
Instance details
Defined in [Hadolint.Config.Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html)

Methods

[(==)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:-61--61-) :: [PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:-47--61-) :: [PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[Bool](https://hackage.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:-47--61-)

[applyPartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html) :: [Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration") ->[PartialConfiguration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:PartialConfiguration "Hadolint.Config.Configuration") ->[Configuration](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#t:Configuration "Hadolint.Config.Configuration")[Source](https://hackage.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Config.Configuration.html#applyPartialConfiguration)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Config-Configuration.html#v:applyPartialConfiguration)

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
