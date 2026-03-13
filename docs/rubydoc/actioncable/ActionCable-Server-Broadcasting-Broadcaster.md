# Class: ActionCable::Server::Broadcasting::Broadcaster
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Server::Broadcasting::Broadcaster
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/server/broadcasting.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**broadcasting**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute broadcasting.

  

    
      
- 
  
    
      #**coder**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute coder.

  

    
      
- 
  
    
      #**server**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute server.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**broadcast**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(server, broadcasting, coder:)  ⇒ Broadcaster 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Broadcaster.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(server, broadcasting, coder:)  ⇒ Broadcaster 
  

  

  

  
    

Returns a new instance of Broadcaster.

  

  

  
    
      

```

48
49
50
```

    
    
      

```
# File 'lib/action_cable/server/broadcasting.rb', line 48

def initialize(server, broadcasting, coder:)
  @server, @broadcasting, @coder = server, broadcasting, coder
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**broadcasting**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute broadcasting.

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/action_cable/server/broadcasting.rb', line 46

def broadcasting
  @broadcasting
end
```

    
  

    
      
      
      
  
### 
  
    #**coder**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute coder.

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/action_cable/server/broadcasting.rb', line 46

def coder
  @coder
end
```

    
  

    
      
      
      
  
### 
  
    #**server**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute server.

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/action_cable/server/broadcasting.rb', line 46

def server
  @server
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**broadcast**(message)  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
55
56
57
58
59
60
```

    
    
      

```
# File 'lib/action_cable/server/broadcasting.rb', line 52

def broadcast(message)
  server.logger.debug { "[ActionCable] Broadcasting to #{broadcasting}: #{message.inspect.truncate(300)}" }

  payload = { broadcasting: broadcasting, message: message, coder: coder }
  ActiveSupport::Notifications.instrument("broadcast.action_cable", payload) do
    encoded = coder ? coder.encode(message) : message
    server.pubsub.broadcast broadcasting, encoded
  end
end
```