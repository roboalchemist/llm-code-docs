# Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html

Title: Hadolint.Rule

URL Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html

Markdown Content:
Documentation
-------------

[(|>)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html) :: a -> (a -> b) -> b infixl 0[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#%7C%3E)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-124--62-)

newtype[RuleCode](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#RuleCode)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode)

Constructors

#### Instances

Instances details
[IsString](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:IsString "Distribution.Compat.Prelude")[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-81)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[fromString](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:fromString) :: [String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:fromString)
[Show](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Show "Distribution.Compat.Prelude")[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-78)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[showsPrec](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showsPrec) :: [Int](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showsPrec)

[show](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:show) :: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:show)

[showList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showList) :: [[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showList)
[Eq](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Eq "Distribution.Compat.Prelude")[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-76)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[(==)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-61--61-) :: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-47--61-) :: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-47--61-)
[Ord](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Ord "Distribution.Compat.Prelude")[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-76)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[compare](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:compare) :: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[Ordering](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Ordering "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:compare)

[(<)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-60-) :: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-60-)

[(<=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-60--61-) :: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-60--61-)

[(>)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-62-) :: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-62-)

[(>=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-62--61-) :: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-62--61-)

[max](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:max) :: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:max)

[min](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:min) :: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:min)
[Pretty](https://hackage-content.haskell.org/package/optparse-applicative-0.19.0.0/docs/Options-Applicative-Help-Pretty.html#t:Pretty "Options.Applicative.Help.Pretty")[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-84)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[pretty](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:pretty) :: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule") ->[Doc](https://hackage-content.haskell.org/package/prettyprinter-1.7.1/docs/Prettyprinter.html#t:Doc "Prettyprinter") ann [#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:pretty)

[prettyList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:prettyList) :: [[RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")] ->[Doc](https://hackage-content.haskell.org/package/prettyprinter-1.7.1/docs/Prettyprinter.html#t:Doc "Prettyprinter") ann [#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:prettyList)

data[CheckFailure](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#CheckFailure)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure)

Constructors

#### Instances

Instances details
[Show](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Show "Distribution.Compat.Prelude")[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-94)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[showsPrec](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showsPrec) :: [Int](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showsPrec)

[show](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:show) :: [CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:show)

[showList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showList) :: [[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule")] ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showList)
[Eq](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Eq "Distribution.Compat.Prelude")[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-94)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[(==)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-61--61-) :: [CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-47--61-) :: [CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-47--61-)
[Ord](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Ord "Distribution.Compat.Prelude")[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-96)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[compare](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:compare) :: [CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[Ordering](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Ordering "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:compare)

[(<)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-60-) :: [CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-60-)

[(<=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-60--61-) :: [CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-60--61-)

[(>)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-62-) :: [CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-62-)

[(>=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-62--61-) :: [CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-62--61-)

[max](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:max) :: [CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:max)

[min](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:min) :: [CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule") ->[CheckFailure](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:CheckFailure "Hadolint.Rule")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:min)

data[LabelType](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#LabelType)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType)

Constructors

[Email](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)
[GitHash](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)
[RawText](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)
[Rfc3339](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)
[SemVer](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)
[Spdx](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)
[Url](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

#### Instances

Instances details
[FromYAML](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:FromYAML "Data.YAML")[LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-133)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[parseYAML](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:parseYAML) :: [Node](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:Node "Data.YAML")[Pos](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML-Event.html#t:Pos "Data.YAML.Event") ->[Parser](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:Parser "Data.YAML")[LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:parseYAML)
[Show](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Show "Distribution.Compat.Prelude")[LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-120)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[showsPrec](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showsPrec) :: [Int](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude") ->[LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule") ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showsPrec)

[show](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:show) :: [LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule") ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:show)

[showList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showList) :: [[LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule")] ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:showList)
[Eq](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Eq "Distribution.Compat.Prelude")[LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-120)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[(==)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-61--61-) :: [LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule") ->[LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-47--61-) :: [LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule") ->[LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:-47--61-)
[Pretty](https://hackage-content.haskell.org/package/optparse-applicative-0.19.0.0/docs/Options-Applicative-Help-Pretty.html#t:Pretty "Options.Applicative.Help.Pretty")[LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#line-143)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType)
Instance details
Defined in [Hadolint.Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)

Methods

[pretty](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:pretty) :: [LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule") ->[Doc](https://hackage-content.haskell.org/package/prettyprinter-1.7.1/docs/Prettyprinter.html#t:Doc "Prettyprinter") ann [#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:pretty)

[prettyList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:prettyList) :: [[LabelType](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:LabelType "Hadolint.Rule")] ->[Doc](https://hackage-content.haskell.org/package/prettyprinter-1.7.1/docs/Prettyprinter.html#t:Doc "Prettyprinter") ann [#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:prettyList)

[simpleRule](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#simpleRule)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:simpleRule)

Arguments

:: [RuleCode](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:RuleCode "Hadolint.Rule")rule code
->[DLSeverity](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:DLSeverity "Hadolint.Rule")severity for the rule
->[Text](https://hackage-content.haskell.org/package/foldl-1.4.18/docs/Control-Foldl-Text.html#t:Text "Control.Foldl.Text")failure message for the rule
-> ([Instruction](https://hackage-content.haskell.org/package/language-docker-15.0.0/docs/Language-Docker-Syntax.html#t:Instruction "Language.Docker.Syntax") args ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude"))step calculation for the rule. Returns True or False for each line in the dockerfile depending on its validity.
->[Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:Rule "Hadolint.Rule") args

A simple rule that can be implemented in terms of returning True or False for each instruction If you need to calculate some state to decide upon past information, use `customRule`

[customRule](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html) :: ([Linenumber](https://hackage-content.haskell.org/package/language-docker-15.0.0/docs/Language-Docker-Syntax.html#t:Linenumber "Language.Docker.Syntax") ->[State](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:State "Hadolint.Rule") a ->[Instruction](https://hackage-content.haskell.org/package/language-docker-15.0.0/docs/Language-Docker-Syntax.html#t:Instruction "Language.Docker.Syntax") args ->[State](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:State "Hadolint.Rule") a) ->[State](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:State "Hadolint.Rule") a ->[Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:Rule "Hadolint.Rule") args [Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#customRule)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:customRule)

A rule that accumulates a State a. The state contains the collection of failed lines and a custom data type that can be used to track properties for the rule. Each step always returns the new State, which offers the ability to both accumulate properties and mark failures for every given instruction.

[veryCustomRule](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html)[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#veryCustomRule)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:veryCustomRule)

Arguments

:: ([Linenumber](https://hackage-content.haskell.org/package/language-docker-15.0.0/docs/Language-Docker-Syntax.html#t:Linenumber "Language.Docker.Syntax") ->[State](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:State "Hadolint.Rule") a ->[Instruction](https://hackage-content.haskell.org/package/language-docker-15.0.0/docs/Language-Docker-Syntax.html#t:Instruction "Language.Docker.Syntax") args ->[State](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:State "Hadolint.Rule") a)step calculation for the rule. Called for each instruction in the docker file it must return the state after being modified by the rule
->[State](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:State "Hadolint.Rule") a initial state
-> ([State](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:State "Hadolint.Rule") a ->[Failures](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:Failures "Hadolint.Rule"))done callaback. It is passed the final accumulated state and it should return all failures found by the rule
->[Rule](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:Rule "Hadolint.Rule") args

Similarly to `customRule`, it returns a State a for each step, but it has the ability to run a done callback as the last step of the rule. The done callback can be used to transform the state and mark failures for any arbitrary line in the input. This helper is meant for rules that need to do lookahead. Instead of looking ahead, the state should store the facts and make a decision about them once the input is finished.

[aliasMustBe](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html) :: ([Text](https://hackage-content.haskell.org/package/foldl-1.4.18/docs/Control-Foldl-Text.html#t:Text "Control.Foldl.Text") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")) ->[Instruction](https://hackage-content.haskell.org/package/language-docker-15.0.0/docs/Language-Docker-Syntax.html#t:Instruction "Language.Docker.Syntax") a ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Rule.html#aliasMustBe)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#v:aliasMustBe)

Returns the result of running the check function on the image alias name, if the passed instruction is a FROM instruction with a stage alias. Otherwise, returns True.
