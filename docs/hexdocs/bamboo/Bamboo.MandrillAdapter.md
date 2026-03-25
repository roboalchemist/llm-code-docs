# 
      Bamboo.MandrillAdapter 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Sends email using Mandrill's JSON API.

Use this adapter to send emails through Mandrill's API. Requires that an API
key is set in the config. See `Bamboo.MandrillHelper` for extra functions that
can be used by `Bamboo.MandrillAdapter` (tagging, merge vars, etc.)
## **Example config

```
# In config/config.exs, or config/prod.exs, etc.
config :my_app, MyApp.Mailer,
  adapter: Bamboo.MandrillAdapter,
  api_key: "my_api_key",
  hackney_opts: [
    recv_timeout: :timer.minutes(1)
  ]

# Define a Mailer. Maybe in lib/my_app/mailer.ex
defmodule MyApp.Mailer do
  use Bamboo.Mailer, otp_app: :my_app
end
```

    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        deliver(email, config)

      

        

Callback implementation for `Bamboo.Adapter.deliver/2`.

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# deliver(email, config)

        
          **
        

    
  

  

Callback implementation for `Bamboo.Adapter.deliver/2`.