# Class: RuboCop::Cop::Base
  
    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Cop::Base

        show all
      
    
  
  

  
  
  
      Extended by:
      NodePattern::Macros, AST::Sexp, ExcludeLimit
  
  
  
  
  
      Includes:
      AST::Sexp, AutocorrectLogic, IgnoredNode, Util
  
    Defined in:
    lib/rubocop/cop/base.rb
  
## Overview

A scaffold for concrete cops.

The Cop::Base class is meant to be extended.

Cops track offenses and can autocorrect them on the fly.

A commissioner object is responsible for traversing the AST and invoking the specific callbacks on each cop.

First the callback `on_new_investigation` is called; if a cop needs to do its own processing of the AST or depends on something else.

Then callbacks like `on_def`, `on_send` (see AST::Traversal) are called with their respective nodes.

Finally the callback `on_investigation_end` is called.

Within these callbacks, cops are meant to call `add_offense` or `add_global_offense`. Use the `processed_source` method to get the currently processed source being investigated.

In case of invalid syntax / unparsable content, the callback `on_other_file` is called instead of all the other `on_...` callbacks.

Private methods are not meant for custom cops consumption, nor are any instance variables.

## Direct Known Subclasses

RuboCop::Cop::Bundler::DuplicatedGem, RuboCop::Cop::Bundler::DuplicatedGroup, RuboCop::Cop::Bundler::GemComment, RuboCop::Cop::Bundler::GemFilename, RuboCop::Cop::Bundler::GemVersion, RuboCop::Cop::Bundler::InsecureProtocolSource, RuboCop::Cop::Bundler::OrderedGems, Cop, Gemspec::AddRuntimeDependency, Gemspec::AttributeAssignment, Gemspec::DependencyVersion, Gemspec::DeprecatedAttributeAssignment, Gemspec::DevelopmentDependencies, Gemspec::DuplicatedAssignment, Gemspec::OrderedDependencies, Gemspec::RequireMFA, Gemspec::RequiredRubyVersion, Gemspec::RubyVersionGlobalsUsage, InternalAffairs::CopDescription, InternalAffairs::CopEnabled, InternalAffairs::CreateEmptyFile, InternalAffairs::EmptyLineBetweenExpectOffenseAndCorrection, InternalAffairs::ExampleDescription, InternalAffairs::ExampleHeredocDelimiter, InternalAffairs::InheritDeprecatedCopClass, InternalAffairs::ItblockHandler, InternalAffairs::LambdaOrProc, InternalAffairs::LocationExists, InternalAffairs::LocationExpression, InternalAffairs::LocationLineEqualityComparison, InternalAffairs::MethodNameEndWith, InternalAffairs::MethodNameEqual, InternalAffairs::NodeDestructuring, InternalAffairs::NodeFirstOrLastArgument, InternalAffairs::NodeMatcherDirective, InternalAffairs::NodePatternGroups, InternalAffairs::NodeTypeGroup, InternalAffairs::NodeTypeMultiplePredicates, InternalAffairs::NodeTypePredicate, InternalAffairs::NumblockHandler, InternalAffairs::OffenseLocationKeyword, InternalAffairs::OnSendWithoutOnCSend, InternalAffairs::OperatorKeyword, InternalAffairs::ProcessedSourceBufferName, InternalAffairs::RedundantContextConfigParameter, InternalAffairs::RedundantDescribedClassAsSubject, InternalAffairs::RedundantExpectOffenseArguments, InternalAffairs::RedundantLetRuboCopConfigNew, InternalAffairs::RedundantLocationArgument, InternalAffairs::RedundantMessageArgument, InternalAffairs::RedundantMethodDispatchNode, InternalAffairs::RedundantSourceRange, InternalAffairs::SingleLineComparison, InternalAffairs::StyleDetectedApiUse, InternalAffairs::UndefinedConfig, InternalAffairs::UselessMessageAssertion, InternalAffairs::UselessRestrictOnSend, Layout::AccessModifierIndentation, Layout::ArgumentAlignment, Layout::ArrayAlignment, Layout::AssignmentIndentation, Layout::BeginEndAlignment, Layout::BlockAlignment, Layout::BlockEndNewline, Layout::CaseIndentation, Layout::ClassStructure, Layout::ClosingHeredocIndentation, Layout::ClosingParenthesisIndentation, Layout::CommentIndentation, Layout::ConditionPosition, Layout::DefEndAlignment, Layout::DotPosition, Layout::ElseAlignment, Layout::EmptyComment, Layout::EmptyLineAfterGuardClause, Layout::EmptyLineAfterMagicComment, Layout::EmptyLineAfterMultilineCondition, Layout::EmptyLineBetweenDefs, Layout::EmptyLines, Layout::EmptyLinesAfterModuleInclusion, Layout::EmptyLinesAroundAccessModifier, Layout::EmptyLinesAroundArguments, Layout::EmptyLinesAroundAttributeAccessor, Layout::EmptyLinesAroundBeginBody, Layout::EmptyLinesAroundBlockBody, Layout::EmptyLinesAroundClassBody, Layout::EmptyLinesAroundExceptionHandlingKeywords, Layout::EmptyLinesAroundMethodBody, Layout::EmptyLinesAroundModuleBody, Layout::EndAlignment, Layout::EndOfLine, Layout::ExtraSpacing, Layout::FirstArgumentIndentation, Layout::FirstArrayElementIndentation, Layout::FirstArrayElementLineBreak, Layout::FirstHashElementIndentation, Layout::FirstHashElementLineBreak, Layout::FirstMethodArgumentLineBreak, Layout::FirstMethodParameterLineBreak, Layout::FirstParameterIndentation, Layout::HashAlignment, Layout::HeredocArgumentClosingParenthesis, Layout::HeredocIndentation, Layout::IndentationConsistency, Layout::IndentationStyle, Layout::IndentationWidth, Layout::InitialIndentation, Layout::LeadingCommentSpace, Layout::LeadingEmptyLines, Layout::LineContinuationLeadingSpace, Layout::LineContinuationSpacing, Layout::LineEndStringConcatenationIndentation, Layout::LineLength, Layout::MultilineArrayBraceLayout, Layout::MultilineArrayLineBreaks, Layout::MultilineAssignmentLayout, Layout::MultilineBlockLayout, Layout::MultilineHashBraceLayout, Layout::MultilineHashKeyLineBreaks, Layout::MultilineMethodArgumentLineBreaks, Layout::MultilineMethodCallBraceLayout, Layout::MultilineMethodCallIndentation, Layout::MultilineMethodDefinitionBraceLayout, Layout::MultilineMethodParameterLineBreaks, Layout::MultilineOperationIndentation, Layout::ParameterAlignment, Layout::RedundantLineBreak, Layout::RescueEnsureAlignment, Layout::SingleLineBlockChain, Layout::SpaceAfterColon, Layout::SpaceAfterComma, Layout::SpaceAfterMethodName, Layout::SpaceAfterNot, Layout::SpaceAfterSemicolon, Layout::SpaceAroundBlockParameters, Layout::SpaceAroundEqualsInParameterDefault, Layout::SpaceAroundKeyword, Layout::SpaceAroundMethodCallOperator, Layout::SpaceAroundOperators, Layout::SpaceBeforeBlockBraces, Layout::SpaceBeforeBrackets, Layout::SpaceBeforeComma, Layout::SpaceBeforeComment, Layout::SpaceBeforeFirstArg, Layout::SpaceBeforeSemicolon, Layout::SpaceInLambdaLiteral, Layout::SpaceInsideArrayLiteralBrackets, Layout::SpaceInsideArrayPercentLiteral, Layout::SpaceInsideBlockBraces, Layout::SpaceInsideHashLiteralBraces, Layout::SpaceInsideParens, Layout::SpaceInsidePercentLiteralDelimiters, Layout::SpaceInsideRangeLiteral, Layout::SpaceInsideReferenceBrackets, Layout::SpaceInsideStringInterpolation, Layout::TrailingEmptyLines, Layout::TrailingWhitespace, Lint::AmbiguousAssignment, Lint::AmbiguousBlockAssociation, Lint::AmbiguousOperator, Lint::AmbiguousOperatorPrecedence, Lint::AmbiguousRange, Lint::AmbiguousRegexpLiteral, Lint::ArrayLiteralInRegexp, Lint::AssignmentInCondition, Lint::BigDecimalNew, Lint::BinaryOperatorWithIdenticalOperands, Lint::BooleanSymbol, Lint::CircularArgumentReference, Lint::ConstantDefinitionInBlock, Lint::ConstantOverwrittenInRescue, Lint::ConstantReassignment, Lint::ConstantResolution, Lint::CopDirectiveSyntax, Lint::DataDefineOverride, Lint::Debugger, Lint::DeprecatedClassMethods, Lint::DeprecatedConstants, Lint::DeprecatedOpenSSLConstant, Lint::DisjunctiveAssignmentInConstructor, Lint::DuplicateBranch, Lint::DuplicateCaseCondition, Lint::DuplicateElsifCondition, Lint::DuplicateHashKey, Lint::DuplicateMagicComment, Lint::DuplicateMatchPattern, Lint::DuplicateMethods, Lint::DuplicateRegexpCharacterClassElement, Lint::DuplicateRequire, Lint::DuplicateRescueException, Lint::DuplicateSetElement, Lint::EachWithObjectArgument, Lint::ElseLayout, Lint::EmptyBlock, Lint::EmptyClass, Lint::EmptyConditionalBody, Lint::EmptyEnsure, Lint::EmptyExpression, Lint::EmptyFile, Lint::EmptyInPattern, Lint::EmptyInterpolation, Lint::EmptyWhen, Lint::EnsureReturn, Lint::ErbNewArguments, Lint::FlipFlop, Lint::FloatComparison, Lint::FloatOutOfRange, Lint::FormatParameterMismatch, Lint::HashCompareByIdentity, Lint::HashNewWithKeywordArgumentsAsDefault, Lint::HeredocMethodCallPosition, Lint::IdentityComparison, Lint::ImplicitStringConcatenation, Lint::IncompatibleIoSelectWithFiberScheduler, Lint::IneffectiveAccessModifier, Lint::InheritException, Lint::InterpolationCheck, Lint::ItWithoutArgumentsInBlock, Lint::LambdaWithoutLiteralBlock, Lint::LiteralAsCondition, Lint::LiteralAssignmentInCondition, Lint::LiteralInInterpolation, Lint::Loop, Lint::MissingCopEnableDirective, Lint::MissingSuper, Lint::MixedCaseRange, Lint::MixedRegexpCaptureTypes, Lint::MultipleComparison, Lint::NestedMethodDefinition, Lint::NestedPercentLiteral, Lint::NextWithoutAccumulator, Lint::NoReturnInBeginEndBlocks, Lint::NonAtomicFileOperation, Lint::NonDeterministicRequireOrder, Lint::NonLocalExitFromIterator, Lint::NumberConversion, Lint::NumberedParameterAssignment, Lint::NumericOperationWithConstantResult, Lint::OrAssignmentToConstant, Lint::OrderedMagicComments, Lint::OutOfRangeRegexpRef, Lint::ParenthesesAsGroupedExpression, Lint::PercentStringArray, Lint::PercentSymbolArray, Lint::RaiseException, Lint::RandOne, Lint::RedundantCopDisableDirective, Lint::RedundantCopEnableDirective, Lint::RedundantDirGlobSort, Lint::RedundantRegexpQuantifiers, Lint::RedundantRequireStatement, Lint::RedundantSafeNavigation, Lint::RedundantSplatExpansion, Lint::RedundantStringCoercion, Lint::RedundantTypeConversion, Lint::RedundantWithIndex, Lint::RedundantWithObject, Lint::RefinementImportMethods, Lint::RegexpAsCondition, Lint::RequireParentheses, Lint::RequireRangeParentheses, Lint::RequireRelativeSelfPath, Lint::RescueException, Lint::RescueType, Lint::ReturnInVoidContext, Lint::SafeNavigationChain, Lint::SafeNavigationConsistency, Lint::SafeNavigationWithEmpty, Lint::ScriptPermission, Lint::SelfAssignment, Lint::SendWithMixinArgument, Lint::ShadowedArgument, Lint::ShadowedException, Lint::ShadowingOuterLocalVariable, Lint::SharedMutableDefault, Lint::StructNewOverride, Lint::SuppressedException, Lint::SuppressedExceptionInNumberConversion, Lint::SymbolConversion, Lint::Syntax, Lint::ToEnumArguments, Lint::ToJSON, Lint::TopLevelReturnWithArgument, Lint::TrailingCommaInAttributeDeclaration, Lint::TripleQuotes, Lint::UnderscorePrefixedVariableName, Lint::UnescapedBracketInRegexp, Lint::UnexpectedBlockArity, Lint::UnifiedInteger, Lint::UnmodifiedReduceAccumulator, Lint::UnreachableCode, Lint::UnreachableLoop, Lint::UnreachablePatternBranch, Lint::UnusedBlockArgument, Lint::UnusedMethodArgument, Lint::UriEscapeUnescape, Lint::UriRegexp, Lint::UselessAccessModifier, Lint::UselessAssignment, Lint::UselessConstantScoping, Lint::UselessDefaultValueArgument, Lint::UselessDefined, Lint::UselessElseWithoutRescue, Lint::UselessMethodDefinition, Lint::UselessNumericOperation, Lint::UselessOr, Lint::UselessRescue, Lint::UselessRuby2Keywords, Lint::UselessSetterCall, Lint::UselessTimes, Lint::Void, Metrics::AbcSize, Metrics::BlockLength, Metrics::BlockNesting, Metrics::ClassLength, Metrics::CollectionLiteralLength, Metrics::CyclomaticComplexity, Metrics::MethodLength, Metrics::ModuleLength, Metrics::ParameterLists, Migration::DepartmentName, Naming::AccessorMethodName, Naming::AsciiIdentifiers, Naming::BinaryOperatorParameterName, Naming::BlockForwarding, Naming::BlockParameterName, Naming::ClassAndModuleCamelCase, Naming::ConstantName, Naming::FileName, Naming::HeredocDelimiterCase, Naming::HeredocDelimiterNaming, Naming::InclusiveLanguage, Naming::MemoizedInstanceVariableName, Naming::MethodName, Naming::MethodParameterName, Naming::PredicateMethod, Naming::PredicatePrefix, Naming::RescuedExceptionsVariableName, Naming::VariableName, Naming::VariableNumber, Security::CompoundHash, Security::Eval, Security::IoMethods, Security::JSONLoad, Security::MarshalLoad, Security::Open, Security::YAMLLoad, Style::AccessModifierDeclarations, Style::AccessorGrouping, Style::Alias, Style::AmbiguousEndlessMethodDefinition, Style::AndOr, Style::ArgumentsForwarding, Style::ArrayCoercion, Style::ArrayFirstLast, Style::ArrayIntersect, Style::ArrayIntersectWithSingleElement, Style::ArrayJoin, Style::AsciiComments, Style::Attr, Style::AutoResourceCleanup, Style::BarePercentLiterals, Style::BeginBlock, Style::BisectedAttrAccessor, Style::BitwisePredicate, Style::BlockComments, Style::BlockDelimiters, Style::CaseEquality, Style::CaseLikeIf, Style::CharacterLiteral, Style::ClassAndModuleChildren, Style::ClassCheck, Style::ClassEqualityComparison, Style::ClassMethods, Style::ClassMethodsDefinitions, Style::ClassVars, Style::CollectionCompact, Style::CollectionMethods, Style::CollectionQuerying, Style::ColonMethodCall, Style::ColonMethodDefinition, Style::CombinableDefined, Style::CombinableLoops, Style::CommandLiteral, Style::CommentAnnotation, Style::CommentedKeyword, Style::ComparableBetween, Style::ComparableClamp, Style::ConcatArrayLiterals, Style::ConditionalAssignment, Style::ConstantVisibility, Style::Copyright, Style::DataInheritance, Style::DateTime, Style::DefWithParentheses, Style::DigChain, Style::Dir, Style::DirEmpty, Style::DisableCopsWithinSourceCodeDirective, Style::DocumentDynamicEvalDefinition, Style::Documentation, Style::DocumentationMethod, Style::DoubleCopDisableDirective, Style::DoubleNegation, Style::EachForSimpleLoop, Style::EachWithObject, Style::EmptyBlockParameter, Style::EmptyCaseCondition, Style::EmptyClassDefinition, Style::EmptyElse, Style::EmptyHeredoc, Style::EmptyLambdaParameter, Style::EmptyLiteral, Style::EmptyMethod, Style::EmptyStringInsideInterpolation, Style::Encoding, Style::EndBlock, Style::EndlessMethod, Style::EnvHome, Style::EvalWithLocation, Style::EvenOdd, Style::ExactRegexpMatch, Style::ExpandPathArguments, Style::ExplicitBlockArgument, Style::ExponentialNotation, Style::FetchEnvVar, Style::FileEmpty, Style::FileNull, Style::FileOpen, Style::FileRead, Style::FileTouch, Style::FileWrite, Style::FloatDivision, Style::For, Style::FormatString, Style::FormatStringToken, Style::FrozenStringLiteralComment, Style::GlobalStdStream, Style::GlobalVars, Style::GuardClause, Style::HashAsLastArrayItem, Style::HashConversion, Style::HashEachMethods, Style::HashExcept, Style::HashFetchChain, Style::HashLikeCase, Style::HashLookupMethod, Style::HashSlice, Style::HashSyntax, Style::HashTransformKeys, Style::HashTransformValues, Style::IdenticalConditionalBranches, Style::IfInsideElse, Style::IfUnlessModifier, Style::IfUnlessModifierOfIfUnless, Style::IfWithBooleanLiteralBranches, Style::IfWithSemicolon, Style::ImplicitRuntimeError, Style::InPatternThen, Style::InfiniteLoop, Style::InlineComment, Style::InverseMethods, Style::InvertibleUnlessCondition, Style::IpAddresses, Style::ItAssignment, Style::ItBlockParameter, Style::KeywordArgumentsMerging, Style::KeywordParametersOrder, Style::Lambda, Style::LambdaCall, Style::LineEndConcatenation, Style::MagicCommentFormat, Style::MapCompactWithConditionalBlock, Style::MapIntoArray, Style::MapJoin, Style::MapToHash, Style::MapToSet, Style::MethodCallWithArgsParentheses, Style::MethodCallWithoutArgsParentheses, Style::MethodCalledOnDoEndBlock, Style::MethodDefParentheses, Style::MinMax, Style::MinMaxComparison, Style::MissingElse, Style::MissingRespondToMissing, Style::MixinGrouping, Style::MixinUsage, Style::ModuleFunction, Style::ModuleMemberExistenceCheck, Style::MultilineBlockChain, Style::MultilineIfModifier, Style::MultilineIfThen, Style::MultilineInPatternThen, Style::MultilineMemoization, Style::MultilineMethodSignature, Style::MultilineTernaryOperator, Style::MultilineWhenThen, Style::MultipleComparison, Style::MutableConstant, Style::NegatedIf, Style::NegatedIfElseCondition, Style::NegatedUnless, Style::NegatedWhile, Style::NegativeArrayIndex, Style::NestedFileDirname, Style::NestedModifier, Style::NestedParenthesizedCalls, Style::NestedTernaryOperator, Style::Next, Style::NilComparison, Style::NilLambda, Style::NonNilCheck, Style::Not, Style::NumberedParameters, Style::NumberedParametersLimit, Style::NumericLiteralPrefix, Style::NumericLiterals, Style::NumericPredicate, Style::ObjectThen, Style::OneClassPerFile, Style::OneLineConditional, Style::OpenStructUse, Style::OperatorMethodCall, Style::OptionHash, Style::OptionalArguments, Style::OptionalBooleanParameter, Style::OrAssignment, Style::ParallelAssignment, Style::ParenthesesAroundCondition, Style::PartitionInsteadOfDoubleSelect, Style::PercentLiteralDelimiters, Style::PercentQLiterals, Style::PerlBackrefs, Style::PredicateWithKind, Style::PreferredHashMethods, Style::Proc, Style::QuotedSymbols, Style::RaiseArgs, Style::RandomWithOffset, Style::ReduceToHash, Style::RedundantArgument, Style::RedundantArrayConstructor, Style::RedundantArrayFlatten, Style::RedundantAssignment, Style::RedundantBegin, Style::RedundantCapitalW, Style::RedundantCondition, Style::RedundantConditional, Style::RedundantConstantBase, Style::RedundantCurrentDirectoryInPath, Style::RedundantDoubleSplatHashBraces, Style::RedundantEach, Style::RedundantException, Style::RedundantFetchBlock, Style::RedundantFileExtensionInRequire, Style::RedundantFilterChain, Style::RedundantFormat, Style::RedundantFreeze, Style::RedundantHeredocDelimiterQuotes, Style::RedundantInitialize, Style::RedundantInterpolation, Style::RedundantInterpolationUnfreeze, Style::RedundantLineContinuation, Style::RedundantMinMaxBy, Style::RedundantParentheses, Style::RedundantPercentQ, Style::RedundantRegexpArgument, Style::RedundantRegexpCharacterClass, Style::RedundantRegexpConstructor, Style::RedundantRegexpEscape, Style::RedundantReturn, Style::RedundantSelf, Style::RedundantSelfAssignment, Style::RedundantSelfAssignmentBranch, Style::RedundantSort, Style::RedundantSortBy, Style::RedundantStringEscape, Style::RedundantStructKeywordInit, Style::RegexpLiteral, Style::RequireOrder, Style::RescueModifier, Style::RescueStandardError, Style::ReturnNil, Style::ReturnNilInPredicateMethodDefinition, Style::ReverseFind, Style::SafeNavigation, Style::SafeNavigationChainLength, Style::Sample, Style::SelectByKind, Style::SelectByRange, Style::SelectByRegexp, Style::SelfAssignment, Style::Semicolon, Style::Send, Style::SendWithLiteralMethodName, Style::SignalException, Style::SingleArgumentDig, Style::SingleLineBlockParams, Style::SingleLineDoEndBlock, Style::SingleLineMethods, Style::SlicingWithRange, Style::SoleNestedConditional, Style::SpecialGlobalVars, Style::StabbyLambdaParentheses, Style::StaticClass, Style::StderrPuts, Style::StringChars, Style::StringConcatenation, Style::StringHashKeys, Style::StringLiterals, Style::StringLiteralsInInterpolation, Style::StringMethods, Style::Strip, Style::StructInheritance, Style::SuperArguments, Style::SuperWithArgsParentheses, Style::SwapValues, Style::SymbolArray, Style::SymbolLiteral, Style::SymbolProc, Style::TallyMethod, Style::TernaryParentheses, Style::TopLevelMethodDefinition, Style::TrailingBodyOnClass, Style::TrailingBodyOnMethodDefinition, Style::TrailingBodyOnModule, Style::TrailingCommaInArguments, Style::TrailingCommaInArrayLiteral, Style::TrailingCommaInBlockArgs, Style::TrailingCommaInHashLiteral, Style::TrailingMethodEndStatement, Style::TrailingUnderscoreVariable, Style::TrivialAccessors, Style::UnlessElse, Style::UnlessLogicalOperators, Style::UnpackFirst, Style::VariableInterpolation, Style::WhenThen, Style::WhileUntilDo, Style::WhileUntilModifier, Style::WordArray, Style::YAMLFileRead, Style::YodaCondition, Style::YodaExpression, Style::ZeroLengthPredicate

