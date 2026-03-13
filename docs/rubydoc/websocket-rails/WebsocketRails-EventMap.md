# Class: WebsocketRails::EventMap
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::EventMap
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/event_map.rb
  
  

## Overview

  
    

Provides a DSL for mapping client events to controller actions.

## Example events.rb file

```
# located in config/initializers/events.rb
WebsocketRails::EventMap.describe do
  subscribe :client_connected, to: ChatController, with_method: :client_connected
end

```

A single event can be mapped to any number of controller actions.

```
subscribe :new_message, :to => ChatController, :with_method => :rebroadcast_message
subscribe :new_message, :to => LogController, :with_method => :log_message

```

Events can be nested underneath namesapces.

```
namespace :product do
  subscribe :new, :to => ProductController, :with_method => :new
end

```

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** DSL, Namespace
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**namespace**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute namespace.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**describe**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(dispatcher)  ⇒ EventMap 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of EventMap.

  

      
        
- 
  
    
      #**reload_controllers!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Proxy the reload_controllers! method to the global namespace.

  

      
        
- 
  
    
      #**routes_for**(event, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(dispatcher)  ⇒ EventMap 
  

  

  

  
    

Returns a new instance of EventMap.

  

  

  
    
      

```

28
29
30
31
32
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 28

def initialize(dispatcher)
  @dispatcher = dispatcher
  @namespace  = DSL.new(dispatcher).evaluate WebsocketRails.config.route_block
  @namespace  = DSL.new(dispatcher,@namespace).evaluate InternalEvents.events
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**namespace**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute namespace.

  

  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 26

def namespace
  @namespace
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**describe**(&block)  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 22

def self.describe(&block)
  WebsocketRails.config.route_block = block
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**reload_controllers!**  ⇒ Object 
  

  

  

  
    

Proxy the reload_controllers! method to the global namespace.

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 39

def reload_controllers!
  @namespace.reload_controllers!
end
```

    
  

    
      
  
### 
  
    #**routes_for**(event, &block)  ⇒ Object 
  

  

  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 34

def routes_for(event, &block)
  @namespace.routes_for event, &block
end
```