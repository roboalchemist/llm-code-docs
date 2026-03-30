# Class: RuboCop::Cop::Naming::AccessorMethodName
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Naming::AccessorMethodName

        show all
      

    Defined in:
    lib/rubocop/cop/naming/accessor_method_name.rb
  
## Overview

Avoid prefixing accessor method names with `get_` or `set_`. Applies to both instance and class methods.

NOTE: Method names starting with `get_` or `set_` only register an offense when the methods match the expected arity for getters and setters respectively. Getters (`get_attribute`) must have no arguments to be registered, and setters (‘set_attribute(value)`) must have exactly one.

#### Examples

```
# bad
def set_attribute(value)
end

# good
def attribute=(value)
end

# bad
def get_attribute
end

# good
def attribute
end

# accepted, incorrect arity for getter
def get_value(attr)
end

# accepted, incorrect arity for setter
def set_value
end

```

##

      Constant Summary
      collapse
    

    
      
        MSG_READER =
          
        
        

```
'Do not prefix reader method names with `get_`.'

```

        MSG_WRITER =
          
        
        

```
'Do not prefix writer method names with `set_`.'

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
  
      #**on_def**(node)  ⇒ Object 
    

    
      (also: #on_defs)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**on_def**(node)  ⇒ Object 
  

  
    Also known as:
    on_defs
    
  

  

  
    
      

```

42
43
44
45
46
47
48
49
```

```
# File 'lib/rubocop/cop/naming/accessor_method_name.rb', line 42

def on_def(node)
  return unless proper_attribute_name?(node)
  return unless bad_reader_name?(node) || bad_writer_name?(node)

  message = message(node)

  add_offense(node.loc.name, message: message)
end

```
