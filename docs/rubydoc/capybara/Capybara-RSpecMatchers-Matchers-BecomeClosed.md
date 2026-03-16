# Class: Capybara::RSpecMatchers::Matchers::BecomeClosed
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::RSpecMatchers::Matchers::BecomeClosed
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matchers/become_closed.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**failure_message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**failure_message_when_negated**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(options)  ⇒ BecomeClosed 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of BecomeClosed.

  

      
        
- 
  
    
      #**matches?**(window)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(options)  ⇒ BecomeClosed 
  

  

  

  
    

Returns a new instance of BecomeClosed.

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/become_closed.rb', line 7

def initialize(options)
  @options = options
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**failure_message**  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/become_closed.rb', line 23

def failure_message
  "expected #{@window.inspect} to become closed after #{@wait_time} seconds"
end
```

    
  

    
      
  
### 
  
    #**failure_message_when_negated**  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/become_closed.rb', line 27

def failure_message_when_negated
  "expected #{@window.inspect} not to become closed after #{@wait_time} seconds"
end
```

    
  

    
      
  
### 
  
    #**matches?**(window)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

11
12
13
14
15
16
17
18
19
20
21
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/become_closed.rb', line 11

def matches?(window)
  @window = window
  @wait_time = Capybara::Queries::BaseQuery.wait(@options, window.session.config.default_max_wait_time)
  timer = Capybara::Helpers.timer(expire_in: @wait_time)
  while window.exists?
    return false if timer.expired?

    sleep 0.01
  end
  true
end
```