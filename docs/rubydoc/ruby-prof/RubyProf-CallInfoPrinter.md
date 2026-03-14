# Class: RubyProf::CallInfoPrinter
  
  
  

  
  
    Inherits:
    
      AbstractPrinter
      
        

          
- Object
          
            
- AbstractPrinter
          
            
- RubyProf::CallInfoPrinter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/printers/call_info_printer.rb
  
  

## Overview

  
    

Prints out the call graph based on CallTree instances. This is mainly for debugging purposes as it provides access into into RubyProf’s internals.

To use the printer:

```
result = RubyProf.profile do
  [code to profile]
end

printer = RubyProf::CallInfoPrinter.new(result)
printer.print(STDOUT)

```

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        TIME_WIDTH =
          
        
        

```
0

```

      
    
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from AbstractPrinter

  

#filter_by, #max_percent, #min_percent, #sort_method

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods inherited from AbstractPrinter

  

#initialize, #method_href, #method_location, needs_dir?, #open_asset, #print, #print_column_headers, #print_thread, #print_threads, #time_format

  
## Constructor Details

  
    

This class inherits a constructor from RubyProf::AbstractPrinter