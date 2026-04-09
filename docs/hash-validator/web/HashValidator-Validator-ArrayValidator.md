# Class: HashValidator::Validator::ArrayValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::ArrayValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/array_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**  ⇒ ArrayValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ArrayValidator.

  

      
        
- 
  
    
      #**should_validate?**(rhs)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate**(key, value, specification, errors)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#error_message

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ ArrayValidator 
  

  

  

  
    

Returns a new instance of ArrayValidator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/array_validator.rb', line 4

def initialize
  super("__array__")  # The name of the validator, underscored as it won't usually be directly invoked (invoked through use of validator)
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
11
12
13
14
```

    
    
      

```
# File 'lib/hash_validator/validators/array_validator.rb', line 8

def should_validate?(rhs)
  return false unless rhs.is_a?(Array)
  return false unless rhs.size > 0
  return false unless rhs[0] == :array

  true
end
```

    
  

    
      
  
### 
  
    #**validate**(key, value, specification, errors)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/hash_validator/validators/array_validator.rb', line 16

def validate(key, value, specification, errors)
  # Validate specification format
  if specification[0] != :array
    errors[key] = "Wrong array specification. The #{:array} is expected as first item."
  elsif specification.size > 2
    errors[key] = "Wrong size of array specification. Allowed is one or two items."
  elsif !value.is_a?(Array)
    errors[key] = "#{Array} required"
  elsif specification.size >= 2 && !specification[1].nil?
    validate_array_specification(key, value, specification[1], errors)
  end
end
```