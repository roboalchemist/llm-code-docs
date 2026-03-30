# Class: RuboCop::Cop::Layout::AccessModifierIndentation
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Layout::AccessModifierIndentation

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      Alignment, ConfigurableEnforcedStyle, RangeHelp
  
    Defined in:
    lib/rubocop/cop/layout/access_modifier_indentation.rb
  
## Overview

Bare access modifiers (those not applying to specific methods) should be indented as deep as method definitions, or as deep as the `class`/`module` keyword, depending on configuration.

#### Examples

#####

EnforcedStyle: indent (default)

```
# bad
class Plumbus
private
  def smooth; end
end

# good
class Plumbus
  private
  def smooth; end
end

```

#####

EnforcedStyle: outdent

```
# bad
class Plumbus
  private
  def smooth; end
end

# good
class Plumbus
private
  def smooth; end
end

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'%<style>s access modifiers like `%<node>s`.'

```

### Constants included

     from RangeHelp

RangeHelp::BYTE_ORDER_MARK, RangeHelp::NOT_GIVEN

### Constants included

     from Alignment

Alignment::SPACE

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
    

    
      (also: #on_sclass, #on_module, #on_block)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
    on_sclass, on_module, on_block
    
  

  

  
    
      

```

43
44
45
46
47
```

```
# File 'lib/rubocop/cop/layout/access_modifier_indentation.rb', line 43

def on_class(node)
  return unless node.body&.begin_type?

  check_body(node.body, node)
end

```
