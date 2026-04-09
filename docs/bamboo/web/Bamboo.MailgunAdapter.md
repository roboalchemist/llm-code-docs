# 
      Bamboo.MailgunAdapter 
      (bamboo v2.5.0)

    

      
        **
        View Source
      

  

Sends email using Mailgun's API.

Use this adapter to send emails through Mailgun's API. Requires that an API
key and a domain are set in the config.

See `Bamboo.MailgunHelper` for extra functions that can be used by Bamboo.MailgunAdapter (tagging, merge vars, etc.)
## **Example config

```
# In config/config.exs, or config.prod.exs, etc.
config :my_app, MyApp.Mailer,
  adapter: Bamboo.MailgunAdapter,
  api_key: "my_api_key" # or {:system, "MAILGUN_API_KEY"},
  domain: "your.domain" # or {:system, "MAILGUN_DOMAIN"},
  hackney_opts: [
    recv_timeout: :timer.minutes(1)
  ]

# Define a Mailer. Maybe in lib/my_app/mailer.ex
defmodule MyApp.Mailer do
  use Bamboo.Mailer, otp_app: :my_app
end
```

## **API base URI configuration

Mailgun makes a difference in the API base URL between sender
domains from within the EU and outside.

By default, the base URL is set to `https://api.mailgun.net/v3`.
To override this globally, you can use the Application environment:

```
Application.put_env(:bamboo, :mailgun_base_uri, "https://api.eu.mailgun.net/v3")
```

However, for advanced configurations (for instance, for multi-tenant
setups where you pass in the adapter config when an email is sent),
you might want to specify this on the adapter level:

```
config :my_app, MyApp.Mailer,
  adapter: Bamboo.MailgunAdapter,
  api_key: "my_api_key",
  domain: "your.domain",
  base_uri: "https://api.eu.mailgun.net/v3"
```

    

    
# 
      
        **
      
      Summary
    

  
## 
    Functions
  

    
      
        deliver(email, config)

      

        

Callback implementation for `Bamboo.Adapter.deliver/2`.

    

    
      
        filter_non_empty_mailgun_fields(body)

      

    

  

    
# 
      
        **
      
      Functions
    

    

  
    
      **
    
    
      
# deliver(email, config)

        
          **
        

    
  

  

Callback implementation for `Bamboo.Adapter.deliver/2`.
  

  
    
      **
    
    
      
# filter_non_empty_mailgun_fields(body)

        
          **