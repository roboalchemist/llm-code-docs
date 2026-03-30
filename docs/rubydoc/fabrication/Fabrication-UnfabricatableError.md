# Exception: Fabrication::UnfabricatableError
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- Fabrication::UnfabricatableError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/errors/unfabricatable_error.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(name, original_error)  ⇒ UnfabricatableError 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of UnfabricatableError.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, original_error)  ⇒ UnfabricatableError 
  

  

  

  
    

Returns a new instance of UnfabricatableError.

  

  

  
    
      

```

3
4
5
```

    
    
      

```
# File 'lib/fabrication/errors/unfabricatable_error.rb', line 3

def initialize(name, original_error)
  super("No class found for '#{name}' (original exception: #{original_error.message})")
end
```