# Class: EventMachine::WebSocket::Handler03
  
  
  

  
  
    Inherits:
    
      Handler
      
        

          
- Object
          
            
- Handler
          
            
- EventMachine::WebSocket::Handler03
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Close03, Framing03, MessageProcessor03
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/handler03.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Handler

  

#request, #state

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods included from Close03

  

#close_websocket, #supports_close_codes?

  
  
  
  
  
  
  
  
  
### Methods included from MessageProcessor03

  

#message, #pingable?

  
  
  
  
  
  
  
  
  
### Methods included from Framing03

  

#initialize_framing, #process_data, #send_frame, #send_text_frame

  
  
  
  
  
  
  
  
  
### Methods inherited from Handler

  

#close_websocket, #fail_websocket, #initialize, klass_factory, #ping, #pingable?, #receive_data, #start_close_timeout, #unbind

  
  
  
  
  
  
  
## Constructor Details

  
    

This class inherits a constructor from EventMachine::WebSocket::Handler