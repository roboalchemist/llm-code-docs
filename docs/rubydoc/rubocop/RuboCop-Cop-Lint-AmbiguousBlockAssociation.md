# Class: RuboCop::Cop::Lint::AmbiguousBlockAssociation
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Lint::AmbiguousBlockAssociation

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      AllowedMethods, AllowedPattern
  
    Defined in:
    lib/rubocop/cop/lint/ambiguous_block_association.rb
  
## Overview

Checks for ambiguous block association with method when param passed without parentheses.

This cop can customize allowed methods with `AllowedMethods`. By default, there are no methods to allowed.

#### Examples

```

# bad
some_method a { |val| puts val }

# good
# With parentheses, there's no ambiguity.
some_method(a { |val| puts val })
# or (different meaning)
some_method(a) { |val| puts val }

# good
# Operator methods require no disambiguation
foo == bar { |b| b.baz }

# good
# Lambda arguments require no disambiguation
foo = ->(bar) { bar.baz }

```

#####

AllowedMethods: [] (default)

```

# bad
expect { do_something }.to change { object.attribute }

```

#####

AllowedMethods: [change]

```

# good
expect { do_something }.to change { object.attribute }

```

#####

AllowedPatterns: [] (default)

```

# bad
expect { do_something }.to change { object.attribute }

```

#####

AllowedPatterns: [‘change’]

```

# good
expect { do_something }.to change { object.attribute }
expect { do_something }.to not_change { object.attribute }

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Parenthesize the param `%<param>s` to make sure that the ' \
'block will be associated with the `%<method>s` method ' \
'call.'

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

62
63
64
65
66
67
68
69
70
71
72
73
74
```

```
# File 'lib/rubocop/cop/lint/ambiguous_block_association.rb', line 62

def on_send(node)
  return unless node.arguments?

  return unless ambiguous_block_association?(node)
  return if node.parenthesized? || node.last_argument.lambda_or_proc? ||
            allowed_method_pattern?(node)

  message = message(node)

  add_offense(node, message: message) do |corrector|
    wrap_in_parentheses(corrector, node)
  end
end

```
