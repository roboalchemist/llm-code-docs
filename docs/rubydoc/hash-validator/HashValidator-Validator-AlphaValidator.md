# Class: HashValidator::Validator::AlphaValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::AlphaValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/alpha_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ AlphaValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of AlphaValidator.

  

      
        
- 
  
    
      #**valid?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#should_validate?, #validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ AlphaValidator 
  

  

  

  
    

Returns a new instance of AlphaValidator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/alpha_validator.rb', line 4

def initialize
  super("alpha")  # The name of the validator
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**error_message**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/hash_validator/validators/alpha_validator.rb', line 8

def error_message
  "must contain only letters"
end
```

    
  

    
      
  
### 
  
    #**valid?**(value)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/hash_validator/validators/alpha_validator.rb', line 12

def valid?(value)
  value.is_a?(String) && /\A[a-zA-Z]+\z/.match?(value)
end
```