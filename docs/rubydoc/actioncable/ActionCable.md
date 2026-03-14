# Module: ActionCable
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable.rb,

  lib/action_cable/engine.rb,
 lib/action_cable/version.rb,
 lib/action_cable/test_case.rb,
 lib/action_cable/deprecator.rb,
 lib/action_cable/gem_version.rb,
 lib/action_cable/server/base.rb,
 lib/action_cable/test_helper.rb,
 lib/action_cable/channel/base.rb,
 lib/action_cable/server/worker.rb,
 lib/action_cable/channel/naming.rb,
 lib/action_cable/channel/streams.rb,
 lib/action_cable/connection/base.rb,
 lib/action_cable/channel/callbacks.rb,
 lib/action_cable/channel/test_case.rb,
 lib/action_cable/connection/stream.rb,
 lib/action_cable/remote_connections.rb,
 lib/action_cable/server/connections.rb,
 lib/action_cable/server/broadcasting.rb,
 lib/action_cable/channel/broadcasting.rb,
 lib/action_cable/connection/callbacks.rb,
 lib/action_cable/connection/test_case.rb,
 lib/action_cable/server/configuration.rb,
 lib/action_cable/connection/web_socket.rb,
 lib/action_cable/channel/periodic_timers.rb,
 lib/action_cable/connection/authorization.rb,
 lib/action_cable/connection/client_socket.rb,
 lib/action_cable/connection/subscriptions.rb,
 lib/action_cable/connection/identification.rb,
 lib/action_cable/connection/message_buffer.rb,
 lib/action_cable/subscription_adapter/base.rb,
 lib/action_cable/subscription_adapter/test.rb,
 lib/action_cable/subscription_adapter/async.rb,
 lib/action_cable/subscription_adapter/redis.rb,
 lib/action_cable/connection/internal_channel.rb,
 lib/action_cable/helpers/action_cable_helper.rb,
 lib/action_cable/subscription_adapter/inline.rb,
 lib/action_cable/connection/stream_event_loop.rb,
 lib/action_cable/connection/tagged_logger_proxy.rb,
 lib/action_cable/subscription_adapter/postgresql.rb,
 lib/action_cable/subscription_adapter/channel_prefix.rb,
 lib/action_cable/subscription_adapter/subscriber_map.rb,
 lib/action_cable/server/worker/active_record_connection_management.rb

  
  

## Overview

  
    

:markup: markdown

  

  

## Defined Under Namespace

  
    
      **Modules:** Channel, Connection, Helpers, Server, SubscriptionAdapter, TestHelper, VERSION
    
  
    
      **Classes:** Engine, RemoteConnections, TestCase
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        INTERNAL =
          
        
        

```
{
  message_types: {
    welcome: "welcome",
    disconnect: "disconnect",
    ping: "ping",
    confirmation: "confirm_subscription",
    rejection: "reject_subscription"
  },
  disconnect_reasons: {
    unauthorized: "unauthorized",
    invalid_request: "invalid_request",
    server_restart: "server_restart",
    remote: "remote"
  },
  default_mount_path: "/cable",
  protocols: ["actioncable-v1-json", "actioncable-unsupported"].freeze
}
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**deprecator**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      .**gem_version**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the currently loaded version of Action Cable as a `Gem::Version`.

  

      
        
- 
  
    
      .**server**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Singleton instance of the server.

  

      
        
- 
  
    
      .**version**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the currently loaded version of Action Cable as a `Gem::Version`.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**deprecator**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/action_cable/deprecator.rb', line 6

def self.deprecator # :nodoc:
  @deprecator ||= ActiveSupport::Deprecation.new
end
```

    
  

    
      
  
### 
  
    .**gem_version**  ⇒ Object 
  

  

  

  
    

Returns the currently loaded version of Action Cable as a `Gem::Version`.

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/action_cable/gem_version.rb', line 7

def self.gem_version
  Gem::Version.new VERSION::STRING
end
```

    
  

    
      
  
### 
  
    .**server**  ⇒ Object 
  

  

  

  
    

Singleton instance of the server

  

  

  
    
      

```

77
78
79
```

    
    
      

```
# File 'lib/action_cable.rb', line 77

module_function def server
  @server ||= ActionCable::Server::Base.new
end
```

    
  

    
      
  
### 
  
    .**version**  ⇒ Object 
  

  

  

  
    

Returns the currently loaded version of Action Cable as a `Gem::Version`.

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/action_cable/version.rb', line 9

def self.version
  gem_version
end
```