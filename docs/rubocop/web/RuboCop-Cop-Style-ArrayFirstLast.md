# Class: RuboCop::Cop::Style::ArrayFirstLast
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::ArrayFirstLast

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
    Defined in:
    lib/rubocop/cop/style/array_first_last.rb
  
## Overview

Identifies usages of `arr[0]` and `arr[-1]` and suggests to change them to use `arr.first` and `arr.last` instead.

The cop is disabled by default due to safety concerns.

#### Examples

```
# bad
arr[0]
arr[-1]

# good
arr.first
arr.last
arr[0] = 2
arr[0][-2]

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Use `%<preferred>s`.'

```

        RESTRICT_ON_SEND =
          
        
        

```
i[[]].freeze

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
    
  
  
  
  
  
  
  
  

  
    

rubocop:disable Metrics/AbcSize.

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
    
  

  

  
    

rubocop:disable Metrics/AbcSize

```

35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
```

```
# File 'lib/rubocop/cop/style/array_first_last.rb', line 35

def on_send(node)
  return unless node.arguments.size == 1 && node.first_argument.int_type?

  value = node.first_argument.value
  return unless [0, -1].include?(value)

  node = innermost_braces_node(node)
  return if node.parent && brace_method?(node.parent)

  preferred = (value.zero? ? 'first' : 'last')
  offense_range = find_offense_range(node)

  add_offense(offense_range, message: format(MSG, preferred: preferred)) do |corrector|
    corrector.replace(offense_range, preferred_value(node, preferred))
  end
end

```
