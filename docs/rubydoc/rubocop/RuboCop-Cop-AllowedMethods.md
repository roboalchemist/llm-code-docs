# Module: RuboCop::Cop::AllowedMethods
  
    Included in:
    Layout::EmptyLinesAroundAttributeAccessor, Layout::FirstMethodArgumentLineBreak, Lint::AmbiguousBlockAssociation, Lint::ConstantDefinitionInBlock, Lint::NestedMethodDefinition, Lint::NumberConversion, Lint::RedundantSafeNavigation, MethodComplexity, Metrics::BlockLength, Metrics::MethodLength, Naming::PredicateMethod, Naming::PredicatePrefix, NilMethods, Style::BlockDelimiters, Style::ClassEqualityComparison, Style::FormatStringToken, Style::IfWithBooleanLiteralBranches, Style::MethodCallWithArgsParentheses, Style::MethodCallWithoutArgsParentheses, Style::ModuleMemberExistenceCheck, Style::NestedParenthesizedCalls, Style::NumericPredicate, Style::OptionalBooleanParameter, Style::RedundantCondition, Style::ReturnNilInPredicateMethodDefinition, Style::SymbolProc, Style::TrivialAccessors
  
  

  
  
    Defined in:
    lib/rubocop/cop/mixin/allowed_methods.rb
  
## Overview

This module encapsulates the ability to allow certain methods when parsing. Even if the code is in offense, if it contains methods that are allowed. This module is equivalent to the IgnoredMethods module, which will be deprecated in RuboCop 2.0.
