# Class: EventMachine::WebSocket::Handler06
  
  
  

  
  
    Inherits:
    
      Handler
      
        

          
- Object
          
            
- Handler
          
            
- EventMachine::WebSocket::Handler06
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Close06, Framing05, MessageProcessor06
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/handler06.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Handler

  

#request, #state

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods included from Close06

  

#close_websocket, #supports_close_codes?

  
  
  
  
  
  
  
  
  
### Methods included from MessageProcessor06

  

#message, #pingable?

  
  
  
  
  
  
  
  
  
### Methods included from Framing05

  

#initialize_framing, #process_data, #send_frame, #send_text_frame

  
  
  
  
  
  
  
  
  
### Methods inherited from Handler

  

#close_websocket, #fail_websocket, #initialize, klass_factory, #ping, #pingable?, #receive_data, #start_close_timeout, #unbind

  
  
  
  
  
  
  
## Constructor Details

  
    

This class inherits a constructor from EventMachine::WebSocket::Handler