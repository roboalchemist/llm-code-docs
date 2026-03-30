# Class: HashValidator::Validator::DynamicPatternValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::DynamicPatternValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/dynamic_pattern_validator.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**custom_error_message**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute custom_error_message.

  

    
      
- 
  
    
      #**pattern**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute pattern.

  

    
  

  
  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(name, pattern, error_message = nil)  ⇒ DynamicPatternValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of DynamicPatternValidator.

  

      
        
- 
  
    
      #**valid?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#should_validate?, #validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, pattern, error_message = nil)  ⇒ DynamicPatternValidator 
  

  

  

  
    

Returns a new instance of DynamicPatternValidator.

  

  

  
    
      

```

6
7
8
9
10
11
12
13
14
15
```

    
    
      

```
# File 'lib/hash_validator/validators/dynamic_pattern_validator.rb', line 6

def initialize(name, pattern, error_message = nil)
  super(name)

  unless pattern.is_a?(Regexp)
    raise ArgumentError, "Pattern must be a regular expression"
  end

  @pattern = pattern
  @custom_error_message = error_message
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**custom_error_message**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute custom_error_message.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/dynamic_pattern_validator.rb', line 4

def custom_error_message
  @custom_error_message
end
```

    
  

    
      
      
      
  
### 
  
    #**pattern**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute pattern.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/dynamic_pattern_validator.rb', line 4

def pattern
  @pattern
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**error_message**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/hash_validator/validators/dynamic_pattern_validator.rb', line 17

def error_message
  @custom_error_message || super
end
```

    
  

    
      
  
### 
  
    #**valid?**(value)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

21
22
23
24
```

    
    
      

```
# File 'lib/hash_validator/validators/dynamic_pattern_validator.rb', line 21

def valid?(value)
  return false unless value.respond_to?(:to_s)
  @pattern.match?(value.to_s)
end
```