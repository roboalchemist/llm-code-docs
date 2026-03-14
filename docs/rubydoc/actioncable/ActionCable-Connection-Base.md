# Class: ActionCable::Connection::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Connection::Base
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Authorization, Callbacks, Identification, InternalChannel, ActiveSupport::Rescuable
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/base.rb
  
  

## Overview

  
    

# Action Cable Connection Base

For every WebSocket connection the Action Cable server accepts, a Connection object will be instantiated. This instance becomes the parent of all of the channel subscriptions that are created from there on. Incoming messages are then routed to these channel subscriptions based on an identifier sent by the Action Cable consumer. The Connection itself does not deal with any specific application logic beyond authentication and authorization.

Here’s a basic example:

```
module ApplicationCable
  class Connection < ActionCable::Connection::Base
    identified_by :current_user

    def connect
      self.current_user = find_verified_user
      logger.add_tags current_user.name
    end

    def disconnect
      # Any cleanup work needed when the cable connection is cut.
    end

    private
      def find_verified_user
        User.find_by_identity(cookies.encrypted[:identity_id]) ||
          reject_unauthorized_connection
      end
  end
end

```

First, we declare that this connection can be identified by its current_user. This allows us to later be able to find all connections established for that current_user (and potentially disconnect them). You can declare as many identification indexes as you like. Declaring an identification means that an attr_accessor is automatically set for that key.

Second, we rely on the fact that the WebSocket connection is established with the cookies from the domain being sent along. This makes it easy to use signed cookies that were set when logging in via a web interface to authorize the WebSocket connection.

Finally, we add a tag to the connection-specific logger with the name of the current user to easily distinguish their messages in the log.

Pretty simple, eh?

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**env**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute env.

  

    
      
- 
  
    
      #**logger**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute logger.

  

    
      
- 
  
    
      #**protocol**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute protocol.

  

    
      
- 
  
    
      #**server**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute server.

  

    
      
- 
  
    
      #**subscriptions**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute subscriptions.

  

    
      
- 
  
    
      #**worker_pool**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute worker_pool.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**beat**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**close**(reason: nil, reconnect: true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Close the WebSocket connection.

  

      
        
- 
  
    
      #**dispatch_websocket_message**(websocket_message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**handle_channel_command**(payload)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(server, env, coder: ActiveSupport::JSON)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**on_close**(reason, code)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**on_error**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**on_message**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**on_open**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**process**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Called by the server when a new WebSocket connection is established.

  

      
        
- 
  
    
      #**receive**(websocket_message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Decodes WebSocket messages and dispatches them to subscribed channels.

  

      
        
- 
  
    
      #**send_async**(method, *arguments)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Invoke a method on the connection asynchronously through the pool of thread workers.

  

      
        
- 
  
    
      #**statistics**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return a basic hash of statistics for the connection keyed with `identifier`, `started_at`, `subscriptions`, and `request_id`.

  

      
        
- 
  
    
      #**transmit**(cable_message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Authorization

  

#reject_unauthorized_connection

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Identification

  

#connection_identifier

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(server, env, coder: ActiveSupport::JSON)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

67
68
69
70
71
72
73
74
75
76
77
78
79
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 67

def initialize(server, env, coder: ActiveSupport::JSON)
  @server, @env, @coder = server, env, coder

  @worker_pool = server.worker_pool
  @logger = new_tagged_logger

  @websocket      = ActionCable::Connection::WebSocket.new(env, self, event_loop)
  @subscriptions  = ActionCable::Connection::Subscriptions.new(self)
  @message_buffer = ActionCable::Connection::MessageBuffer.new(self)

  @_internal_subscriptions = nil
  @started_at = Time.now
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**env**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute env.

  

  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 64

def env
  @env
end
```

    
  

    
      
      
      
  
### 
  
    #**logger**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute logger.

  

  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 64

def logger
  @logger
end
```

    
  

    
      
      
      
  
### 
  
    #**protocol**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute protocol.

  

  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 64

def protocol
  @protocol
end
```

    
  

    
      
      
      
  
### 
  
    #**server**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute server.

  

  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 64

def server
  @server
end
```

    
  

    
      
      
      
  
### 
  
    #**subscriptions**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute subscriptions.

  

  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 64

def subscriptions
  @subscriptions