## Defined Under Namespace

      **Classes:** InvestigationReport
    
  

  
    
##

      Constant Summary
      collapse
    

    
      
        RESTRICT_ON_SEND =
          
  
    

List of methods names to restrict calls for `on_send` / `on_csend`

```
Set[].freeze
```

## Class Attribute Summary collapse

-
  
      .**gem_requirements**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute gem_requirements.

## Instance Attribute Summary collapse

-
  
      #**config**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute config.

-
  
      #**processed_source**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute processed_source.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**autocorrect_incompatible_with**  ⇒ Array<RuboCop::Cop::Base> 
    

    
  
  
  
  
  
  
  
  

  
    

List of cops that should not try to autocorrect at the same time as this cop.

-
  
      .**badge**  ⇒ Object 

Naming.

-
  
      .**callbacks_needed**  ⇒ Object 

  private

-
  
      .**cop_name**  ⇒ Object 

-
  
      .**department**  ⇒ Object 

-
  
      .**documentation_url**(config = nil)  ⇒ String? 

Returns a url to view this cops documentation online.

-
  
      .**exclude_from_registry**  ⇒ Object 

Call for abstract Cop classes.

-
  
      .**inherited**(subclass)  ⇒ Object 

-
  
      .**joining_forces**  ⇒ Object 

