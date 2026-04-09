# Class: RuboCop::Cop::Style::AccessorGrouping
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::AccessorGrouping

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      ConfigurableEnforcedStyle, RangeHelp, VisibilityHelp
  
    Defined in:
    lib/rubocop/cop/style/accessor_grouping.rb
  
## Overview

Checks for grouping of accessors in `class` and `module` bodies. By default it enforces accessors to be placed in grouped declarations, reducing boilerplate. It can also be configured to enforce separating them into individual declarations for easier diffing and per-attribute documentation.

NOTE: If there is a method call before the accessor method it is always allowed as it might be intended like Sorbet.

NOTE: If there is a RBS::Inline annotation comment just after the accessor method it is always allowed.

#### Examples

#####

EnforcedStyle: grouped (default)

```
# bad
class Foo
  attr_reader :bar
  attr_reader :bax
  attr_reader :baz
end

# good
class Foo
  attr_reader :bar, :bax, :baz
end

# good
class Foo
  # may be intended comment for bar.
  attr_reader :bar

  sig { returns(String) }
  attr_reader :bax

  may_be_intended_annotation :baz
  attr_reader :baz
end

```

#####

EnforcedStyle: separated

```
# bad
class Foo
  attr_reader :bar, :baz
end

# good
class Foo
  attr_reader :bar
  attr_reader :baz
end

```

##

      Constant Summary
      collapse
    

    
      
        GROUPED_MSG =
          
        
        

```
'Group together all `%<accessor>s` attributes.'

```

        SEPARATED_MSG =
          
        
        

```
'Use one attribute per `%<accessor>s`.'

```

### Constants included

     from VisibilityHelp

VisibilityHelp::VISIBILITY_SCOPES

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
  
      #**on_class**(node)  ⇒ Object 
    

    
      (also: #on_sclass, #on_module)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from ConfigurableEnforcedStyle

# alternative_style, #alternative_styles, #ambiguous_style_detected, #correct_style_detected, #detected_style, #detected_style=, #no_acceptable_style!, #no_acceptable_style?, #opposite_style_detected, #style, #style_configured?, #style_detected, #style_parameter_name, #supported_styles, #unexpected_style_detected

### Methods inherited from Base

# active_support_extensions_enabled?, #add_global_offense, #add_offense, #always_autocorrect?, autocorrect_incompatible_with, badge, #begin_investigation, #callbacks_needed, callbacks_needed, #config_to_allow_offenses, #config_to_allow_offenses=, #contextual_autocorrect?, #cop_config, cop_name, #cop_name, department, documentation_url, exclude_from_registry, #excluded_file?, #external_dependency_checksum, inherited, #initialize, #inspect, joining_forces, lint?, match?, #offenses, #on_investigation_end, #on_new_investigation, #on_other_file, #parse, #parser_engine, #ready, #relevant_file?, requires_gem, #string_literals_frozen_by_default?, support_autocorrect?, support_multiple_source?, #target_gem_version, #target_rails_version, #target_ruby_version

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
  
    #**on_class**(node)  ⇒ Object 
  

  
    Also known as:
    on_sclass, on_module
    
  

  

  
    
      

```

64
65
66
67
68
69
70
```

```
# File 'lib/rubocop/cop/style/accessor_grouping.rb', line 64

def on_class(node)
  class_send_elements(node).each do |macro|
    next unless macro.attribute_accessor?

    check(macro)
  end
end

```
