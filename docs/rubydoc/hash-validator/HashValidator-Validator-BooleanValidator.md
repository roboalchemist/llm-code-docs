# Class: HashValidator::Validator::BooleanValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::BooleanValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/boolean_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**  ⇒ BooleanValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of BooleanValidator.

  

      
        
- 
  
    
      #**valid?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#error_message, #should_validate?, #validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ BooleanValidator 
  

  

  

  
    

Returns a new instance of BooleanValidator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/boolean_validator.rb', line 4

def initialize
  super("boolean")  # The name of the validator
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**valid?**(value)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/hash_validator/validators/boolean_validator.rb', line 8

def valid?(value)
  [TrueClass, FalseClass].include?(value.class)
end
```