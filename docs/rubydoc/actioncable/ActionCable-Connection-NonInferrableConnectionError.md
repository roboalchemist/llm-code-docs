# Exception: ActionCable::Connection::NonInferrableConnectionError
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- ActionCable::Connection::NonInferrableConnectionError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/test_case.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(name)  ⇒ NonInferrableConnectionError 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of NonInferrableConnectionError.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name)  ⇒ NonInferrableConnectionError 
  

  

  

  
    

Returns a new instance of NonInferrableConnectionError.

  

  

  
    
      

```

15
16
17
18
19
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 15

def initialize(name)
  super "Unable to determine the connection to test from #{name}. " +
    "You'll need to specify it using `tests YourConnection` in your " +
    "test case definition."
end
```