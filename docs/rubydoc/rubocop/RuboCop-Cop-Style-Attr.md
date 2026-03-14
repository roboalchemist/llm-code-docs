# Class: RuboCop::Cop::Style::Attr
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::Attr

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      RangeHelp
  
    Defined in:
    lib/rubocop/cop/style/attr.rb
  
## Overview

Checks for uses of ‘Module#attr`. The`attr` method has confusing behavior: with a single argument it creates a reader (like `attr_reader`), but with a second boolean argument it creates an accessor (deprecated in Ruby 1.9). Use`attr_reader` or `attr_accessor` to make intent explicit.

#### Examples

```
# bad
attr :something, true
attr :one, :two, :three # behaves as attr_reader

# good
attr_accessor :something
attr_reader :one, :two, :three
```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Do not use `attr`. Use `%<replacement>s` instead.'
```

        RESTRICT_ON_SEND =
          
        
        

```
%i[attr].freeze
```

### Constants included

     from RangeHelp

RangeHelp::BYTE_ORDER_MARK, RangeHelp::NOT_GIVEN

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  

  

  

  
    
      

```

27
28
29
30
31
32
33
34
35
36
```

```
# File 'lib/rubocop/cop/style/attr.rb', line 27

def on_send(node)
  return unless node.command?(:attr) && node.arguments?
  # check only for method definitions in class/module body
  return if allowed_context?(node)

  message = message(node)
  add_offense(node.loc.selector, message: message) do |corrector|
    autocorrect(corrector, node)
  end
end
```
