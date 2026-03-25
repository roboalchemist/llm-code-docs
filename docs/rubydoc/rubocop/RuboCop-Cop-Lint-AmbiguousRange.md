# Class: RuboCop::Cop::Lint::AmbiguousRange
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Lint::AmbiguousRange

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      RationalLiteral
  
    Defined in:
    lib/rubocop/cop/lint/ambiguous_range.rb
  
## Overview

Checks for ambiguous ranges.

Ranges have quite low precedence, which leads to unexpected behavior when using a range with other operators. This cop avoids that by making ranges explicit by requiring parenthesis around complex range boundaries (anything that is not a literal: numerics, strings, symbols, etc.).

This cop can be configured with `RequireParenthesesForMethodChains` in order to specify whether method chains (including `self.foo`) should be wrapped in parens by this cop.

NOTE: Regardless of this configuration, if a method receiver is a basic literal value, it will be wrapped in order to prevent the ambiguity of `1..2.to_a`.

#### Examples

```
# bad
x || 1..2
x - 1..2
(x || 1..2)
x || 1..y || 2
1..2.to_a

# good, unambiguous
1..2
'a'..'z'
:bar..:baz
MyClass::MIN..MyClass::MAX
@min..@max
a..b
-a..b

# good, ambiguity removed
x || (1..2)
(x - 1)..2
(x || 1)..2
(x || 1)..(y || 2)
(1..2).to_a

```

#####

RequireParenthesesForMethodChains: false (default)

```
# good
a.foo..b.bar
(a.foo)..(b.bar)

```

#####

RequireParenthesesForMethodChains: true

```
# bad
a.foo..b.bar

# good
(a.foo)..(b.bar)

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Wrap complex range boundaries with parentheses to avoid ambiguity.'

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
  
      #**on_irange**(node)  ⇒ Object 
    

    
      (also: #on_erange)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**on_irange**(node)  ⇒ Object 
  

  
    Also known as:
    on_erange
    
  

  

  
    
      

```

68
69
70
71
72
73
74
75
76
```

```
# File 'lib/rubocop/cop/lint/ambiguous_range.rb', line 68

def on_irange(node)
  each_boundary(node) do |boundary|
    next if acceptable?(boundary)

    add_offense(boundary) do |corrector|
      corrector.wrap(boundary, '(', ')')
    end
  end
end

```
