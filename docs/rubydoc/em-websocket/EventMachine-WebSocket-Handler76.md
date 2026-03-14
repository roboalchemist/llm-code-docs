# Class: EventMachine::WebSocket::Handler76
  
  
  

  
  
    Inherits:
    
      Handler
      
        

          
- Object
          
            
- Handler
          
            
- EventMachine::WebSocket::Handler76
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Close75, Framing76, Handshake76
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/handler76.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        TERMINATE_STRING =
          
  
    

“377000” is octet version and “xffx00” is hex version

  

  

        
        

```
"\xff\x00"
```

      
    
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Handler

  

#request, #state

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods included from Close75

  

#close_websocket, #supports_close_codes?

  
  
  
  
  
  
  
  
  
### Methods included from Framing76

  

#initialize_framing, #process_data, #send_text_frame

  
  
  
  
  
  
  
  
  
### Methods included from Handshake76

  

handshake

  
  
  
  
  
  
  
  
  
### Methods inherited from Handler

  

#close_websocket, #fail_websocket, #initialize, klass_factory, #ping, #pingable?, #receive_data, #start_close_timeout, #unbind

  
  
  
  
  
  
  
## Constructor Details

  
    

This class inherits a constructor from EventMachine::WebSocket::Handler