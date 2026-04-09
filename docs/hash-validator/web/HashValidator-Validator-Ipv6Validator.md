# Class: HashValidator::Validator::Ipv6Validator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::Ipv6Validator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/ipv6_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ Ipv6Validator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Ipv6Validator.

  

      
        
- 
  
    
      #**valid?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#should_validate?, #validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ Ipv6Validator 
  

  

  

  
    

Returns a new instance of Ipv6Validator.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/hash_validator/validators/ipv6_validator.rb', line 6

def initialize
  super("ipv6")  # The name of the validator
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
# File 'lib/hash_validator/validators/ipv6_validator.rb', line 10

def error_message
  "is not a valid IPv6 address"
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
# File 'lib/hash_validator/validators/ipv6_validator.rb', line 14

def valid?(value)
  return false unless value.is_a?(String)
  # Use IPAddr to validate IPv6 addresses (handles standard and compressed notation)
  addr = IPAddr.new(value)
  addr.ipv6?
rescue IPAddr::Error, IPAddr::InvalidAddressError
  false
end
```