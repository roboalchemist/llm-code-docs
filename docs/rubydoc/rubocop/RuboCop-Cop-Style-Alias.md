# Class: RuboCop::Cop::Style::Alias
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::Alias

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      ConfigurableEnforcedStyle
  
    Defined in:
    lib/rubocop/cop/style/alias.rb
  
## Overview

Enforces the use of either `#alias` or `#alias_method` depending on configuration. Consistent use of one or the other prevents confusion about their different semantics (e.g., `alias` is resolved at parse time, while `alias_method` is resolved at runtime). It also flags uses of ‘alias :symbol` rather than `alias bareword`.

However, it will always enforce `method_alias` when used `alias` in an instance method definition and in a singleton method definition. If used in a block, always enforce `alias_method` unless it is an `instance_eval` block.

#### Examples

#####

EnforcedStyle: prefer_alias (default)

```
# bad
alias_method :bar, :foo
alias :bar :foo

# good
alias bar foo

```

#####

EnforcedStyle: prefer_alias_method

```
# bad
alias :bar :foo
alias bar foo

# good
alias_method :bar, :foo

```

##

      Constant Summary
      collapse
    

    
      
        MSG_ALIAS =
          
        
        

```
'Use `alias_method` instead of `alias`.'

```

        MSG_ALIAS_METHOD =
          
        
        

```
'Use `alias` instead of `alias_method` %<current>s.'

```

        MSG_SYMBOL_ARGS =
          
        
        

```
'Use `alias %<prefer>s` instead of `alias %<current>s`.'

```

        RESTRICT_ON_SEND =
          
        
        

```
i[alias_method].freeze

```

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**on_alias**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**on_alias**(node)  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
58
59
60
61
62
63
64
65
```

```
# File 'lib/rubocop/cop/style/alias.rb', line 55

def on_alias(node)
  return unless alias_method_possible?(node)

  if scope_type(node) == :dynamic || style == :prefer_alias_method
    add_offense(node.loc.keyword, message: MSG_ALIAS) do |corrector|
      autocorrect(corrector, node)
    end
  elsif node.children.none? { |arg| bareword?(arg) }
    add_offense_for_args(node) { |corrector| autocorrect(corrector, node) }
  end
end

```

###
  
    #**on_send**(node)  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/rubocop/cop/style/alias.rb', line 44

def on_send(node)
  return unless node.command?(:alias_method)
  return unless style == :prefer_alias && alias_keyword_possible?(node)
  return unless node.arguments.count == 2

  msg = format(MSG_ALIAS_METHOD, current: lexical_scope_type(node))
  add_offense(node.loc.selector, message: msg) do |corrector|
    autocorrect(corrector, node)
  end
end

```
