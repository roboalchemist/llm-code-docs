# Class: WebsocketRails::SpecHelperEvent
  
  
  

  
  
    Inherits:
    
      Event
      
        

          
- Object
          
            
- Event
          
            
- WebsocketRails::SpecHelperEvent
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/spec_helpers/spec_helper_event.rb
  
  

  
## Constant Summary

  
  
### Constants included
     from Logging

  

Logging::ANSI, Logging::LOGGABLE_DATA

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**dispatcher**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute dispatcher.

  

    
      
- 
  
    
      #**triggered**  ⇒ Object 
    

    
      (also: #triggered?)
    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute triggered.

  

    
  

  
  
  
### Attributes inherited from Event

  

#channel, #data, #id, #name, #namespace, #result, #server_token, #success, #token, #user_id

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**connection**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**dispatch**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(event_name, options = {})  ⇒ SpecHelperEvent 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of SpecHelperEvent.

  

      
        
- 
  
    
      #**trigger**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Event

  

#as_json, #encoded_name, #is_channel?, #is_internal?, #is_invalid?, #is_user?, log_header, new_from_json, #serialize

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

#color_for_level, #colorize, configure, #log, #log_data?, #log_event, #log_event?, #log_event_end, #log_event_start, #log_exception, #log_header, log_level, #wrap

  
  
  
  
  
  
  
  
  
### Methods included from StaticEvents

  

#new_on_close, #new_on_error, #new_on_invalid_event_received, #new_on_open, #new_on_ping

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(event_name, options = {})  ⇒ SpecHelperEvent 
  

  

  

  
    

Returns a new instance of SpecHelperEvent.

  

  

  
    
      

```

9
10
11
12
13
```

    
    
      

```
# File 'lib/spec_helpers/spec_helper_event.rb', line 9

def initialize(event_name,options={})
  super(event_name, options)
  @triggered = false
  @dispatcher =  Dispatcher.new(nil)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**dispatcher**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute dispatcher.

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/spec_helpers/spec_helper_event.rb', line 5

def dispatcher
  @dispatcher
end
```

    
  

    
      
      
      
  
### 
  
    #**triggered**  ⇒ Object  (readonly)
  

  
    Also known as:
    triggered?
    
  

  

  
    

Returns the value of attribute triggered.

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/spec_helpers/spec_helper_event.rb', line 5

def triggered
  @triggered
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**connection**  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/spec_helpers/spec_helper_event.rb', line 24

def connection
  OpenStruct.new(:id => 1)
end
```

    
  

    
      
  
### 
  
    #**dispatch**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
22
```

    
    
      

```
# File 'lib/spec_helpers/spec_helper_event.rb', line 19

def dispatch
  @dispatcher.dispatch(self)
  self
end
```

    
  

    
      
  
### 
  
    #**trigger**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/spec_helpers/spec_helper_event.rb', line 15

def trigger
  @triggered = true
end
```