Override and return the Force class(es) you need to join.

-
  
      .**lint?**  ⇒ Boolean 

-
  
      .**match?**(given_names)  ⇒ Boolean 

Returns true if the cop name or the cop namespace matches any of the given names.

-
  
      .**requires_gem**(gem_name, *version_requirements)  ⇒ Object 

Register a version requirement for the given gem name.

-
  
      .**support_autocorrect?**  ⇒ Boolean 

Returns if class supports autocorrect.

-
  
      .**support_multiple_source?**  ⇒ Boolean 

Override if your cop should be called repeatedly for multiple investigations Between calls to `on_new_investigation` and `on_investigation_end`, the result of `processed_source` will remain constant.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**active_support_extensions_enabled?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**add_global_offense**(message = nil, severity: nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Adds an offense that has no particular location.

-
  
      #**add_offense**(node_or_range, message: nil, severity: nil, &block)  ⇒ Object 

Adds an offense on the specified range (or node with an expression) Unless that offense is disabled for this range, a corrector will be yielded to provide the cop the opportunity to autocorrect the offense.

-
  
      #**always_autocorrect?**  ⇒ Boolean 

  private

-
  
      #**begin_investigation**(processed_source, offset: 0, original: processed_source)  ⇒ Object 

  private

Called before any investigation.

-
  
      #**callbacks_needed**  ⇒ Object 

  private

rubocop:disable Layout/ClassStructure.

-
  
      #**config_to_allow_offenses**  ⇒ Object 

-
  
      #**config_to_allow_offenses=**(hash)  ⇒ Object 

-
  
      #**contextual_autocorrect?**  ⇒ Boolean 

  private

-
  
      #**cop_config**  ⇒ Object 

Configuration Helpers.

-
  
      #**cop_name**  ⇒ Object 

      (also: #name)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**excluded_file?**(file)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**external_dependency_checksum**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This method should be overridden when a cop’s behavior depends on state that lives outside of these locations:.

-
  
      #**initialize**(config = nil, options = nil)  ⇒ Base 

    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

-
  
      #**inspect**  ⇒ Object 

:nodoc:.

-
  
      #**message**(_range = nil)  ⇒ Object 

Gets called if no message is specified when calling `add_offense` or `add_global_offense` Cops are discouraged to override this; instead pass your message directly.

-
  
      #**offenses**  ⇒ Object 

  deprecated
  
    **Deprecated.** 

Make potential errors with previous API more obvious

-
  
      #**on_investigation_end**  ⇒ Object 

Called after all on_…

-
  
      #**on_new_investigation**  ⇒ Object 

Called before all on_…

-
  
      #**on_other_file**  ⇒ Object 

Called instead of all on_…

-
  
      #**parse**(source, path = nil)  ⇒ Object 

There should be very limited reasons for a Cop to do it’s own parsing.

-
  
      #**parser_engine**  ⇒ Object 

-
  
      #**ready**  ⇒ Object 

  private

Called between investigations.

-
  
      #**relevant_file?**(file)  ⇒ Boolean 

-
  
      #**string_literals_frozen_by_default?**  ⇒ Boolean 

-
  
      #**target_gem_version**(gem_name)  ⇒ Object 

Returns a gems locked versions (i.e. from Gemfile.lock or gems.locked).

-
  
      #**target_rails_version**  ⇒ Object 

-
  
      #**target_ruby_version**  ⇒ Object 

### Methods included from ExcludeLimit

exclude_limit

### Methods included from AutocorrectLogic

# autocorrect?, #autocorrect_enabled?, #autocorrect_requested?, #autocorrect_with_disable_uncorrectable?, #correctable?, #disable_uncorrectable?, #safe_autocorrect?

### Methods included from IgnoredNode

# ignore_node, #ignored_node?, #part_of_ignored_node?

### Methods included from Util

silence_warnings

## Constructor Details

###
  
    #**initialize**(config = nil, options = nil)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

```

156
157
158
159
160
```

```
# File 'lib/rubocop/cop/base.rb', line 156

def initialize(config = nil, options = nil)
  @config = config || Config.new
  @options = options || { debug: false }
  reset_investigation
end
```

## Class Attribute Details

###
  
    .**gem_requirements**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute gem_requirements.

```

138
139
140
```

```
# File 'lib/rubocop/cop/base.rb', line 138

def gem_requirements
  @gem_requirements
end
```

## Instance Attribute Details

###
  
    #**config**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute config.

```

43
44
45
```

```
# File 'lib/rubocop/cop/base.rb', line 43

def config
  @config
end
```

###
  
    #**processed_source**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute processed_source.

```

43
44
45
```

```
# File 'lib/rubocop/cop/base.rb', line 43

def processed_source
  @processed_source
end
```

## Class Method Details

###
  
    .**autocorrect_incompatible_with**  ⇒ Array<RuboCop::Cop::Base> 
  

  

  

  
    

List of cops that should not try to autocorrect at the same time as this cop

Returns:

-

        (Array<RuboCop::Cop::Base>)

```

59
60
61
```

```
# File 'lib/rubocop/cop/base.rb', line 59

def self.autocorrect_incompatible_with
  []
end
```

###
  
    .**badge**  ⇒ Object 
  

  

  

  
    

Naming

```

93
94
95
```

```
# File 'lib/rubocop/cop/base.rb', line 93

def self.badge
  @badge ||= Badge.for(name)
end
```

###
  
    .**callbacks_needed**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

329
330
331
332
333
334
335
336
337
338
```

```
# File 'lib/rubocop/cop/base.rb', line 329

def self.callbacks_needed
  @callbacks_needed ||= public_instance_methods.select do |m|
    # OPTIMIZE: Check method existence first to make fewer `start_with?` calls.
    # At the time of writing this comment, this excludes 98 of ~104 methods.
    # `start_with?` with two string arguments instead of a regex is faster
    # in this specific case as well.
    !Base.method_defined?(m) && # exclude standard "callbacks" like 'on_begin_investigation'
      m.start_with?('on_', 'after_')
  end
end
```

###
  
    .**cop_name**  ⇒ Object 
  

  

  

  
    
      

```

97
98
99
```

```
# File 'lib/rubocop/cop/base.rb', line 97

def self.cop_name
  badge.to_s
end
```

###
  
    .**department**  ⇒ Object 
  

  

  

  
    
      

```

101
102
103
```

```
# File 'lib/rubocop/cop/base.rb', line 101

def self.department
  badge.department
end
```

###
  
    .**documentation_url**(config = nil)  ⇒ String? 
  

  

  

  
    

Returns a url to view this cops documentation online. Requires ‘DocumentationBaseURL’ to be set for your department. Will follow the convention of RuboCops own documentation structure, overwrite this method to accommodate your custom layout.

Returns:

-

        (String, nil)

```

70
71
72
```

```
# File 'lib/rubocop/cop/base.rb', line 70

def self.documentation_url(config = nil)
  Documentation.url_for(self, config)
end
```

###
  
    .**exclude_from_registry**  ⇒ Object 
  

  

  

  
    

Call for abstract Cop classes

```

81
82
83
```

```
# File 'lib/rubocop/cop/base.rb', line 81

def self.exclude_from_registry
  Registry.global.dismiss(self)
end
```

###
  
    .**inherited**(subclass)  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
77
78
```

```
# File 'lib/rubocop/cop/base.rb', line 74

def self.inherited(subclass)
  super
  subclass.instance_variable_set(:@gem_requirements, gem_requirements.dup)
  Registry.global.enlist(subclass)
end
```

###
  
    .**joining_forces**  ⇒ Object 
  

  

  

  
    

Override and return the Force class(es) you need to join

```

118
```

```
# File 'lib/rubocop/cop/base.rb', line 118

def self.joining_forces; end
```

###
  
    .**lint?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

105
106
107
```

```
# File 'lib/rubocop/cop/base.rb', line 105

def self.lint?
  department == :Lint
end
```

###
  
    .**match?**(given_names)  ⇒ Boolean 
  

  

  

  
    

Returns true if the cop name or the cop namespace matches any of the given names.

Returns:

-

        (Boolean)

```

111
112
113
114
115
```

```
# File 'lib/rubocop/cop/base.rb', line 111

def self.match?(given_names)
  return false unless given_names

  given_names.include?(cop_name) || given_names.include?(badge.department_name)
end
```

###
  
    .**requires_gem**(gem_name, *version_requirements)  ⇒ Object 
  

  

  

  
    

Register a version requirement for the given gem name. This cop will be skipped unless the target satisfies **all** requirements.

Parameters:

-

        gem_name

        (String)
      
      
      
    
  
    
-

        version_requirements
      
      
        (Array<String>)
      
      
      
        —
        

The version requirements, using the same syntax as a Gemfile, e.g. “>= 1.2.3”

If omitted, any version of the gem will be accepted.

guides.rubygems.org/patterns/#declaring-dependencies

```

151
152
153
```

```
# File 'lib/rubocop/cop/base.rb', line 151

def requires_gem(gem_name, *version_requirements)
  @gem_requirements[gem_name] = Gem::Requirement.new(version_requirements)
end
```

###
  
    .**support_autocorrect?**  ⇒ Boolean 
  

  

  

  
    

Returns if class supports autocorrect. It is recommended to extend AutoCorrector instead of overriding

Returns:

-

        (Boolean)

```

87
88
89
```

```
# File 'lib/rubocop/cop/base.rb', line 87

def self.support_autocorrect?
  false
end
```

###
  
    .**support_multiple_source?**  ⇒ Boolean 
  

  

  

  
    

Override if your cop should be called repeatedly for multiple investigations Between calls to `on_new_investigation` and `on_investigation_end`, the result of `processed_source` will remain constant. You should invalidate any caches that depend on the current `processed_source` in the `on_new_investigation` callback. If your cop does autocorrections, be aware that your instance may be called multiple times with the same `processed_source.path` but different content.

Returns:

-

        (Boolean)

```

129
130
131
```

```
# File 'lib/rubocop/cop/base.rb', line 129

def self.support_multiple_source?
  false
end
```

## Instance Method Details

###
  
    #**active_support_extensions_enabled?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

278
279
280
```

```
# File 'lib/rubocop/cop/base.rb', line 278

def active_support_extensions_enabled?
  @config.active_support_extensions_enabled?
end
```

###
  
    #**add_global_offense**(message = nil, severity: nil)  ⇒ Object 
  

  

  

  
    

Adds an offense that has no particular location. No correction can be applied to global offenses

```

189
190
191
192
193
194
195
```

```
# File 'lib/rubocop/cop/base.rb', line 189

def add_global_offense(message = nil, severity: nil)
  severity = find_severity(nil, severity)
  message = find_message(nil, message)
  range = Offense::NO_LOCATION
  status = enabled_line?(range.line) ? :unsupported : :disabled
  current_offenses << Offense.new(severity, range, message, name, status)
end
```

###
  
    #**add_offense**(node_or_range, message: nil, severity: nil, &block)  ⇒ Object 
  

  

  

  
    

Adds an offense on the specified range (or node with an expression) Unless that offense is disabled for this range, a corrector will be yielded to provide the cop the opportunity to autocorrect the offense. If message is not specified, the method `message` will be called.

```

201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
```

```
# File 'lib/rubocop/cop/base.rb', line 201

def add_offense(node_or_range, message: nil, severity: nil, &block)
  range = range_from_node_or_range(node_or_range)
  return unless current_offense_locations.add?(range)

  range_to_pass = callback_argument(range)

  severity = find_severity(range_to_pass, severity)
  message = find_message(range_to_pass, message)

  status, corrector = enabled_line?(range.line) ? correct(range, &block) : :disabled

  # Since this range may be generated from Ruby code embedded in some
  # template file, we convert it to location info in the original file.
  range = range_for_original(range)

  current_offenses << Offense.new(severity, range, message, name, status, corrector)
end
```

###
  
    #**always_autocorrect?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

357
358
359
360
```

```
# File 'lib/rubocop/cop/base.rb', line 357

def always_autocorrect?
  # `true` is the same as `'always'` for backward compatibility.
  ['always', true].include?(cop_config.fetch('AutoCorrect', 'always'))
end
```

###
  
    #**begin_investigation**(processed_source, offset: 0, original: processed_source)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Called before any investigation

```

343
344
345
346
347
348
349
350
351
352
353
354
```

```
# File 'lib/rubocop/cop/base.rb', line 343

def begin_investigation(processed_source, offset: 0, original: processed_source)
  @current_offenses = nil
  @current_offense_locations = nil
  @currently_disabled_lines = nil
  @processed_source = processed_source
  @current_corrector = nil

  # We need to keep track of the original source and offset,
  # because `processed_source` here may be an embedded code in it.
  @current_offset = offset
  @current_original = original
end
```

###
  
    #**callbacks_needed**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

rubocop:disable Layout/ClassStructure

```

324
325
326
```

```
# File 'lib/rubocop/cop/base.rb', line 324

def callbacks_needed
  self.class.callbacks_needed
end
```

###
  
    #**config_to_allow_offenses**  ⇒ Object 
  

  

  

  
    
      

```

252
253
254
```

```
# File 'lib/rubocop/cop/base.rb', line 252

def config_to_allow_offenses
  Formatter::DisabledConfigFormatter.config_to_allow_offenses[cop_name] ||= {}
end
```

###
  
    #**config_to_allow_offenses=**(hash)  ⇒ Object 
  

  

  

  
    
      

```

256
257
258
```

```
# File 'lib/rubocop/cop/base.rb', line 256

def config_to_allow_offenses=(hash)
  Formatter::DisabledConfigFormatter.config_to_allow_offenses[cop_name] = hash
end
```

###
  
    #**contextual_autocorrect?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

363
364
365
```

```
# File 'lib/rubocop/cop/base.rb', line 363

def contextual_autocorrect?
  cop_config.fetch('AutoCorrect', 'always') == 'contextual'
end
```

###
  
    #**cop_config**  ⇒ Object 
  

  

  

  
    

Configuration Helpers

```

246
247
248
249
250
```

```
# File 'lib/rubocop/cop/base.rb', line 246

def cop_config
  # Use department configuration as basis, but let individual cop
  # configuration override.
  @cop_config ||= @config.for_badge(self.class.badge)
end
```

###
  
    #**cop_name**  ⇒ Object 
  

  
    Also known as:
    name
    
  

  

  
    
      

```

238
239
240
```

```
# File 'lib/rubocop/cop/base.rb', line 238

def cop_name
  @cop_name ||= self.class.cop_name
end
```

###
  
    #**excluded_file?**(file)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

295
296
297
```

```
# File 'lib/rubocop/cop/base.rb', line 295

def excluded_file?(file)
  !relevant_file?(file)
end
```

###
  
    #**external_dependency_checksum**  ⇒ Object 
  

  

  

  
    

This method should be overridden when a cop’s behavior depends on state that lives outside of these locations:

```
(1) the file under inspection
(2) the cop's source code
(3) the config (eg a .rubocop.yml file)

```

For example, some cops may want to look at other parts of the codebase being inspected to find violations. A cop may use the presence or absence of file `foo.rb` to determine whether a certain violation exists in `bar.rb`.

Overriding this method allows the cop to indicate to RuboCop’s ResultCache system when those external dependencies change, ie when the ResultCache should be invalidated.

```

234
235
236
```

```
# File 'lib/rubocop/cop/base.rb', line 234

def external_dependency_checksum
  nil
end
```

###
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

:nodoc:

```

367
368
369
```

```
# File 'lib/rubocop/cop/base.rb', line 367

def inspect # :nodoc:
  "#<#{self.class.name}:#{object_id} @config=#{@config} @options=#{@options}>"
end
```

###
  
    #**message**(_range = nil)  ⇒ Object 
  

  

  

  
    

Gets called if no message is specified when calling `add_offense` or `add_global_offense` Cops are discouraged to override this; instead pass your message directly

```

183
184
185
```

```
# File 'lib/rubocop/cop/base.rb', line 183

def message(_range = nil)
  self.class::MSG
end
```

###
  
    #**offenses**  ⇒ Object 
  

  

  

  
    **Deprecated.** 

Make potential errors with previous API more obvious

```

315
316
317
318
```

```
# File 'lib/rubocop/cop/base.rb', line 315

def offenses
  raise 'The offenses are not directly available; ' \
        'they are returned as the result of the investigation'
end
```

###
  
    #**on_investigation_end**  ⇒ Object 
  

  

  

  
    

Called after all on_… have been called When refining this method, always call `super`

```

170
171
172
```

```
# File 'lib/rubocop/cop/base.rb', line 170

def on_investigation_end
  # Typically do nothing here
end
```

###
  
    #**on_new_investigation**  ⇒ Object 
  

  

  

  
    

Called before all on_… have been called When refining this method, always call `super`

```

164
165
166
```

```
# File 'lib/rubocop/cop/base.rb', line 164

def on_new_investigation
  # Typically do nothing here
end
```

###
  
    #**on_other_file**  ⇒ Object 
  

  

  

  
    

Called instead of all on_… callbacks for unrecognized files / syntax errors When refining this method, always call `super`

```

176
177
178
```

```
# File 'lib/rubocop/cop/base.rb', line 176

def on_other_file
  # Typically do nothing here
end
```

###
  
    #**parse**(source, path = nil)  ⇒ Object 
  

  

  

  
    

There should be very limited reasons for a Cop to do it’s own parsing

```

300
301
302
```

```
# File 'lib/rubocop/cop/base.rb', line 300

def parse(source, path = nil)
  ProcessedSource.new(source, target_ruby_version, path, parser_engine: parser_engine)
end
```

###
  
    #**parser_engine**  ⇒ Object 
  

  

  

  
    
      

```

270
271
272
```

```
# File 'lib/rubocop/cop/base.rb', line 270

def parser_engine
  @config.parser_engine
end
```

###
  
    #**ready**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Called between investigations

```

306
307
308
309
310
```

```
# File 'lib/rubocop/cop/base.rb', line 306

def ready
  return self if self.class.support_multiple_source?

  self.class.new(@config, @options)
end
```

###
  
    #**relevant_file?**(file)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

286
287
288
289
290
291
292
293
```

```
# File 'lib/rubocop/cop/base.rb', line 286

def relevant_file?(file)
  return false unless target_satisfies_all_gem_version_requirements?
  return true unless @config.clusivity_config_for_badge?(self.class.badge)

  file == RuboCop::AST::ProcessedSource::STRING_SOURCE_NAME ||
    (file_name_matches_any?(file, 'Include', true) &&
      !file_name_matches_any?(file, 'Exclude', false))
end
```

###
  
    #**string_literals_frozen_by_default?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

282
283
284
```

```
# File 'lib/rubocop/cop/base.rb', line 282

def string_literals_frozen_by_default?
  @config.string_literals_frozen_by_default?
end
```

###
  
    #**target_gem_version**(gem_name)  ⇒ Object 
  

  

  

  
    

Returns a gems locked versions (i.e. from Gemfile.lock or gems.locked)

```

266
267
268
```

```
# File 'lib/rubocop/cop/base.rb', line 266

def target_gem_version(gem_name)
  @config.gem_versions_in_target && @config.gem_versions_in_target[gem_name]
end
```

###
  
    #**target_rails_version**  ⇒ Object 
  

  

  

  
    
      

```

274
275
276
```

```
# File 'lib/rubocop/cop/base.rb', line 274

def target_rails_version
  @config.target_rails_version
end
```

###
  
    #**target_ruby_version**  ⇒ Object 
  

  

  

  
    
      

```

260
261
262
```

```
# File 'lib/rubocop/cop/base.rb', line 260

def target_ruby_version
  @config.target_ruby_version
end
```
