# Class: HashValidator::Validations::Multiple
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- HashValidator::Validations::Multiple
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validations/multiple.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**validations**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute validations.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(validations)  ⇒ Multiple 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Multiple.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(validations)  ⇒ Multiple 
  

  

  

  
    

Returns a new instance of Multiple.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/hash_validator/validations/multiple.rb', line 6

def initialize(validations)
  @validations = validations
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**validations**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute validations.

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/hash_validator/validations/multiple.rb', line 5

def validations
  @validations
end
```