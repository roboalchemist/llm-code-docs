# Exception: EventMachine::WebSocket::WSProtocolError
  
  
  

  
  
    Inherits:
    
      WebSocketError
      
        

          
- Object
          
            
- RuntimeError
          
            
- WebSocketError
          
            
- EventMachine::WebSocket::WSProtocolError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/websocket.rb
  
  

## Overview

  
    

Used for errors which should cause the connection to close. See RFC6455 §7.4.1 for a full description of meanings

  

  

  
## Direct Known Subclasses

  

InvalidDataError, WSMessageTooBigError

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**code**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**code**  ⇒ Object 
  

  

  

  
    
      

```

20
```

    
    
      

```
# File 'lib/em-websocket/websocket.rb', line 20

def code; 1002; end
```