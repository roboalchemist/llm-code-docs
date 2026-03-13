# Class: ActionCable::Connection::MessageBuffer
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Connection::MessageBuffer
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/message_buffer.rb
  
  

## Overview

  
    

Allows us to buffer messages received from the WebSocket before the Connection has been fully initialized, and is ready to receive them.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**append**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(connection)  ⇒ MessageBuffer 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**process!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**processing?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(connection)  ⇒ MessageBuffer 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

10
11
12
13
```

    
    
      

```
# File 'lib/action_cable/connection/message_buffer.rb', line 10

def initialize(connection)
  @connection = connection
  @buffered_messages = []
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**append**(message)  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
18
19
20
21
22
23
24
25
```

    
    
      

```
# File 'lib/action_cable/connection/message_buffer.rb', line 15

def append(message)
  if valid? message
    if processing?
      receive message
    else
      buffer message
    end
  else
    connection.logger.error "Couldn't handle non-string message: #{message.class}"
  end
end
```

    
  

    
      
  
### 
  
    #**process!**  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
34
```

    
    
      

```
# File 'lib/action_cable/connection/message_buffer.rb', line 31

def process!
  @processing = true
  receive_buffered_messages
end
```

    
  

    
      
  
### 
  
    #**processing?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/action_cable/connection/message_buffer.rb', line 27

def processing?
  @processing
end
```