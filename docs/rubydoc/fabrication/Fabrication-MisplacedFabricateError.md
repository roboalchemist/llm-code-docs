# Exception: Fabrication::MisplacedFabricateError
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- Fabrication::MisplacedFabricateError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/errors/misplaced_fabricate_error.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(name)  ⇒ MisplacedFabricateError 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of MisplacedFabricateError.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name)  ⇒ MisplacedFabricateError 
  

  

  

  
    

Returns a new instance of MisplacedFabricateError.

  

  

  
    
      

```

3
4
5
6
7
```

    
    
      

```
# File 'lib/fabrication/errors/misplaced_fabricate_error.rb', line 3

def initialize(name)
  super("You tried to fabricate `#{name}` while Fabricators were still loading. " \
        "Check your fabricator files and make sure you didn't accidentally type " \
        '`Fabricate` instead of `Fabricator` in there somewhere.')
end
```