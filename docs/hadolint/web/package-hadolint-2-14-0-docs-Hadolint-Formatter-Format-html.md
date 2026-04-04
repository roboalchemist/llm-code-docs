# Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html

Title: Hadolint.Formatter.Format

URL Source: https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html

Markdown Content:
Synopsis
*   data[OutputFormat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat)
    *   = [Json](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:Json)
    *   | [SonarQube](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:SonarQube)
    *   | [TTY](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:TTY)
    *   | [CodeclimateJson](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:CodeclimateJson)
    *   | [GitLabCodeclimateJson](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:GitLabCodeclimateJson)
    *   | [Gnu](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:Gnu)
    *   | [Checkstyle](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:Checkstyle)
    *   | [Codacy](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:Codacy)
    *   | [Sarif](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:Sarif)

*   data[Result](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:Result) s e = [Result](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:Result) {
    *   [fileName](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:fileName) :: [Text](https://hackage-content.haskell.org/package/foldl-1.4.18/docs/Control-Foldl-Text.html#t:Text "Control.Foldl.Text")
    *   [errors](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:errors) :: [Seq](https://hackage-content.haskell.org/package/containers-0.7/docs/Data-Sequence.html#t:Seq "Data.Sequence") ([ParseErrorBundle](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Error.html#t:ParseErrorBundle "Text.Megaparsec.Error") s e)
    *   [checks](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:checks) :: [Failures](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:Failures "Hadolint.Rule")

}
*   [errorBundlePretty](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:errorBundlePretty) :: ([VisualStream](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Stream.html#t:VisualStream "Text.Megaparsec.Stream") s, [TraversableStream](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Stream.html#t:TraversableStream "Text.Megaparsec.Stream") s, [ShowErrorComponent](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Error.html#t:ShowErrorComponent "Text.Megaparsec.Error") e) =>[ParseErrorBundle](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Error.html#t:ParseErrorBundle "Text.Megaparsec.Error") s e ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")
*   [errorMessage](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:errorMessage) :: ([VisualStream](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Stream.html#t:VisualStream "Text.Megaparsec.Stream") s, [ShowErrorComponent](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Error.html#t:ShowErrorComponent "Text.Megaparsec.Error") e) =>[ParseErrorBundle](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Error.html#t:ParseErrorBundle "Text.Megaparsec.Error") s e ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")
*   [errorMessageLine](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:errorMessageLine) :: ([VisualStream](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Stream.html#t:VisualStream "Text.Megaparsec.Stream") s, [TraversableStream](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Stream.html#t:TraversableStream "Text.Megaparsec.Stream") s, [ShowErrorComponent](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Error.html#t:ShowErrorComponent "Text.Megaparsec.Error") e) =>[ParseErrorBundle](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Error.html#t:ParseErrorBundle "Text.Megaparsec.Error") s e ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")
*   [errorPosition](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:errorPosition) :: [TraversableStream](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Stream.html#t:TraversableStream "Text.Megaparsec.Stream") s =>[ParseErrorBundle](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Error.html#t:ParseErrorBundle "Text.Megaparsec.Error") s e ->[SourcePos](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Pos.html#t:SourcePos "Text.Megaparsec.Pos")
*   [errorPositionPretty](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:errorPositionPretty) :: [TraversableStream](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Stream.html#t:TraversableStream "Text.Megaparsec.Stream") s =>[ParseErrorBundle](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Error.html#t:ParseErrorBundle "Text.Megaparsec.Error") s e ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")
*   [severityText](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:severityText) :: [DLSeverity](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:DLSeverity "Hadolint.Rule") ->[Text](https://hackage-content.haskell.org/package/foldl-1.4.18/docs/Control-Foldl-Text.html#t:Text "Control.Foldl.Text")
*   [stripNewlines](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:stripNewlines) :: [String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude") ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")
*   [readMaybeOutputFormat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:readMaybeOutputFormat) :: [Text](https://hackage-content.haskell.org/package/foldl-1.4.18/docs/Control-Foldl-Text.html#t:Text "Control.Foldl.Text") ->[Maybe](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Maybe "Distribution.Compat.Prelude")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")
*   [toResult](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:toResult) :: [Text](https://hackage-content.haskell.org/package/foldl-1.4.18/docs/Control-Foldl-Text.html#t:Text "Control.Foldl.Text") ->[Either](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Either "Distribution.Compat.Prelude") ([ParseErrorBundle](https://hackage-content.haskell.org/package/megaparsec-9.7.0/docs/Text-Megaparsec-Error.html#t:ParseErrorBundle "Text.Megaparsec.Error") s e) [Failures](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Rule.html#t:Failures "Hadolint.Rule") ->[Result](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:Result "Hadolint.Formatter.Format") s e

Documentation
-------------

data[OutputFormat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#OutputFormat)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat)

Constructors

[Json](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)
[SonarQube](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)
[TTY](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)
[CodeclimateJson](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)
[GitLabCodeclimateJson](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)
[Gnu](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)
[Checkstyle](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)
[Codacy](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)
[Sarif](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

#### Instances

Instances details
[FromYAML](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:FromYAML "Data.YAML")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-59)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[parseYAML](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:parseYAML) :: [Node](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:Node "Data.YAML")[Pos](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML-Event.html#t:Pos "Data.YAML.Event") ->[Parser](https://hackage-content.haskell.org/package/HsYAML-0.2.1.5/docs/Data-YAML.html#t:Parser "Data.YAML")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:parseYAML)
[Default](https://hackage-content.haskell.org/package/data-default-0.8.0.1/docs/Data-Default-Internal.html#t:Default "Data.Default.Internal")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-72)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[def](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:def) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:def)
[Monoid](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Semigroup.html#t:Monoid "Distribution.Compat.Semigroup")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-56)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[mempty](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:mempty) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:mempty)

[mappend](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:mappend) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:mappend)

[mconcat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:mconcat) :: [[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")] ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:mconcat)
[Semigroup](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Semigroup.html#t:Semigroup "Distribution.Compat.Semigroup")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-53)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[(<>)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:-60--62-) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:-60--62-)

[sconcat](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:sconcat) :: [NonEmpty](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:NonEmpty "Distribution.Compat.Prelude")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:sconcat)

[stimes](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:stimes) :: [Integral](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Integral "Distribution.Compat.Prelude") b => b ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:stimes)
[Show](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Show "Distribution.Compat.Prelude")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-40)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[showsPrec](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:showsPrec) :: [Int](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:showsPrec)

[show](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:show) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:show)

[showList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:showList) :: [[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")] ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:showList)
[Eq](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Eq "Distribution.Compat.Prelude")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-40)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[(==)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:-61--61-) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:-47--61-) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.12.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:-47--61-)
[Pretty](https://hackage-content.haskell.org/package/optparse-applicative-0.19.0.0/docs/Options-Applicative-Help-Pretty.html#t:Pretty "Options.Applicative.Help.Pretty")[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")[Source](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/src/Hadolint.Formatter.Format.html#line-42)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat)
Instance details
Defined in [Hadolint.Formatter.Format](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)

Methods

[pretty](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:pretty) :: [OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format") ->[Doc](https://hackage-content.haskell.org/package/prettyprinter-1.7.1/docs/Prettyprinter.html#t:Doc "Prettyprinter") ann [#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:pretty)

[prettyList](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:prettyList) :: [[OutputFormat](https://hackage-content.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#t:OutputFormat "Hadolint.Formatter.Format")] ->[Doc](https://hackage-content.haskell.org/package/prettyprinter-1.7.1/docs/Prettyprinter.html#t:Doc "Prettyprinter") ann [#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:prettyList)

[errorBundlePretty](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html)[#](https://hackage.haskell.org/package/hadolint-2.14.0/docs/Hadolint-Formatter-Format.html#v:errorBundlePretty)

Arguments

Pretty-print a `ParseErrorBundle`. All `ParseError`s in the bundle will be pretty-printed in order together with the corresponding offending lines by doing a single pass over the input stream. The rendered `String` always ends with a newline.

_Since: megaparsec-7.0.0_
