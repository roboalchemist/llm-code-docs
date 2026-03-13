# Class: ActionCable::SubscriptionAdapter::Inline
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- ActionCable::SubscriptionAdapter::Inline
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/subscription_adapter/inline.rb
  
  

## Overview

  
    

:nodoc:

  

  

  
## Direct Known Subclasses

  

Async

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#logger, #server

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**broadcast**(channel, payload)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ Inline 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Inline.

  

      
        
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
  
    #**initialize**  ⇒ Inline 
  

  

  

  
    

Returns a new instance of Inline.

  

  

  
    
      

```

8
9
10
11
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/inline.rb', line 8

def initialize(*)
  super
  @subscriber_map = nil
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**broadcast**(channel, payload)  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/inline.rb', line 13

def broadcast(channel, payload)
  subscriber_map.broadcast(channel, payload)
end
```

    
  

    
      
  
### 
  
    #**shutdown**  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/inline.rb', line 25

def shutdown
  # nothing to do
end
```

    
  

    
      
  
### 
  
    #**subscribe**(channel, callback, success_callback = nil)  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/inline.rb', line 17

def subscribe(channel, callback, success_callback = nil)
  subscriber_map.add_subscriber(channel, callback, success_callback)
end
```

    
  

    
      
  
### 
  
    #**unsubscribe**(channel, callback)  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/inline.rb', line 21

def unsubscribe(channel, callback)
  subscriber_map.remove_subscriber(channel, callback)
end
```