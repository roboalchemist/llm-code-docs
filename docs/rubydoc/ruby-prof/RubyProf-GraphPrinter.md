# Class: RubyProf::GraphPrinter
  
  
  

  
  
    Inherits:
    
      AbstractPrinter
      
        

          
- Object
          
            
- AbstractPrinter
          
            
- RubyProf::GraphPrinter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/printers/graph_printer.rb
  
  

## Overview

  
    

Generates graph profile reports as text. To use the graph printer:

```
result = RubyProf.profile do
  [code to profile]
end

printer = RubyProf::GraphPrinter.new(result)
printer.print(STDOUT)

```

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        PERCENTAGE_WIDTH =
          
        
        

```
8
```

      
        TIME_WIDTH =
          
        
        

```
11
```

      
        CALL_WIDTH =
          
        
        

```
17
```

      
    
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from AbstractPrinter

  

#filter_by, #max_percent, #min_percent, #sort_method

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**print**(output = STDOUT, sort_method: :total_time, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Override to default sort by total time.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from AbstractPrinter

  

#initialize, #method_href, #method_location, needs_dir?, #open_asset, #print_column_headers, #print_footer, #print_thread, #print_threads, #time_format

  
## Constructor Details

  
    

This class inherits a constructor from RubyProf::AbstractPrinter
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**print**(output = STDOUT, sort_method: :total_time, **options)  ⇒ Object 
  

  

  

  
    

Override to default sort by total time

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/ruby-prof/printers/graph_printer.rb', line 20

def print(output = STDOUT, sort_method: :total_time, **options)
  super(output, sort_method: sort_method, **options)
end
```