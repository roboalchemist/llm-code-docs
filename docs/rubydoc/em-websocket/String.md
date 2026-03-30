# Class: String
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- String
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/em-websocket.rb
  
  

  
## Direct Known Subclasses

  

EventMachine::WebSocket::MaskedString

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**getbyte**(i)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**getbyte**(i)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/em-websocket.rb', line 20

def getbyte(i)
  self[i]
end
```