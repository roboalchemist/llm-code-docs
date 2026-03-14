# Module: EventMachine::WebSocket::Close05
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Handler05
  
  

  
  
    Defined in:
    lib/em-websocket/close05.rb
  
  

  
    
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
```

    
    
      

```
# File 'lib/em-websocket/close05.rb', line 4

def close_websocket(code, body)
  # TODO: Ideally send body data and check that it matches in ack
  send_frame(:close, "\x53")
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

11
```

    
    
      

```
# File 'lib/em-websocket/close05.rb', line 11

def supports_close_codes?; false; end
```