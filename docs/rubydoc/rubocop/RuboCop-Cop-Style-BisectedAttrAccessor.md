# Class: RuboCop::Cop::Style::BisectedAttrAccessor
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::BisectedAttrAccessor

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      RangeHelp
  
    Defined in:
    lib/rubocop/cop/style/bisected_attr_accessor.rb,

  lib/rubocop/cop/style/bisected_attr_accessor/macro.rb

## Overview

Checks for places where `attr_reader` and `attr_writer` for the same method can be combined into single `attr_accessor`.

#### Examples

```
# bad
class Foo
  attr_reader :bar
  attr_writer :bar
end

# good
class Foo
  attr_accessor :bar
end

```

## Defined Under Namespace

      **Classes:** Macro
    
  

  
    
##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Combine both accessors into `attr_accessor %<name>s`.'

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
  
      #**after_class**(class_node)  ⇒ Object 
    

    
      (also: #after_sclass, #after_module)
    
  
  
  
  
  
  
  
  

  
    

Each offending macro is captured and registered in `on_class` but correction happens in `after_class` because a macro might have multiple attributes rewritten from it.

-
  
      #**on_class**(class_node)  ⇒ Object 

      (also: #on_sclass, #on_module)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
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
  
    #**after_class**(class_node)  ⇒ Object 
  

  
    Also known as:
    after_sclass, after_module
    
  

  

  
    

Each offending macro is captured and registered in `on_class` but correction happens in `after_class` because a macro might have multiple attributes rewritten from it

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
66
67
68
```

```
# File 'lib/rubocop/cop/style/bisected_attr_accessor.rb', line 55

def after_class(class_node)
  @macros_to_rewrite[class_node].each do |macro|
    node = macro.node
    range = range_by_whole_lines(node.source_range, include_final_newline: true)

    correct(range) do |corrector|
      if macro.writer?
        correct_writer(corrector, macro, node, range)
      else
        correct_reader(corrector, macro, node, range)
      end
    end
  end
end

```

###
  
    #**on_class**(class_node)  ⇒ Object 
  

  
    Also known as:
    on_sclass, on_module
    
  

  

  
    
      

```

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
44
45
46
47
48
```

```
# File 'lib/rubocop/cop/style/bisected_attr_accessor.rb', line 33

def on_class(class_node)
  @macros_to_rewrite[class_node] = Set.new

  find_macros(class_node.body).each_value do |macros|
    bisected = find_bisection(macros)
    next unless bisected.any?

    macros.each do |macro|
      attrs = macro.bisect(*bisected)
      next if attrs.none?

      @macros_to_rewrite[class_node] << macro
      attrs.each { |attr| register_offense(attr) }
    end
  end
end

```

###
  
    #**on_new_investigation**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

```
# File 'lib/rubocop/cop/style/bisected_attr_accessor.rb', line 29

def on_new_investigation
  @macros_to_rewrite = {}
end

```
