# Class: EventMachine::WebSocket::Handler08
  
  
  

  
  
    Inherits:
    
      Handler
      
        

          
- Object
          
            
- Handler
          
            
- EventMachine::WebSocket::Handler08
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Close06, Framing07, MessageProcessor06
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/handler08.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Handler

  

#request, #state

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods included from Close06

  

#close_websocket, #supports_close_codes?

  
  
  
  
  
  
  
  
  
### Methods included from MessageProcessor06

  

#message, #pingable?

  
  
  
  
  
  
  
  
  
### Methods included from Framing07

  

#initialize_framing, #process_data, #send_frame, #send_text_frame

  
  
  
  
  
  
  
  
  
### Methods inherited from Handler

  

#close_websocket, #fail_websocket, #initialize, klass_factory, #ping, #pingable?, #receive_data, #start_close_timeout, #unbind

  
  
  
  
  
  
  
## Constructor Details

  
    

This class inherits a constructor from EventMachine::WebSocket::Handler