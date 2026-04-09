# Exception: WebsocketRails::EventRoutingError
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- WebsocketRails::EventRoutingError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket-rails.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**controller**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute controller.

  

    
      
- 
  
    
      #**event**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute event.

  

    
      
- 
  
    
      #**method**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute method.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(event, controller, method)  ⇒ EventRoutingError 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of EventRoutingError.

  

      
        
- 
  
    
      #**to_json**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(event, controller, method)  ⇒ EventRoutingError 
  

  

  

  
    

Returns a new instance of EventRoutingError.

  

  

  
    
      

```

63
64
65
66
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 63

def initialize(event, controller, method)
  @event = event
  @controller = controller
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**controller**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute controller.

  

  

  
    
      

```

61
62
63
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 61

def controller
  @controller
end
```

    
  

    
      
      
      
  
### 
  
    #**event**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute event.

  

  

  
    
      

```

61
62
63
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 61

def event
  @event
end
```

    
  

    
      
      
      
  
### 
  
    #**method**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute method.

  

  

  
    
      

```

61
62
63
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 61

def method
  @method
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**to_json**  ⇒ Object 
  

  

  

  
    
      

```

75
76
77
78
79
80
81
82
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 75

def to_json
  super({
    :error => "EventRoutingError",
    :event => event.name,
    :method => method,
    :reason => "Controller #{controller.class} does not respond to #{method}"
  })
end
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

68
69
70
71
72
73
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 68

def to_s
  out =  "Routing Error:\n"
  out << "Event: #{event.name}\n"
  out << "Controller #{controller.class} does not respond to #{method}"
  out
end
```