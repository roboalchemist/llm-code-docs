# Class: RuboCop::Cop::Style::BarePercentLiterals
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::BarePercentLiterals

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      ConfigurableEnforcedStyle
  
    Defined in:
    lib/rubocop/cop/style/bare_percent_literals.rb
  
## Overview

Checks if usage of ‘%()` or `%Q()` matches configuration. Consistent use of one style makes the codebase easier to read.

#### Examples

#####

EnforcedStyle: bare_percent (default)

```
# bad
%Q(He said: "#{greeting}")
%q{She said: 'Hi'}

# good
%(He said: "#{greeting}")
%{She said: 'Hi'}
```

#####

EnforcedStyle: percent_q

```
# bad
%|He said: "#{greeting}"|
%/She said: 'Hi'/

# good
%Q|He said: "#{greeting}"|
%q/She said: 'Hi'/
```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Use `%%%<good>s` instead of `%%%<bad>s`.'
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
  
      #**on_dstr**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_str**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from ConfigurableEnforcedStyle

# alternative_style, #alternative_styles, #ambiguous_style_detected, #correct_style_detected, #detected_style, #detected_style=, #no_acceptable_style!, #no_acceptable_style?, #opposite_style_detected, #style, #style_configured?, #style_detected, #style_parameter_name, #supported_styles, #unexpected_style_detected

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
  
    #**on_dstr**(node)  ⇒ Object 
  

  

  

  
    
      

```

34
35
36
```

```
# File 'lib/rubocop/cop/style/bare_percent_literals.rb', line 34

def on_dstr(node)
  check(node)
end
```

###
  
    #**on_str**(node)  ⇒ Object 
  

  

  

  
    
      

```

38
39
40
```

```
# File 'lib/rubocop/cop/style/bare_percent_literals.rb', line 38

def on_str(node)
  check(node)
end
```
