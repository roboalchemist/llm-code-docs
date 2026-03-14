# Class: EventMachine::WebSocket::Handler05
  
  
  

  
  
    Inherits:
    
      Handler
      
        

          
- Object
          
            
- Handler
          
            
- EventMachine::WebSocket::Handler05
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Close05, Framing05, MessageProcessor03
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/handler05.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Handler

  

#request, #state

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods included from Close05

  

#close_websocket, #supports_close_codes?

  
  
  
  
  
  
  
  
  
### Methods included from MessageProcessor03

  

#message, #pingable?

  
  
  
  
  
  
  
  
  
### Methods included from Framing05

  

#initialize_framing, #process_data, #send_frame, #send_text_frame

  
  
  
  
  
  
  
  
  
### Methods inherited from Handler

  

#close_websocket, #fail_websocket, #initialize, klass_factory, #ping, #pingable?, #receive_data, #start_close_timeout, #unbind

  
  
  
  
  
  
  
## Constructor Details

  
    

This class inherits a constructor from EventMachine::WebSocket::Handler