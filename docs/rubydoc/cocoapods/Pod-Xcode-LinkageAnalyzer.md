# Class: Pod::Xcode::LinkageAnalyzer
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Xcode::LinkageAnalyzer
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/xcode/linkage_analyzer.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**dynamic_binary?**(binary)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether `binary` can be dynamically linked.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**dynamic_binary?**(binary)  ⇒ Boolean 
  

  

  

  
    

Returns Whether `binary` can be dynamically linked.

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

The file to be checked for being a dynamic Mach-O binary.

      
    
  

Returns:

  
    
- 
      
      
      
      
        
        

Whether `binary` can be dynamically linked.

      
    
  

  
    
      

```

11
12
13
14
15
16
17
18
19
```

    
    
      

```
# File 'lib/cocoapods/xcode/linkage_analyzer.rb', line 11

def self.dynamic_binary?(binary)
  @cached_dynamic_binary_results ||= {}
  return @cached_dynamic_binary_results[binary] unless @cached_dynamic_binary_results[binary].nil?
  return false unless binary.file?

  @cached_dynamic_binary_results[binary] = MachO.open(binary).dylib?
rescue MachO::MachOError
  @cached_dynamic_binary_results[binary] = false
end

```