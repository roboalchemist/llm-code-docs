# 
      Bamboo.TestAdapter 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Used for testing email delivery.

No emails are sent, instead a message is sent to the current process and can
be asserted on with helpers from `Bamboo.Test`.
## **Example config

```
# Typically done in config/test.exs
config :my_app, MyApp.Mailer,
  adapter: Bamboo.TestAdapter

# Define a Mailer. Typically in lib/my_app/mailer.ex
defmodule MyApp.Mailer do
  use Bamboo.Mailer, otp_app: :my_app
end
```

    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        handle_config(config)

      

        

Callback implementation for `Bamboo.Adapter.handle_config/1`.

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# handle_config(config)

        
          **
        

    
  

  

Callback implementation for `Bamboo.Adapter.handle_config/1`.