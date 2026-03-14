# Module: EventMachine::WebSocket
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/close03.rb,

  lib/em-websocket/close05.rb,
 lib/em-websocket/close06.rb,
 lib/em-websocket/close75.rb,
 lib/em-websocket/handler.rb,
 lib/em-websocket/debugger.rb,
 lib/em-websocket/framing03.rb,
 lib/em-websocket/framing04.rb,
 lib/em-websocket/framing05.rb,
 lib/em-websocket/framing07.rb,
 lib/em-websocket/framing76.rb,
 lib/em-websocket/handler03.rb,
 lib/em-websocket/handler05.rb,
 lib/em-websocket/handler06.rb,
 lib/em-websocket/handler07.rb,
 lib/em-websocket/handler08.rb,
 lib/em-websocket/handler13.rb,
 lib/em-websocket/handler75.rb,
 lib/em-websocket/handler76.rb,
 lib/em-websocket/handshake.rb,
 lib/em-websocket/masking04.rb,
 lib/em-websocket/websocket.rb,
 lib/em-websocket/connection.rb,
 lib/em-websocket/handshake04.rb,
 lib/em-websocket/handshake75.rb,
 lib/em-websocket/handshake76.rb,
 lib/em-websocket/message_processor_03.rb,
 lib/em-websocket/message_processor_06.rb

  
  

## Defined Under Namespace

  
    
      **Modules:** Close03, Close05, Close06, Close75, Debugger, Framing03, Framing04, Framing05, Framing07, Framing76, Handshake04, Handshake75, Handshake76, MessageProcessor03, MessageProcessor06
    
  
    
      **Classes:** Connection, Handler, Handler03, Handler05, Handler06, Handler07, Handler08, Handler13, Handler75, Handler76, Handshake, HandshakeError, InvalidDataError, MaskedString, WSMessageTooBigError, WSProtocolError, WebSocketError
    
  

  
## Class Attribute Summary collapse

  

    
      
- 
  
    
      .**close_timeout**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute close_timeout.

  

    
      
- 
  
    
      .**max_frame_size**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute max_frame_size.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**run**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Start WebSocket server inside eventmachine run loop.

  

      
        
- 
  
    
      .**start**(options, &blk)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Start WebSocket server, including starting eventmachine run loop.

  

      
        
- 
  
    
      .**stop**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Attribute Details

    
      
      
      
  
### 
  
    .**close_timeout**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute close_timeout.

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/em-websocket/websocket.rb', line 5

def close_timeout
  @close_timeout
end
```

    
  

    
      
      
      
  
### 
  
    .**max_frame_size**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute max_frame_size.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/em-websocket/websocket.rb', line 4

def max_frame_size
  @max_frame_size
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**run**(options)  ⇒ Object 
  

  

  

  
    

Start WebSocket server inside eventmachine run loop

  

  

  
    
      

```

44
45
46
47
48
49
```

    
    
      

```
# File 'lib/em-websocket/websocket.rb', line 44

def self.run(options)
  host, port = options.values_at(:host, :port)
  EM.start_server(host, port, Connection, options) do |c|
    yield c
  end
end
```

    
  

    
      
  
### 
  
    .**start**(options, &blk)  ⇒ Object 
  

  

  

  
    

Start WebSocket server, including starting eventmachine run loop

  

  

  
    
      

```

33
34
35
36
37
38
39
40
41
```

    
    
      

```
# File 'lib/em-websocket/websocket.rb', line 33

def self.start(options, &blk)
  EM.epoll
  EM.run {
    trap("TERM") { stop }
    trap("INT")  { stop }

    run(options, &blk)
  }
end
```

    
  

    
      
  
### 
  
    .**stop**  ⇒ Object 
  

  

  

  
    
      

```

51
52
53
54
```

    
    
      

```
# File 'lib/em-websocket/websocket.rb', line 51

def self.stop
  puts "Terminating WebSocket Server"
  EM.stop
end
```