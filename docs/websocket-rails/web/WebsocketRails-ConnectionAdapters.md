# Module: WebsocketRails::ConnectionAdapters
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/connection_adapters.rb,

  lib/websocket_rails/connection_adapters/http.rb,
 lib/websocket_rails/connection_adapters/web_socket.rb

  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** Base, Http, WebSocket
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**adapters**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the value of attribute adapters.

  

      
        
- 
  
    
      .**establish_connection**(request, dispatcher)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**register**(adapter)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**adapters**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute adapters.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 4

def adapters
  @adapters
end
```

    
  

    
      
  
### 
  
    .**establish_connection**(request, dispatcher)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 12

def self.establish_connection(request, dispatcher)
  adapter = adapters.detect { |a| a.accepts?(request.env) } || raise(InvalidConnectionError)
  adapter.new request, dispatcher
end
```

    
  

    
      
  
### 
  
    .**register**(adapter)  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters.rb', line 7

def self.register(adapter)
  @adapters ||= []
  @adapters.unshift adapter
end
```