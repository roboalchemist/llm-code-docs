# Class: ActionCable::SubscriptionAdapter::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::SubscriptionAdapter::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/subscription_adapter/base.rb
  
  

  
## Direct Known Subclasses

  

Inline, PostgreSQL, Redis

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**logger**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute logger.

  

    
      
- 
  
    
      #**server**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute server.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**broadcast**(channel, payload)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**identifier**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(server)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**shutdown**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**subscribe**(channel, message_callback, success_callback = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unsubscribe**(channel, message_callback)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(server)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

10
11
12
13
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/base.rb', line 10

def initialize(server)
  @server = server
  @logger = @server.logger
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**logger**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute logger.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/base.rb', line 8

def logger
  @logger
end

```

    
  

    
      
      
      
  
### 
  
    #**server**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute server.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/base.rb', line 8

def server
  @server
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**broadcast**(channel, payload)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/base.rb', line 15

def broadcast(channel, payload)
  raise NotImplementedError
end

```

    
  

    
      
  
### 
  
    #**identifier**  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
34
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/base.rb', line 31

def identifier
  @server.config.cable[:id] = "ActionCable-PID-#{$$}" unless @server.config.cable.key?(:id)
  @server.config.cable[:id]
end

```

    
  

    
      
  
### 
  
    #**shutdown**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/base.rb', line 27

def shutdown
  raise NotImplementedError
end

```

    
  

    
      
  
### 
  
    #**subscribe**(channel, message_callback, success_callback = nil)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/base.rb', line 19

def subscribe(channel, message_callback, success_callback = nil)
  raise NotImplementedError
end

```

    
  

    
      
  
### 
  
    #**unsubscribe**(channel, message_callback)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/base.rb', line 23

def unsubscribe(channel, message_callback)
  raise NotImplementedError
end

```