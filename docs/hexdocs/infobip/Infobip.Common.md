infobip
      
      **
        v0.2.0
      **
    

  

  

    
- Pages

      
- Modules

  

  
  

  
    

      
# 
Infobip.Common (infobip v0.2.0)

      

        

Helper module for making Infobip requests.
        

          
# 
            
              
              Link to this section
            
            Summary
          

  
    
## 
      Functions
    

  
    handle_http_error(reason)

  

    

Generates a meaningful error message for an HTTP error.

  
    http_config()

  

    

Loads the Infobip config.

  

        

          
# 
            
              
              Link to this section
            
Functions
          

          

  
    
      
      Link to this function
    
    
# handle_http_error(reason)

  

  

      
## Specs

      

          

```
handle_http_error(any()) :: {atom(), {atom(), any()}}
```

      

Generates a meaningful error message for an HTTP error.
### 
  
  Examples

```
iex> handle_http_error(:nxdomain)
{:error, {:http, "Could not reach Infobip API"}}
```

  

  
    
      
      Link to this function
    
    
# http_config()

  

  

      
## Specs

      

          

```
http_config() :: map()
```

      

Loads the Infobip config.