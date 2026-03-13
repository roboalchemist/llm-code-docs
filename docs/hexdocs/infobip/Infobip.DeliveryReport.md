infobip
      
      **
        v0.2.0
      **
    

  

  

    
- Pages

      
- Modules

  

  
  

  
    

      
# 
Infobip.DeliveryReport (infobip v0.2.0)

      

        

Fetches a text message delivery report.
        

          
# 
            
              
              Link to this section
            
            Summary
          

  
    
## 
      Types
    

  
    fetch_response()

  

  

  
    
## 
      Functions
    

  
    fetch(message_id)

  

    

Fetches a text message delivery report.

  

        

          
# 
            
              
              Link to this section
            
Types
          

          

  
    
      
      Link to this type
    
    
# fetch_response()

  

  

      
## Specs

      

          

```
fetch_response() :: {:ok, {atom(), binary()}} | {:error, any()}
```

      

  

          
# 
            
              
              Link to this section
            
Functions
          

          

  
    
      
      Link to this function
    
    
# fetch(message_id)

  

  

      
## Specs

      

          

```
fetch(binary()) :: fetch_response()
```

      

Fetches a text message delivery report.