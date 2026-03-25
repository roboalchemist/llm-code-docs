# Class: RuboCop::Cop::Style::AutoResourceCleanup
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::AutoResourceCleanup

        show all
      

    Defined in:
    lib/rubocop/cop/style/auto_resource_cleanup.rb
  
## Overview

Checks for cases when you could use a block accepting version of a method that does automatic resource cleanup.

#### Examples

```

# bad
f = File.open('file')

# good
File.open('file') do |f|
  # ...
end

# bad
f = Tempfile.open('temp')

# good
Tempfile.open('temp') do |f|
  # ...
end

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Use the block version of `%<current>s`.'

```

        RESTRICT_ON_SEND =
          
        
        

```
i[open].freeze

```

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**file_open_method?**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**file_open_method?**(node)  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
```

```
# File 'lib/rubocop/cop/style/auto_resource_cleanup.rb', line 32

def_node_matcher :file_open_method?, "(send (const {nil? cbase} {:File :Tempfile}) :open ...)\n"

```

###
  
    #**on_send**(node)  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
39
40
41
42
```

```
# File 'lib/rubocop/cop/style/auto_resource_cleanup.rb', line 36

def on_send(node)
  return if !file_open_method?(node) || cleanup?(node)

  current = node.receiver.source_range.begin.join(node.selector.end).source

  add_offense(node, message: format(MSG, current: current))
end

```
