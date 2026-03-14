# Class: RuboCop::Cop::Style::ArrayIntersectWithSingleElement
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::ArrayIntersectWithSingleElement

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
    Defined in:
    lib/rubocop/cop/style/array_intersect_with_single_element.rb
  
## Overview

Use ‘include?(element)` instead of `intersect?()`.

#### Examples

```
# bad
array.intersect?([element])

# good
array.include?(element)
```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Use `include?(element)` instead of `intersect?([element])`.'
```

        RESTRICT_ON_SEND =
          
        
        

```
%i[intersect?].freeze
```

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
      (also: #on_csend)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**single_element**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**on_send**(node)  ⇒ Object 
  

  
    Also known as:
    on_csend
    
  

  

  
    
      

```

29
30
31
32
33
34
35
36
37
38
39
40
41
42
```

```
# File 'lib/rubocop/cop/style/array_intersect_with_single_element.rb', line 29

def on_send(node)
  array, element = single_element(node)
  return unless array

  add_offense(
    node.source_range.with(begin_pos: node.loc.selector.begin_pos)
  ) do |corrector|
    corrector.replace(node.loc.selector, 'include?')
    corrector.replace(
      array,
      array.percent_literal? ? element.value.inspect : element.source
    )
  end
end
```

###
  
    #**single_element**(node)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

```
# File 'lib/rubocop/cop/style/array_intersect_with_single_element.rb', line 25

def_node_matcher :single_element, <<~PATTERN
  (send _ _ $(array $_))
PATTERN
```
