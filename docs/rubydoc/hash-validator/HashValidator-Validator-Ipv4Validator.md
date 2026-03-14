# Class: HashValidator::Validator::Ipv4Validator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::Ipv4Validator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/ipv4_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ Ipv4Validator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Ipv4Validator.

  

      
        
- 
  
    
      #**valid?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#should_validate?, #validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ Ipv4Validator 
  

  

  

  
    

Returns a new instance of Ipv4Validator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/ipv4_validator.rb', line 4

def initialize
  super("ipv4")  # The name of the validator
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
# File 'lib/hash_validator/validators/ipv4_validator.rb', line 8

def error_message
  "is not a valid IPv4 address"
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
15
16
17
```

    
    
      

```
# File 'lib/hash_validator/validators/ipv4_validator.rb', line 12

def valid?(value)
  return false unless value.is_a?(String)
  # IPv4 regex: 4 octets, each 0-255
  ipv4_regex = /\A(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\z/
  value.match?(ipv4_regex)
end
```