# Class: WebsocketRails::UserManager
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::UserManager
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/user_manager.rb
  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** LocalConnection, MissingConnection, RemoteConnection
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**users**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute users.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**[]**(identifier)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**[]=**(identifier, connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**delete**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**each**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Behaves similarly to Ruby’s Array#each, yielding each connection object stored in the UserManager.

  

      
        
- 
  
    
      #**initialize**  ⇒ UserManager 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of UserManager.

  

      
        
- 
  
    
      #**map**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Behaves similarly to Ruby’s Array#map, invoking the given block with each active connection object and returning a new array with the results.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ UserManager 
  

  

  

  
    

Returns a new instance of UserManager.

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 40

def initialize
  @users = {}
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**users**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute users.

  

  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 38

def users
  @users
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**[]**(identifier)  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
47
48
49
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 44

def [](identifier)
  unless user = (@users[identifier.to_s] || find_remote_user(identifier.to_s))
    user = MissingConnection.new(identifier.to_s)
  end
  user
end
```

    
  

    
      
  
### 
  
    #**[]=**(identifier, connection)  ⇒ Object 
  

  

  

  
    
      

```

51
52
53
54
55
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 51

def []=(identifier, connection)
  @users[identifier.to_s] ||= LocalConnection.new
  @users[identifier.to_s] << connection
  Synchronization.register_user(connection) if WebsocketRails.synchronize?
end
```

    
  

    
      
  
### 
  
    #**delete**(connection)  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
60
61
62
63
64
65
66
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 57

def delete(connection)
  identifier = connection.user_identifier.to_s

  if (@users.has_key?(identifier) && @users[identifier].connections.count > 1)
    @users[identifier].delete(connection)
  else
    @users.delete(identifier)
    Synchronization.destroy_user(identifier) if WebsocketRails.synchronize?
  end
end
```

    
  

    
      
  
### 
  
    #**each**(&block)  ⇒ Object 
  

  

  

  
    

Behaves similarly to Ruby’s Array#each, yielding each connection object stored in the WebsocketRails::UserManager. If synchronization is enabled, each connection from every active worker will be yielded.

You can access the `current_user` object through the #user method.

You can trigger an event on this user using the #send_message method which behaves identically to BaseController#send_message.

If Synchronization is enabled, the state of the `current_user` object will be equivalent to it’s state at the time the connection was opened. It will not reflect changes made after the connection has been opened.

  

  

  
    
      

```

80
81
82
83
84
85
86
87
88
89
90
91
92
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 80

def each(&block)
  if WebsocketRails.synchronize?
    users_hash = Synchronization.all_users || return
    users_hash.each do |identifier, user_json|
      connection = remote_connection_from_json(identifier, user_json)
      block.call(connection) if block
    end
  else
    users.each do |_, connection|
      block.call(connection) if block
    end
  end
end
```

    
  

    
      
  
### 
  
    #**map**(&block)  ⇒ Object 
  

  

  

  
    

Behaves similarly to Ruby’s Array#map, invoking the given block with each active connection object and returning a new array with the results.

See UserManager#each for details on the current usage and limitations.

  

  

  
    
      

```

98
99
100
101
102
103
104
105
106
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 98

def map(&block)
  collection = []

  each do |connection|
    collection << block.call(connection) if block
  end

  collection
end
```