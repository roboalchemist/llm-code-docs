# Class: HashValidator::Validator::OptionalValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::OptionalValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/optional_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**  ⇒ OptionalValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of OptionalValidator.

  

      
        
- 
  
    
      #**should_validate?**(validation)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate**(key, value, validations, errors)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#error_message

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ OptionalValidator 
  

  

  

  
    

Returns a new instance of OptionalValidator.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/hash_validator/validators/optional_validator.rb', line 6

def initialize
  super("_optional")  # The name of the validator, underscored as it won't usually be directly invoked (invoked through use of validator)
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**should_validate?**(validation)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/hash_validator/validators/optional_validator.rb', line 10

def should_validate?(validation)
  validation.is_a?(Validations::Optional)
end
```

    
  

    
      
  
### 
  
    #**validate**(key, value, validations, errors)  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
18
19
```

    
    
      

```
# File 'lib/hash_validator/validators/optional_validator.rb', line 14

def validate(key, value, validations, errors)
  unless value.nil?
    ::HashValidator.validator_for(validations.validation).validate(key, value, validations.validation, errors)
    errors.delete(key) if errors[key].respond_to?(:empty?) && errors[key].empty?
  end
end
```