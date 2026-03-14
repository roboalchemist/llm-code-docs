# Class: RuboCop::Cop::Naming::AsciiIdentifiers
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Naming::AsciiIdentifiers

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      RangeHelp
  
    Defined in:
    lib/rubocop/cop/naming/ascii_identifiers.rb
  
## Overview

Checks for non-ascii characters in identifier and constant names. Identifiers are always checked and whether constants are checked can be controlled using AsciiConstants config.

#### Examples

```
# bad
def 
```

#####

AsciiConstants: true (default)

```
# bad
class Fo
```

#####

AsciiConstants: false

```
# good
class Fo
```

##

      Constant Summary
      collapse
    

    
      
        IDENTIFIER_MSG =
          
        
        

```
'Use only ascii symbols in identifiers.'

```

        CONSTANT_MSG =
          
        
        

```
'Use only ascii symbols in constants.'

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
  
      #**on_new_investigation**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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

59
60
61
62
63
64
65
66
```

```
# File 'lib/rubocop/cop/naming/ascii_identifiers.rb', line 59

def on_new_investigation
  processed_source.tokens.each do |token|
    next if !should_check?(token) || token.text.ascii_only?

    message = token.type == :tIDENTIFIER ? IDENTIFIER_MSG : CONSTANT_MSG
    add_offense(first_offense_range(token), message: message)
  end
end

```
