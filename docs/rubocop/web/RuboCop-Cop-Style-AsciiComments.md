# Class: RuboCop::Cop::Style::AsciiComments
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::AsciiComments

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      RangeHelp
  
    Defined in:
    lib/rubocop/cop/style/ascii_comments.rb
  
## Overview

Checks for non-ascii (non-English) characters in comments. Non-ascii characters can cause issues with portability and encoding across different environments and editors. You could set an array of allowed non-ascii chars in `AllowedChars` attribute (copyright notice “©” by default).

#### Examples

```
# bad
# Translates from English to 日本語。

# good
# Translates from English to Japanese
```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Use only ascii symbols in comments.'
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

24
25
26
27
28
29
30
31
```

```
# File 'lib/rubocop/cop/style/ascii_comments.rb', line 24

def on_new_investigation
  processed_source.comments.each do |comment|
    next if comment.text.ascii_only?
    next if only_allowed_non_ascii_chars?(comment.text)

    add_offense(first_offense_range(comment))
  end
end
```
