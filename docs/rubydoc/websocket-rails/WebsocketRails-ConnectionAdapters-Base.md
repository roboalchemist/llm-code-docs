# Class: WebsocketRails::ConnectionAdapters::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::ConnectionAdapters::Base
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Logging
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/connection_adapters.rb
  
  

  
## Direct Known Subclasses

  

Http, WebSocket

  
## Constant Summary

  
  
### Constants included
     from Logging

  

Logging::ANSI, Logging::LOGGABLE_DATA

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**data_store**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute data_store.

  

    
      
- 
  
    
      #**dispatcher**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute dispatcher.

  

    
      
- 
  
    
      #**env**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute env.

  

    
      
- 
  
    
      #**id**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The ConnectionManager will set the connection ID when the connection is opened.

  

    
      
- 
  
    
      #**pong**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute pong.

  

    
      
- 
  
    
      #**queue**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute queue.

  

    
      
- 
  
    
      #**request**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute request.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**accepts?**(env)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**inherited**(adapter)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**connected?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**controller_delegate**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**enqueue**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**flush**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(request, dispatcher)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**on_close**(data = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**on_error**(data = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**on_message**(encoded_data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**on_open**(data = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**rack_response**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_message**(event_name, data = {}, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**user**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**user_connection?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**user_identifier**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

#color_for_level, #colorize, configure, #log, #log_data?, #log_event, #log_event?, #log_event_end, #log_event_start, #log_exception, #log_header, log_level, #wrap

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(request, dispatcher)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

35
36
37
38
39
40
41
42
43
44
45
46
47
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 35

def initialize(request, dispatcher)
  @env        = request.env.dup
  @request    = request
  @dispatcher = dispatcher
  @connected  = true
  @queue      = EventQueue.new
  @data_store = DataStore::Connection.new(self)
  @delegate   = WebsocketRails::DelegationController.new
  @delegate.instance_variable_set(:@_env, request.env)
  @delegate.instance_variable_set(:@_request, request)

  start_ping_timer
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**data_store**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute data_store.

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 29

def data_store
  @data_store
end
```

    
  

    
      
      
      
  
### 
  
    #**dispatcher**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute dispatcher.

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 29

def dispatcher
  @dispatcher
end
```

    
  

    
      
      
      
  
### 
  
    #**env**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute env.

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 29

def env
  @env
end
```

    
  

    
      
      
      
  
### 
  
    #**id**  ⇒ Object 
  

  

  

  
    

The ConnectionManager will set the connection ID when the connection is opened.

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 33

def id
  @id
end
```

    
  

    
      
      
      
  
### 
  
    #**pong**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute pong.

  

  

  
    
      

```

162
163
164
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 162

def pong
  @pong
end
```

    
  

    
      
      
      
  
### 
  
    #**queue**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute queue.

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 29

def queue
  @queue
end
```

    
  

    
      
      
      
  
### 
  
    #**request**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute request.

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 29

def request
  @request
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**accepts?**(env)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 21

def self.accepts?(env)
  false
end
```

    
  

    
      
  
### 
  
    .**inherited**(adapter)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 25

def self.inherited(adapter)
  ConnectionAdapters.register adapter
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**connected?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

108
109
110
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 108

def connected?
  true & @connected
end
```

    
  

    
      
  
### 
  
    #**controller_delegate**  ⇒ Object 
  

  

  

  
    
      

```

104
105
106
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 104

def controller_delegate
  @delegate
end
```

    
  

    
      
  
### 
  
    #**enqueue**(event)  ⇒ Object 
  

  

  

  
    
      

```

72
73
74
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 72

def enqueue(event)
  @queue << event
end
```

    
  

    
      
  
### 
  
    #**flush**  ⇒ Object 
  

  

  

  
    
      

```

80
81
82
83
84
85
86
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 80

def flush
  message = []
  @queue.flush do |event|
    message << event.as_json
  end
  send message.to_json
end
```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

112
113
114
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 112

def inspect
  "#<Connection::#{id}>"
end
```

    
  

    
      
  
### 
  
    #**on_close**(data = nil)  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
63
64
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 60

def on_close(data=nil)
  @ping_timer.cancel
  dispatch Event.new_on_close( self, data )
  close_connection
end
```

    
  

    
      
  
### 
  
    #**on_error**(data = nil)  ⇒ Object 
  

  

  

  
    
      

```

66
67
68
69
70
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 66

def on_error(data=nil)
  event = Event.new_on_error( self, data )
  dispatch event
  on_close event.data
end
```

    
  

    
      
  
### 
  
    #**on_message**(encoded_data)  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
58
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 55

def on_message(encoded_data)
  event = Event.new_from_json( encoded_data, self )
  dispatch event
end
```

    
  

    
      
  
### 
  
    #**on_open**(data = nil)  ⇒ Object 
  

  

  

  
    
      

```

49
50
51
52
53
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 49

def on_open(data=nil)
  event = Event.new_on_open( self, data )
  dispatch event
  trigger event
end
```

    
  

    
      
  
### 
  
    #**rack_response**  ⇒ Object 
  

  

  

  
    
      

```

100
101
102
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 100

def rack_response
  [ -1, {}, [] ]
end
```

    
  

    
      
  
### 
  
    #**send**(message)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

96
97
98
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 96

def send(message)
  raise NotImplementedError, "Override this method in the connection specific adapter class"
end
```

    
  

    
      
  
### 
  
    #**send_message**(event_name, data = {}, options = {})  ⇒ Object 
  

  

  

  
    
      

```

88
89
90
91
92
93
94
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 88

def send_message(event_name, data = {}, options = {})
  options.merge! :user_id => user_identifier, :connection => self
  options[:data] = data

  event = Event.new(event_name, options)
  event.trigger
end
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

116
117
118
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 116

def to_s
  inspect
end
```

    
  

    
      
  
### 
  
    #**trigger**(event)  ⇒ Object 
  

  

  

  
    
      

```

76
77
78
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 76

def trigger(event)
  send "[#{event.serialize}]"
end
```

    
  

    
      
  
### 
  
    #**user**  ⇒ Object 
  

  

  

  
    
      

```

124
125
126
127
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 124

def user
  return unless user_connection?
  controller_delegate.current_user
end
```

    
  

    
      
  
### 
  
    #**user_connection?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

120
121
122
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 120

def user_connection?
  not user_identifier.nil?
end
```

    
  

    
      
  
### 
  
    #**user_identifier**  ⇒ Object 
  

  

  

  
    
      

```

129
130
131
132
133
134
135
136
137
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 129

def user_identifier
  @user_identifier ||= begin
    identifier = WebsocketRails.config.user_identifier

    return unless current_user_responds_to?(identifier)

    controller_delegate.current_user.send(identifier)
   end
end
```