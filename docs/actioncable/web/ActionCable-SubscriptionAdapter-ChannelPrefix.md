# Module: ActionCable::SubscriptionAdapter::ChannelPrefix
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    PostgreSQL, Redis
  
  

  
  
    Defined in:
    lib/action_cable/subscription_adapter/channel_prefix.rb
  
  

## Overview

  
    

:nodoc:

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**broadcast**(channel, payload)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**subscribe**(channel, callback, success_callback = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unsubscribe**(channel, callback)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**broadcast**(channel, payload)  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/channel_prefix.rb', line 8

def broadcast(channel, payload)
  channel = channel_with_prefix(channel)
  super
end
```

    
  

    
      
  
### 
  
    #**subscribe**(channel, callback, success_callback = nil)  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/channel_prefix.rb', line 13

def subscribe(channel, callback, success_callback = nil)
  channel = channel_with_prefix(channel)
  super
end
```

    
  

    
      
  
### 
  
    #**unsubscribe**(channel, callback)  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
21
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/channel_prefix.rb', line 18

def unsubscribe(channel, callback)
  channel = channel_with_prefix(channel)
  super
end
```