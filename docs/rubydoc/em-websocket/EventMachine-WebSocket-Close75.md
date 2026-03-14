# Module: EventMachine::WebSocket::Close75
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Handler75, Handler76
  
  

  
  
    Defined in:
    lib/em-websocket/close75.rb
  
  

  
    
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
```

    
    
      

```
# File 'lib/em-websocket/close75.rb', line 4

def close_websocket(code, body)
  @connection.close_connection_after_writing
end
```

    
  

    
      
  
### 
  
    #**supports_close_codes?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

8
```

    
    
      

```
# File 'lib/em-websocket/close75.rb', line 8

def supports_close_codes?; false; end
```