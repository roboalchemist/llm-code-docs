# Module: EventMachine::WebSocket::Handshake76
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Handler76
  
  

  
  
    Defined in:
    lib/em-websocket/handshake76.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**handshake**(headers, path, secure)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**handshake**(headers, path, secure)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/em-websocket/handshake76.rb', line 6

def handshake(headers, path, secure)
  challenge_response = solve_challenge(
    headers['sec-websocket-key1'],
    headers['sec-websocket-key2'],
    headers['third-key']
  )

  scheme = (secure ? "wss" : "ws")
  location = "#{scheme}://#{headers['host']}#{path}"

  upgrade =  "HTTP/1.1 101 WebSocket Protocol Handshake\r\n"
  upgrade << "Upgrade: WebSocket\r\n"
  upgrade << "Connection: Upgrade\r\n"
  upgrade << "Sec-WebSocket-Location: #{location}\r\n"
  upgrade << "Sec-WebSocket-Origin: #{headers['origin']}\r\n"
  if protocol = headers['sec-websocket-protocol']
    validate_protocol!(protocol)
    upgrade << "Sec-WebSocket-Protocol: #{protocol}\r\n"
  end
  upgrade << "\r\n"
  upgrade << challenge_response

  return upgrade
end
```