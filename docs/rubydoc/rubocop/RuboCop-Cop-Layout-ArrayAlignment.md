# Class: RuboCop::Cop::Layout::ArrayAlignment
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Layout::ArrayAlignment

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      Alignment
  
    Defined in:
    lib/rubocop/cop/layout/array_alignment.rb
  
## Overview

Checks that the elements of a multi-line array literal are aligned.

#### Examples

#####

EnforcedStyle: with_first_element (default)

```
# good

array = [1, 2, 3,
         4, 5, 6]
array = ['run',
         'forrest',
         'run']

# bad

array = [1, 2, 3,
  4, 5, 6]
array = ['run',
     'forrest',
     'run']

```

#####

EnforcedStyle: with_fixed_indentation

```
# good

array = [1, 2, 3,
  4, 5, 6]

# bad

array = [1, 2, 3,
         4, 5, 6]

```

##

      Constant Summary
      collapse
    

    
      
        ALIGN_ELEMENTS_MSG =
          
        
        

```
'Align the elements of an array literal ' \
'if they span more than one line.'

```

        FIXED_INDENT_MSG =
          
        
        

```
'Use one level of indentation for elements ' \
'following the first line of a multi-line array.'

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
  
      #**on_array**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**on_array**(node)  ⇒ Object 
  

  

  

  
    
      

```

46
47
48
49
50
51
```

```
# File 'lib/rubocop/cop/layout/array_alignment.rb', line 46

def on_array(node)
  return if node.children.size < 2
  return if node.parent&.masgn_type?

  check_alignment(node.children, base_column(node, node.children))
end

```
