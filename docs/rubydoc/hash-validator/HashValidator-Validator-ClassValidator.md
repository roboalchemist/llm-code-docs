# Class: HashValidator::Validator::ClassValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::ClassValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/class_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**  ⇒ ClassValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ClassValidator.

  

      
        
- 
  
    
      #**should_validate?**(rhs)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate**(key, value, klass, errors)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#error_message

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ ClassValidator 
  

  

  

  
    

Returns a new instance of ClassValidator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/class_validator.rb', line 4

def initialize
  super("_class")  # The name of the validator, underscored as it won't usually be directly invoked (invoked through use of validator)
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
# File 'lib/hash_validator/validators/class_validator.rb', line 8

def should_validate?(rhs)
  rhs.is_a?(Class)
end
```

    
  

    
      
  
### 
  
    #**validate**(key, value, klass, errors)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
```

    
    
      

```
# File 'lib/hash_validator/validators/class_validator.rb', line 12

def validate(key, value, klass, errors)
  unless value.is_a?(klass)
    errors[key] = "#{klass} required"
  end
end
```