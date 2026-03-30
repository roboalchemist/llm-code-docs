# Module: RuboCop::Cop::AutoCorrector
  
    Included in:
    Bundler::InsecureProtocolSource, Bundler::OrderedGems, Gemspec::AddRuntimeDependency, Gemspec::DeprecatedAttributeAssignment, Gemspec::OrderedDependencies, Gemspec::RequireMFA, InternalAffairs::CopDescription, InternalAffairs::CopEnabled, InternalAffairs::CreateEmptyFile, InternalAffairs::EmptyLineBetweenExpectOffenseAndCorrection, InternalAffairs::ExampleDescription, InternalAffairs::ExampleHeredocDelimiter, InternalAffairs::LambdaOrProc, InternalAffairs::LocationExists, InternalAffairs::LocationExpression, InternalAffairs::LocationLineEqualityComparison, InternalAffairs::MethodNameEndWith, InternalAffairs::MethodNameEqual, InternalAffairs::NodeFirstOrLastArgument, InternalAffairs::NodeMatcherDirective, InternalAffairs::NodePatternGroups, InternalAffairs::NodeTypeGroup, InternalAffairs::NodeTypeMultiplePredicates, InternalAffairs::NodeTypePredicate, InternalAffairs::OffenseLocationKeyword, InternalAffairs::OperatorKeyword, InternalAffairs::ProcessedSourceBufferName, InternalAffairs::RedundantContextConfigParameter, InternalAffairs::RedundantDescribedClassAsSubject, InternalAffairs::RedundantExpectOffenseArguments, InternalAffairs::RedundantLetRuboCopConfigNew, InternalAffairs::RedundantLocationArgument, InternalAffairs::RedundantMessageArgument, InternalAffairs::RedundantMethodDispatchNode, InternalAffairs::RedundantSourceRange, InternalAffairs::SingleLineComparison, InternalAffairs::UselessRestrictOnSend, Layout::AccessModifierIndentation, Layout::ArgumentAlignment, Layout::ArrayAlignment, Layout::AssignmentIndentation, Layout::BeginEndAlignment, Layout::BlockAlignment, Layout::BlockEndNewline, Layout::CaseIndentation, Layout::ClassStructure, Layout::ClosingHeredocIndentation, Layout::ClosingParenthesisIndentation, Layout::CommentIndentation, Layout::ConditionPosition, Layout::DefEndAlignment, Layout::DotPosition, Layout::ElseAlignment, Layout::EmptyComment, Layout::EmptyLineAfterGuardClause, Layout::EmptyLineAfterMagicComment, Layout::EmptyLineAfterMultilineCondition, Layout::EmptyLineBetweenDefs, Layout::EmptyLines, Layout::EmptyLinesAfterModuleInclusion, Layout::EmptyLinesAroundAccessModifier, Layout::EmptyLinesAroundArguments, Layout::EmptyLinesAroundAttributeAccessor, Layout::EmptyLinesAroundBeginBody, Layout::EmptyLinesAroundBlockBody, Layout::EmptyLinesAroundClassBody, Layout::EmptyLinesAroundExceptionHandlingKeywords, Layout::EmptyLinesAroundMethodBody, Layout::EmptyLinesAroundModuleBody, Layout::EndAlignment, Layout::ExtraSpacing, Layout::FirstArgumentIndentation, Layout::FirstArrayElementIndentation, Layout::FirstArrayElementLineBreak, Layout::FirstHashElementIndentation, Layout::FirstHashElementLineBreak, Layout::FirstMethodArgumentLineBreak, Layout::FirstMethodParameterLineBreak, Layout::FirstParameterIndentation, Layout::HashAlignment, Layout::HeredocArgumentClosingParenthesis, Layout::HeredocIndentation, Layout::IndentationConsistency, Layout::IndentationStyle, Layout::IndentationWidth, Layout::InitialIndentation, Layout::LeadingCommentSpace, Layout::LeadingEmptyLines, Layout::LineContinuationLeadingSpace, Layout::LineContinuationSpacing, Layout::LineEndStringConcatenationIndentation, Layout::LineLength, Layout::MultilineArrayBraceLayout, Layout::MultilineArrayLineBreaks, Layout::MultilineAssignmentLayout, Layout::MultilineBlockLayout, Layout::MultilineHashBraceLayout, Layout::MultilineHashKeyLineBreaks, Layout::MultilineMethodArgumentLineBreaks, Layout::MultilineMethodCallBraceLayout, Layout::MultilineMethodCallIndentation, Layout::MultilineMethodDefinitionBraceLayout, Layout::MultilineMethodParameterLineBreaks, Layout::MultilineOperationIndentation, Layout::ParameterAlignment, Layout::RedundantLineBreak, Layout::RescueEnsureAlignment, Layout::SingleLineBlockChain, Layout::SpaceAfterColon, Layout::SpaceAfterComma, Layout::SpaceAfterMethodName, Layout::SpaceAfterNot, Layout::SpaceAfterSemicolon, Layout::SpaceAroundBlockParameters, Layout::SpaceAroundEqualsInParameterDefault, Layout::SpaceAroundKeyword, Layout::SpaceAroundMethodCallOperator, Layout::SpaceAroundOperators, Layout::SpaceBeforeBlockBraces, Layout::SpaceBeforeBrackets, Layout::SpaceBeforeComma, Layout::SpaceBeforeComment, Layout::SpaceBeforeFirstArg, Layout::SpaceBeforeSemicolon, Layout::SpaceInLambdaLiteral, Layout::SpaceInsideArrayLiteralBrackets, Layout::SpaceInsideArrayPercentLiteral, Layout::SpaceInsideBlockBraces, Layout::SpaceInsideHashLiteralBraces, Layout::SpaceInsideParens, Layout::SpaceInsidePercentLiteralDelimiters, Layout::SpaceInsideRangeLiteral, Layout::SpaceInsideReferenceBrackets, Layout::SpaceInsideStringInterpolation, Layout::TrailingEmptyLines, Layout::TrailingWhitespace, Lint::AmbiguousBlockAssociation, Lint::AmbiguousOperator, Lint::AmbiguousOperatorPrecedence, Lint::AmbiguousRange, Lint::AmbiguousRegexpLiteral, Lint::ArrayLiteralInRegexp, Lint::AssignmentInCondition, Lint::BigDecimalNew, Lint::BooleanSymbol, Lint::ConstantOverwrittenInRescue, Lint::DeprecatedClassMethods, Lint::DeprecatedConstants, Lint::DeprecatedOpenSSLConstant, Lint::DisjunctiveAssignmentInConstructor, Lint::DuplicateMagicComment, Lint::DuplicateRegexpCharacterClassElement, Lint::DuplicateRequire, Lint::DuplicateSetElement, Lint::ElseLayout, Lint::EmptyConditionalBody, Lint::EmptyEnsure, Lint::EmptyInterpolation, Lint::ErbNewArguments, Lint::HashNewWithKeywordArgumentsAsDefault, Lint::HeredocMethodCallPosition, Lint::IdentityComparison, Lint::ImplicitStringConcatenation, Lint::IncompatibleIoSelectWithFiberScheduler, Lint::InheritException, Lint::InterpolationCheck, Lint::LambdaWithoutLiteralBlock, Lint::LiteralAsCondition, Lint::LiteralInInterpolation, Lint::Loop, Lint::MixedCaseRange, Lint::MultipleComparison, Lint::NonAtomicFileOperation, Lint::NonDeterministicRequireOrder, Lint::NumberConversion, Lint::NumericOperationWithConstantResult, Lint::OrAssignmentToConstant, Lint::OrderedMagicComments, Lint::ParenthesesAsGroupedExpression, Lint::PercentStringArray, Lint::PercentSymbolArray, Lint::RaiseException, Lint::RedundantCopDisableDirective, Lint::RedundantCopEnableDirective, Lint::RedundantDirGlobSort, Lint::RedundantRegexpQuantifiers, Lint::RedundantRequireStatement, Lint::RedundantSafeNavigation, Lint::RedundantSplatExpansion, Lint::RedundantStringCoercion, Lint::RedundantTypeConversion, Lint::RedundantWithIndex, Lint::RedundantWithObject, Lint::RegexpAsCondition, Lint::RequireRelativeSelfPath, Lint::RescueType, Lint::SafeNavigationChain, Lint::SafeNavigationConsistency, Lint::SafeNavigationWithEmpty, Lint::ScriptPermission, Lint::SendWithMixinArgument, Lint::SuppressedExceptionInNumberConversion, Lint::SymbolConversion, Lint::ToJSON, Lint::TopLevelReturnWithArgument, Lint::TrailingCommaInAttributeDeclaration, Lint::TripleQuotes, Lint::UnescapedBracketInRegexp, Lint::UnifiedInteger, Lint::UnusedBlockArgument, Lint::UnusedMethodArgument, Lint::UriRegexp, Lint::UselessAccessModifier, Lint::UselessAssignment, Lint::UselessDefaultValueArgument, Lint::UselessMethodDefinition, Lint::UselessNumericOperation, Lint::UselessOr, Lint::UselessSetterCall, Lint::UselessTimes, Lint::Void, Migration::DepartmentName, Naming::BinaryOperatorParameterName, Naming::BlockForwarding, Naming::HeredocDelimiterCase, Naming::InclusiveLanguage, Naming::MemoizedInstanceVariableName, Naming::RescuedExceptionsVariableName, Security::IoMethods, Security::JSONLoad, Security::YAMLLoad, Style::AccessModifierDeclarations, Style::AccessorGrouping, Style::Alias, Style::AmbiguousEndlessMethodDefinition, Style::AndOr, Style::ArgumentsForwarding, Style::ArrayCoercion, Style::ArrayFirstLast, Style::ArrayIntersect, Style::ArrayIntersectWithSingleElement, Style::ArrayJoin, Style::Attr, Style::BarePercentLiterals, Style::BisectedAttrAccessor, Style::BitwisePredicate, Style::BlockComments, Style::BlockDelimiters, Style::CaseEquality, Style::CaseLikeIf, Style::CharacterLiteral, Style::ClassAndModuleChildren, Style::ClassCheck, Style::ClassEqualityComparison, Style::ClassMethods, Style::ClassMethodsDefinitions, Style::CollectionCompact, Style::CollectionMethods, Style::CollectionQuerying, Style::ColonMethodCall, Style::ColonMethodDefinition, Style::CombinableDefined, Style::CombinableLoops, Style::CommandLiteral, Style::CommentAnnotation, Style::CommentedKeyword, Style::ComparableBetween, Style::ComparableClamp, Style::ConcatArrayLiterals, Style::ConditionalAssignment, Style::Copyright, Style::DataInheritance, Style::DateTime, Style::DefWithParentheses, Style::DigChain, Style::Dir, Style::DirEmpty, Style::DisableCopsWithinSourceCodeDirective, Style::DoubleCopDisableDirective, Style::DoubleNegation, Style::EachForSimpleLoop, Style::EachWithObject, Style::EmptyBlockParameter, Style::EmptyCaseCondition, Style::EmptyClassDefinition, Style::EmptyElse, Style::EmptyHeredoc, Style::EmptyLambdaParameter, Style::EmptyLiteral, Style::EmptyMethod, Style::EmptyStringInsideInterpolation, Style::Encoding, Style::EndBlock, Style::EndlessMethod, Style::EnvHome, Style::EvalWithLocation, Style::EvenOdd, Style::ExactRegexpMatch, Style::ExpandPathArguments, Style::ExplicitBlockArgument, Style::FetchEnvVar, Style::FileEmpty, Style::FileNull, Style::FileRead, Style::FileTouch, Style::FileWrite, Style::FloatDivision, Style::For, Style::FormatString, Style::FormatStringToken, Style::FrozenStringLiteralComment, Style::GlobalStdStream, Style::GuardClause, Style::HashAsLastArrayItem, Style::HashConversion, Style::HashEachMethods, Style::HashExcept, Style::HashFetchChain, Style::HashLookupMethod, Style::HashSlice, Style::HashSyntax, Style::HashTransformKeys, Style::HashTransformValues, Style::IdenticalConditionalBranches, Style::IfInsideElse, Style::IfUnlessModifier, Style::IfUnlessModifierOfIfUnless, Style::IfWithBooleanLiteralBranches, Style::IfWithSemicolon, Style::InPatternThen, Style::InfiniteLoop, Style::InverseMethods, Style::InvertibleUnlessCondition, Style::ItBlockParameter, Style::KeywordArgumentsMerging, Style::KeywordParametersOrder, Style::Lambda, Style::LambdaCall, Style::LineEndConcatenation, Style::MagicCommentFormat, Style::MapCompactWithConditionalBlock, Style::MapIntoArray, Style::MapJoin, Style::MapToHash, Style::MapToSet, Style::MethodCallWithArgsParentheses, Style::MethodCallWithoutArgsParentheses, Style::MethodDefParentheses, Style::MinMax, Style::MinMaxComparison, Style::MissingElse, Style::MixinGrouping, Style::ModuleFunction, Style::ModuleMemberExistenceCheck, Style::MultilineIfModifier, Style::MultilineIfThen, Style::MultilineInPatternThen, Style::MultilineMemoization, Style::MultilineMethodSignature, Style::MultilineTernaryOperator, Style::MultilineWhenThen, Style::MultipleComparison, Style::MutableConstant, Style::NegatedIf, Style::NegatedIfElseCondition, Style::NegatedUnless, Style::NegatedWhile, Style::NegativeArrayIndex, Style::NestedFileDirname, Style::NestedModifier, Style::NestedParenthesizedCalls, Style::NestedTernaryOperator, Style::Next, Style::NilComparison, Style::NilLambda, Style::NonNilCheck, Style::Not, Style::NumericLiteralPrefix, Style::NumericLiterals, Style::NumericPredicate, Style::ObjectThen, Style::OneLineConditional, Style::OperatorMethodCall, Style::OrAssignment, Style::ParallelAssignment, Style::ParenthesesAroundCondition, Style::PartitionInsteadOfDoubleSelect, Style::PercentLiteralDelimiters, Style::PercentQLiterals, Style::PerlBackrefs, Style::PredicateWithKind, Style::PreferredHashMethods, Style::Proc, Style::QuotedSymbols, Style::RaiseArgs, Style::RandomWithOffset, Style::ReduceToHash, Style::RedundantArgument, Style::RedundantArrayConstructor, Style::RedundantArrayFlatten, Style::RedundantAssignment, Style::RedundantBegin, Style::RedundantCapitalW, Style::RedundantCondition, Style::RedundantConditional, Style::RedundantConstantBase, Style::RedundantCurrentDirectoryInPath, Style::RedundantDoubleSplatHashBraces, Style::RedundantEach, Style::RedundantException, Style::RedundantFetchBlock, Style::RedundantFileExtensionInRequire, Style::RedundantFilterChain, Style::RedundantFormat, Style::RedundantFreeze, Style::RedundantHeredocDelimiterQuotes, Style::RedundantInitialize, Style::RedundantInterpolation, Style::RedundantInterpolationUnfreeze, Style::RedundantLineContinuation, Style::RedundantMinMaxBy, Style::RedundantParentheses, Style::RedundantPercentQ, Style::RedundantRegexpArgument, Style::RedundantRegexpCharacterClass, Style::RedundantRegexpConstructor, Style::RedundantRegexpEscape, Style::RedundantReturn, Style::RedundantSelf, Style::RedundantSelfAssignment, Style::RedundantSelfAssignmentBranch, Style::RedundantSort, Style::RedundantSortBy, Style::RedundantStringEscape, Style::RedundantStructKeywordInit, Style::RegexpLiteral, Style::RequireOrder, Style::RescueModifier, Style::RescueStandardError, Style::ReturnNil, Style::ReturnNilInPredicateMethodDefinition, Style::ReverseFind, Style::SafeNavigation, Style::Sample, Style::SelectByKind, Style::SelectByRange, Style::SelectByRegexp, Style::SelfAssignment, Style::Semicolon, Style::SendWithLiteralMethodName, Style::SignalException, Style::SingleArgumentDig, Style::SingleLineBlockParams, Style::SingleLineDoEndBlock, Style::SingleLineMethods, Style::SlicingWithRange, Style::SoleNestedConditional, Style::SpecialGlobalVars, Style::StabbyLambdaParentheses, Style::StaticClass, Style::StderrPuts, Style::StringChars, Style::StringConcatenation, Style::StringHashKeys, Style::StringLiterals, Style::StringLiteralsInInterpolation, Style::StringMethods, Style::Strip, Style::StructInheritance, Style::SuperArguments, Style::SuperWithArgsParentheses, Style::SwapValues, Style::SymbolArray, Style::SymbolLiteral, Style::SymbolProc, Style::TallyMethod, Style::TernaryParentheses, Style::TrailingBodyOnClass, Style::TrailingBodyOnMethodDefinition, Style::TrailingBodyOnModule, Style::TrailingCommaInArguments, Style::TrailingCommaInArrayLiteral, Style::TrailingCommaInBlockArgs, Style::TrailingCommaInHashLiteral, Style::TrailingMethodEndStatement, Style::TrailingUnderscoreVariable, Style::TrivialAccessors, Style::UnlessElse, Style::UnpackFirst, Style::VariableInterpolation, Style::WhenThen, Style::WhileUntilDo, Style::WhileUntilModifier, Style::WordArray, Style::YAMLFileRead, Style::YodaCondition, Style::YodaExpression, Style::ZeroLengthPredicate
  
  

  
  
    Defined in:
    lib/rubocop/cop/mixin/auto_corrector.rb
  
## Overview

extend this module to signal autocorrection support

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**support_autocorrect?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**support_autocorrect?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

7
8
9
```

```
# File 'lib/rubocop/cop/mixin/auto_corrector.rb', line 7

def support_autocorrect?
  true
end

```
