# Class: HashValidator::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- HashValidator::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/base.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**errors**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute errors.

  

    
      
- 
  
    
      #**hash**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute hash.

  

    
      
- 
  
    
      #**validations**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute validations.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**strict?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**validate**(hash, validations, strict = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(hash, validations)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**valid?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(hash, validations)  ⇒ Base 
  

  

  

  
    

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
# File 'lib/hash_validator/base.rb', line 7

def initialize(hash, validations)
  self.errors      = {}
  self.hash        = hash
  self.validations = validations

  validate
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**errors**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute errors.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/base.rb', line 4

def errors
  @errors
end
```

    
  

    
      
      
      
  
### 
  
    #**hash**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute hash.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/base.rb', line 4

def hash
  @hash
end
```

    
  

    
      
      
      
  
### 
  
    #**validations**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute validations.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/hash_validator/base.rb', line 4

def validations
  @validations
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**strict?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/hash_validator/base.rb', line 24

def self.strict?
  @strict
end
```

    
  

    
      
  
### 
  
    .**validate**(hash, validations, strict = false)  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
22
```

    
    
      

```
# File 'lib/hash_validator/base.rb', line 19

def self.validate(hash, validations, strict = false)
  @strict = strict
  new(hash, validations)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**valid?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/hash_validator/base.rb', line 15

def valid?
  errors.empty?
end
```