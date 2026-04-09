# Class: RuboCop::Cop::Lint::BigDecimalNew
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Lint::BigDecimalNew

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
    Defined in:
    lib/rubocop/cop/lint/big_decimal_new.rb
  
## Overview

‘BigDecimal.new()` is deprecated since BigDecimal 1.3.3. This cop identifies places where `BigDecimal.new()` can be replaced by `BigDecimal()`.

#### Examples

```
# bad
BigDecimal.new(123.456, 3)

# good
BigDecimal(123.456, 3)

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'`BigDecimal.new()` is deprecated. Use `BigDecimal()` instead.'

```

        RESTRICT_ON_SEND =
          
        
        

```
i[new].freeze

```

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**big_decimal_new**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**big_decimal_new**(node)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
27
```

```
# File 'lib/rubocop/cop/lint/big_decimal_new.rb', line 24

def_node_matcher :big_decimal_new, "(send\n  (const ${nil? cbase} :BigDecimal) :new ...)\n"

```

###
  
    #**on_send**(node)  ⇒ Object 
  

  

  

  
    
      

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
```

```
# File 'lib/rubocop/cop/lint/big_decimal_new.rb', line 29

def on_send(node)
  big_decimal_new(node) do |cbase|
    add_offense(node.loc.selector) do |corrector|
      corrector.remove(node.loc.selector)
      corrector.remove(node.loc.dot)
      corrector.remove(cbase) if cbase
    end
  end
end

```
