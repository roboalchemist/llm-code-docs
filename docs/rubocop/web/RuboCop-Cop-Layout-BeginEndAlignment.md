# Class: RuboCop::Cop::Layout::BeginEndAlignment
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Layout::BeginEndAlignment

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      EndKeywordAlignment
  
    Defined in:
    lib/rubocop/cop/layout/begin_end_alignment.rb
  
## Overview

Checks whether the end keyword of `begin` is aligned properly.

Two modes are supported through the `EnforcedStyleAlignWith` configuration parameter. If it’s set to `start_of_line` (which is the default), the `end` shall be aligned with the start of the line where the `begin` keyword is. If it’s set to `begin`, the `end` shall be aligned with the `begin` keyword.

`Layout/EndAlignment` cop aligns with keywords (e.g. `if`, `while`, `case`) by default. On the other hand, ‘||= begin` that this cop targets tends to align with the start of the line, it defaults to `EnforcedStyleAlignWith: start_of_line`. These style can be configured by each cop.

#### Examples

#####

EnforcedStyleAlignWith: start_of_line (default)

```
# bad
foo ||= begin
          do_something
        end

# good
foo ||= begin
  do_something
end

```

#####

EnforcedStyleAlignWith: begin

```
# bad
foo ||= begin
  do_something
end

# good
foo ||= begin
          do_something
        end

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'`end` at %d, %d is not aligned with `%s` at %d, %d.'

```

### Constants included

     from RangeHelp

RangeHelp::BYTE_ORDER_MARK, RangeHelp::NOT_GIVEN

### Constants inherited

     from Base

Base::RESTRICT_ON_SEND

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**on_kwbegin**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from ConfigurableEnforcedStyle

# alternative_style, #alternative_styles, #ambiguous_style_detected, #correct_style_detected, #detected_style, #detected_style=, #no_acceptable_style!, #no_acceptable_style?, #opposite_style_detected, #style, #style_configured?, #style_detected, #style_parameter_name, #supported_styles, #unexpected_style_detected

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
  
## Instance Method Details

###
  
    #**on_kwbegin**(node)  ⇒ Object 
  

  

  

  
    
      

```

47
48
49
```

```
# File 'lib/rubocop/cop/layout/begin_end_alignment.rb', line 47

def on_kwbegin(node)
  check_begin_alignment(node)
end

```
