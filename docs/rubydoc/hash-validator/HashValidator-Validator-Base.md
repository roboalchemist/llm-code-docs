# Class: HashValidator::Validator::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- HashValidator::Validator::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/base.rb
  
  

  
## Direct Known Subclasses

  

AlphaValidator, AlphanumericValidator, ArrayValidator, BooleanValidator, ClassValidator, DigitsValidator, DynamicFuncValidator, DynamicPatternValidator, EmailValidator, EnumerableValidator, HashValidator, HexColorValidator, IpValidator, Ipv4Validator, Ipv6Validator, JsonValidator, LambdaValidator, ManyValidator, MultipleValidator, OptionalValidator, PresenceValidator, RegexpValidator, SimpleValidator, UrlValidator

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(name)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**should_validate?**(name)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validate**(key, value, validations, errors)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

7
8
9
10
11
12
13
```

    
    
      

```
# File 'lib/hash_validator/validators/base.rb', line 7

def initialize(name)
  self.name = name.to_s

  unless self.name.size > 0
    raise StandardError.new("Validator must be initialized with a valid name (length greater than zero)")
  end
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**name**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute name.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/base.rb', line 4

def name
  @name
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**error_message**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/hash_validator/validators/base.rb', line 19

def error_message
  "#{self.name} required"
end
```

    
  

    
      
  
### 
  
    #**should_validate?**(name)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/hash_validator/validators/base.rb', line 15

def should_validate?(name)
  self.name == name.to_s
end
```

    
  

    
      
  
### 
  
    #**validate**(key, value, validations, errors)  ⇒ Object 
  

  

  

  
    
      

```

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
40
41
42
43
```

    
    
      

```
# File 'lib/hash_validator/validators/base.rb', line 23

def validate(key, value, validations, errors)
  # If the subclass implements valid?, use that for simple boolean validation
  if self.class.instance_methods(false).include?(:valid?)
    # Check the arity of the valid? method to determine how many arguments to pass
    valid_result = case method(:valid?).arity
    when 1
      valid?(value)
    when 2
      valid?(value, validations)
    else
      raise StandardError.new("valid? method must accept either 1 argument (value) or 2 arguments (value, validations)")
    end

    unless valid_result
      errors[key] = error_message
    end
  else
    # Otherwise, subclass must override validate
    raise StandardError.new("Validator must implement either valid? or override validate method")
  end
end
```