# Class: RuboCop::Cop::Style::BitwisePredicate
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::BitwisePredicate

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector, TargetRubyVersion
  
    Defined in:
    lib/rubocop/cop/style/bitwise_predicate.rb
  
## Overview

Prefer bitwise predicate methods over direct comparison operations.

#### Examples

```

# bad - checks any set bits
(variable & flags).positive?

# good
variable.anybits?(flags)

# bad - checks all set bits
(variable & flags) == flags

# good
variable.allbits?(flags)

# bad - checks no set bits
(variable & flags).zero?

# good
variable.nobits?(flags)
```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Replace with `%<preferred>s` for comparison with bit flags.'
```

        RESTRICT_ON_SEND =
          
        
        

```
%i[!= == > >= positive? zero?].freeze
```

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**allbits?**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**anybits?**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**bit_operation?**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**nobits?**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

rubocop:disable Metrics/AbcSize.

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from TargetRubyVersion

maximum_target_ruby_version, minimum_target_ruby_version, required_maximum_ruby_version, required_minimum_ruby_version, support_target_ruby_version?

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
  
    #**allbits?**(node)  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
55
56
57
```

```
# File 'lib/rubocop/cop/style/bitwise_predicate.rb', line 52

def_node_matcher :allbits?, <<~PATTERN
  {
    (send (begin (send _ :& _flags)) :== _flags)
    (send (begin (send _flags :& _)) :== _flags)
  }
PATTERN
```

###
  
    #**anybits?**(node)  ⇒ Object 
  

  

  

  
    
      

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
# File 'lib/rubocop/cop/style/bitwise_predicate.rb', line 42

def_node_matcher :anybits?, <<~PATTERN
  {
    (send #bit_operation? :positive?)
    (send #bit_operation? :> (int 0))
    (send #bit_operation? :>= (int 1))
    (send #bit_operation? :!= (int 0))
  }
PATTERN
```

###
  
    #**bit_operation?**(node)  ⇒ Object 
  

  

  

  
    
      

```

68
69
70
71
```

```
# File 'lib/rubocop/cop/style/bitwise_predicate.rb', line 68

def_node_matcher :bit_operation?, <<~PATTERN
  (begin
    (send _ :& _))
PATTERN
```

###
  
    #**nobits?**(node)  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
63
64
65
```

```
# File 'lib/rubocop/cop/style/bitwise_predicate.rb', line 60

def_node_matcher :nobits?, <<~PATTERN
  {
    (send #bit_operation? :zero?)
    (send #bit_operation? :== (int 0))
  }
PATTERN
```

###
  
    #**on_send**(node)  ⇒ Object 
  

  

  

  
    

rubocop:disable Metrics/AbcSize

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
83
84
85
86
87
88
89
90
```

```
# File 'lib/rubocop/cop/style/bitwise_predicate.rb', line 74

def on_send(node)
  return unless node.receiver&.begin_type?
  return unless (preferred_method = preferred_method(node))

  bit_operation = node.receiver.children.first
  lhs, _operator, rhs = *bit_operation

  preferred = if preferred_method == 'allbits?' && lhs.source == node.first_argument.source
                "#{rhs.source}.allbits?(#{lhs.source})"
              else
                "#{lhs.source}.#{preferred_method}(#{rhs.source})"
              end

  add_offense(node, message: format(MSG, preferred: preferred)) do |corrector|
    corrector.replace(node, preferred)
  end
end
```
