# Class: RuboCop::Cop::Lint::AmbiguousAssignment
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Lint::AmbiguousAssignment

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      RangeHelp
  
    Defined in:
    lib/rubocop/cop/lint/ambiguous_assignment.rb
  
## Overview

Checks for mistyped shorthand assignments.

#### Examples

```
# bad
x =- y
x =+ y
x =* y
x =! y

# good
x -= y # or x = -y
x += y # or x = +y
x *= y # or x = *y
x != y # or x = !y
```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Suspicious assignment detected. Did you mean `%<op>s`?'
```

        SIMPLE_ASSIGNMENT_TYPES =
          
        
        

```
%i[lvasgn ivasgn cvasgn gvasgn casgn].freeze
```

        MISTAKES =
          
        
        

```
{ '=-' => '-=', '=+' => '+=', '=*' => '*=', '=!' => '!=' }.freeze
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
  
      #**on_asgn**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**on_asgn**(node)  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
33
34
35
36
37
38
```

```
# File 'lib/rubocop/cop/lint/ambiguous_assignment.rb', line 30

def on_asgn(node)
  return unless (rhs = rhs(node))

  range = range_between(node.loc.operator.end_pos - 1, rhs.source_range.begin_pos + 1)
  source = range.source
  return unless MISTAKES.key?(source)

  add_offense(range, message: format(MSG, op: MISTAKES[source]))
end
```
