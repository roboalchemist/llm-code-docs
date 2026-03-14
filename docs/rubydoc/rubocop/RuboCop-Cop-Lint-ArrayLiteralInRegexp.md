# Class: RuboCop::Cop::Lint::ArrayLiteralInRegexp
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Lint::ArrayLiteralInRegexp

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      Interpolation
  
    Defined in:
    lib/rubocop/cop/lint/array_literal_in_regexp.rb
  
## Overview

Checks for an array literal interpolated inside a regexp.

When interpolating an array literal, it is converted to a string. This means that when inside a regexp, it acts as a character class but with additional quotes, spaces and commas that are likely not intended. For example, ‘/#b c]/` parses as `/[“a”, “b”, “c”]/` (or `/[“a, bc]/` without repeated characters).

The cop can autocorrect to a character class (if all items in the array are a single character) or alternation (if the array contains longer items).

NOTE: This only considers interpolated arrays that contain only strings, symbols, integers, and floats. Any other type is not easily convertible to a character class or regexp alternation.

#### Examples

```
# bad
/#{%w[a b c]}/

# good
/[abc]/

# bad
/#{%w[foo bar baz]}/

# good
/(?:foo|bar|baz)/

# bad - construct a regexp rather than interpolate an array of identifiers
/#{[foo, bar]}/

```

##

      Constant Summary
      collapse
    

    
      
        MSG_CHARACTER_CLASS =
          
        
        

```
'Use a character class instead of interpolating an array in a regexp.'

```

        MSG_ALTERNATION =
          
        
        

```
'Use alternation instead of interpolating an array in a regexp.'

```

        MSG_UNKNOWN =
          
        
        

```
'Use alternation or a character class instead of interpolating an array ' \
'in a regexp.'

```

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
  
      #**on_interpolation**(begin_node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from Interpolation

# on_dstr, #on_node_with_interpolations

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
  
    #**on_interpolation**(begin_node)  ⇒ Object 
  

  

  

  
    
      

```

53
54
55
56
57
58
59
60
61
62
63
```

```
# File 'lib/rubocop/cop/lint/array_literal_in_regexp.rb', line 53

def on_interpolation(begin_node)
  return unless (final_node = begin_node.children.last)
  return unless final_node.array_type?
  return unless begin_node.parent.regexp_type?

  if array_of_literal_values?(final_node)
    register_array_of_literal_values(begin_node, final_node)
  else
    register_array_of_nonliteral_values(begin_node)
  end
end

```
