# Class: HashValidator::Validator::ManyValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::ManyValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/many_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ ManyValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ManyValidator.

  

      
        
- 
  
    
      #**should_validate?**(validation)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate**(key, value, validations, errors)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ ManyValidator 
  

  

  

  
    

Returns a new instance of ManyValidator.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/hash_validator/validators/many_validator.rb', line 6

def initialize
  super("_many")  # The name of the validator, underscored as it won't usually be directly invoked (invoked through use of validator)
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**error_message**  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/hash_validator/validators/many_validator.rb', line 14

def error_message
  "enumerable required"
end
```

    
  

    
      
  
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
# File 'lib/hash_validator/validators/many_validator.rb', line 10

def should_validate?(validation)
  validation.is_a?(Validations::Many)
end
```

    
  

    
      
  
### 
  
    #**validate**(key, value, validations, errors)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/hash_validator/validators/many_validator.rb', line 18

def validate(key, value, validations, errors)
  unless value.is_a?(Enumerable)
    errors[key] = error_message
    return
  end

  element_errors = Array.new

  value.each_with_index do |element, i|
    ::HashValidator.validator_for(validations.validation).validate(i, element, validations.validation, element_errors)
  end

  element_errors.each_with_index do |e, i|
    if e.respond_to?(:empty?) && e.empty?
      element_errors[i] = nil
    end
  end

  errors[key] = element_errors unless element_errors.all?(&:nil?)
end
```