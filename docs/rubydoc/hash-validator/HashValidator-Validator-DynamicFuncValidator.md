# Class: HashValidator::Validator::DynamicFuncValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::DynamicFuncValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/dynamic_func_validator.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**custom_error_message**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute custom_error_message.

  

    
      
- 
  
    
      #**func**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute func.

  

    
  

  
  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(name, func, error_message = nil)  ⇒ DynamicFuncValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of DynamicFuncValidator.

  

      
        
- 
  
    
      #**valid?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#should_validate?, #validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, func, error_message = nil)  ⇒ DynamicFuncValidator 
  

  

  

  
    

Returns a new instance of DynamicFuncValidator.

  

  

  
    
      

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
# File 'lib/hash_validator/validators/dynamic_func_validator.rb', line 6

def initialize(name, func, error_message = nil)
  super(name)

  unless func.respond_to?(:call)
    raise ArgumentError, "Function must be callable (proc or lambda)"
  end

  @func = func
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
# File 'lib/hash_validator/validators/dynamic_func_validator.rb', line 4

def custom_error_message
  @custom_error_message
end
```

    
  

    
      
      
      
  
### 
  
    #**func**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute func.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/dynamic_func_validator.rb', line 4

def func
  @func
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
# File 'lib/hash_validator/validators/dynamic_func_validator.rb', line 17

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
25
```

    
    
      

```
# File 'lib/hash_validator/validators/dynamic_func_validator.rb', line 21

def valid?(value)
  !!@func.call(value)
rescue
  false
end
```