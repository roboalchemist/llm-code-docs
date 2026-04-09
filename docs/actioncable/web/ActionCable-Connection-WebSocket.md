# Class: ActionCable::Connection::WebSocket
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Connection::WebSocket
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/web_socket.rb
  
  

## Overview

  
    

# Action Cable Connection WebSocket

Wrap the real socket to minimize the externally-presented API

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**alive?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**close**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(env, event_target, event_loop, protocols: ActionCable::INTERNAL[:protocols])  ⇒ WebSocket 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**possible?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**protocol**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**rack_response**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**transmit**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(env, event_target, event_loop, protocols: ActionCable::INTERNAL[:protocols])  ⇒ WebSocket 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/action_cable/connection/web_socket.rb', line 13

def initialize(env, event_target, event_loop, protocols: ActionCable::INTERNAL[:protocols])
  @websocket = ::WebSocket::Driver.websocket?(env) ? ClientSocket.new(env, event_target, event_loop, protocols) : nil
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**alive?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/action_cable/connection/web_socket.rb', line 21

def alive?
  websocket&.alive?
end
```

    
  

    
      
  
### 
  
    #**close**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/action_cable/connection/web_socket.rb', line 29

def close(...)
  websocket&.close(...)
end
```

    
  

    
      
  
### 
  
    #**possible?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/action_cable/connection/web_socket.rb', line 17

def possible?
  websocket
end
```

    
  

    
      
  
### 
  
    #**protocol**  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/action_cable/connection/web_socket.rb', line 33

def protocol
  websocket&.protocol
end
```

    
  

    
      
  
### 
  
    #**rack_response**  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/action_cable/connection/web_socket.rb', line 37

def rack_response
  websocket&.rack_response
end
```

    
  

    
      
  
### 
  
    #**transmit**  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/action_cable/connection/web_socket.rb', line 25

def transmit(...)
  websocket&.transmit(...)
end
```