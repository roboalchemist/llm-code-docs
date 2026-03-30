# Class: RuboCop::Cop::Layout::AssignmentIndentation
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Layout::AssignmentIndentation

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      Alignment, CheckAssignment
  
    Defined in:
    lib/rubocop/cop/layout/assignment_indentation.rb
  
## Overview

Checks the indentation of the first line of the right-hand-side of a multi-line assignment.

The indentation of the remaining lines can be corrected with other cops such as `Layout/IndentationConsistency` and `Layout/EndAlignment`.

#### Examples

```
# bad
value =
if foo
  'bar'
end

# good
value =
  if foo
    'bar'
  end

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Indent the first line of the right-hand-side of a multi-line assignment.'

```

### Constants included

     from Alignment

Alignment::SPACE

### Constants inherited

     from Base

Base::RESTRICT_ON_SEND

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

## Method Summary

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from CheckAssignment

extract_rhs, #on_lvasgn, #on_send

### Methods inherited from Base

# active_support_extensions_enabled?, #add_global_offense, #add_offense, #always_autocorrect?, autocorrect_incompatible_with, badge, #begin_investigation, #callbacks_needed, callbacks_needed, #config_to_allow_offenses, #config_to_allow_offenses=, #contextual_autocorrect?, #cop_config, #cop_name, cop_name, department, documentation_url, exclude_from_registry, #excluded_file?, #external_dependency_checksum, inherited, #initialize, #inspect, joining_forces, lint?, match?, #message, #offenses, #on_investigation_end, #on_new_investigation, #on_other_file, #parse, #parser_engine, #ready, #relevant_file?, requires_gem, #string_literals_frozen_by_default?, support_autocorrect?, support_multiple_source?, #target_gem_version, #target_rails_version, #target_ruby_version

### Methods included from ExcludeLimit

# exclude_limit

### Methods included from AutocorrectLogic

# autocorrect?, #autocorrect_enabled?, #autocorrect_requested?, #autocorrect_with_disable_uncorrectable?, #correctable?, #disable_uncorrectable?, #safe_autocorrect?

### Methods included from IgnoredNode

# ignore_node, #ignored_node?, #part_of_ignored_node?

### Methods included from Util

silence_warnings

## Constructor Details

This class inherits a constructor from RuboCop::Cop::Base
