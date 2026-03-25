infobip
      
      **
        v0.2.0
      **
    

  

  

    
- Pages

      
- Modules

  

  
  

  
    

      
# 
Infobip.TextMessage (infobip v0.2.0)

      

        

Builds and sends a text message.
        

          
# 
            
              
              Link to this section
            
            Summary
          

  
    
## 
      Types
    

  
    send_response()

  

  

  
    
## 
      Functions
    

  
    send(recipient, message)

  

    

Sends a text message.

  
    send(recipient, message, message_id)

  

  

        

          
# 
            
              
              Link to this section
            
Types
          

          

  
    
      
      Link to this type
    
    
# send_response()

  

  

      
## Specs

      

          

```
send_response() :: :ok | {:error, {:xml, term()} | {:infobip, term()}}
```

      

  

          
# 
            
              
              Link to this section
            
Functions
          

          

  
    
      
      Link to this function
    
    
# send(recipient, message)

  

  

      
## Specs

      

          

```
send(binary(), binary()) :: send_response()
```

      

Sends a text message.
  

  
    
      
      Link to this function
    
    
# send(recipient, message, message_id)

  

  

      
## Specs

      

          

```
send(binary(), binary(), binary()) :: send_response()
```