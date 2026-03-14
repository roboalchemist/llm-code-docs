# Source: https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html

Title: HIndent

URL Source: https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html

Markdown Content:
Contents

*   [The entry point.](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:1)
*   [Formatting functions.](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:2)
*   [Config](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:3)
*   [Extension](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:4)
*   [Error](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:5)
*   [Testing](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:6)

Description

Haskell indenter.

Synopsis
*   [hindent](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:hindent) :: [[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")] ->[IO](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:IO "Distribution.Compat.Prelude") ()
*   [reformat](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:reformat) :: [Config](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:Config "HIndent") -> [[Extension](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:Extension "HIndent")] ->[Maybe](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Maybe "Distribution.Compat.Prelude")[FilePath](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:FilePath "Distribution.Compat.Prelude") ->[ByteString](https://hackage-content.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Either "Distribution.Compat.Prelude")[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")[ByteString](https://hackage-content.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString")
*   data[Config](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:Config) = [Config](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:Config) {
    *   [configMaxColumns](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:configMaxColumns) :: ![Int64](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Int64 "Distribution.Compat.Prelude")
    *   [configIndentSpaces](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:configIndentSpaces) :: ![Int64](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Int64 "Distribution.Compat.Prelude")
    *   [configTrailingNewline](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:configTrailingNewline) :: ![Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")
    *   [configSortImports](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:configSortImports) :: ![Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")
    *   [configLineBreaks](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:configLineBreaks) :: [[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")]
    *   [configExtensions](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:configExtensions) :: [[Extension](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:Extension "HIndent")]

}
*   [defaultConfig](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:defaultConfig) :: [Config](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:Config "HIndent")
*   [getConfig](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:getConfig) :: [IO](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:IO "Distribution.Compat.Prelude")[Config](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:Config "HIndent")
*   data[Extension](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:Extension)
    *   = [EnableExtension](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:EnableExtension)[Extension](https://hackage-content.haskell.org/package/ghc-lib-parser-9.12.3.20251228/docs/GHC-Internal-LanguageExtensions.html#t:Extension "GHC.Internal.LanguageExtensions")
    *   | [DisableExtension](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:DisableExtension)[Extension](https://hackage-content.haskell.org/package/ghc-lib-parser-9.12.3.20251228/docs/GHC-Internal-LanguageExtensions.html#t:Extension "GHC.Internal.LanguageExtensions")

*   [defaultExtensions](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:defaultExtensions) :: [[Extension](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:Extension "HIndent")]
*   data[ParseError](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError) = [ParseError](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:ParseError) {
    *   [errorLine](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:errorLine) :: [Int](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude")
    *   [errorCol](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:errorCol) :: [Int](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude")
    *   [errorFile](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:errorFile) :: [FilePath](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:FilePath "Distribution.Compat.Prelude")

}
*   [prettyParseError](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:prettyParseError) :: [ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")
*   [testAst](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:testAst) :: [ByteString](https://hackage-content.haskell.org/package/bytestring-0.12.2.0/docs/Data-ByteString.html#t:ByteString "Data.ByteString") ->[Either](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Either "Distribution.Compat.Prelude")[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")[HsModule'](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:HsModule-39- "HIndent")
*   type[HsModule'](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:HsModule-39-) = [HsModule](https://hackage-content.haskell.org/package/ghc-lib-parser-9.12.3.20251228/docs/Language-Haskell-Syntax.html#t:HsModule "Language.Haskell.Syntax")[GhcPs](https://hackage-content.haskell.org/package/ghc-lib-parser-9.12.3.20251228/docs/GHC-Hs-Extension.html#t:GhcPs "GHC.Hs.Extension")

[The entry point. ----------------](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:1)[Formatting functions. ---------------------](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:2)[Config ------](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:3)[Extension ---------](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:4)

data[Extension](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html)[Source](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/src/HIndent.LanguageExtension.Types.html#Extension)[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:Extension)

Language Extension. Either enabled or disabled.

The `Cabal` package also has an `Extension` type that can be used to indicate whether an extension is enabled or disabled, but Cabal's one should be avoided as much as possible. The `KnownExtension` of `Cabal` may not have the latest extensions, and if such extensions are used, there will be cases where GHC can build, but HIndent cannot format.

Constructors

[Error -----](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:5)

data[ParseError](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html)[Source](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/src/HIndent.Error.html#ParseError)[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError)

Parse error type with the location.

#### Instances

Instances details
[Read](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Read "Distribution.Compat.Prelude")[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")[Source](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/src/HIndent.Error.html#line-14)[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError)
Instance details
Defined in [HIndent.Error](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent-Error.html)

Methods

[readsPrec](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:readsPrec) :: [Int](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude") ->[ReadS](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:ReadS "Distribution.Compat.Prelude")[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:readList) :: [ReadS](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:ReadS "Distribution.Compat.Prelude") [[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")] [#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:readList)

[readPrec](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:readPrec) :: [ReadPrec](https://hackage-content.haskell.org/package/base-4.21.0.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:readListPrec) :: [ReadPrec](https://hackage-content.haskell.org/package/base-4.21.0.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")] [#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:readListPrec)
[Show](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Show "Distribution.Compat.Prelude")[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")[Source](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/src/HIndent.Error.html#line-14)[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError)
Instance details
Defined in [HIndent.Error](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent-Error.html)

Methods

[showsPrec](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:showsPrec) :: [Int](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Int "Distribution.Compat.Prelude") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:showsPrec)

[show](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:show) :: [ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[String](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:String "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:show)

[showList](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:showList) :: [[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")] ->[ShowS](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:ShowS "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:showList)
[Eq](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Eq "Distribution.Compat.Prelude")[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")[Source](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/src/HIndent.Error.html#line-14)[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError)
Instance details
Defined in [HIndent.Error](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent-Error.html)

Methods

[(==)](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-61--61-) :: [ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-47--61-) :: [ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-47--61-)
[Ord](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Ord "Distribution.Compat.Prelude")[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")[Source](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/src/HIndent.Error.html#line-14)[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError)
Instance details
Defined in [HIndent.Error](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent-Error.html)

Methods

[compare](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:compare) :: [ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[Ordering](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Ordering "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:compare)

[(<)](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-60-) :: [ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-60-)

[(<=)](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-60--61-) :: [ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-60--61-)

[(>)](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-62-) :: [ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-62-)

[(>=)](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-62--61-) :: [ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[Bool](https://hackage-content.haskell.org/package/Cabal-syntax-3.14.1.0/docs/Distribution-Compat-Prelude.html#t:Bool "Distribution.Compat.Prelude")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:-62--61-)

[max](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:max) :: [ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:max)

[min](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:min) :: [ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent") ->[ParseError](https://hackage-content.haskell.org/package/hindent-6.3.0/docs/HIndent.html#t:ParseError "HIndent")[#](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#v:min)

[Testing -------](https://hackage.haskell.org/package/hindent-6.3.0/docs/HIndent.html#g:6)
