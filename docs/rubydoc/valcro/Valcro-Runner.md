# Class: Valcro::Runner
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Valcro::Runner
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/valcro/runner.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**error_list**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute error_list.

  

    
      
- 
  
    
      #**validators**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute validators.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_validator**(validator)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**clear!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(error_list = ErrorList.new)  ⇒ Runner 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Runner.

  

      
        
- 
  
    
      #**validate**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(error_list = ErrorList.new)  ⇒ Runner 
  

  

  

  
    

Returns a new instance of Runner.

  

  

  
    
      

```

6
7
8
9
```

    
    
      

```
# File 'lib/valcro/runner.rb', line 6

def initialize(error_list = ErrorList.new)
  @validators = []
  @error_list = error_list
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**error_list**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute error_list.

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/valcro/runner.rb', line 5

def error_list
  @error_list
end
```

    
  

    
      
      
      
  
### 
  
    #**validators**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute validators.

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/valcro/runner.rb', line 5

def validators
  @validators
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_validator**(validator)  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/valcro/runner.rb', line 16

def add_validator(validator)
  @validators << validator
end
```

    
  

    
      
  
### 
  
    #**clear!**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
14
```

    
    
      

```
# File 'lib/valcro/runner.rb', line 11

def clear!
  @validators.clear
  @error_list.clear!
end
```

    
  

    
      
  
### 
  
    #**validate**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
24
```

    
    
      

```
# File 'lib/valcro/runner.rb', line 20

def validate
  @validators.each do |validator|
    validator.call error_list
  end
end
```