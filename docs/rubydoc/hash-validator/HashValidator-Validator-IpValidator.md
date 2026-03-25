# Class: HashValidator::Validator::IpValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::IpValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/ip_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ IpValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of IpValidator.

  

      
        
- 
  
    
      #**valid?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#should_validate?, #validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ IpValidator 
  

  

  

  
    

Returns a new instance of IpValidator.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/hash_validator/validators/ip_validator.rb', line 6

def initialize
  super("ip")  # The name of the validator
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**error_message**  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/hash_validator/validators/ip_validator.rb', line 10

def error_message
  "is not a valid IP address"
end
```

    
  

    
      
  
### 
  
    #**valid?**(value)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

14
15
16
17
18
19
20
21
```

    
    
      

```
# File 'lib/hash_validator/validators/ip_validator.rb', line 14

def valid?(value)
  return false unless value.is_a?(String)
  # Use IPAddr to validate both IPv4 and IPv6 addresses
  IPAddr.new(value)
  true
rescue IPAddr::Error, IPAddr::InvalidAddressError
  false
end
```