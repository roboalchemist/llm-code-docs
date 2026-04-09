# Class: WebsocketRails::ConnectionAdapters::WebSocket
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- WebsocketRails::ConnectionAdapters::WebSocket
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/connection_adapters/web_socket.rb
  
  

  
## Constant Summary

  
  
### Constants included
     from Logging

  

Logging::ANSI, Logging::LOGGABLE_DATA

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#data_store, #dispatcher, #env, #id, #pong, #queue, #request

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**accepts?**(env)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**close!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(request, dispatcher)  ⇒ WebSocket 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of WebSocket.

  

      
        
- 
  
    
      #**on_message**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#connected?, #controller_delegate, #enqueue, #flush, inherited, #inspect, #on_close, #on_error, #on_open, #rack_response, #send_message, #to_s, #trigger, #user, #user_connection?, #user_identifier

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

#color_for_level, #colorize, configure, #log, #log_data?, #log_event, #log_event?, #log_event_end, #log_event_start, #log_exception, #log_header, log_level, #wrap

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(request, dispatcher)  ⇒ WebSocket 
  

  

  

  
    

Returns a new instance of WebSocket.

  

  

  
    
      

```

9
10
11
12
13
14
15
16
17
18
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/web_socket.rb', line 9

def initialize(request, dispatcher)
  super
  @connection = Faye::WebSocket.new(request.env)
  @connection.onmessage = method(:on_message)
  @connection.onerror   = method(:on_error)
  @connection.onclose   = method(:on_close)
  EM.next_tick do
    on_open
  end
end
```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**accepts?**(env)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/web_socket.rb', line 5

def self.accepts?(env)
  Faye::WebSocket.websocket?( env )
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**close!**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/web_socket.rb', line 29

def close!
  @connection.close
end
```

    
  

    
      
  
### 
  
    #**on_message**(event)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
27
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/web_socket.rb', line 24

def on_message(event)
  data = event.respond_to?(:data) ? event.data : event
  super data
end
```

    
  

    
      
  
### 
  
    #**send**(message)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/web_socket.rb', line 20

def send(message)
  @connection.send message
end
```