# Module: EventMachine::WebSocket::Close06
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Handler06, Handler07, Handler08, Handler13
  
  

  
  
    Defined in:
    lib/em-websocket/close06.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**close_websocket**(code, body)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**supports_close_codes?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**close_websocket**(code, body)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/em-websocket/close06.rb', line 4

def close_websocket(code, body)
  if code
    close_data = [code].pack('n')
    close_data << body if body
    send_frame(:close, close_data)
  else
    send_frame(:close, '')
  end
  @state = :closing
  start_close_timeout
end
```

    
  

    
      
  
### 
  
    #**supports_close_codes?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

16
```

    
    
      

```
# File 'lib/em-websocket/close06.rb', line 16

def supports_close_codes?; true; end
```