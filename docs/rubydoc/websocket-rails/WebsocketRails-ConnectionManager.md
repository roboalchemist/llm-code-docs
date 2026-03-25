# Class: WebsocketRails::ConnectionManager
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::ConnectionManager
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Logging
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/connection_manager.rb
  
  

## Overview

  
    

The `ConnectionManager` class implements the core Rack application that handles incoming WebSocket connections.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        SuccessfulResponse =
          
        
        

```
[200,{'Content-Type' => 'text/plain'},['success']].freeze
```

      
        BadRequestResponse =
          
        
        

```
[400,{'Content-Type' => 'text/plain'},['invalid']].freeze
```

      
        ExceptionResponse =
          
        
        

```
[500,{'Content-Type' => 'text/plain'},['exception']].freeze
```

      
    
  

  
  
  
### Constants included
     from Logging

  

Logging::ANSI, Logging::LOGGABLE_DATA

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**connections**  ⇒ Hash 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Contains a Hash of currently open connections.

  

    
      
- 
  
    
      #**dispatcher**  ⇒ Dispatcher 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Contains the Dispatcher instance for the active server.

  

    
      
- 
  
    
      #**synchronization**  ⇒ Synchronization 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Contains the Synchronization instance for the active server.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**call**(env)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Primary entry point for the Rack application.

  

      
        
- 
  
    
      #**close_connection**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ ConnectionManager 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ConnectionManager.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

#color_for_level, #colorize, configure, #log, #log_data?, #log_event, #log_event?, #log_event_end, #log_event_start, #log_exception, #log_header, log_level, #wrap

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ ConnectionManager 
  

  

  

  
    

Returns a new instance of ConnectionManager.

  

  

  
    
      

```

30
31
32
33
34
35
36
37
38
39
40
41
42
```

    
    
      

```
# File 'lib/websocket_rails/connection_manager.rb', line 30

def initialize
  @connections = {}
  @dispatcher  = Dispatcher.new(self)

  if WebsocketRails.synchronize?
    EM.next_tick do
      Fiber.new {
        Synchronization.synchronize!
        EM.add_shutdown_hook { Synchronization.shutdown! }
      }.resume
    end
  end
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**connections**  ⇒ Hash  (readonly)
  

  

  

  
    

Contains a Hash of currently open connections.

  

  

Returns:

  
    
- 
      
      
        (Hash)
      
      
      
    
  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/websocket_rails/connection_manager.rb', line 20

def connections
  @connections
end
```

    
  

    
      
      
      
  
### 
  
    #**dispatcher**  ⇒ Dispatcher  (readonly)
  

  

  

  
    

Contains the Dispatcher instance for the active server.

  

  

Returns:

  
    
- 
      
      
        (Dispatcher)
      
      
      
    
  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/websocket_rails/connection_manager.rb', line 24

def dispatcher
  @dispatcher
end
```

    
  

    
      
      
      
  
### 
  
    #**synchronization**  ⇒ Synchronization  (readonly)
  

  

  

  
    

Contains the Synchronization instance for the active server.

  

  

Returns:

  
    
- 
      
      
        (Synchronization)
      
      
      
    
  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/websocket_rails/connection_manager.rb', line 28

def synchronization
  @synchronization
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**call**(env)  ⇒ Object 
  

  

  

  
    

Primary entry point for the Rack application

  

  

  
    
      

```

49
50
51
52
53
54
55
56
57
58
59
60
61
```

    
    
      

```
# File 'lib/websocket_rails/connection_manager.rb', line 49

def call(env)
  request = ActionDispatch::Request.new(env)

  if request.post?
    response = parse_incoming_event(request.params)
  else
    response = open_connection(request)
  end

  response
rescue InvalidConnectionError
  BadRequestResponse
end
```

    
  

    
      
  
### 
  
    #**close_connection**(connection)  ⇒ Object 
  

  

  

  
    
      

```

89
90
91
92
93
94
95
96
97
```

    
    
      

```
# File 'lib/websocket_rails/connection_manager.rb', line 89

def close_connection(connection)
  WebsocketRails.channel_manager.unsubscribe connection
  destroy_user_connection connection

  connections.delete connection.id

  info "Connection closed: #{connection}"
  connection = nil
end
```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/websocket_rails/connection_manager.rb', line 44

def inspect
  "websocket_rails"
end
```