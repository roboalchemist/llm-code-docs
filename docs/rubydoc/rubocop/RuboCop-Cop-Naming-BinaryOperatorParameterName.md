# Class: RuboCop::Cop::Naming::BinaryOperatorParameterName
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Naming::BinaryOperatorParameterName

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
    Defined in:
    lib/rubocop/cop/naming/binary_operator_parameter_name.rb
  
## Overview

Makes sure that certain binary operator methods have their sole  parameter named `other`.

#### Examples

```

# bad
def +(amount); end

# good
def +(other); end

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'When defining the `%<opr>s` operator, name its argument `other`.'

```

        OP_LIKE_METHODS =
          
        
        

```
i[eql? equal?].freeze

```

        EXCLUDED =
          
        
        

```
i[+@ -@ [] []= << === ` =~].freeze

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
  
      #**on_def**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**op_method_candidate?**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

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
  
    #**on_def**(node)  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
32
33
34
35
36
37
38
39
40
41
```

```
# File 'lib/rubocop/cop/naming/binary_operator_parameter_name.rb', line 29

def on_def(node)
  op_method_candidate?(node) do |name, arg|
    add_offense(arg, message: format(MSG, opr: name)) do |corrector|
      corrector.replace(arg, 'other')
      node.each_descendant(:lvar, :lvasgn) do |lvar|
        lvar_location = lvar.loc.name
        next unless lvar_location.source == arg.source

        corrector.replace(lvar_location, 'other')
      end
    end
  end
end

```

###
  
    #**op_method_candidate?**(node)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

```
# File 'lib/rubocop/cop/naming/binary_operator_parameter_name.rb', line 25

def_node_matcher :op_method_candidate?, "(def [#op_method? $_] (args $(arg [!:other !:_other])) _)\n"

```
