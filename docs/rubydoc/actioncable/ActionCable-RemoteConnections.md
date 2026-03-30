# Class: ActionCable::RemoteConnections
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::RemoteConnections
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/remote_connections.rb
  
  

## Overview

  
    

# Action Cable Remote Connections

If you need to disconnect a given connection, you can go through the RemoteConnections. You can find the connections you’re looking for by searching for the identifier declared on the connection. For example:

```
module ApplicationCable
  class Connection < ActionCable::Connection::Base
    identified_by :current_user
    ....
  end
end

ActionCable.server.remote_connections.where(current_user: User.find(1)).disconnect

```

This will disconnect all the connections established for ‘User.find(1)`, across all servers running on all machines, because it uses the internal channel that all of these servers are subscribed to.

By default, server sends a “disconnect” message with “reconnect” flag set to true. You can override it by specifying the `reconnect` option:

```
ActionCable.server.remote_connections.where(current_user: User.find(1)).disconnect(reconnect: false)

```

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** RemoteConnection
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**server**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute server.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(server)  ⇒ RemoteConnections 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of RemoteConnections.

  

      
        
- 
  
    
      #**where**(identifier)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(server)  ⇒ RemoteConnections 
  

  

  

  
    

Returns a new instance of RemoteConnections.

  

  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/action_cable/remote_connections.rb', line 34

def initialize(server)
  @server = server
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**server**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute server.

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/action_cable/remote_connections.rb', line 32

def server
  @server
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**where**(identifier)  ⇒ Object 
  

  

  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/action_cable/remote_connections.rb', line 38

def where(identifier)
  RemoteConnection.new(server, identifier)
end
```