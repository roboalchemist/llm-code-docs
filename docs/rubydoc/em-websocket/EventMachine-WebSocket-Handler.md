# Class: EventMachine::WebSocket::Handler
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- EventMachine::WebSocket::Handler
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Debugger
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/handler.rb
  
  

  
## Direct Known Subclasses

  

Handler03, Handler05, Handler06, Handler07, Handler08, Handler13, Handler75, Handler76

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**request**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute request.

  

    
      
- 
  
    
      #**state**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute state.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**klass_factory**(version)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**close_websocket**(code, body)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fail_websocket**(e)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This corresponds to “Fail the WebSocket Connection” in the spec.

  

      
        
- 
  
    
      #**initialize**(connection, debug = false)  ⇒ Handler 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Handler.

  

      
        
- 
  
    
      #**ping**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**pingable?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**receive_data**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**start_close_timeout**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Used to avoid un-acked and unclosed remaining open indefinitely.

  

      
        
- 
  
    
      #**unbind**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(connection, debug = false)  ⇒ Handler 
  

  

  

  
    

Returns a new instance of Handler.

  

  

  
    
      

```

37
38
39
40
41
42
43
```

    
    
      

```
# File 'lib/em-websocket/handler.rb', line 37

def initialize(connection, debug = false)
  @connection = connection
  @debug = debug
  @state = :connected
  @close_timer = nil
  initialize_framing
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**request**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute request.

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/em-websocket/handler.rb', line 35

def request
  @request
end
```

    
  

    
      
      
      
  
### 
  
    #**state**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute state.

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/em-websocket/handler.rb', line 35

def state
  @state
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**klass_factory**(version)  ⇒ Object 
  

  

  

  
    
      

```

4
5
6
7
8
9
10
11
12
13
14
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
26
27
28
29
30
31
```

    
    
      

```
# File 'lib/em-websocket/handler.rb', line 4

def self.klass_factory(version)
  case version
  when 75
    Handler75
  when 76
    Handler76
  when 1..3
    # We'll use handler03 - I believe they're all compatible
    Handler03
  when 5
    Handler05
  when 6
    Handler06
  when 7
    Handler07
  when 8
    # drafts 9, 10, 11 and 12 should never change the version
    # number as they are all the same as version 08.
    Handler08
  when 13
    # drafts 13 to 17 all identify as version 13 as they are
    # only minor changes or text changes.
    Handler13
  else
    # According to spec should abort the connection
    raise HandshakeError, "Protocol version #{version} not supported"
  end
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**close_websocket**(code, body)  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
```

    
    
      

```
# File 'lib/em-websocket/handler.rb', line 52

def close_websocket(code, body)
  # Implemented in subclass
end
```

    
  

    
      
  
### 
  
    #**fail_websocket**(e)  ⇒ Object 
  

  

  

  
    

This corresponds to “Fail the WebSocket Connection” in the spec.

  

  

  
    
      

```

66
67
68
69
70
71
```

    
    
      

```
# File 'lib/em-websocket/handler.rb', line 66

def fail_websocket(e)
  debug [:error, e]
  close_websocket(e.code, e.message)
  @connection.close_connection_after_writing
  @connection.trigger_on_error(e)
end
```

    
  

    
      
  
### 
  
    #**ping**  ⇒ Object 
  

  

  

  
    
      

```

86
87
88
89
```

    
    
      

```
# File 'lib/em-websocket/handler.rb', line 86

def ping
  # Overridden in subclass
  false
end
```

    
  

    
      
  
### 
  
    #**pingable?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

91
92
93
94
```

    
    
      

```
# File 'lib/em-websocket/handler.rb', line 91

def pingable?
  # Also Overridden
  false
end
```

    
  

    
      
  
### 
  
    #**receive_data**(data)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
48
49
50
```

    
    
      

```
# File 'lib/em-websocket/handler.rb', line 45

def receive_data(data)
  @data << data
  process_data
rescue WSProtocolError => e
  fail_websocket(e)
end
```

    
  

    
      
  
### 
  
    #**start_close_timeout**  ⇒ Object 
  

  

  

  
    

Used to avoid un-acked and unclosed remaining open indefinitely

  

  

  
    
      

```

57
58
59
60
61
62
63
```

    
    
      

```
# File 'lib/em-websocket/handler.rb', line 57

def start_close_timeout
  @close_timer = EM::Timer.new(@connection.close_timeout) {
    @connection.close_connection
    e = WSProtocolError.new("Close handshake un-acked after #{@connection.close_timeout}s, closing tcp connection")
    @connection.trigger_on_error(e)
  }
end
```

    
  

    
      
  
### 
  
    #**unbind**  ⇒ Object 
  

  

  

  
    
      

```

73
74
75
76
77
78
79
80
81
82
83
84
```

    
    
      

```
# File 'lib/em-websocket/handler.rb', line 73

def unbind
  @state = :closed

  @close_timer.cancel if @close_timer

  @close_info = defined?(@close_info) ? @close_info : {
    :code => 1006,
    :was_clean => false,
  }

  @connection.trigger_on_close(@close_info)
end
```