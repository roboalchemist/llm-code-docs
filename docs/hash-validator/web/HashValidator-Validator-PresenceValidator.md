# Class: HashValidator::Validator::PresenceValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::PresenceValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/presence_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ PresenceValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of PresenceValidator.

  

      
        
- 
  
    
      #**valid?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#should_validate?, #validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ PresenceValidator 
  

  

  

  
    

Returns a new instance of PresenceValidator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/presence_validator.rb', line 4

def initialize
  super("required")
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
# File 'lib/hash_validator/validators/presence_validator.rb', line 8

def error_message
  "is required"
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
# File 'lib/hash_validator/validators/presence_validator.rb', line 12

def valid?(value)
  !value.nil?
end
```