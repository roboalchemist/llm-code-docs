# Module: WebsocketRails::StaticEvents
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Event
  
  

  
  
    Defined in:
    lib/websocket_rails/event.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**new_on_close**(connection, data = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**new_on_error**(connection, data = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**new_on_invalid_event_received**(connection, data = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**new_on_open**(connection, data = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**new_on_ping**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**new_on_close**(connection, data = nil)  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 13

def new_on_close(connection,data=nil)
  Event.new :client_disconnected, :data => data, :connection => connection
end
```

    
  

    
      
  
### 
  
    #**new_on_error**(connection, data = nil)  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 17

def new_on_error(connection,data=nil)
  Event.new :client_error, :data => data, :connection => connection
end
```

    
  

    
      
  
### 
  
    #**new_on_invalid_event_received**(connection, data = nil)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 25

def new_on_invalid_event_received(connection,data=nil)
  Event.new :invalid_event, :data => data, :connection => connection
end
```

    
  

    
      
  
### 
  
    #**new_on_open**(connection, data = nil)  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
8
9
10
11
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 5

def new_on_open(connection,data=nil)
  connection_id = {
    :connection_id => connection.id
  }
  data = data.is_a?(Hash) ? data.merge( connection_id ) : connection_id
  Event.new :client_connected, :data => data, :connection => connection
end
```

    
  

    
      
  
### 
  
    #**new_on_ping**(connection)  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 21

def new_on_ping(connection)
  Event.new :ping, :data => {}, :connection => connection, :namespace => :websocket_rails
end
```