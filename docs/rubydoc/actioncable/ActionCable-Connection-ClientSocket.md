# Class: ActionCable::Connection::ClientSocket
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Connection::ClientSocket
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/client_socket.rb
  
  

## Overview

  
    

– This class is heavily based on faye-websocket-ruby

Copyright © 2010-2015 James Coglan

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        CONNECTING =
          
        
        

```
0

```

      
        OPEN =
          
        
        

```
1

```

      
        CLOSING =
          
        
        

```
2

```

      
        CLOSED =
          
        
        

```
3

```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**env**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute env.

  

    
      
- 
  
    
      #**url**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute url.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**determine_url**(env)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      .**secure_request?**(env)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**alive?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**client_gone**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**close**(code = nil, reason = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(env, event_target, event_loop, protocols)  ⇒ ClientSocket 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ClientSocket.

  

      
        
- 
  
    
      #**parse**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**protocol**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**rack_response**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**start_driver**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**transmit**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**write**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(env, event_target, event_loop, protocols)  ⇒ ClientSocket 
  

  

  

  
    
      

```

36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 36

def initialize(env, event_target, event_loop, protocols)
  @env          = env
  @event_target = event_target
  @event_loop   = event_loop

  @url = ClientSocket.determine_url(@env)

  @driver = @driver_started = nil
  @close_params = ["", 1006]

  @ready_state = CONNECTING

  # The driver calls `env`, `url`, and `write`
  @driver = ::WebSocket::Driver.rack(self, protocols: protocols)

  @driver.on(:open)    { |e| open }
  @driver.on(:message) { |e| receive_message(e.data) }
  @driver.on(:close)   { |e| begin_close(e.reason, e.code) }
  @driver.on(:error)   { |e| emit_error(e.message) }

  @stream = ActionCable::Connection::Stream.new(@event_loop, self)
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**env**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute env.

  

  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 34

def env
  @env
end

```

    
  

    
      
      
      
  
### 
  
    #**url**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute url.

  

  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 34

def url
  @url
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**determine_url**(env)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

14
15
16
17
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 14

def self.determine_url(env)
  scheme = secure_request?(env) ? "wss:" : "ws:"
  "#{ scheme }//#{ env['HTTP_HOST'] }#{ env['REQUEST_URI'] }"
end

```

    
  

    
      
  
### 
  
    .**secure_request?**(env)  ⇒ Boolean 
  

  

  

  
    
      

```

19
20
21
22
23
24
25
26
27
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 19

def self.secure_request?(env)
  return true if env["HTTPS"] == "on"
  return true if env["HTTP_X_FORWARDED_SSL"] == "on"
  return true if env["HTTP_X_FORWARDED_SCHEME"] == "https"
  return true if env["HTTP_X_FORWARDED_PROTO"] == "https"
  return true if env["rack.url_scheme"] == "https"

  false
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**alive?**  ⇒ Boolean 
  

  

  

  
    
      

```

114
115
116
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 114

def alive?
  @ready_state == OPEN
end

```

    
  

    
      
  
### 
  
    #**client_gone**  ⇒ Object 
  

  

  

  
    
      

```

110
111
112
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 110

def client_gone
  finalize_close
end

```

    
  

    
      
  
### 
  
    #**close**(code = nil, reason = nil)  ⇒ Object 
  

  

  

  
    
      

```

92
93
94
95
96
97
98
99
100
101
102
103
104
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 92

def close(code = nil, reason = nil)
  code   ||= 1000
  reason ||= ""

  unless code == 1000 || (code >= 3000 && code <= 4999)
    raise ArgumentError, "Failed to execute 'close' on WebSocket: " \
                         "The code must be either 1000, or between 3000 and 4999. " \
                         "#{code} is neither."
  end

  @ready_state = CLOSING unless @ready_state == CLOSED
  @driver.close(reason, code)
end

```

    
  

    
      
  
### 
  
    #**parse**(data)  ⇒ Object 
  

  

  

  
    
      

```

106
107
108
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 106

def parse(data)
  @driver.parse(data)
end

```

    
  

    
      
  
### 
  
    #**protocol**  ⇒ Object 
  

  

  

  
    
      

```

118
119
120
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 118

def protocol
  @driver.protocol
end

```

    
  

    
      
  
### 
  
    #**rack_response**  ⇒ Object 
  

  

  

  
    
      

```

71
72
73
74
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 71

def rack_response
  start_driver
  [ -1, {}, [] ]
end

```

    
  

    
      
  
### 
  
    #**start_driver**  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
62
63
64
65
66
67
68
69
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 59

def start_driver
  return if @driver.nil? || @driver_started
  @stream.hijack_rack_socket

  if callback = @env["async.callback"]
    callback.call([101, {}, @stream])
  end

  @driver_started = true
  @driver.start
end

```

    
  

    
      
  
### 
  
    #**transmit**(message)  ⇒ Object 
  

  

  

  
    
      

```

82
83
84
85
86
87
88
89
90
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 82

def transmit(message)
  return false if @ready_state > OPEN
  case message
  when Numeric then @driver.text(message.to_s)
  when String  then @driver.text(message)
  when Array   then @driver.binary(message)
  else false
  end
end

```

    
  

    
      
  
### 
  
    #**write**(data)  ⇒ Object 
  

  

  

  
    
      

```

76
77
78
79
80
```

    
    
      

```
# File 'lib/action_cable/connection/client_socket.rb', line 76

def write(data)
  @stream.write(data)
rescue => e
  emit_error e.message
end

```