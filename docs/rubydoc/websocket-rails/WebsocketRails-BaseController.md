# Class: WebsocketRails::BaseController
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::BaseController
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      AbstractController::Callbacks, Metal
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/base_controller.rb
  
  

## Overview

  
    

Provides controller helper methods for developing a WebsocketRails controller. Action methods defined on a WebsocketRails controller can be mapped to events using the EventMap class.

## Example WebsocketRails controller

```
class ChatController < WebsocketRails::BaseController
  # Can be mapped to the :client_connected event in the events.rb file.
  def new_user
    send_message :new_message, {:message => 'Welcome to the Chat Room!'}
  end
end

```

It is best to use the provided DataStore to temporarily persist data for each client between events. Read more about it in the DataStore documentation.

  

  

  
## Direct Known Subclasses

  

InternalController

## Defined Under Namespace

  
    
      **Modules:** Metal
    
  
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**controller_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**inherited**(controller)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Tell Rails that BaseController and children can be reloaded when in the Development environment.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**accept_channel**(data = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**action_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**broadcast_message**(event_name, message, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Broadcasts a message to all connected clients.

  

      
        
- 
  
    
      #**client_id**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The numerical ID for the client connection that initiated the event.

  

      
        
- 
  
    
      #**connection**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Provides direct access to the connection object for the client that initiated the event that is currently being executed.

  

      
        
- 
  
    
      #**connection_store**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**controller_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**controller_store**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Provides access to the DataStore for the current controller.

  

      
        
- 
  
    
      #**deny_channel**(data = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**event**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The Event object that triggered this action.

  

      
        
- 
  
    
      #**message**  ⇒ Object 
    

    
      (also: #data)
    
  
  
  
  
  
  
  
  

  
    

The current message that was passed from the client when the event was initiated.

  

      
        
- 
  
    
      #**request**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_message**(event_name, message, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sends a message to the client that initiated the current event being executed.

  

      
        
- 
  
    
      #**trigger_failure**(data = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Trigger the failure callback function attached to the client event that triggered this action.

  

      
        
- 
  
    
      #**trigger_success**(data = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Trigger the success callback function attached to the client event that triggered this action.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
### Methods included from Metal

  

#process_action, #response_body

  
## Dynamic Method Handling

  

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
### 
  
    #**method_missing**(method, *args, &block)  ⇒ Object  (private)
  

  

  

  
    
      

```

163
164
165
166
167
168
169
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 163

def method_missing(method,*args,&block)
  if delegate.respond_to? method
    delegate.send method, *args, &block
  else
    super
  end
end
```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**controller_name**  ⇒ Object 
  

  

  

  
    
      

```

149
150
151
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 149

def self.controller_name
  self.name.underscore.gsub(/_controller$/,'')
end
```

    
  

    
      
  
### 
  
    .**inherited**(controller)  ⇒ Object 
  

  

  

  
    

Tell Rails that BaseController and children can be reloaded when in the Development environment.

  

  

  
    
      

```

42
43
44
45
46
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 42

def self.inherited(controller)
  unless controller.name == "WebsocketRails::InternalController" || Rails.version =~/^4/
    unloadable controller
  end
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**accept_channel**(data = nil)  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
97
98
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 94

def accept_channel(data=nil)
  channel_name = event.data[:channel]
  WebsocketRails[channel_name].subscribe connection
  trigger_success data
end
```

    
  

    
      
  
### 
  
    #**action_name**  ⇒ Object 
  

  

  

  
    
      

```

134
135
136
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 134

def action_name
  @_action_name
end
```

    
  

    
      
  
### 
  
    #**broadcast_message**(event_name, message, options = {})  ⇒ Object 
  

  

  

  
    

Broadcasts a message to all connected clients. See #send_message for message passing details.

  

  

  
    
      

```

124
125
126
127
128
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 124

def broadcast_message(event_name, message, options={})
  options.merge! :connection => connection, :data => message
  event = Event.new( event_name, options )
  @_dispatcher.broadcast_message event if @_dispatcher.respond_to?(:broadcast_message)
end
```

    
  

    
      
  
### 
  
    #**client_id**  ⇒ Object 
  

  

  

  
    

The numerical ID for the client connection that initiated the event. The ID is unique for each currently active connection but can not be used to associate a client between multiple connection attempts.

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 57

def client_id
  connection.id
end
```

    
  

    
      
  
### 
  
    #**connection**  ⇒ Object 
  

  

  

  
    

Provides direct access to the connection object for the client that initiated the event that is currently being executed.

  

  

  
    
      

```

50
51
52
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 50

def connection
  @_event.connection
end
```

    
  

    
      
  
### 
  
    #**connection_store**  ⇒ Object 
  

  

  

  
    
      

```

145
146
147
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 145

def connection_store
  connection.data_store
end
```

    
  

    
      
  
### 
  
    #**controller_name**  ⇒ Object 
  

  

  

  
    
      

```

153
154
155
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 153

def controller_name
  self.class.controller_name
end
```

    
  

    
      
  
### 
  
    #**controller_store**  ⇒ Object 
  

  

  

  
    

Provides access to the DataStore for the current controller. The DataStore provides convenience methods for keeping track of data associated with active connections. See it’s documentation for more information.

  

  

  
    
      

```

141
142
143
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 141

def controller_store
  @_controller_store
end
```

    
  

    
      
  
### 
  
    #**deny_channel**(data = nil)  ⇒ Object 
  

  

  

  
    
      

```

100
101
102
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 100

def deny_channel(data=nil)
  trigger_failure data
end
```

    
  

    
      
  
### 
  
    #**event**  ⇒ Object 
  

  

  

  
    

The Event object that triggered this action. Find the current event name with event.name Access the data sent with the event with event.data Find the event’s namespace with event.namespace

  

  

  
    
      

```

65
66
67
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 65

def event
  @_event
end
```

    
  

    
      
  
### 
  
    #**message**  ⇒ Object 
  

  
    Also known as:
    data
    
  

  

  
    

The current message that was passed from the client when the event was initiated. The message is typically a standard ruby Hash object. See the README for more information.

  

  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 71

def message
  @_event.data
end
```

    
  

    
      
  
### 
  
    #**request**  ⇒ Object 
  

  

  

  
    
      

```

130
131
132
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 130

def request
  connection.request
end
```

    
  

    
      
  
### 
  
    #**send_message**(event_name, message, options = {})  ⇒ Object 
  

  

  

  
    

Sends a message to the client that initiated the current event being executed. Messages are serialized as JSON into a two element Array where the first element is the event and the second element is the message that was passed, typically a Hash.

To send an event under a namespace, add the ‘:namespace => :target_namespace` option.

```
send_message :new_message, message_hash, :namespace => :product

```

Nested namespaces can be passed as an array like the following:

```
send_message :new, message_hash, :namespace => [:products,:glasses]

```

See the EventMap documentation for more on mapping namespaced actions.

  

  

  
    
      

```

117
118
119
120
121
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 117

def send_message(event_name, message, options={})
  options.merge! :connection => connection, :data => message
  event = Event.new( event_name, options )
  @_dispatcher.send_message event if @_dispatcher.respond_to?(:send_message)
end
```

    
  

    
      
  
### 
  
    #**trigger_failure**(data = nil)  ⇒ Object 
  

  

  

  
    

Trigger the failure callback function attached to the client event that triggered this action. The object passed to this method will be passed as an argument to the callback function on the client.

  

  

  
    
      

```

88
89
90
91
92
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 88

def trigger_failure(data=nil)
  event.success = false
  event.data = data
  event.trigger
end
```

    
  

    
      
  
### 
  
    #**trigger_success**(data = nil)  ⇒ Object 
  

  

  

  
    

Trigger the success callback function attached to the client event that triggered this action. The object passed to this method will be passed as an argument to the callback function on the client.

  

  

  
    
      

```

79
80
81
82
83
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 79

def trigger_success(data=nil)
  event.success = true
  event.data = data
  event.trigger
end
```