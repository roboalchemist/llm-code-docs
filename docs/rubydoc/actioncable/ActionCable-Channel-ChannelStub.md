# Module: ActionCable::Channel::ChannelStub
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/channel/test_case.rb
  
  

## Overview

  
    

# Action Cable Channel Stub

Stub `stream_from` to track streams for the channel. Add public aliases for `subscription_confirmation_sent?` and `subscription_rejected?`.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**confirmed?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**rejected?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**start_periodic_timers**  ⇒ Object 
    

    
      (also: #stop_periodic_timers)
    
  
  
  
  
  
  
  
  

  
    

Make periodic timers no-op.

  

      
        
- 
  
    
      #**stop_all_streams**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**stream_from**(broadcasting)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**streams**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**confirmed?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 25

def confirmed?
  subscription_confirmation_sent?
end
```

    
  

    
      
  
### 
  
    #**rejected?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 29

def rejected?
  subscription_rejected?
end
```

    
  

    
      
  
### 
  
    #**start_periodic_timers**  ⇒ Object 
  

  
    Also known as:
    stop_periodic_timers
    
  

  

  
    

Make periodic timers no-op

  

  

  
    
      

```

46
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 46

def start_periodic_timers; end
```

    
  

    
      
  
### 
  
    #**stop_all_streams**  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 37

def stop_all_streams
  @_streams = []
end
```

    
  

    
      
  
### 
  
    #**stream_from**(broadcasting)  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 33

def stream_from(broadcasting, *)
  streams << broadcasting
end
```

    
  

    
      
  
### 
  
    #**streams**  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 41

def streams
  @_streams ||= []
end
```