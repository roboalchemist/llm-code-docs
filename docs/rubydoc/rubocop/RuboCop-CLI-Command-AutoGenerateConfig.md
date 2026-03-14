# Class: RuboCop::CLI::Command::AutoGenerateConfig
  
  Private

    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::CLI::Command::AutoGenerateConfig

        show all
      

    Defined in:
    lib/rubocop/cli/command/auto_generate_config.rb
  
## Overview

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

Generate a configuration file acting as a TODO list.

##

      Constant Summary
      collapse
    

    
      
        AUTO_GENERATED_FILE =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

```
'.rubocop_todo.yml'

```

        YAML_OPTIONAL_DOC_START =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

```
/\A---(\s+#|\s*\z)/.freeze

```

        PLACEHOLDER =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

```
'###rubocop:inherit_here'

```

        PHASE_1 =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

```
'Phase 1 of 2: run Layout/LineLength cop'

```

        PHASE_2 =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

```
'Phase 2 of 2: run all cops'

```

        PHASE_1_OVERRIDDEN =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

```
'(skipped because the default Layout/LineLength:Max is overridden)'

```

        PHASE_1_DISABLED =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

```
'(skipped because Layout/LineLength is disabled)'

```

        PHASE_1_SKIPPED_ONLY_COPS =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

```
'(skipped because a list of cops is passed to the `--only` flag)'

```

        PHASE_1_SKIPPED_ONLY_EXCLUDE =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

```
'(skipped because only excludes will be generated due to `--auto-gen-only-exclude` flag)'

```

## Instance Attribute Summary

### Attributes inherited from Base

# env

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**run**  ⇒ Object 
    

    
  
  private

### Methods inherited from Base

by_command_name, inherited, #initialize

## Constructor Details

This class inherits a constructor from RuboCop::CLI::Command::Base
  
## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

25
26
27
28
29
30
```

```
# File 'lib/rubocop/cli/command/auto_generate_config.rb', line 25

def run
  add_formatter
  reset_config_and_auto_gen_file
  line_length_contents = maybe_run_line_length_cop
  run_all_cops(line_length_contents)
end

```
