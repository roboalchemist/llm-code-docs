# Class: RuboCop::Cop::Lint::AmbiguousOperatorPrecedence
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Lint::AmbiguousOperatorPrecedence

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
    Defined in:
    lib/rubocop/cop/lint/ambiguous_operator_precedence.rb
  
## Overview

Looks for expressions containing multiple binary operators where precedence is ambiguous due to lack of parentheses. For example, in ‘1 + 2 * 3`, the multiplication will happen before the addition, but lexically it appears that the addition will happen first.

The cop does not consider unary operators (ie. ‘!a` or `-b`) or comparison operators (ie.`a =~ b`) because those are not ambiguous.

NOTE: Ranges are handled by `Lint/AmbiguousRange`.

#### Examples

```
# bad
a + b * c
a || b && c
a ** b + c

# good (different precedence)
a + (b * c)
a || (b && c)
(a ** b) + c

# good (same precedence)
a + b + c
a * b / c % d

```

##

      Constant Summary
      collapse
    

    
      
        PRECEDENCE =
          
  
    

See ruby-doc.org/core-3.0.2/doc/syntax/precedence_rdoc.html

```
[
  i[**],
  i[* / %],
  %i[+ -],
  %i[<< >>],
  %i[&],
  %i[| ^],
  %i[&&],
  %i[||]
].freeze

```

        RESTRICT_ON_SEND =
          
        
        

```
PRECEDENCE.flatten.freeze

```

        MSG =
          
        
        

```
'Wrap expressions with varying precedence with parentheses to avoid ambiguity.'

```

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**on_and**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_new_investigation**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods inherited from Base

# active_support_extensions_enabled?, #add_global_offense, #add_offense, #always_autocorrect?, autocorrect_incompatible_with, badge, #begin_investigation, #callbacks_needed, callbacks_needed, #config_to_allow_offenses, #config_to_allow_offenses=, #contextual_autocorrect?, #cop_config, cop_name, #cop_name, department, documentation_url, exclude_from_registry, #excluded_file?, #external_dependency_checksum, inherited, #initialize, #inspect, joining_forces, lint?, match?, #message, #offenses, #on_investigation_end, #on_other_file, #parse, #parser_engine, #ready, #relevant_file?, requires_gem, #string_literals_frozen_by_default?, support_autocorrect?, support_multiple_source?, #target_gem_version, #target_rails_version, #target_ruby_version

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
  

  

  

  
    
      

```

54
55
56
57
58
59
60
61
62
63
```

```
# File 'lib/rubocop/cop/lint/ambiguous_operator_precedence.rb', line 54

def on_and(node)
  return unless (parent = node.parent)

  return if parent.begin_type? # if the `and` is in a `begin`, it's parenthesized already
  return unless parent.or_type?

  add_offense(node) do |corrector|
    autocorrect(corrector, node)
  end
end

```

###
  
    #**on_new_investigation**  ⇒ Object 
  

  

  

  
    
      

```

47
48
49
50
51
52
```

```
# File 'lib/rubocop/cop/lint/ambiguous_operator_precedence.rb', line 47

def on_new_investigation
  # Cache the precedence of each node being investigated
  # so that we only need to calculate it once
  @node_precedences = {}
  super
end

```

###
  
    #**on_send**(node)  ⇒ Object 
  

  

  

  
    
      

```

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
75
```

```
# File 'lib/rubocop/cop/lint/ambiguous_operator_precedence.rb', line 65

def on_send(node)
  return if node.parenthesized?

  return unless (parent = node.parent)
  return unless operator?(parent)
  return unless greater_precedence?(node, parent)

  add_offense(node) do |corrector|
    autocorrect(corrector, node)
  end
end

```
