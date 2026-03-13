# Class: WebsocketRails::EventMap::Namespace
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::EventMap::Namespace
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Logging
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/event_map.rb
  
  

## Overview

  
    

Stores route map for nested namespaces

  

  

  
## Constant Summary

  
  
### Constants included
     from Logging

  

Logging::ANSI, Logging::LOGGABLE_DATA

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**actions**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute actions.

  

    
      
- 
  
    
      #**controllers**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute controllers.

  

    
      
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

  

    
      
- 
  
    
      #**namespaces**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute namespaces.

  

    
      
- 
  
    
      #**parent**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute parent.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**find_or_create**(namespace)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(name, dispatcher, parent = nil)  ⇒ Namespace 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Namespace.

  

      
        
- 
  
    
      #**routes_for**(event, event_namespace = nil, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Iterates through the namespace tree and yields all controller/action pairs stored for the target event.

  

      
        
- 
  
    
      #**store**(event_name, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Stores controller/action pairs for events subscribed under this namespace.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

#color_for_level, #colorize, configure, #log, #log_data?, #log_event, #log_event?, #log_event_end, #log_event_start, #log_exception, #log_header, log_level, #wrap

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, dispatcher, parent = nil)  ⇒ Namespace 
  

  

  

  
    

Returns a new instance of Namespace.

  

  

  
    
      

```

82
83
84
85
86
87
88
89
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 82

def initialize(name,dispatcher,parent=nil)
  @name        = name
  @parent      = parent
  @dispatcher  = dispatcher
  @actions     = Hash.new {|h,k| h[k] = Array.new}
  @controllers = Hash.new
  @namespaces  = Hash.new
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**actions**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute actions.

  

  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 80

def actions
  @actions
end
```

    
  

    
      
      
      
  
### 
  
    #**controllers**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute controllers.

  

  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 80

def controllers
  @controllers
end
```

    
  

    
      
      
      
  
### 
  
    #**name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute name.

  

  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 80

def name
  @name
end
```

    
  

    
      
      
      
  
### 
  
    #**namespaces**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute namespaces.

  

  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 80

def namespaces
  @namespaces
end
```

    
  

    
      
      
      
  
### 
  
    #**parent**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute parent.

  

  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 80

def parent
  @parent
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**find_or_create**(namespace)  ⇒ Object 
  

  

  

  
    
      

```

91
92
93
94
95
96
97
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 91

def find_or_create(namespace)
  unless child = namespaces[namespace]
    child = Namespace.new namespace, @dispatcher, self
    namespaces[namespace] = child
  end
  child
end
```

    
  

    
      
  
### 
  
    #**routes_for**(event, event_namespace = nil, &block)  ⇒ Object 
  

  

  

  
    

Iterates through the namespace tree and yields all controller/action pairs stored for the target event.

  

  

  
    
      

```

108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 108

def routes_for(event, event_namespace=nil, &block)

  # Grab the first level namespace from the namespace array
  # and remove it from the copy.
  event_namespace = copy_event_namespace( event, event_namespace ) || return
  namespace       = event_namespace.shift

  # If the namespace matches the current namespace and we are
  # at the last namespace level, yield any controller/action
  # pairs for this event.
  #
  # If the namespace does not match, search the list of child
  # namespaces stored at this level for a match and delegate
  # to it's #routes_for method, passing along the current
  # copy of the event's namespace array.
  if namespace == @name and event_namespace.empty?
    actions[event.name].each do |klass,action|
      block.call klass, action
    end
  else
    child_namespace = event_namespace.first
    child = namespaces[child_namespace]
    child.routes_for event, event_namespace, &block unless child.nil?
  end
end
```

    
  

    
      
  
### 
  
    #**store**(event_name, options)  ⇒ Object 
  

  

  

  
    

Stores controller/action pairs for events subscribed under this namespace.

  

  

  
    
      

```

101
102
103
104
```

    
    
      

```
# File 'lib/websocket_rails/event_map.rb', line 101

def store(event_name,options)
  klass, action = TargetValidator.validate_target options
  actions[event_name] << [klass,action]
end
```