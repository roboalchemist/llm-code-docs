# Exception: Fabrication::UnknownFabricatorError
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- Fabrication::UnknownFabricatorError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/errors/unknown_fabricator_error.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(name)  ⇒ UnknownFabricatorError 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of UnknownFabricatorError.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name)  ⇒ UnknownFabricatorError 
  

  

  

  
    

Returns a new instance of UnknownFabricatorError.

  

  

  
    
      

```

3
4
5
```

    
    
      

```
# File 'lib/fabrication/errors/unknown_fabricator_error.rb', line 3

def initialize(name)
  super("No Fabricator defined for '#{name}'")
end
```