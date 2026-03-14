# Class: Valcro::ErrorList
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Valcro::ErrorList
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/valcro/error_list.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**errors**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute errors.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**<<**(error)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**[]**(prop)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**add**(prop, message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**any?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**clear!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**full_messages**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ ErrorList 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ErrorList.

  

      
        
- 
  
    
      #**none?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ ErrorList 
  

  

  

  
    

Returns a new instance of ErrorList.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/valcro/error_list.rb', line 6

def initialize
  @errors = []
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**errors**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute errors.

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/valcro/error_list.rb', line 5

def errors
  @errors
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**<<**(error)  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/valcro/error_list.rb', line 10

def <<(error)
  @errors << error
end
```

    
  

    
      
  
### 
  
    #**[]**(prop)  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/valcro/error_list.rb', line 18

def [](prop)
  @errors.select { |error| error.property == prop }.map(&:message) || []
end
```

    
  

    
      
  
### 
  
    #**add**(prop, message)  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/valcro/error_list.rb', line 14

def add(prop, message)
  @errors << Valcro::Error.new(prop, message)
end
```

    
  

    
      
  
### 
  
    #**any?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/valcro/error_list.rb', line 34

def any?
  @errors.any?
end
```

    
  

    
      
  
### 
  
    #**clear!**  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/valcro/error_list.rb', line 22

def clear!
  @errors = []
end
```

    
  

    
      
  
### 
  
    #**full_messages**  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/valcro/error_list.rb', line 26

def full_messages
  @errors.map(&:to_s)
end
```

    
  

    
      
  
### 
  
    #**none?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/valcro/error_list.rb', line 38

def none?
  @errors.none?
end
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
```

    
    
      

```
# File 'lib/valcro/error_list.rb', line 30

def to_s
  full_messages.join(" ")
end
```