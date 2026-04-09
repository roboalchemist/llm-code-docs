# Module: ActionCable::Server::Connections
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Base
  
  

  
  
    Defined in:
    lib/action_cable/server/connections.rb
  
  

## Overview

  
    

# Action Cable Server Connections

Collection class for all the connections that have been established on this specific server. Remember, usually you’ll run many Action Cable servers, so you can’t use this collection as a full list of all of the connections established against your application. Instead, use RemoteConnections for that.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        BEAT_INTERVAL =
          
  
    

:nodoc:

  

  

        
        

```
3
```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_connection**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**connections**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**open_connections_statistics**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_connection**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**setup_heartbeat_timer**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

WebSocket connection implementations differ on when they’ll mark a connection as stale.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_connection**(connection)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/action_cable/server/connections.rb', line 20

def add_connection(connection)
  connections << connection
end
```

    
  

    
      
  
### 
  
    #**connections**  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/action_cable/server/connections.rb', line 16

def connections
  @connections ||= []
end
```

    
  

    
      
  
### 
  
    #**open_connections_statistics**  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/action_cable/server/connections.rb', line 39

def open_connections_statistics
  connections.map(&:statistics)
end
```

    
  

    
      
  
### 
  
    #**remove_connection**(connection)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/action_cable/server/connections.rb', line 24

def remove_connection(connection)
  connections.delete connection
end
```

    
  

    
      
  
### 
  
    #**setup_heartbeat_timer**  ⇒ Object 
  

  

  

  
    

WebSocket connection implementations differ on when they’ll mark a connection as stale. We basically never want a connection to go stale, as you then can’t rely on being able to communicate with the connection. To solve this, a 3 second heartbeat runs on all connections. If the beat fails, we automatically disconnect.

  

  

  
    
      

```

33
34
35
36
37
```

    
    
      

```
# File 'lib/action_cable/server/connections.rb', line 33

def setup_heartbeat_timer
  @heartbeat_timer ||= event_loop.timer(BEAT_INTERVAL) do
    event_loop.post { connections.each(&:beat) }
  end
end
```