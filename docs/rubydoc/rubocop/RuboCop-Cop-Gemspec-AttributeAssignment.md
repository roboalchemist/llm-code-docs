# Class: RuboCop::Cop::Gemspec::AttributeAssignment
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Gemspec::AttributeAssignment

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      RuboCop::Cop::GemspecHelp
  
    Defined in:
    lib/rubocop/cop/gemspec/attribute_assignment.rb
  
## Overview

Use consistent style for Gemspec attributes assignment.

#### Examples

```

# bad
# This example uses two styles for assignment of metadata attribute.
Gem::Specification.new do |spec|
  spec.metadata = { 'key' => 'value' }
  spec.metadata['another-key'] = 'another-value'
end

# good
Gem::Specification.new do |spec|
  spec.metadata['key'] = 'value'
  spec.metadata['another-key'] = 'another-value'
end

# good
Gem::Specification.new do |spec|
  spec.metadata = { 'key' => 'value', 'another-key' => 'another-value' }
end

# bad
# This example uses two styles for assignment of authors attribute.
Gem::Specification.new do |spec|
  spec.authors = %w[author-0 author-1]
  spec.authors[2] = 'author-2'
end

# good
Gem::Specification.new do |spec|
  spec.authors = %w[author-0 author-1 author-2]
end

# good
Gem::Specification.new do |spec|
  spec.authors[0] = 'author-0'
  spec.authors[1] = 'author-1'
  spec.authors[2] = 'author-2'
end

# good
# This example uses consistent assignment per attribute,
# even though two different styles are used overall.
Gem::Specification.new do |spec|
  spec.metadata = { 'key' => 'value' }
  spec.authors[0] = 'author-0'
  spec.authors[1] = 'author-1'
  spec.authors[2] = 'author-2'
end
```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Use consistent style for Gemspec attributes assignment.'
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
  
      #**on_new_investigation**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from RuboCop::Cop::GemspecHelp

# assignment_method_declarations, #gem_specification, #gem_specification?, #indexed_assignment_method_declarations, #match_block_variable_name?

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

62
63
64
65
66
67
68
69
70
71
72
73
```

```
# File 'lib/rubocop/cop/gemspec/attribute_assignment.rb', line 62

def on_new_investigation
  return if processed_source.blank?

  assignments = source_assignments(processed_source.ast)
  indexed_assignments = source_indexed_assignments(processed_source.ast)

  assignments.keys.intersection(indexed_assignments.keys).each do |attribute|
    indexed_assignments[attribute].each do |node|
      add_offense(node)
    end
  end
end
```
