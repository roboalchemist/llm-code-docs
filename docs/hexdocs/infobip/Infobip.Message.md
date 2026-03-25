infobip
      
      **
        v0.2.0
      **
    

  

  

    
- Pages

      
- Modules

  

  
  

  
    

      
# 
Infobip.Message (infobip v0.2.0)

      

        

Builds the XML message to send to the Infobip API.
        

          
# 
            
              
              Link to this section
            
            Summary
          

  
    
## 
      Functions
    

  
    build(recipient, message)

  

    

Builds valid XML for the Infobip text message API.

  
    build(recipient, message, message_id)

  

  

        

          
# 
            
              
              Link to this section
            
Functions
          

          

  
    
      
      Link to this function
    
    
# build(recipient, message)

  

  

      
## Specs

      

          

```
build(binary(), binary()) :: binary()
```

      

Builds valid XML for the Infobip text message API.
  

  
    
      
      Link to this function
    
    
# build(recipient, message, message_id)

  

  

      
## Specs

      

          

```
build(binary(), binary(), binary()) :: binary()
```