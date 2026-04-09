# Class: HashValidator::Validator::MultipleValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::MultipleValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/multiple_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**  ⇒ MultipleValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of MultipleValidator.

  

      
        
- 
  
    
      #**should_validate?**(validation)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate**(key, value, validations, errors)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#error_message

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ MultipleValidator 
  

  

  

  
    

Returns a new instance of MultipleValidator.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/hash_validator/validators/multiple_validator.rb', line 6

def initialize
  super("_multiple")  # The name of the validator, underscored as it won't usually be directly invoked (invoked through use of validator)
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
# File 'lib/hash_validator/validators/multiple_validator.rb', line 10

def should_validate?(validation)
  validation.is_a?(Validations::Multiple)
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
20
21
22
23
24
```

    
    
      

```
# File 'lib/hash_validator/validators/multiple_validator.rb', line 14

def validate(key, value, validations, errors)
  multiple_errors = []

  validations.validations.each do |validation|
    validation_error = {}
    ::HashValidator.validator_for(validation).validate(key, value, validation, validation_error)
    multiple_errors << validation_error[key] if validation_error[key]
  end

  errors[key] = multiple_errors.join(", ") if multiple_errors.any?
end
```