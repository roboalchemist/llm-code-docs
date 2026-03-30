# Class: RuboCop::Cop::Style::BeginBlock
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::BeginBlock

        show all
      

    Defined in:
    lib/rubocop/cop/style/begin_block.rb
  
## Overview

Checks for `BEGIN` blocks. They are Perl-style constructs that execute code before the rest of the file is parsed, making the control flow harder to follow and reason about.

#### Examples

```
# bad
BEGIN { test }
```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Avoid the use of `BEGIN` blocks.'
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
  
      #**on_preexe**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**on_preexe**(node)  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

```
# File 'lib/rubocop/cop/style/begin_block.rb', line 17

def on_preexe(node)
  add_offense(node.loc.keyword)
end
```
