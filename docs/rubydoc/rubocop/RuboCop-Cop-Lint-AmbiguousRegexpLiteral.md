# Class: RuboCop::Cop::Lint::AmbiguousRegexpLiteral
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Lint::AmbiguousRegexpLiteral

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
    Defined in:
    lib/rubocop/cop/lint/ambiguous_regexp_literal.rb
  
## Overview

Checks for ambiguous regexp literals in the first argument of a method invocation without parentheses.

#### Examples

```

# bad

# This is interpreted as a method invocation with a regexp literal,
# but it could possibly be `/` method invocations.
# (i.e. `do_something./(pattern)./(i)`)
do_something /pattern/i

# good

# With parentheses, there's no ambiguity.
do_something(/pattern/i)

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Ambiguous regexp literal. Parenthesize the method arguments ' \
"if it's surely a regexp literal, or add a whitespace to the " \
'right of the `/` if it should be a division.'

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
  
      #**on_new_investigation**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**on_new_investigation**  ⇒ Object 
  

  

  

  
    
      

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
43
```

```
# File 'lib/rubocop/cop/lint/ambiguous_regexp_literal.rb', line 29

def on_new_investigation
  processed_source.diagnostics.each do |diagnostic|
    if target_ruby_version >= 3.0
      next unless diagnostic.reason == :ambiguous_regexp
    else
      next unless diagnostic.reason == :ambiguous_literal
    end

    offense_node = find_offense_node_by(diagnostic)

    add_offense(diagnostic.location, severity: diagnostic.level) do |corrector|
      add_parentheses(offense_node, corrector)
    end
  end
end

```
