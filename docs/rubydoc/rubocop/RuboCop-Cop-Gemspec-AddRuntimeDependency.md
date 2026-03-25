# Class: RuboCop::Cop::Gemspec::AddRuntimeDependency
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Gemspec::AddRuntimeDependency

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
    Defined in:
    lib/rubocop/cop/gemspec/add_runtime_dependency.rb
  
## Overview

Prefer `add_dependency` over `add_runtime_dependency` as the latter is considered soft-deprecated.

#### Examples

```

# bad
Gem::Specification.new do |spec|
  spec.add_runtime_dependency('rubocop')
end

# good
Gem::Specification.new do |spec|
  spec.add_dependency('rubocop')
end

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Use `add_dependency` instead of `add_runtime_dependency`.'

```

        RESTRICT_ON_SEND =
          
        
        

```
i[add_runtime_dependency].freeze

```

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
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
  
    #**on_send**(node)  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
31
32
33
34
```

```
# File 'lib/rubocop/cop/gemspec/add_runtime_dependency.rb', line 28

def on_send(node)
  return if !node.receiver || node.arguments.empty?

  add_offense(node.loc.selector) do |corrector|
    corrector.replace(node.loc.selector, 'add_dependency')
  end
end

```
