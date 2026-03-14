# Class: EventMachine::WebSocket::Handler75
  
  
  

  
  
    Inherits:
    
      Handler
      
        

          
- Object
          
            
- Handler
          
            
- EventMachine::WebSocket::Handler75
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Close75, Framing76, Handshake75
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/handler75.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Handler

  

#request, #state

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods included from Close75

  

#close_websocket, #supports_close_codes?

  
  
  
  
  
  
  
  
  
### Methods included from Framing76

  

#initialize_framing, #process_data, #send_text_frame

  
  
  
  
  
  
  
  
  
### Methods included from Handshake75

  

handshake, validate_protocol!

  
  
  
  
  
  
  
  
  
### Methods inherited from Handler

  

#close_websocket, #fail_websocket, #initialize, klass_factory, #ping, #pingable?, #receive_data, #start_close_timeout, #unbind

  
  
  
  
  
  
  
## Constructor Details

  
    

This class inherits a constructor from EventMachine::WebSocket::Handler