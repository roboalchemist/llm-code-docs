# Module: WebsocketRails::BaseController::Metal
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    WebsocketRails::BaseController
  
  

  
  
    Defined in:
    lib/websocket_rails/base_controller.rb
  
  

## Overview

  
    

We need process_action to be in a module loaded before AbstractController::Callbacks to get inheritance properly

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**process_action**(method, event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**response_body**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**process_action**(method, event)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
28
29
30
31
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 25

def process_action(method, event)
  if respond_to?(method)
    self.send(method)
  else
    raise EventRoutingError.new(event, self, method)
  end
end
```

    
  

    
      
  
### 
  
    #**response_body**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/websocket_rails/base_controller.rb', line 32

def response_body
  false
end
```