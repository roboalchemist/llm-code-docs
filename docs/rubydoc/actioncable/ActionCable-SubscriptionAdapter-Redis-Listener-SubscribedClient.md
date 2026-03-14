# Class: ActionCable::SubscriptionAdapter::Redis::Listener::SubscribedClient
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::SubscriptionAdapter::Redis::Listener::SubscribedClient
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/subscription_adapter/redis.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(raw_client)  ⇒ SubscribedClient 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of SubscribedClient.

  

      
        
- 
  
    
      #**subscribe**(*channel)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unsubscribe**(*channel)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(raw_client)  ⇒ SubscribedClient 
  

  

  

  
    

Returns a new instance of SubscribedClient.

  

  

  
    
      

```

216
217
218
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 216

def initialize(raw_client)
  @raw_client = raw_client
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**subscribe**(*channel)  ⇒ Object 
  

  

  

  
    
      

```

220
221
222
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 220

def subscribe(*channel)
  send_command("subscribe", *channel)
end
```

    
  

    
      
  
### 
  
    #**unsubscribe**(*channel)  ⇒ Object 
  

  

  

  
    
      

```

224
225
226
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 224

def unsubscribe(*channel)
  send_command("unsubscribe", *channel)
end
```