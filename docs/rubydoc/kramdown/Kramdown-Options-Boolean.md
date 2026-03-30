# Class: Kramdown::Options::Boolean
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Kramdown::Options::Boolean
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/options.rb
  
  

## Overview

  
    

Helper class introducing a boolean type for specifying boolean values (`true` and `false`) as option types.

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**===**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return `true` if `other` is either `true` or `false`.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**===**(other)  ⇒ Object 
  

  

  

  
    

Return `true` if `other` is either `true` or `false`

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/kramdown/options.rb', line 23

def self.===(other)
  FalseClass === other || TrueClass === other
end

```