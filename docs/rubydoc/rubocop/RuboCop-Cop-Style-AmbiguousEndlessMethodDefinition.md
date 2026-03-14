# Class: RuboCop::Cop::Style::AmbiguousEndlessMethodDefinition
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::AmbiguousEndlessMethodDefinition

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector, TargetRubyVersion
  
  
  
  
  
      Includes:
      EndlessMethodRewriter, RangeHelp
  
    Defined in:
    lib/rubocop/cop/style/ambiguous_endless_method_definition.rb
  
## Overview

Looks for endless methods inside operations of lower precedence (`and`, `or`, and modifier forms of `if`, `unless`, `while`, `until`) that are ambiguous due to lack of parentheses. This may lead to unexpected behavior as the code may appear to use these keywords as part of the method but in fact they modify the method definition itself.

In these cases, using a normal method definition is more clear.

#### Examples

```

# bad
def foo = true if bar

# good - using a non-endless method is more explicit
def foo
  true
end if bar

# ok - method body is explicit
def foo = (true if bar)

# ok - method definition is explicit
(def foo = true) if bar

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Avoid using `%<keyword>s` statements with endless methods.'

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
  
      #**ambiguous_endless_method_body**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_def**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from TargetRubyVersion

maximum_target_ruby_version, minimum_target_ruby_version, required_maximum_ruby_version, required_minimum_ruby_version, support_target_ruby_version?

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from EndlessMethodRewriter

# correct_to_multiline

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
  
    #**ambiguous_endless_method_body**(node)  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
43
44
45
46
```

```
# File 'lib/rubocop/cop/style/ambiguous_endless_method_definition.rb', line 40

def_node_matcher :ambiguous_endless_method_body, "^${\n  (if _ <def _>)\n  ({and or} def _)\n  ({while until} _ def)\n}\n"

```

###
  
    #**on_def**(node)  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
51
52
53
54
55
56
57
58
59
```

```
# File 'lib/rubocop/cop/style/ambiguous_endless_method_definition.rb', line 48

def on_def(node)
  return unless node.endless?

  operation = ambiguous_endless_method_body(node)
  return unless operation

  return unless modifier_form?(operation)

  add_offense(operation, message: format(MSG, keyword: keyword(operation))) do |corrector|
    correct_to_multiline(corrector, node)
  end
end

```
