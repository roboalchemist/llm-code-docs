# Class: Brakeman::Logger::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Brakeman::Logger::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/logger.rb
  
  

  
## Direct Known Subclasses

  

Console, Plain, Quiet

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**alert**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Notify regarding errors - use sparingly.

  

      
        
- 
  
    
      #**announce**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Notify about important information - use sparingly.

  

      
        
- 
  
    
      #**cleanup**(newline = true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Called on exit.

  

      
        
- 
  
    
      #**color**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Use ANSI codes to color a string.

  

      
        
- 
  
    
      #**color?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**context**(description) {|_self| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Wraps a step in the scanning process.

  

      
        
- 
  
    
      #**debug**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Output debug information.

  

      
        
- 
  
    
      #**initialize**(options, log_destination = $stderr)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**log**(message, newline: true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Output a message to the log.

  

      
        
- 
  
    
      #**show_timing?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**single_context**(description)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Wraps a substep (e.g. processing one file).

  

      
        
- 
  
    
      #**spin**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Show a spinner.

  

      
        
- 
  
    
      #**update_progress**(current, total, type = 'files')  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Update progress towards a known total.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(options, log_destination = $stderr)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

19
20
21
22
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 19

def initialize(options, log_destination = $stderr)
  @dest = log_destination
  @show_timing = options[:debug] || options[:show_timing]
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**alert**(message)  ⇒ Object 
  

  

  

  
    

Notify regarding errors - use sparingly

  

  

  
    
      

```

38
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 38

def alert(message); end
```

    
  

    
      
  
### 
  
    #**announce**(message)  ⇒ Object 
  

  

  

  
    

Notify about important information - use sparingly

  

  

  
    
      

```

35
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 35

def announce(message); end
```

    
  

    
      
  
### 
  
    #**cleanup**(newline = true)  ⇒ Object 
  

  

  

  
    

Called on exit

  

  

  
    
      

```

60
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 60

def cleanup(newline = true); end
```

    
  

    
      
  
### 
  
    #**color**(message)  ⇒ Object 
  

  

  

  
    

Use ANSI codes to color a string

  

  

  
    
      

```

65
66
67
68
69
70
71
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 65

def color(message, *)
  if @highline
    @highline.color(message, *)
  else
    message
  end
end
```

    
  

    
      
  
### 
  
    #**color?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

73
74
75
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 73

def color?
  @highline and @highline.use_color?
end
```

    
  

    
      
  
### 
  
    #**context**(description) {|_self| ... } ⇒ Object 
  

  

  

  
    

Wraps a step in the scanning process

  

  

Yields:

  
    
- 
      
      
        (_self)
      
      
      
    
  

Yield Parameters:

  
    
- 
      
        _self
      
      
        (Brakeman::Logger::Base)
      
      
      
        —
        

the object that the method was called on

      
    
  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 44

def context(description, &)
  yield self
end
```

    
  

    
      
  
### 
  
    #**debug**(message)  ⇒ Object 
  

  

  

  
    

Output debug information

  

  

  
    
      

```

41
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 41

def debug(message); end
```

    
  

    
      
  
### 
  
    #**log**(message, newline: true)  ⇒ Object 
  

  

  

  
    

Output a message to the log. If newline is `false`, does not output a newline after message.

  

  

  
    
      

```

26
27
28
29
30
31
32
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 26

def log(message, newline: true)
  if newline
    @dest.puts message
  else
    @dest.write message
  end
end
```

    
  

    
      
  
### 
  
    #**show_timing?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

62
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 62

def show_timing? = @show_timing
```

    
  

    
      
  
### 
  
    #**single_context**(description)  ⇒ Object 
  

  

  

  
    

Wraps a substep (e.g. processing one file)

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 49

def single_context(description, &)
  yield
end
```

    
  

    
      
  
### 
  
    #**spin**  ⇒ Object 
  

  

  

  
    

Show a spinner

  

  

  
    
      

```

57
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 57

def spin; end
```

    
  

    
      
  
### 
  
    #**update_progress**(current, total, type = 'files')  ⇒ Object 
  

  

  

  
    

Update progress towards a known total

  

  

  
    
      

```

54
```

    
    
      

```
# File 'lib/brakeman/logger.rb', line 54

def update_progress(current, total, type = 'files'); end
```