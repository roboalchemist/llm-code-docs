# Class: ActionCable::Server::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Server::Base
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Broadcasting, Connections
  
  
  

  

  
  
    Defined in:
    lib/action_cable/server/base.rb
  
  

## Overview

  
    

# Action Cable Server Base

A singleton ActionCable::Server instance is available via ActionCable.server. It’s used by the Rack process that starts the Action Cable server, but is also used by the user to reach the RemoteConnections object, which is used for finding and disconnecting connections across all servers.

Also, this is the server instance used for broadcasting. See Broadcasting for more information.

  

  

  
## Constant Summary

  
  
### Constants included
     from Connections

  

Connections::BEAT_INTERVAL

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**config**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute config.

  

    
      
- 
  
    
      #**mutex**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute mutex.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**logger**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**call**(env)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Called by Rack to set up the server.

  

      
        
- 
  
    
      #**connection_identifiers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

All of the identifiers applied to the connection class associated with this server.

  

      
        
- 
  
    
      #**disconnect**(identifiers)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Disconnect all the connections identified by `identifiers` on this server or any others via RemoteConnections.

  

      
        
- 
  
    
      #**event_loop**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(config: self.class.config)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**pubsub**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Adapter used for all streams/broadcasting.

  

      
        
- 
  
    
      #**remote_connections**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Gateway to RemoteConnections.

  

      
        
- 
  
    
      #**restart**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**worker_pool**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The worker pool is where we run connection callbacks and channel actions.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Connections

  

#add_connection, #connections, #open_connections_statistics, #remove_connection, #setup_heartbeat_timer

  
  
  
  
  
  
  
  
  
### Methods included from Broadcasting

  

#broadcast, #broadcaster_for

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(config: self.class.config)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

31
32
33
34
35
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 31

def initialize(config: self.class.config)
  @config = config
  @mutex = Monitor.new
  @remote_connections = @event_loop = @worker_pool = @pubsub = nil
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**config**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute config.

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 24

def config
  @config
end
```

    
  

    
      
      
      
  
### 
  
    #**mutex**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute mutex.

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 29

def mutex
  @mutex
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**logger**  ⇒ Object 
  

  

  

  
    
      

```

26
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 26

def self.logger; config.logger; end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**call**(env)  ⇒ Object 
  

  

  

  
    

Called by Rack to set up the server.

  

  

  
    
      

```

38
39
40
41
42
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 38

def call(env)
  return config.health_check_application.call(env) if env["PATH_INFO"] == config.health_check_path
  setup_heartbeat_timer
  config.connection_class.call.new(self, env).process
end
```

    
  

    
      
  
### 
  
    #**connection_identifiers**  ⇒ Object 
  

  

  

  
    

All of the identifiers applied to the connection class associated with this server.

  

  

  
    
      

```

102
103
104
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 102

def connection_identifiers
  config.connection_class.call.identifiers
end
```

    
  

    
      
  
### 
  
    #**disconnect**(identifiers)  ⇒ Object 
  

  

  

  
    

Disconnect all the connections identified by `identifiers` on this server or any others via RemoteConnections.

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 46

def disconnect(identifiers)
  remote_connections.where(identifiers).disconnect
end
```

    
  

    
      
  
### 
  
    #**event_loop**  ⇒ Object 
  

  

  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 71

def event_loop
  @event_loop || @mutex.synchronize { @event_loop ||= ActionCable::Connection::StreamEventLoop.new }
end
```

    
  

    
      
  
### 
  
    #**pubsub**  ⇒ Object 
  

  

  

  
    

Adapter used for all streams/broadcasting.

  

  

  
    
      

```

96
97
98
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 96

def pubsub
  @pubsub || @mutex.synchronize { @pubsub ||= config.pubsub_adapter.new(self) }
end
```

    
  

    
      
  
### 
  
    #**remote_connections**  ⇒ Object 
  

  

  

  
    

Gateway to RemoteConnections. See that class for details.

  

  

  
    
      

```

67
68
69
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 67

def remote_connections
  @remote_connections || @mutex.synchronize { @remote_connections ||= RemoteConnections.new(self) }
end
```

    
  

    
      
  
### 
  
    #**restart**  ⇒ Object 
  

  

  

  
    
      

```

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
62
63
64
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 50

def restart
  connections.each do |connection|
    connection.close(reason: ActionCable::INTERNAL[:disconnect_reasons][:server_restart])
  end

  @mutex.synchronize do
    # Shutdown the worker pool
    @worker_pool.halt if @worker_pool
    @worker_pool = nil

    # Shutdown the pub/sub adapter
    @pubsub.shutdown if @pubsub
    @pubsub = nil
  end
end
```

    
  

    
      
  
### 
  
    #**worker_pool**  ⇒ Object 
  

  

  

  
    

The worker pool is where we run connection callbacks and channel actions. We do as little as possible on the server’s main thread. The worker pool is an executor service that’s backed by a pool of threads working from a task queue. The thread pool size maxes out at 4 worker threads by default. Tune the size yourself with `config.action_cable.worker_pool_size`.

Using Active Record, Redis, etc within your channel actions means you’ll get a separate connection from each thread in the worker pool. Plan your deployment accordingly: 5 servers each running 5 Puma workers each running an 8-thread worker pool means at least 200 database connections.

Also, ensure that your database connection pool size is as least as large as your worker pool size. Otherwise, workers may oversubscribe the database connection pool and block while they wait for other workers to release their connections. Use a smaller worker pool or a larger database connection pool instead.

  

  

  
    
      

```

91
92
93
```

    
    
      

```
# File 'lib/action_cable/server/base.rb', line 91

def worker_pool
  @worker_pool || @mutex.synchronize { @worker_pool ||= ActionCable::Server::Worker.new(max_size: config.worker_pool_size) }
end
```