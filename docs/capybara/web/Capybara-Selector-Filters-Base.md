# Class: Capybara::Selector::Filters::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Selector::Filters::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selector/filters/base.rb
  
  

  
## Direct Known Subclasses

  

ExpressionFilter, NodeFilter

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**boolean?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**format**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**handles_option?**(option_name)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(name, matcher, block, **options)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**matcher?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**skip?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, matcher, block, **options)  ⇒ Base 
  

  

  

  
    

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
# File 'lib/capybara/selector/filters/base.rb', line 7

def initialize(name, matcher, block, **options)
  @name = name
  @matcher = matcher
  @block = block
  @options = options
  @options[:valid_values] = [true, false] if options[:boolean]
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**boolean?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/capybara/selector/filters/base.rb', line 35

def boolean?
  !!@options[:boolean]
end
```

    
  

    
      
  
### 
  
    #**default**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/capybara/selector/filters/base.rb', line 19

def default
  @options[:default]
end
```

    
  

    
      
  
### 
  
    #**default?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/capybara/selector/filters/base.rb', line 15

def default?
  @options.key?(:default)
end
```

    
  

    
      
  
### 
  
    #**format**  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/capybara/selector/filters/base.rb', line 27

def format
  @options[:format]
end
```

    
  

    
      
  
### 
  
    #**handles_option?**(option_name)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

39
40
41
42
43
44
45
```

    
    
      

```
# File 'lib/capybara/selector/filters/base.rb', line 39

def handles_option?(option_name)
  if matcher?
    @matcher.match? option_name
  else
    @name == option_name
  end
end
```

    
  

    
      
  
### 
  
    #**matcher?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/capybara/selector/filters/base.rb', line 31

def matcher?
  !@matcher.nil?
end
```

    
  

    
      
  
### 
  
    #**skip?**(value)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/capybara/selector/filters/base.rb', line 23

def skip?(value)
  @options.key?(:skip_if) && value == @options[:skip_if]
end
```