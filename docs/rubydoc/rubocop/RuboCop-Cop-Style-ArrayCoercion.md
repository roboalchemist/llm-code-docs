# Class: RuboCop::Cop::Style::ArrayCoercion
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::ArrayCoercion

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
    Defined in:
    lib/rubocop/cop/style/array_coercion.rb
  
## Overview

Enforces the use of ‘Array()` instead of explicit `Array` check or `[*var]`.

The cop is disabled by default due to safety concerns.

#### Examples

```
# bad
paths = [paths] unless paths.is_a?(Array)
paths.each { |path| do_something(path) }

# bad (always creates a new Array instance)
[*paths].each { |path| do_something(path) }

# good (and a bit more readable)
Array(paths).each { |path| do_something(path) }

```

##

      Constant Summary
      collapse
    

    
      
        SPLAT_MSG =
          
        
        

```
'Use `Array(%<arg>s)` instead of `[*%<arg>s]`.'

```

        CHECK_MSG =
          
        
        

```
'Use `Array(%<arg>s)` instead of explicit `Array` check.'

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
  
      #**array_splat?**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_array**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_if**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**unless_array?**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**array_splat?**(node)  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
```

```
# File 'lib/rubocop/cop/style/array_coercion.rb', line 48

def_node_matcher :array_splat?, "(array (splat $_))\n"

```

###
  
    #**on_array**(node)  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/rubocop/cop/style/array_coercion.rb', line 63

def on_array(node)
  return unless node.square_brackets?

  array_splat?(node) do |arg_node|
    message = format(SPLAT_MSG, arg: arg_node.source)
    add_offense(node, message: message) do |corrector|
      corrector.replace(node, "Array(#{arg_node.source})")
    end
  end
end

```

###
  
    #**on_if**(node)  ⇒ Object 
  

  

  

  
    
      

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
```

```
# File 'lib/rubocop/cop/style/array_coercion.rb', line 74

def on_if(node)
  unless_array?(node) do |var_a, var_b, var_c|
    if var_a == var_b && var_c == var_b
      message = format(CHECK_MSG, arg: var_a)
      add_offense(node, message: message) do |corrector|
        corrector.replace(node, "#{var_a} = Array(#{var_a})")
      end
    end
  end
end

```

###
  
    #**unless_array?**(node)  ⇒ Object 
  

  

  

  
    
      

```

53
54
55
56
57
58
59
60
61
```

```
# File 'lib/rubocop/cop/style/array_coercion.rb', line 53

def_node_matcher :unless_array?, "(if\n  (send\n    (lvar $_) :is_a?\n    (const nil? :Array)) nil?\n  (lvasgn $_\n    (array\n      (lvar $_))))\n"

```
