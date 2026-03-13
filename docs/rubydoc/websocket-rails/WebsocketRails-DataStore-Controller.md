# Class: WebsocketRails::DataStore::Controller
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- ActiveSupport::HashWithIndifferentAccess
          
            
- Base
          
            
- WebsocketRails::DataStore::Controller
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/data_store.rb
  
  

## Overview

  
    

The Controller DataStore acts as a stand-in for instance variables in your controller. At it’s core, it is a Hash which is accessible inside your controller through the `#controller_store` instance method. Any values set in the controller store will be visible by all connected users which trigger events that use that controller. However, values set in one controller will not be visible by other controllers.

```
class AccountController < WebsocketRails::BaseController
  # We will use a before filter to set the initial value
  before_action { controller_store[:event_count] ||= 0 }

  # Mapped as `accounts.important_event` in the Event Router
  def important_event
    # This will be private for each controller
    controller_store[:event_count] += 1
    trigger_success controller_store[:event_count]
  end
end

class ProductController < WebsocketRails::BaseController
  # We will use a before filter to set the initial value
  before_action { controller_store[:event_count] ||= 0 }

  # Mapped as `products.boring_event` in the Event Router
  def boring_event
    # This will be private for each controller
    controller_store[:event_count] += 1
    trigger_success controller_store[:event_count]
  end
end

# trigger `accounts.important_event`
=> 1
# trigger `accounts.important_event`
=> 2
# trigger `products.boring_event`
=> 1

```

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**controller**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute controller.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(controller)  ⇒ Controller 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Controller.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

clear_all_instances, #collect_all, #destroy!, #instances

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(controller)  ⇒ Controller 
  

  

  

  
    

Returns a new instance of Controller.

  

  

  
    
      

```

138
139
140
141
```

    
    
      

```
# File 'lib/websocket_rails/data_store.rb', line 138

def initialize(controller)
  super()
  @controller = controller
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**controller**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute controller.

  

  

  
    
      

```

136
137
138
```

    
    
      

```
# File 'lib/websocket_rails/data_store.rb', line 136

def controller
  @controller
end
```