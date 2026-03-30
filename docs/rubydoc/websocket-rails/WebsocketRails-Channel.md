# Class: WebsocketRails::Channel
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::Channel
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Logging
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/channel.rb
  
  

  
## Constant Summary

  
  
### Constants included
     from Logging

  

Logging::ANSI, Logging::LOGGABLE_DATA

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

  

    
      
- 
  
    
      #**subscribers**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute subscribers.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(channel_name)  ⇒ Channel 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Channel.

  

      
        
- 
  
    
      #**is_private?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**make_private**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**subscribe**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**token**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger**(event_name, data = {}, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger_event**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unsubscribe**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

#color_for_level, #colorize, configure, #log, #log_data?, #log_event, #log_event?, #log_event_end, #log_event_start, #log_exception, #log_header, log_level, #wrap

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(channel_name)  ⇒ Channel 
  

  

  

  
    

Returns a new instance of Channel.

  

  

  
    
      

```

10
11
12
13
14
```

    
    
      

```
# File 'lib/websocket_rails/channel.rb', line 10

def initialize(channel_name)
  @subscribers = []
  @name        = channel_name
  @private     = false
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute name.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/websocket_rails/channel.rb', line 8

def name
  @name
end
```

    
  

    
      
      
      
  
### 
  
    #**subscribers**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute subscribers.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/websocket_rails/channel.rb', line 8

def subscribers
  @subscribers
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**is_private?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

53
54
55
```

    
    
      

```
# File 'lib/websocket_rails/channel.rb', line 53

def is_private?
  @private
end
```

    
  

    
      
  
### 
  
    #**make_private**  ⇒ Object 
  

  

  

  
    
      

```

46
47
48
49
50
51
```

    
    
      

```
# File 'lib/websocket_rails/channel.rb', line 46

def make_private
  unless config.keep_subscribers_when_private?
    @subscribers.clear
  end
  @private = true
end
```

    
  

    
      
  
### 
  
    #**subscribe**(connection)  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
19
20
21
```

    
    
      

```
# File 'lib/websocket_rails/channel.rb', line 16

def subscribe(connection)
  info "#{connection} subscribed to channel #{name}"
  trigger 'subscriber_join', connection.user if config.broadcast_subscriber_events?
  @subscribers << connection
  send_token connection
end
```

    
  

    
      
  
### 
  
    #**token**  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/websocket_rails/channel.rb', line 57

def token
  @token ||= channel_tokens[@name] ||= generate_unique_token
end
```

    
  

    
      
  
### 
  
    #**trigger**(event_name, data = {}, options = {})  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
33
34
35
36
37
38
```

    
    
      

```
# File 'lib/websocket_rails/channel.rb', line 30

def trigger(event_name,data={},options={})
  options.merge! :channel => name, :token => token
  options[:data] = data

  event = Event.new event_name, options

  info "[#{name}] #{event.data.inspect}"
  send_data event
end
```

    
  

    
      
  
### 
  
    #**trigger_event**(event)  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
43
44
```

    
    
      

```
# File 'lib/websocket_rails/channel.rb', line 40

def trigger_event(event)
  return if event.token != token
  info "[#{name}] #{event.data.inspect}"
  send_data event
end
```

    
  

    
      
  
### 
  
    #**unsubscribe**(connection)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
26
27
28
```

    
    
      

```
# File 'lib/websocket_rails/channel.rb', line 23

def unsubscribe(connection)
  return unless @subscribers.include? connection
  info "#{connection} unsubscribed from channel #{name}"
  @subscribers.delete connection
  trigger 'subscriber_part', connection.user if config.broadcast_subscriber_events?
end
```