# Module: ActionCable::Connection::Authorization
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Base
  
  

  
  
    Defined in:
    lib/action_cable/connection/authorization.rb
  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** UnauthorizedError
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**reject_unauthorized_connection**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Closes the WebSocket connection if it is open and returns an “unauthorized” reason.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**reject_unauthorized_connection**  ⇒ Object 
  

  

  

  
    

Closes the WebSocket connection if it is open and returns an “unauthorized” reason.

  

  

Raises:

  
    
- 
      
      
        (UnauthorizedError)
      
      
      
    
  

  
    
      

```

12
13
14
15
```

    
    
      

```
# File 'lib/action_cable/connection/authorization.rb', line 12

def reject_unauthorized_connection
  logger.error "An unauthorized connection attempt was rejected"
  raise UnauthorizedError
end
```