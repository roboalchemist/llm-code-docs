# Class: HashValidator::Validator::RegexpValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::RegexpValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/regex_validator.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ RegexpValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of RegexpValidator.

  

      
        
- 
  
    
      #**should_validate?**(rhs)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**valid?**(value, regexp)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ RegexpValidator 
  

  

  

  
    

Returns a new instance of RegexpValidator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/regex_validator.rb', line 4

def initialize
  super("_regex")  # The name of the validator, underscored as it won't usually be directly invoked (invoked through use of validator)
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
# File 'lib/hash_validator/validators/regex_validator.rb', line 12

def error_message
  "does not match regular expression"
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
# File 'lib/hash_validator/validators/regex_validator.rb', line 8

def should_validate?(rhs)
  rhs.is_a?(Regexp)
end
```

    
  

    
      
  
### 
  
    #**valid?**(value, regexp)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/hash_validator/validators/regex_validator.rb', line 16

def valid?(value, regexp)
  regexp.match(value.to_s)
end
```