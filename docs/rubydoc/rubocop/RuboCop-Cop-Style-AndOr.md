# Class: RuboCop::Cop::Style::AndOr
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::AndOr

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      ConfigurableEnforcedStyle, RangeHelp
  
    Defined in:
    lib/rubocop/cop/style/and_or.rb
  
## Overview

Checks for uses of `and` and `or`, and suggests using ‘&&` and `||` instead. It can be configured to check only in conditions or in all contexts.

#### Examples

#####

EnforcedStyle: conditionals (default)

```
# bad
if foo and bar
end

# good
foo.save && return

# good
foo.save and return

# good
if foo && bar
end

```

#####

EnforcedStyle: always

```
# bad
foo.save and return

# bad
if foo and bar
end

# good
foo.save && return

# good
if foo && bar
end

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Use `%<prefer>s` instead of `%<current>s`.'

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
  
      #**on_and**(node)  ⇒ Object 
    

    
      (also: #on_or)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_if**(node)  ⇒ Object 
    

    
      (also: #on_while, #on_while_post, #on_until, #on_until_post)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from ConfigurableEnforcedStyle

# alternative_style, #alternative_styles, #ambiguous_style_detected, #correct_style_detected, #detected_style, #detected_style=, #no_acceptable_style!, #no_acceptable_style?, #opposite_style_detected, #style, #style_configured?, #style_detected, #style_parameter_name, #supported_styles, #unexpected_style_detected

### Methods inherited from Base

# active_support_extensions_enabled?, #add_global_offense, #add_offense, #always_autocorrect?, autocorrect_incompatible_with, badge, #begin_investigation, #callbacks_needed, callbacks_needed, #config_to_allow_offenses, #config_to_allow_offenses=, #contextual_autocorrect?, #cop_config, cop_name, #cop_name, department, documentation_url, exclude_from_registry, #excluded_file?, #external_dependency_checksum, inherited, #initialize, #inspect, joining_forces, lint?, match?, #offenses, #on_investigation_end, #on_new_investigation, #on_other_file, #parse, #parser_engine, #ready, #relevant_file?, requires_gem, #string_literals_frozen_by_default?, support_autocorrect?, support_multiple_source?, #target_gem_version, #target_rails_version, #target_ruby_version

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
  
    #**on_and**(node)  ⇒ Object 
  

  
    Also known as:
    on_or
    
  

  

  
    
      

```

51
52
53
```

```
# File 'lib/rubocop/cop/style/and_or.rb', line 51

def on_and(node)
  process_logical_operator(node) if style == :always
end

```

###
  
    #**on_if**(node)  ⇒ Object 
  

  
    Also known as:
    on_while, on_while_post, on_until, on_until_post
    
  

  

  
    
      

```

56
57
58
```

```
# File 'lib/rubocop/cop/style/and_or.rb', line 56

def on_if(node)
  on_conditionals(node) if style == :conditionals
end

```
