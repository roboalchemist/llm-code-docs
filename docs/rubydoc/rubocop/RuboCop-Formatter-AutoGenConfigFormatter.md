# Class: RuboCop::Formatter::AutoGenConfigFormatter
  
    Inherits:
    
      ProgressFormatter
      
        

          
- Object

- BaseFormatter

- SimpleTextFormatter

- ClangStyleFormatter

- ProgressFormatter

- RuboCop::Formatter::AutoGenConfigFormatter

        show all
      

    Defined in:
    lib/rubocop/formatter/auto_gen_config_formatter.rb
  
## Overview

Does not show individual offenses in the console.

## Constant Summary

### Constants inherited

     from ProgressFormatter

ProgressFormatter::DOT

### Constants inherited

     from ClangStyleFormatter

ClangStyleFormatter::ELLIPSES

### Constants inherited

     from SimpleTextFormatter

SimpleTextFormatter::COLOR_FOR_SEVERITY

### Constants included

     from PathUtil

PathUtil::HIDDEN_FILE_PATTERN

## Instance Attribute Summary

### Attributes inherited from BaseFormatter

# options, #output

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**finished**(inspected_files)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from ProgressFormatter

# file_finished, #initialize, #report_file_as_mark, #started

### Methods included from TextUtil

pluralize

### Methods inherited from ClangStyleFormatter

# report_file

### Methods inherited from SimpleTextFormatter

# file_finished, #report_file, #report_summary, #started

### Methods included from PathUtil

absolute?, glob?, hidden_dir?, hidden_file?, hidden_file_in_not_hidden_dir?, match_path?, maybe_hidden_file?, relative_path, remote_file?, smart_path

### Methods included from Colorizable

# colorize, #rainbow

### Methods inherited from BaseFormatter

# file_finished, #file_started, #initialize, #started

## Constructor Details

This class inherits a constructor from RuboCop::Formatter::ProgressFormatter
  
## Instance Method Details

###
  
    #**finished**(inspected_files)  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
11
12
13
14
```

```
# File 'lib/rubocop/formatter/auto_gen_config_formatter.rb', line 7

def finished(inspected_files)
  output.puts

  report_summary(inspected_files.size,
                 @total_offense_count,
                 @total_correction_count,
                 @total_correctable_count)
end

```
