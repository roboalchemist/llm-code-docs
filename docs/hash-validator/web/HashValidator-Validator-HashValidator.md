# Class: HashValidator::Validator::HashValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::HashValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/hash_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**  ⇒ HashValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of HashValidator.

  

      
        
- 
  
    
      #**should_validate?**(rhs)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate**(key, value, validations, errors)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#error_message

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ HashValidator 
  

  

  

  
    

Returns a new instance of HashValidator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/hash_validator.rb', line 4

def initialize
  super("hash")
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**should_validate?**(rhs)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/hash_validator/validators/hash_validator.rb', line 8

def should_validate?(rhs)
  rhs.is_a?(Hash) || (defined?(ActionController::Parameters) && rhs.is_a?(ActionController::Parameters))
end
```

    
  

    
      
  
### 
  
    #**validate**(key, value, validations, errors)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
```

    
    
      

```
# File 'lib/hash_validator/validators/hash_validator.rb', line 12

def validate(key, value, validations, errors)
  # Convert ActionController::Parameters to Hash if needed
  if !value.is_a?(Hash) && defined?(ActionController::Parameters) && value.is_a?(ActionController::Parameters)
    value = value.to_unsafe_h
  end

  # Validate hash
  unless value.is_a?(Hash)
    errors[key] = error_message
    return
  end

  # Hashes can contain sub-elements, attempt to validator those
  errors = (errors[key] = {})

  validations.each do |v_key, v_value|
    HashValidator.validator_for(v_value).validate(v_key, value[v_key], v_value, errors)
  end

  if HashValidator::Base.strict?
    value.keys.each do |k|
      errors[k] = "key not expected" unless validations[k]
    end
  end

  # Cleanup errors (remove any empty nested errors)
  errors.delete_if { |_, v| v.empty? }
end
```