# Class: RuboCop::Cop::Lint::BinaryOperatorWithIdenticalOperands
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Lint::BinaryOperatorWithIdenticalOperands

        show all
      

    Defined in:
    lib/rubocop/cop/lint/binary_operator_with_identical_operands.rb
  
## Overview

Checks for places where binary operator has identical operands.

It covers comparison operators: ‘==`,`===`,`=~`,`>`,`>=`,`<`, “<=“; bitwise operators:`|`,`^`,`&`; boolean operators:`&&`,`||` and “spaceship” operator - “<=>“.

Simple arithmetic operations are allowed by this cop: ‘+`,`*`,`**`,`<<` and `>>`. Although these can be rewritten in a different way, it should not be necessary to do so. Operations such as`-` or `/`where the result will always be the same (`x - x` will always be 0; `x / x` will always be 1) are offenses, but these are covered by `Lint/NumericOperationWithConstantResult` instead.

#### Examples

```
# bad
x.top >= x.top

if a.x != 0 && a.x != 0
  do_something
end

def child?
  left_child || left_child
end

# good
x + x
1 << 1

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Binary operator `%<op>s` has identical operands.'

```

        RESTRICT_ON_SEND =
          
        
        

```
i[== != === <=> =~ && || > >= < <= | ^].freeze

```

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
  
      #**on_send**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**on_and**(node)  ⇒ Object 
  

  
    Also known as:
    on_or
    
  

  

  
    
      

```

57
58
59
60
61
```

```
# File 'lib/rubocop/cop/lint/binary_operator_with_identical_operands.rb', line 57

def on_and(node)
  return unless node.lhs == node.rhs

  add_offense(node, message: format(MSG, op: node.operator))
end

```

###
  
    #**on_send**(node)  ⇒ Object 
  

  

  

  
    
      

```

50
51
52
53
54
55
```

```
# File 'lib/rubocop/cop/lint/binary_operator_with_identical_operands.rb', line 50

def on_send(node)
  return unless node.binary_operation?
  return unless node.receiver == node.first_argument

  add_offense(node, message: format(MSG, op: node.method_name))
end

```
