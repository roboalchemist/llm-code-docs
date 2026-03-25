# Class: Valcro::Error
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Valcro::Error
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/valcro/error.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**message**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute message.

  

    
      
- 
  
    
      #**property**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute property.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(property, message)  ⇒ Error 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Error.

  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(property, message)  ⇒ Error 
  

  

  

  
    

Returns a new instance of Error.

  

  

  
    
      

```

7
8
9
10
```

    
    
      

```
# File 'lib/valcro/error.rb', line 7

def initialize(property, message)
  @property = property
  @message = message
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**message**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute message.

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/valcro/error.rb', line 5

def message
  @message
end
```

    
  

    
      
      
      
  
### 
  
    #**property**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute property.

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/valcro/error.rb', line 5

def property
  @property
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
17
18
```

    
    
      

```
# File 'lib/valcro/error.rb', line 12

def to_s
  if @property == :base
    message
  else
    "#{property} #{message}"
  end
end
```