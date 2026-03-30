# Module: EventMachine::WebSocket::Handshake75
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Handler75
  
  

  
  
    Defined in:
    lib/em-websocket/handshake75.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**handshake**(headers, path, secure)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**validate_protocol!**(protocol)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**handshake**(headers, path, secure)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/em-websocket/handshake75.rb', line 4

def self.handshake(headers, path, secure)
  scheme = (secure ? "wss" : "ws")
  location = "#{scheme}://#{headers['host']}#{path}"

  upgrade =  "HTTP/1.1 101 Web Socket Protocol Handshake\r\n"
  upgrade << "Upgrade: WebSocket\r\n"
  upgrade << "Connection: Upgrade\r\n"
  upgrade << "WebSocket-Origin: #{headers['origin']}\r\n"
  upgrade << "WebSocket-Location: #{location}\r\n"
  if protocol = headers['sec-websocket-protocol']
    validate_protocol!(protocol)
    upgrade << "Sec-WebSocket-Protocol: #{protocol}\r\n"
  end
  upgrade << "\r\n"

  return upgrade
end
```

    
  

    
      
  
### 
  
    .**validate_protocol!**(protocol)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (HandshakeError)
      
      
      
    
  

  
    
      

```

22
23
24
25
```

    
    
      

```
# File 'lib/em-websocket/handshake75.rb', line 22

def self.validate_protocol!(protocol)
  raise HandshakeError, "Invalid WebSocket-Protocol: empty" if protocol.empty?
  # TODO: Validate characters
end
```