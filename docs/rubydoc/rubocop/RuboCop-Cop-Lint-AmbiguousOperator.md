# Class: RuboCop::Cop::Lint::AmbiguousOperator
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Lint::AmbiguousOperator

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
    Defined in:
    lib/rubocop/cop/lint/ambiguous_operator.rb
  
## Overview

Checks for ambiguous operators in the first argument of a method invocation without parentheses.

#### Examples

```

# bad

# The `*` is interpreted as a splat operator but it could possibly be
# a `*` method invocation (i.e. `do_something.*(some_array)`).
do_something *some_array

# good

# With parentheses, there's no ambiguity.
do_something(*some_array)

```

##

      Constant Summary
      collapse
    

    
      
        AMBIGUITIES =
          
        
        

```
{
  '+'  => { actual: 'positive number', possible: 'an addition' },
  '-'  => { actual: 'negative number', possible: 'a subtraction' },
  '*'  => { actual: 'splat',           possible: 'a multiplication' },
  '&'  => { actual: 'block',           possible: 'a binary AND' },
  '**' => { actual: 'keyword splat',   possible: 'an exponent' }
}.each do |key, hash|
  hash[:operator] = key
end

```

        MSG_FORMAT =
          
        
        

```
'Ambiguous %<actual>s operator. Parenthesize the method ' \
"arguments if it's surely a %<actual>s operator, or add " \
'a whitespace to the right of the `%<operator>s` if it ' \
'should be %<possible>s.'

```

### Constants inherited

     from Base

Base::RESTRICT_ON_SEND

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**autocorrect_incompatible_with**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**on_new_investigation**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods inherited from Base

# active_support_extensions_enabled?, #add_global_offense, #add_offense, #always_autocorrect?, badge, #begin_investigation, callbacks_needed, #callbacks_needed, #config_to_allow_offenses, #config_to_allow_offenses=, #contextual_autocorrect?, #cop_config, cop_name, #cop_name, department, documentation_url, exclude_from_registry, #excluded_file?, #external_dependency_checksum, inherited, #initialize, #inspect, joining_forces, lint?, match?, #offenses, #on_investigation_end, #on_other_file, #parse, #parser_engine, #ready, #relevant_file?, requires_gem, #string_literals_frozen_by_default?, support_autocorrect?, support_multiple_source?, #target_gem_version, #target_rails_version, #target_ruby_version

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
  
## Class Method Details

###
  
    .**autocorrect_incompatible_with**  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
```

```
# File 'lib/rubocop/cop/lint/ambiguous_operator.rb', line 39

def self.autocorrect_incompatible_with
  [Naming::BlockForwarding]
end

```

## Instance Method Details

###
  
    #**on_new_investigation**  ⇒ Object 
  

  

  

  
    
      

```

43
44
45
46
47
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
```

```
# File 'lib/rubocop/cop/lint/ambiguous_operator.rb', line 43

def on_new_investigation
  processed_source.diagnostics.each do |diagnostic|
    next unless diagnostic.reason == :ambiguous_prefix

    offense_node = find_offense_node_by(diagnostic)
    next unless offense_node

    message = message(diagnostic)

    add_offense(
      diagnostic.location, message: message, severity: diagnostic.level
    ) do |corrector|
      add_parentheses(offense_node, corrector)
    end
  end
end

```
