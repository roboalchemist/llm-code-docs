# 
      Bamboo.SendGridAdapter 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Sends email using SendGrid's JSON API.

Use this adapter to send emails through SendGrid's API. Requires that an API
key is set in the config.

If you would like to add a replyto header to your email, then simply pass it in
using the header property or put_header function like so:

```
put_header("reply-to", "foo@bar.com")
```

To set arbitrary email headers, set them in the `headers` property of the Bamboo.Email struct.
Note that some header names are reserved for use by Sendgrid. See
here for full list.
## **Example config

```
# In config/config.exs, or config.prod.exs, etc.
config :my_app, MyApp.Mailer,
  adapter: Bamboo.SendGridAdapter,
  api_key: "my_api_key",
    # or {:system, "SENDGRID_API_KEY"},
    # or {ModuleName, :method_name, []}
  hackney_opts: [
    recv_timeout: :timer.minutes(1)
  ]

# To enable sandbox mode (e.g. in development or staging environments),
# in config/dev.exs or config/prod.exs etc
config :my_app, MyApp.Mailer, sandbox: true

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