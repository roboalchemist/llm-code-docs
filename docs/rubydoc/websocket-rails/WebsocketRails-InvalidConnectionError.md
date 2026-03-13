# Exception: WebsocketRails::InvalidConnectionError
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- WebsocketRails::InvalidConnectionError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket-rails.rb
  
  

## Overview

  
    

Exceptions

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**rack_response**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**rack_response**  ⇒ Object 
  

  

  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 54

def rack_response
  [400,{'Content-Type' => 'text/plain'},['invalid connection']]
end
```