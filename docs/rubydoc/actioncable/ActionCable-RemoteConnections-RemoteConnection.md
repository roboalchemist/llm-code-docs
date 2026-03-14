# Class: ActionCable::RemoteConnections::RemoteConnection
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::RemoteConnections::RemoteConnection
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Connection::Identification, Connection::InternalChannel
  
  
  

  

  
  
    Defined in:
    lib/action_cable/remote_connections.rb
  
  

## Overview

  
    

# Action Cable Remote Connection

Represents a single remote connection found via ‘ActionCable.server.remote_connections.where(*)`. Exists solely for the purpose of calling #disconnect on that connection.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** InvalidIdentifiersError
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**disconnect**(reconnect: true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Uses the internal channel to disconnect the connection.

  

      
        
- 
  
    
      #**initialize**(server, ids)  ⇒ RemoteConnection 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of RemoteConnection.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Connection::Identification

  

#connection_identifier

  
  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(server, ids)  ⇒ RemoteConnection 
  

  

  

  
    

Returns a new instance of RemoteConnection.

  

  

  
    
      

```

52
53
54
55
```

    
    
      

```
# File 'lib/action_cable/remote_connections.rb', line 52

def initialize(server, ids)
  @server = server
  set_identifier_instance_vars(ids)
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**disconnect**(reconnect: true)  ⇒ Object 
  

  

  

  
    

Uses the internal channel to disconnect the connection.

  

  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/action_cable/remote_connections.rb', line 58

def disconnect(reconnect: true)
  server.broadcast internal_channel, { type: "disconnect", reconnect: reconnect }
end
```