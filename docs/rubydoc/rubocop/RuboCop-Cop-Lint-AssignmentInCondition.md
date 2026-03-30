# Class: RuboCop::Cop::Lint::AssignmentInCondition
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Lint::AssignmentInCondition

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      SafeAssignment
  
    Defined in:
    lib/rubocop/cop/lint/assignment_in_condition.rb
  
## Overview

Checks for assignments in the conditions of if/while/until.

`AllowSafeAssignment` option for safe assignment. By safe assignment we mean putting parentheses around an assignment to indicate “I know I’m using an assignment as a condition. It’s not a mistake.”

#### Examples

```
# bad
if some_var = value
  do_something
end

# good
if some_var == value
  do_something
end

```

#####

AllowSafeAssignment: true (default)

```
# good
if (some_var = value)
  do_something
end

```

#####

AllowSafeAssignment: false

```
# bad
if (some_var = value)
  do_something
end

```

##

      Constant Summary
      collapse
    

    
      
        MSG_WITH_SAFE_ASSIGNMENT_ALLOWED =
          
        
        

```
'Use `==` if you meant to do a comparison or wrap the expression ' \
'in parentheses to indicate you meant to assign in a ' \
'condition.'

```

        MSG_WITHOUT_SAFE_ASSIGNMENT_ALLOWED =
          
        
        

```
'Use `==` if you meant to do a comparison or move the assignment ' \
'up out of the condition.'

```

        ASGN_TYPES =
          
        
        

```
[:begin, *AST::Node::EQUALS_ASSIGNMENTS, :send, :csend].freeze

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
  
      #**on_if**(node)  ⇒ Object 
    

    
      (also: #on_while, #on_until)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**on_if**(node)  ⇒ Object 
  

  
    Also known as:
    on_while, on_until
    
  

  

  
    
      

```

55
56
57
58
59
60
61
62
63
64
65
66
```

```
# File 'lib/rubocop/cop/lint/assignment_in_condition.rb', line 55

def on_if(node)
  traverse_node(node.condition) do |asgn_node|
    next :skip_children if skip_children?(asgn_node)
    next if allowed_construct?(asgn_node)

    add_offense(asgn_node.loc.operator) do |corrector|
      next unless safe_assignment_allowed?

      corrector.wrap(asgn_node, '(', ')')
    end
  end
end

```
