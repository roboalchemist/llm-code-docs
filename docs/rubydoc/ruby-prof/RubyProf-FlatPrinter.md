# Class: RubyProf::FlatPrinter
  
  
  

  
  
    Inherits:
    
      AbstractPrinter
      
        

          
- Object
          
            
- AbstractPrinter
          
            
- RubyProf::FlatPrinter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/printers/flat_printer.rb
  
  

## Overview

  
    

Generates flat profile reports as text. To use the flat printer:

```
result = RubyProf.profile do
  [code to profile]
end

printer = RubyProf::FlatPrinter.new(result)
printer.print(STDOUT)

```

  

  

  
## Instance Attribute Summary

  
  
### Attributes inherited from AbstractPrinter

  

#filter_by, #max_percent, #min_percent, #sort_method

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**print**(output = STDOUT, sort_method: :self_time, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Override to default sort by self time.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from AbstractPrinter

  

#initialize, #method_href, #method_location, needs_dir?, #open_asset, #print_footer, #print_header, #print_thread, #print_threads, #time_format

  
## Constructor Details

  
    

This class inherits a constructor from RubyProf::AbstractPrinter
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**print**(output = STDOUT, sort_method: :self_time, **options)  ⇒ Object 
  

  

  

  
    

Override to default sort by self time

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/ruby-prof/printers/flat_printer.rb', line 16

def print(output = STDOUT, sort_method: :self_time, **options)
  super(output, sort_method: sort_method, **options)
end
```