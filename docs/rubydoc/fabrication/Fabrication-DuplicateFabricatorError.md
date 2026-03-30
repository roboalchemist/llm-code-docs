# Exception: Fabrication::DuplicateFabricatorError
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- Fabrication::DuplicateFabricatorError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/errors/duplicate_fabricator_error.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(string)  ⇒ DuplicateFabricatorError 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of DuplicateFabricatorError.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(string)  ⇒ DuplicateFabricatorError 
  

  

  

  
    

Returns a new instance of DuplicateFabricatorError.

  

  

  
    
      

```

3
4
5
```

    
    
      

```
# File 'lib/fabrication/errors/duplicate_fabricator_error.rb', line 3

def initialize(string)
  super("'#{string}' is already defined")
end
```