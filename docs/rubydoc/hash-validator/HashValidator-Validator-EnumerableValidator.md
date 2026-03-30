# Class: HashValidator::Validator::EnumerableValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::EnumerableValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/enumerable_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ EnumerableValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of EnumerableValidator.

  

      
        
- 
  
    
      #**should_validate?**(rhs)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**valid?**(value, validations)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ EnumerableValidator 
  

  

  

  
    

Returns a new instance of EnumerableValidator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/enumerable_validator.rb', line 4

def initialize
  super("_enumerable")  # The name of the validator, underscored as it won't usually be directly invoked (invoked through use of validator)
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**error_message**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/hash_validator/validators/enumerable_validator.rb', line 12

def error_message
  "value from list required"
end
```

    
  

    
      
  
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
# File 'lib/hash_validator/validators/enumerable_validator.rb', line 8

def should_validate?(rhs)
  rhs.is_a?(Enumerable)
end
```

    
  

    
      
  
### 
  
    #**valid?**(value, validations)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/hash_validator/validators/enumerable_validator.rb', line 16

def valid?(value, validations)
  validations.include?(value)
end
```