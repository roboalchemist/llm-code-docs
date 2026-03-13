# Module: EventMachine::WebSocket::Handshake04
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/handshake04.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**handshake**(headers, _, __)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**validate_protocol!**(protocol)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**handshake**(headers, _, __)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/em-websocket/handshake04.rb', line 7

def self.handshake(headers, _, __)
  # Required
  unless key = headers['sec-websocket-key']
    raise HandshakeError, "sec-websocket-key header is required"
  end

  string_to_sign = "#{key}258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
  signature = Base64.encode64(Digest::SHA1.digest(string_to_sign)).chomp

  upgrade = ["HTTP/1.1 101 Switching Protocols"]
  upgrade << "Upgrade: websocket"
  upgrade << "Connection: Upgrade"
  upgrade << "Sec-WebSocket-Accept: #{signature}"
  if protocol = headers['sec-websocket-protocol']
    validate_protocol!(protocol)
    upgrade << "Sec-WebSocket-Protocol: #{protocol}"
  end

  # TODO: Support sec-websocket-protocol selection
  # TODO: sec-websocket-extensions

  return upgrade.join("\r\n") + "\r\n\r\n"
end
```

    
  

    
      
  
### 
  
    .**validate_protocol!**(protocol)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (HandshakeError)
      
      
      
    
  

  
    
      

```

31
32
33
34
```

    
    
      

```
# File 'lib/em-websocket/handshake04.rb', line 31

def self.validate_protocol!(protocol)
  raise HandshakeError, "Invalid WebSocket-Protocol: empty" if protocol.empty?
  # TODO: Validate characters
end
```