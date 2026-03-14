# Class: ActionCable::SubscriptionAdapter::Redis
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- ActionCable::SubscriptionAdapter::Redis
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ChannelPrefix
  
  
  

  

  
  
    Defined in:
    lib/action_cable/subscription_adapter/redis.rb
  
  

## Overview

  
    

:nodoc:

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Listener
    
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#logger, #server

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**broadcast**(channel, payload)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ Redis 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Redis.

  

      
        
- 
  
    
      #**redis_connection_for_subscriptions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shutdown**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**subscribe**(channel, callback, success_callback = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unsubscribe**(channel, callback)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#identifier

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ Redis 
  

  

  

  
    

Returns a new instance of Redis.

  

  

  
    
      

```

22
23
24
25
26
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 22

def initialize(*)
  super
  @listener = nil
  @redis_connection_for_broadcasts = nil
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**broadcast**(channel, payload)  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 28

def broadcast(channel, payload)
  redis_connection_for_broadcasts.publish(channel, payload)
end
```

    
  

    
      
  
### 
  
    #**redis_connection_for_subscriptions**  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 44

def redis_connection_for_subscriptions
  redis_connection
end
```

    
  

    
      
  
### 
  
    #**shutdown**  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 40

def shutdown
  @listener.shutdown if @listener
end
```

    
  

    
      
  
### 
  
    #**subscribe**(channel, callback, success_callback = nil)  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 32

def subscribe(channel, callback, success_callback = nil)
  listener.add_subscriber(channel, callback, success_callback)
end
```

    
  

    
      
  
### 
  
    #**unsubscribe**(channel, callback)  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 36

def unsubscribe(channel, callback)
  listener.remove_subscriber(channel, callback)
end
```