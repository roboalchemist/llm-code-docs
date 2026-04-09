# Class: WebsocketRails::EventMap::DSL
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::EventMap::DSL
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/event_map.rb
  
  

## Overview

  
    

Provides the DSL methods available to the Event routes file

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**evaluate**(route_block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(dispatcher, namespace = nil)  ⇒ DSL 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of DSL.

  

      
        
- 
  
    
      #**namespace**(new_namespace, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**private_channel**(channel)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**subscribe**(event_name, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(dispatcher, namespace = nil)  ⇒ DSL 
  

  

  

  
    

Returns a new instance of DSL.

  

  

  
    
      

```

46
47
48
49
50
51
52
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 46

def initialize(dispatcher,namespace=nil)
  if namespace
    @namespace = namespace
  else
    @namespace = Namespace.new :global, dispatcher
  end
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**evaluate**(route_block)  ⇒ Object 
  

  

  

  
    
      

```

54
55
56
57
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 54

def evaluate(route_block)
  instance_eval &route_block unless route_block.nil?
  @namespace
end
```

    
  

    
      
  
### 
  
    #**namespace**(new_namespace, &block)  ⇒ Object 
  

  

  

  
    
      

```

63
64
65
66
67
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 63

def namespace(new_namespace,&block)
  @namespace = @namespace.find_or_create new_namespace
  instance_eval &block if block.present?
  @namespace = @namespace.parent
end
```

    
  

    
      
  
### 
  
    #**private_channel**(channel)  ⇒ Object 
  

  

  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 69

def private_channel(channel)
  WebsocketRails[channel].make_private
end
```

    
  

    
      
  
### 
  
    #**subscribe**(event_name, options)  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 59

def subscribe(event_name,options)
  @namespace.store event_name, options
end
```