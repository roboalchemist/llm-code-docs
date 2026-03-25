# Class: ActionCable::SubscriptionAdapter::Test
  
  
  

  
  
    Inherits:
    
      Async
      
        

          
- Object
          
            
- Base
          
            
- Inline
          
            
- Async
          
            
- ActionCable::SubscriptionAdapter::Test
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/subscription_adapter/test.rb
  
  

## Overview

  
    

## Test adapter for Action Cable

The test adapter should be used only in testing. Along with ActionCable::TestHelper it makes a great tool to test your Rails application.

To use the test adapter set `adapter` value to `test` in your `config/cable.yml` file.

NOTE: `Test` adapter extends the `ActionCable::SubscriptionAdapter::Async` adapter, so it could be used in system tests too.

  

  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#logger, #server

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**broadcast**(channel, payload)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**broadcasts**(channel)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**clear**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**clear_messages**(channel)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from Inline

  

#initialize, #shutdown, #subscribe, #unsubscribe

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#identifier, #initialize, #shutdown, #subscribe, #unsubscribe

  
## Constructor Details

  
    

This class inherits a constructor from ActionCable::SubscriptionAdapter::Inline
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**broadcast**(channel, payload)  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
21
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/test.rb', line 18

def broadcast(channel, payload)
  broadcasts(channel) << payload
  super
end
```

    
  

    
      
  
### 
  
    #**broadcasts**(channel)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/test.rb', line 23

def broadcasts(channel)
  channels_data[channel] ||= []
end
```

    
  

    
      
  
### 
  
    #**clear**  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/test.rb', line 31

def clear
  @channels_data = nil
end
```

    
  

    
      
  
### 
  
    #**clear_messages**(channel)  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/test.rb', line 27

def clear_messages(channel)
  channels_data[channel] = []
end
```