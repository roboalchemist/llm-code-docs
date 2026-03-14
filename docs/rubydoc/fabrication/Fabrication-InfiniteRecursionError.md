# Exception: Fabrication::InfiniteRecursionError
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- Fabrication::InfiniteRecursionError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/errors/infinite_recursion_error.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(name)  ⇒ InfiniteRecursionError 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of InfiniteRecursionError.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name)  ⇒ InfiniteRecursionError 
  

  

  

  
    

Returns a new instance of InfiniteRecursionError.

  

  

  
    
      

```

3
4
5
```

    
    
      

```
# File 'lib/fabrication/errors/infinite_recursion_error.rb', line 3

def initialize(name)
  super("You appear to have infinite recursion with the `#{name}` fabricator")
end
```