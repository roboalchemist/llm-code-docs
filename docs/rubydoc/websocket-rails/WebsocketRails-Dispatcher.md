# Class: WebsocketRails::Dispatcher
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::Dispatcher
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Logging
  
  
  

  

  
  
    Defined in:
    lib/websocket-rails.rb,

  lib/websocket_rails/dispatcher.rb

  
  

## Overview

  
    

Deprecation Notices

  

  

  
## Constant Summary

  
  
### Constants included
     from Logging

  

Logging::ANSI, Logging::LOGGABLE_DATA

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**connection_manager**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute connection_manager.

  

    
      
- 
  
    
      #**controller_factory**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute controller_factory.

  

    
      
- 
  
    
      #**event_map**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute event_map.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**describe_events**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**broadcast_message**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**dispatch**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(connection_manager)  ⇒ Dispatcher 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Dispatcher.

  

      
        
- 
  
    
      #**receive**(event_name, data, connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**receive_encoded**(encoded_data, connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reload_event_map!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_message**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

#color_for_level, #colorize, configure, #log, #log_data?, #log_event, #log_event?, #log_event_end, #log_event_start, #log_exception, #log_header, log_level, #wrap

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(connection_manager)  ⇒ Dispatcher 
  

  

  

  
    

Returns a new instance of Dispatcher.

  

  

  
    
      

```

8
9
10
11
12
```

    
    
      

```
# File 'lib/websocket_rails/dispatcher.rb', line 8

def initialize(connection_manager)
  @connection_manager = connection_manager
  @controller_factory = ControllerFactory.new(self)
  @event_map = EventMap.new(self)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**connection_manager**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute connection_manager.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/websocket_rails/dispatcher.rb', line 6

def connection_manager
  @connection_manager
end
```

    
  

    
      
      
      
  
### 
  
    #**controller_factory**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute controller_factory.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/websocket_rails/dispatcher.rb', line 6

def controller_factory
  @controller_factory
end
```

    
  

    
      
      
      
  
### 
  
    #**event_map**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute event_map.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/websocket_rails/dispatcher.rb', line 6

def event_map
  @event_map
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**describe_events**(&block)  ⇒ Object 
  

  

  

  
    
      

```

100
101
102
```

    
    
      

```
# File 'lib/websocket-rails.rb', line 100

def self.describe_events(&block)
  raise "This method has been deprecated. Please use WebsocketRails::EventMap.describe instead."
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**broadcast_message**(event)  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
42
43
```

    
    
      

```
# File 'lib/websocket_rails/dispatcher.rb', line 39

def broadcast_message(event)
  connection_manager.connections.map do |_, connection|
    connection.trigger event
  end
end
```

    
  

    
      
  
### 
  
    #**dispatch**(event)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
27
28
29
30
31
32
33
```

    
    
      

```
# File 'lib/websocket_rails/dispatcher.rb', line 24

def dispatch(event)
  return if event.is_invalid?

  if event.is_channel?
    WebsocketRails[event.channel].trigger_event event
  else
    reload_event_map! unless event.is_internal?
    route event
  end
end
```

    
  

    
      
  
### 
  
    #**receive**(event_name, data, connection)  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
22
```

    
    
      

```
# File 'lib/websocket_rails/dispatcher.rb', line 19

def receive(event_name,data,connection)
  event = Event.new event_name, data, connection
  dispatch( event )
end
```

    
  

    
      
  
### 
  
    #**receive_encoded**(encoded_data, connection)  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
```

    
    
      

```
# File 'lib/websocket_rails/dispatcher.rb', line 14

def receive_encoded(encoded_data,connection)
  event = Event.new_from_json( encoded_data, connection )
  dispatch( event )
end
```

    
  

    
      
  
### 
  
    #**reload_event_map!**  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
48
49
50
51
52
53
```

    
    
      

```
# File 'lib/websocket_rails/dispatcher.rb', line 45

def reload_event_map!
  return unless defined?(Rails) and !Rails.configuration.cache_classes
  begin
    load "#{Rails.root}/config/events.rb"
    @event_map = EventMap.new(self)
  rescue Exception => ex
    log(:warn, "EventMap reload failed: #{ex.message}")
  end
end
```

    
  

    
      
  
### 
  
    #**send_message**(event)  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/websocket_rails/dispatcher.rb', line 35

def send_message(event)
  event.connection.trigger event
end
```