end
```

    
  

    
      
      
      
  
### 
  
    #**worker_pool**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute worker_pool.

  

  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 64

def worker_pool
  @worker_pool
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**beat**  ⇒ Object 
  

  

  

  
    
      

```

147
148
149
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 147

def beat
  transmit type: ActionCable::INTERNAL[:message_types][:ping], message: Time.now.to_i
end
```

    
  

    
      
  
### 
  
    #**close**(reason: nil, reconnect: true)  ⇒ Object 
  

  

  

  
    

Close the WebSocket connection.

  

  

  
    
      

```

120
121
122
123
124
125
126
127
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 120

def close(reason: nil, reconnect: true)
  transmit(
    type: ActionCable::INTERNAL[:message_types][:disconnect],
    reason: reason,
    reconnect: reconnect
  )
  websocket.close
end
```

    
  

    
      
  
### 
  
    #**dispatch_websocket_message**(websocket_message)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

101
102
103
104
105
106
107
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 101

def dispatch_websocket_message(websocket_message) # :nodoc:
  if websocket.alive?
    handle_channel_command decode(websocket_message)
  else
    logger.error "Ignoring message processed after the WebSocket was closed: #{websocket_message.inspect})"
  end
end
```

    
  

    
      
  
### 
  
    #**handle_channel_command**(payload)  ⇒ Object 
  

  

  

  
    
      

```

109
110
111
112
113
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 109

def handle_channel_command(payload)
  run_callbacks :command do
    subscriptions.execute_command payload
  end
end
```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

168
169
170
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 168

def inspect # :nodoc:
  "#<#{self.class.name}:#{'%#016x' % (object_id << 1)}>"
end
```

    
  

    
      
  
### 
  
    #**on_close**(reason, code)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

164
165
166
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 164

def on_close(reason, code) # :nodoc:
  send_async :handle_close
end
```

    
  

    
      
  
### 
  
    #**on_error**(message)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

159
160
161
162
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 159

def on_error(message) # :nodoc:
  # log errors to make diagnosing socket errors easier
  logger.error "WebSocket error occurred: #{message}"
end
```

    
  

    
      
  
### 
  
    #**on_message**(message)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

155
156
157
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 155

def on_message(message) # :nodoc:
  message_buffer.append message
end
```

    
  

    
      
  
### 
  
    #**on_open**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

151
152
153
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 151

def on_open # :nodoc:
  send_async :handle_open
end
```

    
  

    
      
  
### 
  
    #**process**  ⇒ Object 
  

  

  

  
    

Called by the server when a new WebSocket connection is established. This configures the callbacks intended for overwriting by the user. This method should not be called directly – instead rely upon on the #connect (and #disconnect) callbacks.

  

  

  
    
      

```

85
86
87
88
89
90
91
92
93
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 85

def process # :nodoc:
  logger.info started_request_message

  if websocket.possible? && allow_request_origin?
    respond_to_successful_request
  else
    respond_to_invalid_request
  end
end
```

    
  

    
      
  
### 
  
    #**receive**(websocket_message)  ⇒ Object 
  

  

  

  
    

Decodes WebSocket messages and dispatches them to subscribed channels. WebSocket message transfer encoding is always JSON.

  

  

  
    
      

```

97
98
99
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 97

def receive(websocket_message) # :nodoc:
  send_async :dispatch_websocket_message, websocket_message
end
```

    
  

    
      
  
### 
  
    #**send_async**(method, *arguments)  ⇒ Object 
  

  

  

  
    

Invoke a method on the connection asynchronously through the pool of thread workers.

  

  

  
    
      

```

131
132
133
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 131

def send_async(method, *arguments)
  worker_pool.async_invoke(self, method, *arguments)
end
```

    
  

    
      
  
### 
  
    #**statistics**  ⇒ Object 
  

  

  

  
    

Return a basic hash of statistics for the connection keyed with `identifier`, `started_at`, `subscriptions`, and `request_id`. This can be returned by a health check against the connection.

  

  

  
    
      

```

138
139
140
141
142
143
144
145
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 138

def statistics
  {
    identifier: connection_identifier,
    started_at: @started_at,
    subscriptions: subscriptions.identifiers,
    request_id: @env["action_dispatch.request_id"]
  }
end
```

    
  

    
      
  
### 
  
    #**transmit**(cable_message)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

115
116
117
```

    
    
      

```
# File 'lib/action_cable/connection/base.rb', line 115

def transmit(cable_message) # :nodoc:
  websocket.transmit encode(cable_message)
end
```