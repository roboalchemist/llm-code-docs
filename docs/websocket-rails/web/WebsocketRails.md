# Module: WebsocketRails
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket-rails.rb,

  lib/websocket_rails/event.rb,
 lib/websocket_rails/engine.rb,
 lib/websocket_rails/channel.rb,
 lib/websocket_rails/logging.rb,
 lib/websocket_rails/version.rb,
 lib/websocket_rails/event_map.rb,
 lib/websocket_rails/data_store.rb,
 lib/websocket_rails/dispatcher.rb,
 lib/websocket_rails/event_queue.rb,
 lib/websocket_rails/user_manager.rb,
 lib/websocket_rails/configuration.rb,
 lib/spec_helpers/spec_helper_event.rb,
 lib/websocket_rails/base_controller.rb,
 lib/websocket_rails/channel_manager.rb,
 lib/websocket_rails/internal_events.rb,
 lib/websocket_rails/synchronization.rb,
 lib/websocket_rails/connection_manager.rb,
 lib/websocket_rails/controller_factory.rb,
 lib/websocket_rails/connection_adapters.rb,
 lib/spec_helpers/matchers/route_matchers.rb,
 lib/spec_helpers/matchers/trigger_matchers.rb,
 lib/websocket_rails/connection_adapters/http.rb,
 lib/websocket_rails/connection_adapters/web_socket.rb,
 lib/generators/websocket_rails/install/install_generator.rb,
 lib/rails/app/controllers/websocket_rails/delegation_controller.rb

  
  

## Defined Under Namespace

  
    
      **Modules:** ConnectionAdapters, DataStore, Generators, Logging, SpecHelpers, StaticEvents
    
  
    
      **Classes:** BaseController, Channel, ChannelManager, ConfigDeprecationError, Configuration, ConnectionManager, ControllerFactory, DelegationController, Dispatcher, Engine, Event, EventMap, EventQueue, EventRoutingError, Events, InternalController, InternalEvents, InvalidConnectionError, SpecHelperEvent, Synchronization, TargetValidator, UserManager
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        VERSION =
          
        
        

```
"0.7.0"
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**[]**(channel)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**channel_manager**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**channel_tokens**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**config**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**logger**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**setup** {|config| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**standalone?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**synchronize?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**users**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Contains a Hash of all connected users.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**[]**(channel)  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/websocket_rails/channel_manager.rb', line 11

def [](channel)
  channel_manager[channel]
end
```

    
  

    
      
  
### 
  
    .**channel_manager**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/websocket_rails/channel_manager.rb', line 7

def channel_manager
  @channel_manager ||= ChannelManager.new
end
```

    
  

    
      
  
### 
  
    .**channel_tokens**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/websocket_rails/channel_manager.rb', line 15

def channel_tokens
  channel_manager.channel_tokens
end
```

    
  

    
      
  
### 
  
    .**config**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 12

def config
  @config ||= Configuration.new
end
```

    
  

    
      
  
### 
  
    .**logger**  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 24

def logger
  config.logger
end
```

    
  

    
      
  
### 
  
    .**setup** {|config| ... } ⇒ Object 
  

  

  

  
    

  

  

Yields:

  
    
- 
      
      
        (config)
      
      
      
    
  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 8

def setup
  yield config
end
```

    
  

    
      
  
### 
  
    .**standalone?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 20

def standalone?
  config.standalone == true
end
```

    
  

    
      
  
### 
  
    .**synchronize?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 16

def synchronize?
  config.synchronize == true || config.standalone == true
end
```

    
  

    
      
  
### 
  
    .**users**  ⇒ Object 
  

  

  

  
    

Contains a Hash of all connected users. This can be used to trigger an event on a specific user from outside of a WebsocketRails controller.

The key for a particular user is defined in the configuration as `config.user_identifier`.

If there is a `current_user` method defined in ApplicationController and a user is signed in to your application when the connection is opened, WebsocketRails will call the method defined in `config.user_identifier` on the `current_user` object and use that value as the key.

```
# In your events.rb file
WebsocketRails.setup do |config|
  # Defaults to :id
  config.user_identifier = :name
end

# In a standard controller or background job
name = current_user.name
WebsocketRails.users[name].send_message :event_name, data

```

If no `current_user` method is defined or the user is not signed in when the WebsocketRails connection is opened, the connection will not be stored in the UserManager.

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 32

def self.users
  @user_manager ||= UserManager.new
end
```