# Class: RuboCop::Cop::Layout::BlockAlignment
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Layout::BlockAlignment

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      ConfigurableEnforcedStyle, RangeHelp
  
    Defined in:
    lib/rubocop/cop/layout/block_alignment.rb
  
## Overview

Checks whether the end keywords are aligned properly for do end blocks.

Three modes are supported through the `EnforcedStyleAlignWith` configuration parameter:

`start_of_block` : the `end` shall be aligned with the start of the line where the `do` appeared.

`start_of_line` : the `end` shall be aligned with the start of the line where the expression started.

`either` (which is the default) : the `end` is allowed to be in either location. The autocorrect will default to `start_of_line`.

#### Examples

#####

EnforcedStyleAlignWith: either (default)

```
# bad

foo.bar
  .each do
    baz
      end

# good

foo.bar
  .each do
    baz
end

```

#####

EnforcedStyleAlignWith: start_of_block

```
# bad

foo.bar
  .each do
    baz
      end

# good

foo.bar
  .each do
    baz
  end

```

#####

EnforcedStyleAlignWith: start_of_line

```
# bad

foo.bar
  .each do
    baz
      end

# good

foo.bar
  .each do
    baz
end

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'%<current>s is not aligned with %<prefer>s%<alt_prefer>s.'

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
  
      #**block_end_align_target?**(node, child)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_block**(node)  ⇒ Object 
    

    
      (also: #on_numblock, #on_itblock)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**style_parameter_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from ConfigurableEnforcedStyle

# alternative_style, #alternative_styles, #ambiguous_style_detected, #correct_style_detected, #detected_style, #detected_style=, #no_acceptable_style!, #no_acceptable_style?, #opposite_style_detected, #style, #style_configured?, #style_detected, #supported_styles, #unexpected_style_detected

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
  
    #**block_end_align_target?**(node, child)  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
77
78
79
80
81
82
```

```
# File 'lib/rubocop/cop/layout/block_alignment.rb', line 74

def_node_matcher :block_end_align_target?, "{assignment?\n any_def\n splat\n and\n or\n (send _ :<<  ...)\n (send equal?(%1) !:[] ...)}\n"

```

###
  
    #**on_block**(node)  ⇒ Object 
  

  
    Also known as:
    on_numblock, on_itblock
    
  

  

  
    
      

```

84
85
86
```

```
# File 'lib/rubocop/cop/layout/block_alignment.rb', line 84

def on_block(node)
  check_block_alignment(start_for_block_node(node), node)
end

```

###
  
    #**style_parameter_name**  ⇒ Object 
  

  

  

  
    
      

```

91
92
93
```

```
# File 'lib/rubocop/cop/layout/block_alignment.rb', line 91

def style_parameter_name
  'EnforcedStyleAlignWith'
end

```
