# Class: RuboCop::Cop::Style::ArrayJoin
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::ArrayJoin

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
    Defined in:
    lib/rubocop/cop/style/array_join.rb
  
## Overview

Checks for uses of ‘*` as a substitute for `Array#join`. Using`join` is clearer about intent and more readable than overloading the `*` operator for string conversion.

Not all cases can be reliably checked, due to Ruby’s dynamic types, so we consider only cases when the first argument is an array literal or the second is a string literal.

#### Examples

```

# bad
%w(foo bar baz) * ","

# good
%w(foo bar baz).join(",")

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Favor `Array#join` over `Array#*`.'

```

        RESTRICT_ON_SEND =
          
        
        

```
i[*].freeze

```

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**join_candidate?**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

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
  
    #**join_candidate?**(node)  ⇒ Object 
  

  

  

  
    
      

```

29
```

```
# File 'lib/rubocop/cop/style/array_join.rb', line 29

def_node_matcher :join_candidate?, '(send $array :* $str)'

```

###
  
    #**on_send**(node)  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
34
35
36
37
```

```
# File 'lib/rubocop/cop/style/array_join.rb', line 31

def on_send(node)
  return unless (array, join_arg = join_candidate?(node))

  add_offense(node.loc.selector) do |corrector|
    corrector.replace(node, "#{array.source}.join(#{join_arg.source})")
  end
end

```
