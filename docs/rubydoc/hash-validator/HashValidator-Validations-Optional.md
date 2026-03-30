# Class: HashValidator::Validations::Optional
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- HashValidator::Validations::Optional
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validations/optional.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**validation**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute validation.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(validation)  ⇒ Optional 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Optional.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(validation)  ⇒ Optional 
  

  

  

  
    

Returns a new instance of Optional.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/hash_validator/validations/optional.rb', line 6

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
# File 'lib/hash_validator/validations/optional.rb', line 5

def validation
  @validation
end
```