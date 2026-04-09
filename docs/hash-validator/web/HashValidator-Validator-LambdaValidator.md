# Class: HashValidator::Validator::LambdaValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::LambdaValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/lambda_validator.rb
  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** InvalidArgumentCount
    
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ LambdaValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of LambdaValidator.

  

      
        
- 
  
    
      #**should_validate?**(rhs)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**valid?**(value, lambda)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ LambdaValidator 
  

  

  

  
    

Returns a new instance of LambdaValidator.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/lambda_validator.rb', line 4

def initialize
  super("_lambda")  # The name of the validator, underscored as it won't usually be directly invoked (invoked through use of validator)
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**error_message**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/hash_validator/validators/lambda_validator.rb', line 20

def error_message
  "is not valid"
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
11
12
13
14
15
16
17
18
```

    
    
      

```
# File 'lib/hash_validator/validators/lambda_validator.rb', line 8

def should_validate?(rhs)
  if rhs.is_a?(Proc)
    if rhs.arity == 1
      true
    else
      raise HashValidator::Validator::LambdaValidator::InvalidArgumentCount.new("Lambda validator should only accept one argument, supplied lambda accepts #{rhs.arity}.")
    end
  else
    false
  end
end
```

    
  

    
      
  
### 
  
    #**valid?**(value, lambda)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

24
25
26
27
28
```

    
    
      

```
# File 'lib/hash_validator/validators/lambda_validator.rb', line 24

def valid?(value, lambda)
  lambda.call(value)
rescue
  false
end
```