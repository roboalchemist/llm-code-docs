# Module: RuboCop::Cop::Alignment
  
    Included in:
    AlignmentCorrector, Layout::AccessModifierIndentation, Layout::ArgumentAlignment, Layout::ArrayAlignment, Layout::AssignmentIndentation, Layout::BlockEndNewline, Layout::CaseIndentation, Layout::ClosingParenthesisIndentation, Layout::CommentIndentation, Layout::ElseAlignment, Layout::FirstArgumentIndentation, Layout::FirstArrayElementIndentation, Layout::FirstHashElementIndentation, Layout::FirstParameterIndentation, Layout::HeredocIndentation, Layout::IndentationConsistency, Layout::IndentationStyle, Layout::IndentationWidth, Layout::LineEndStringConcatenationIndentation, Layout::MultilineMethodCallIndentation, Layout::MultilineOperationIndentation, Layout::ParameterAlignment, LineBreakCorrector, LineLengthHelp, Lint::ElseLayout, Style::ClassAndModuleChildren, Style::ComparableClamp, Style::InfiniteLoop, Style::MultilineIfModifier, Style::MultilineMemoization, Style::OneLineConditional, Style::ParallelAssignment::GenericCorrector, Style::RedundantConditional, Style::RescueModifier, Style::SingleLineMethods, Style::TrailingBodyOnClass, Style::TrailingBodyOnMethodDefinition, Style::TrailingBodyOnModule
  
  

  
  
    Defined in:
    lib/rubocop/cop/mixin/alignment.rb
  
## Overview

This module checks for nodes that should be aligned to the left or right. This amount is determined by the instance variable @column_delta.

##

      Constant Summary
      collapse
    

    
      
        SPACE =
          
        
        

```
' '
```
