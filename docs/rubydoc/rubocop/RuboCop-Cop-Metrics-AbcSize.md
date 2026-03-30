# Class: RuboCop::Cop::Metrics::AbcSize
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Metrics::AbcSize

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      RuboCop::Cop::MethodComplexity
  
    Defined in:
    lib/rubocop/cop/metrics/abc_size.rb
  
## Overview

Checks that the ABC size of methods is not higher than the configured maximum. The ABC size is based on assignments, branches (method calls), and conditions. See c2.com/cgi/wiki?AbcMetric and en.wikipedia.org/wiki/ABC_Software_Metric.

Interpreting ABC size:

-

“<= 17“ satisfactory

-

`18..30` unsatisfactory

-

‘>` 30 dangerous

You can have repeated “attributes” calls count as a single “branch”. For this purpose, attributes are any method with no argument; no attempt is meant to distinguish actual `attr_reader` from other methods.

This cop also takes into account `AllowedMethods` (defaults to `[]`) And `AllowedPatterns` (defaults to `[]`)

#### Examples

#####

CountRepeatedAttributes: false (default is true)

```

# `model` and `current_user`, referenced 3 times each,
# are each counted as only 1 branch each if
# `CountRepeatedAttributes` is set to 'false'

def search
  @posts = model.active.visible_by(current_user)
            .search(params[:q])
  @posts = model.some_process(@posts, current_user)
  @posts = model.another_process(@posts, current_user)

  render 'pages/search/page'
end
```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Assignment Branch Condition size for `%<method>s` is too high. ' \
'[%<abc_vector>s %<complexity>.4g/%<max>.4g]'
```

### Constants inherited

     from Base

Base::RESTRICT_ON_SEND

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

## Method Summary

### Methods included from RuboCop::Cop::MethodComplexity

# on_block, #on_def

### Methods included from ExcludeLimit

# exclude_limit

### Methods included from Utils::RepeatedCsendDiscount

# discount_for_repeated_csend?, #reset_on_lvasgn, #reset_repeated_csend

### Methods inherited from Base

# active_support_extensions_enabled?, #add_global_offense, #add_offense, #always_autocorrect?, autocorrect_incompatible_with, badge, #begin_investigation, #callbacks_needed, callbacks_needed, #config_to_allow_offenses, #config_to_allow_offenses=, #contextual_autocorrect?, #cop_config, #cop_name, cop_name, department, documentation_url, exclude_from_registry, #excluded_file?, #external_dependency_checksum, inherited, #initialize, #inspect, joining_forces, lint?, match?, #message, #offenses, #on_investigation_end, #on_new_investigation, #on_other_file, #parse, #parser_engine, #ready, #relevant_file?, requires_gem, #string_literals_frozen_by_default?, support_autocorrect?, support_multiple_source?, #target_gem_version, #target_rails_version, #target_ruby_version

### Methods included from AutocorrectLogic

# autocorrect?, #autocorrect_enabled?, #autocorrect_requested?, #autocorrect_with_disable_uncorrectable?, #correctable?, #disable_uncorrectable?, #safe_autocorrect?

### Methods included from IgnoredNode

# ignore_node, #ignored_node?, #part_of_ignored_node?

### Methods included from Util

silence_warnings

## Constructor Details

This class inherits a constructor from RuboCop::Cop::Base
