# 
      Bamboo.Interceptor behaviour
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Behaviour for creating an Interceptor.

An interceptor allows you to modify or block an email before it is sent. To
block an email, it must be marked as blocked with `Bamboo.Email.block/1`.
## **Example

```
defmodule Bamboo.DenyListInterceptor do
  @behaviour Bamboo.Interceptor
  @deny_list ["bar@foo.com"]

  def call(email) do
    if email.to in @deny_list do
      Bamboo.Email.block(email)
    else
      email
    end
  end
end
```

    

    
# 
      
        **
      
      Summary
    

  
## 
    Callbacks
  

    
      
        call(email)

      

    

  

    
# 
      
        **
      
      Callbacks
    

    

  
    
      **
    
    
      
# call(email)

        
          **
        

    
  

  

      

          

```
@callback call(email :: Bamboo.Email.t()) :: Bamboo.Email.t()
```