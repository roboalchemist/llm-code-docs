# Exception: ActionCable::Channel::NonInferrableChannelError
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- ActionCable::Channel::NonInferrableChannelError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/channel/test_case.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(name)  ⇒ NonInferrableChannelError 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of NonInferrableChannelError.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name)  ⇒ NonInferrableChannelError 
  

  

  

  
    

Returns a new instance of NonInferrableChannelError.

  

  

  
    
      

```

13
14
15
16
17
```

    
    
      

```
# File 'lib/action_cable/channel/test_case.rb', line 13

def initialize(name)
  super "Unable to determine the channel to test from #{name}. " +
    "You'll need to specify it using `tests YourChannel` in your " +
    "test case definition."
end
```