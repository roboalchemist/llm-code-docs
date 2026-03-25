# 
      Bamboo.ApiError exception
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Error used to represent a problem when sending emails through an external email service API.
    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        build_api_error(message)

      

    

    
      
        build_api_error(service_name, response, params, extra_message \\ "")

      

    

    
      
        raise_api_error(message)

      

        

Raises an `ApiError` with the given `message` or `service_name`, `response` and `params`.

    

    
      
        raise_api_error(service_name, response, params, extra_message \\ "")

      

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# build_api_error(message)

        
          **
        

    
  

  

  

    

  
    
      **
    
    
      
# build_api_error(service_name, response, params, extra_message \\ "")

        
          **
        

    
  

  

  

  
    
      **
    
    
      
# raise_api_error(message)

        
          **
        

    
  

  

Raises an `ApiError` with the given `message` or `service_name`, `response` and `params`.

An extra error message can be added using a fourth parameter `extra_message`.
## **Examples

```
iex> raise_api_error("Error message")
** (Bamboo.ApiError) Error Message

iex> raise_api_error(service_name, response, params)
** (Bamboo.ApiError) There was a problem sending the email through the <service_name> API.

Here is the response:

"<response>"

Here are the params we sent:

"<params>"

iex> raise_api_error(service_name, response, params, extra_message)
** (Bamboo.ApiError) There was a problem sending the email through the <service_name> API.

Here is the response:

"<response>"

Here are the params we sent:

"<params>"

<extra_message>
```

  

    

  
    
      **
    
    
      
# raise_api_error(service_name, response, params, extra_message \\ "")

        
          **