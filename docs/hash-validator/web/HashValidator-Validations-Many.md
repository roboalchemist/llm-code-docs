# Class: HashValidator::Validations::Many
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- HashValidator::Validations::Many
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validations/many.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**validation**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute validation.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(validation)  ⇒ Many 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Many.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(validation)  ⇒ Many 
  

  

  

  
    

Returns a new instance of Many.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/hash_validator/validations/many.rb', line 6

def initialize(validation)
  @validation = validation
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**validation**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute validation.

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/hash_validator/validations/many.rb', line 5

def validation
  @validation
end
```