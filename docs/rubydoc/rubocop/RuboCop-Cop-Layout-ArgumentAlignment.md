# Class: RuboCop::Cop::Layout::ArgumentAlignment
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Layout::ArgumentAlignment

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      Alignment
  
    Defined in:
    lib/rubocop/cop/layout/argument_alignment.rb
  
## Overview

Checks that the arguments on a multi-line method call are aligned.

#### Examples

#####

EnforcedStyle: with_first_argument (default)

```
# good

foo :bar,
    :baz,
    key: value

foo(
  :bar,
  :baz,
  key: value
)

# bad

foo :bar,
  :baz,
  key: value

foo(
  :bar,
    :baz,
    key: value
)
```

#####

EnforcedStyle: with_fixed_indentation

```
# good

foo :bar,
  :baz,
  key: value

# bad

foo :bar,
    :baz,
    key: value
```

##

      Constant Summary
      collapse
    

    
      
        ALIGN_PARAMS_MSG =
          
        
        

```
'Align the arguments of a method call if they span more than one line.'
```

        FIXED_INDENT_MSG =
          
        
        

```
'Use one level of indentation for arguments ' \
'following the first line of a multi-line method call.'
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

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
      (also: #on_csend)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

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
  
    #**on_send**(node)  ⇒ Object 
  

  
    Also known as:
    on_csend
    
  

  

  
    
      

```

54
55
56
57
58
59
60
61
```

```
# File 'lib/rubocop/cop/layout/argument_alignment.rb', line 54

def on_send(node)
  return if !multiple_arguments?(node) || (node.send_type? && node.method?(:[]=)) ||
            autocorrect_incompatible_with_other_cops?

  items = flattened_arguments(node)

  check_alignment(items, base_column(node, items.first))
end
```
