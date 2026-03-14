# Class: HashValidator::Validator::HexColorValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::HexColorValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/hex_color_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ HexColorValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of HexColorValidator.

  

      
        
- 
  
    
      #**valid?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#should_validate?, #validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ HexColorValidator 
  

  

  

  
    

Returns a new instance of HexColorValidator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/hex_color_validator.rb', line 4

def initialize
  super("hex_color")  # The name of the validator
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
# File 'lib/hash_validator/validators/hex_color_validator.rb', line 8

def error_message
  "is not a valid hex color"
end
```

    
  

    
      
  
### 
  
    #**valid?**(value)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/hash_validator/validators/hex_color_validator.rb', line 12

def valid?(value)
  value.is_a?(String) && /\A#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\z/.match?(value)
end
```