# Class: HashValidator::Validator::SimpleValidator
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- HashValidator::Validator::SimpleValidator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/validators/simple_validator.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**lambda**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute lambda.

  

    
  

  
  
  
### Attributes inherited from Base

  

#name

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(name, lambda)  ⇒ SimpleValidator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of SimpleValidator.

  

      
        
- 
  
    
      #**valid?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#error_message, #should_validate?, #validate

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, lambda)  ⇒ SimpleValidator 
  

  

  

  
    

Returns a new instance of SimpleValidator.

  

  

  
    
      

```

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
# File 'lib/hash_validator/validators/simple_validator.rb', line 7

def initialize(name, lambda)
  # lambda must accept one argument (the value)
  if lambda.arity != 1
    raise StandardError.new("lambda should take only one argument - passed lambda takes #{lambda.arity}")
  end

  super(name)
  self.lambda = lambda
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**lambda**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute lambda.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/validators/simple_validator.rb', line 4

def lambda
  @lambda
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**valid?**(value)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/hash_validator/validators/simple_validator.rb', line 17

def valid?(value)
  lambda.call(value)
end
```