# Class: WebsocketRails::InternalController
  
  
  

  
  
    Inherits:
    
      BaseController
      
        

          
- Object
          
            
- BaseController
          
            
- WebsocketRails::InternalController
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Logging
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/internal_events.rb
  
  

  
## Constant Summary

  
  
### Constants included
     from Logging

  

Logging::ANSI, Logging::LOGGABLE_DATA

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**do_pong**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**subscribe_to_channel**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unsubscribe_to_channel**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

#color_for_level, #colorize, configure, #log, #log_data?, #log_event, #log_event?, #log_event_end, #log_event_start, #log_exception, #log_header, log_level, #wrap

  
  
  
  
  
  
  
  
  
### Methods inherited from BaseController

  

#accept_channel, #action_name, #broadcast_message, #client_id, #connection, #connection_store, controller_name, #controller_name, #controller_store, #deny_channel, #event, inherited, #message, #request, #send_message, #trigger_failure, #trigger_success

  
  
  
  
  
  
  
  
  
  
### Methods included from BaseController::Metal

  

#process_action, #response_body

  
## Dynamic Method Handling

  

    This class handles dynamic methods through the method_missing method
    
      in the class WebsocketRails::BaseController
    
  
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**do_pong**  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/websocket_rails/internal_events.rb', line 33

def do_pong
  connection.pong = true
end
```

    
  

    
      
  
### 
  
    #**subscribe_to_channel**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
20
21
22
23
24
25
```

    
    
      

```
# File 'lib/websocket_rails/internal_events.rb', line 17

def subscribe_to_channel
  channel_name = event.data[:channel]
  unless WebsocketRails[channel_name].is_private?
    WebsocketRails[channel_name].subscribe connection
    trigger_success
  else
    trigger_failure( { :reason => "channel is private", :hint => "use subscribe_private instead." } )
  end
end
```

    
  

    
      
  
### 
  
    #**unsubscribe_to_channel**  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
30
31
```

    
    
      

```
# File 'lib/websocket_rails/internal_events.rb', line 27

def unsubscribe_to_channel
  channel_name = event.data[:channel]
  WebsocketRails[channel_name].unsubscribe connection
  trigger_success
end
```