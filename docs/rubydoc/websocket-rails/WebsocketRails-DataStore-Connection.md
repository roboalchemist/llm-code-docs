# Class: WebsocketRails::DataStore::Connection
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- ActiveSupport::HashWithIndifferentAccess
          
            
- Base
          
            
- WebsocketRails::DataStore::Connection
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/data_store.rb
  
  

## Overview

  
    

The connection data store operates much like the Controller store. The biggest difference is that the data placed inside is private for individual users and accessible from any controller. Anything placed inside the connection data store will be deleted when a user disconnects.

The connection data store is accessed through the `#connection_store` instance method inside your controller.

If we were writing a basic chat system, we could use the connection data store to hold onto a user’s current screen name.

```
class UserController < WebsocketRails::BaseController

  def set_screen_name
    connection_store[:screen_name] = message[:screen_name]
  end

end

class ChatController < WebsocketRails::BaseController

  def say_hello
    screen_name = connection_store[:screen_name]
    send_message :new_message, "#{screen_name} says hello"
  end

end

```

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**connection**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute connection.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(connection)  ⇒ Connection 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Connection.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

clear_all_instances, #collect_all, #destroy!, #instances

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(connection)  ⇒ Connection 
  

  

  

  
    

Returns a new instance of Connection.

  

  

  
    
      

```

89
90
91
92
```

    
    
      

```
# File 'lib/websocket_rails/data_store.rb', line 89

def initialize(connection)
  super()
  @connection = connection
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**connection**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute connection.

  

  

  
    
      

```

87
88
89
```

    
    
      

```
# File 'lib/websocket_rails/data_store.rb', line 87

def connection
  @connection
end
```