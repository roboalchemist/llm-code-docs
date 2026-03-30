# Class: ActionCable::SubscriptionAdapter::Async::AsyncSubscriberMap
  
  
  

  
  
    Inherits:
    
      SubscriberMap
      
        

          
- Object
          
            
- SubscriberMap
          
            
- ActionCable::SubscriptionAdapter::Async::AsyncSubscriberMap
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/subscription_adapter/async.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_subscriber**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(event_loop)  ⇒ AsyncSubscriberMap 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of AsyncSubscriberMap.

  

      
        
- 
  
    
      #**invoke_callback**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from SubscriberMap

  

#add_channel, #broadcast, #remove_channel, #remove_subscriber

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(event_loop)  ⇒ AsyncSubscriberMap 
  

  

  

  
    

Returns a new instance of AsyncSubscriberMap.

  

  

  
    
      

```

14
15
16
17
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/async.rb', line 14

def initialize(event_loop)
  @event_loop = event_loop
  super()
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_subscriber**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/async.rb', line 19

def add_subscriber(*)
  @event_loop.post { super }
end
```

    
  

    
      
  
### 
  
    #**invoke_callback**  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/async.rb', line 23

def invoke_callback(*)
  @event_loop.post { super }
end
```