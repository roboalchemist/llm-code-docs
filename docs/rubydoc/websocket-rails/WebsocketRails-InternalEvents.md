# Class: WebsocketRails::InternalEvents
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::InternalEvents
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/internal_events.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**events**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**events**  ⇒ Object 
  

  

  

  
    
      

```

3
4
5
6
7
8
9
10
11
```

    
    
      

```
# File 'lib/websocket_rails/internal_events.rb', line 3

def self.events
  Proc.new do
    namespace :websocket_rails do
      subscribe :pong, :to => InternalController, :with_method => :do_pong
      subscribe :subscribe, :to => InternalController, :with_method => :subscribe_to_channel
      subscribe :unsubscribe, :to => InternalController, :with_method => :unsubscribe_to_channel
    end
  end
end
```